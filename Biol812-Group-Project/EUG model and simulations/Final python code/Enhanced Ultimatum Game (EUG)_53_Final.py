import numpy as np
import matplotlib.pyplot as plt

#-----------------------
#define variables
resource = 20           #Amount of resource to be divided
cost = 0              #Cost for demanding more than MA
runs = 1                #Number of interactions
popsize = 4            #population size/Number of algae
generations = 1       #Number of generations
tsize = 4              #Tournament size
pmr=0.05            #Point mutation rate for proposal
mdr=0.5             #Point mutation rate for demand and MA
epoch=0                 #Number of epoch

#def getKey1(item):
#    return(item[money+2])
#------------------------
#Defines Main loop where characteristics of each alga is created
def main():
#   Create loop for interactions
   for r in range(runs):
        Algaearray = []
#        runPepoch = []
        for i in range(popsize):
            blankalgae = []
#           for each algae, assign a random integer for its MA and Demand value
            MA = np.random.randint(1,resource+1)
            D = np.random.randint(1,resource+1)
#           If Demand is less than MA then set them equal.
            if D < MA:
                D = MA
            for j in range(resource):
#           create array with money,MA,D,fitness for each algae in population
                if j==0:
                    blankalgae.append(0)
                if j==1:
                    blankalgae.append(1)
                if j>=2:
                    blankalgae.append(j-np.random.randint(1,j))
            blankalgae.append(MA)
            blankalgae.append(D)
            blankalgae.append(0)
            Algaearray.append(blankalgae)
#           To see what the initial stats are of each algae, print the algae array...
#        print(Algaearray)    
        

#       Calculate average of initial Algaearray
#        initialstats=[]
#        for i in range(resource+3):
#            a = 0
#            for y in range(popsize):
#                a += Algaearray[y][i]
#            initialstats.append(a/popsize)
#        print(initialstats)

#-------------------------
#Algae interactions. Each algae interacts with each other (once as proposer and again as demander)
        for g in range(generations):       
            for k in range(popsize):
                algae1 = k
                for l in range(popsize):
                    algae2 = l
                    if algae1 != algae2:
                        gameminaccept = Algaearray[algae2][resource]
                        gamedemand = Algaearray[algae2][resource+1]
                        gameproposal = Algaearray[algae1][gamedemand]
                        if gameproposal > gamedemand:
                            gameproposal = gamedemand
                        if gameproposal >= gameminaccept:
                            Algaearray[algae1][resource+2]+= resource-gameproposal
#                            print(gameproposal) if needed
                            Algae2payoff = gameproposal - cost*(abs(gamedemand-gameminaccept))
                            Algaearray[algae2][resource+2]+= Algae2payoff
#       Algae will now have interacted with each other and received a fitness score.
#       One may print the Algae array to view the updated matrix (the last cell of each array will display the fitness scores)...
#        print(Algaearray)
                            
#--------------------------   
#Mutation of the population. To see how algae population evolves.     
                    
        tournamentlist = []
        tournamentlist = np.random.choice(np.arange(0,popsize), tsize, replace = False)
        tournamentarray = []
        a = 0
        for a in range (tsize):
            tournamentarray.append(Algaearray[tournamentlist[a]])
        # tournament= sorted(tournament, reverse = True, key = getKey1)
#           Bubble sort! :) To sort the "fitness" and the group list simultaneously. https://en.wikipedia.org/wiki/Bubble_sort
        for passnum in range(len(tournamentarray)-1,0,-1):
            for i in range(passnum):
                if tournamentarray[i][resource+2]<tournamentarray[i+1][resource+2]:
                   temp1 = tournamentarray[i+1]
                   tournamentarray[i+1] = tournamentarray[i]
                   tournamentarray[i] = temp1
                   temp2 = tournamentlist[i+1]
                   tournamentlist[i+1] = tournamentlist[i]
                   tournamentlist[i] = temp2
#           Below will be using ideas of Point mutation https://en.wikipedia.org/wiki/Point_mutation
#           First, define the algae with the highest "fitness"           
        algae1=[]
        algae2=[]
        for i in range(0,resource+3):
            algae1.append(Algaearray[tournamentlist[0]][i])
            algae2.append(Algaearray[tournamentlist[1]][i])
#       Two point crossover. 
#       Define a random integer value (between 0 and resource) to cp1 and cp2 which will be the points that "cross"                                              
        cp1 = np.random.randint(0,resource)
        cp2 = np.random.randint(0,resource)
#           To ensure cp1 and cp2 do not equal                   
        while cp1==cp2:
            cp2 = np.random.randint(0,resource)
#           To ensure cp2 is larger than cp1
        if cp1 > cp2:
            temp3 = cp1
            cp1 = cp2
            cp2 = temp3
#       swap the specified cells of the two offspring
        while cp1 <= cp2:
            e = algae1[cp1]
            algae1[cp1] = algae2[cp1]
            algae2[cp1] = e
            cp1 += 1
#       update Minaccept and Demand 
           
        for i in range(resource,resource+2):
            algae1[i]= int(0.6667*algae1[i]+0.3333*algae2[i])
            algae2[i]= int(0.6667*algae1[i]+0.3333*algae2[i])
#       define s to be a random number from a uniform distribution            
        for i in range(resource):
            s = np.random.uniform(0,1)
#           point mutation rate for proposal        
            if s < pmr:
                algae1[i]=algae1[i]+ np.random.choice([1, -1])
                algae2[i]=algae2[i]+ np.random.choice([1, -1])
       
#       put range(resource,resource+3) if we want to average fitness scores of parents among offspring
        for i in range(resource,resource+2):
            m = np.random.uniform(0,1)
#           point mutation rate for minaccept and demand        
            if m < mdr:
                algae1[i]=algae1[i]+ np.random.choice([1, -1])
                algae2[i]=algae2[i]+ np.random.choice([1, -1])         
    
#       if any of the proposals, minaccept or demand are equal to 0 or 20, then replace with 1 or 19 respectively    
        for a in range(resource+2):
            if algae1[a]>resource-1:
                algae1[a]=resource-1
            if algae1[a]<1:
                algae1[a]=1
            if algae2[a]>resource-1:
                algae2[a]=resource-1
            if algae2[a]<1:
                algae2[a]=1
#           if minaccept > demand then set them equal
            if algae1[resource] > algae1[resource+1]:
                algae1[resource] = algae1[resource+1]
            if algae2[resource] > algae2[resource+1]:
                algae2[resource] = algae2[resource+1]

#       Replace lowest fitness alga with the mutated algae
        Algaearray[tournamentlist[tsize-1]]= algae1
        Algaearray[tournamentlist[tsize-2]]= algae2 
        
#        print("Top Dog")
#        print(Algaearray[tournamentlist[0]])
#        print("Second Banana")
#        print(Algaearray[tournamentlist[1]])
#
#        print("Offspring 1")
#        print(algae1)
#        print("Offspring 2")
#        print(algae2)
#        print("Updated Algae List")
#        print(Algaearray)

# ----------------------------Calculate Averages  
#       Reset fitness score to zero
        for a in range(popsize):
           Algaearray[a][resource+3]=0
#       Create empty arrays to append averages
        runPepoch = []
        RUNPepoch = []
        epochrunaverages =[]
        Finalavg =[]
#       calculate average 
        if g % epoch == 0:
            epochaverages = [0,1]
            for i in range(2,resource):
                a=0
                for j in range(popsize):
                    a+=Algaearray[j][i]
                epochaverages.append(a/popsize)
            runPepoch.append(epochaverages)
                     
            RUNPepoch.append(runPepoch)
   
        for i in range(epoch+1):
            epochrunaverages=[]
            for j in range(resource):
                a=0
                for k in range(generations):
                    a+=RUNPepoch[k][i][j]
                epochrunaverages.append(a/generations)
            Finalavg.append(epochrunaverages)  
# 
#    limit=11
#----------------------------Plot
#    fig = plt.figure(figsize=(8,8))
#    ax = fig.add_subplot(111)
#    ax.set_prop_cycle(plt.cycler('color', plt.cm.Accent(np.linspace(0, 1, limit))))  
# #   x = np.arange(0,money)
#    print(Finalavg)
#    
#    for a in Finalavg:
#        plt.plot(a)
#        plt.axis([0, generations/epoch, 0, money])
#    plt.show()
#    
main()
