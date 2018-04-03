import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(193721918)
tsize = 1         #tournament size
divisor = 1
resource = 20       #Amount of resource to be divided
population = 2    #Number of algae 
runs = 1          #Number of interactions
cost = 10           #Cost for demanding more than MA
verbose = 0
mutprobarray = [0.4,0.4,0.2]    #Mutation probability array
mutamtarray = [0,1,2]           #Mutation amt array

def main(): 
#   Empty array to store winners
    winners = []
    r = 0
#   Empty array to store agents/players
    agents = []
    for r in range(runs):    
#   initialize population with proposal, demand, min accept, and resource
        m=0
        for m in range(population):
            i = 0
            agent = []
#           Create the proposal part of the array
#           For the proposal v demand part, proposal can never be higher than the demand
            for i in range(resource):
                if i == 0:
                    agent.append(1)
                else:
                    agent.append(np.random.randint(1,i+1))
            minaccept =((-1)**np.random.randint(0,2))*np.random.choice(mutamtarray, p = mutprobarray)
            demand =((-1)**np.random.randint(0,2))*np.random.choice(mutamtarray, p = mutprobarray)
            #create the min accept, demand, and money part of the array
            while demand < minaccept:
                demand = np.random.randint(1,20)
        
            
            agent.append(minaccept)
            agent.append(demand)
            agent.append(0)
            agents.append(agent)
        #Arrays to collect game stats
        gameproposalarray = []
        minacceptingmean =[]
        demandingmean =[]

        minacceptingci =[]
        demandingci =[]

        runmas = []
        runds = []
        j=0
        
        for f in range(population):
            agents[f][22] = agents[f][22]*0.9
        agentlist = np.arange(0,population)
       # player1 = numpy.random.choice(agentlist,p=cashprobability)
        player1 = np.random.choice(agentlist)
        #player2 = numpy.random.choice(agentlist,p=cashprobability)
        player2 = np.random.choice(agentlist)
        while player1 == player2:
                #player2 = numpy.random.choice(agentlist,p=cashprobability)
                player2 = np.random.choice(agentlist)
        b = np.random.randint(0,2)
        if b == 1:
            dummyplayer = player1
            player1 = player2
            player2 = dummyplayer
        #get demand, update demand in gene
        if j % 10 == 0:   #every 10th round 
            demandmut = np.random.randint(0,2)                    
            agents[player2][21] = agents[player2][21] + ((-1)**demandmut)*np.random.choice(mutamtarray, p = mutprobarray)
        if agents[player2][21] > 19:
            agents[player2][21] = 19
        if agents[player2][21] < 1:
            agents[player2][21] = 1
            
        #get min accept, update minaccept in gene
        if j % 10 == 0:  
            minacceptmut = np.random.randint(0,2)
            agents[player2][20] = agents[player2][20] + ((-1)**minacceptmut)*np.random.choice(mutamtarray, p = mutprobarray)
        if agents[player2][20] < 1:
            agents[player2][20] = 1
        if agents[player2][20] > agents[player2][21]:
            agents[player2][20] = agents[player2][21]
        #if agents[player2][2] < agents[player2][1]:
         #   agents[player2][2] = agents[player2][1]
        gamedemand = agents[player2][21]
        gameminaccept = agents[player2][21]            
        #get proposal, update gene
        #proposalmut = (-1)**numpy.random.randint(0,2) 
        
        gameproposal = agents[player1][gamedemand] 
        #if gameproposal > gamedemand:
            #gameproposal = gamedemand
        gameproposalarray.append(gameproposal)
        #check if deal goes through
        if gameproposal >= gameminaccept:
            agents[player1][22] += 20 - gameproposal
            player2payoff = gameproposal - cost*(abs(gamedemand - gameminaccept))
            if player2payoff < 0:
                player2payoff = 0
            agents[player2][22] += player2payoff 
        
        for i in range(population):
            #runps.append(agents[i][0])
            runmas.append(agents[i][20])
            runds.append(agents[i][21])
        if j%divisor == 0:
            #ravgp = numpy.mean(runps)
            ravgma = np.mean(runmas)
            ravgd = np.mean(runds)
           
            #rstdp = numpy.std(runps)
            rstdma = np.std(runmas)
            rstdd = np.std(runds)
    
            #rconfp = 1.96*(rstdp/numpy.sqrt(population))
            rconfma = 1.96*(rstdma/np.sqrt(population))
            rconfd = 1.96*(rstdd/np.sqrt(population))

            #proposingmean.append(ravgp)
            minacceptingmean.append(ravgma)
            demandingmean.append(ravgd)
            #proposingci.append(rconfp)
            minacceptingci.append(rconfma)
            demandingci.append(rconfd)
            gameproposalarray = []
            #runps =[]
            runmas = []
            runds = []
            if verbose == 1:    
                print (ravgma,rconfma,ravgd,rconfd)
            
            #tournament selection for males
            a = []
            a = np.random.choice(population,tsize, replace = False)   
            tourneylist = []
            i = 0
            for i in range(tsize):
                tourneylist.append(agents[a[i]])
        
        #sort the payoffs and the group list simultaneously
            for passnum in range(len(tourneylist)-1,0,-1):
                for i in range(passnum):
                    if tourneylist[i][22]<tourneylist[i+1][22]:
                        temp = tourneylist[i]
                        tourneylist[i] = tourneylist[i+1]
                        tourneylist[i+1] = temp
                        temp2 = a[i]
                        a[i] = a[i+1]
                        a[i+1] = temp2
            #create children
            child1 = agents[a[0]]
            child2 = agents[a[1]]
         
#           two point crossover
            
            cp1 = np.random.randint(0,resource)
            cp2 = np.random.randint(0,resource)
            while cp1 == cp2:
                cp2 = np.random.randint(0,resource)
            if cp1 > cp2:
                h = cp1
                cp1 = cp2
                cp2 = h
#                      
            while cp1 <= cp2:
                e = child1[cp1]
                child1[cp1] = child2[cp1]
                child2[cp1] = e
                cp1 += 1
            #mutation step for the children
            for n in range(resource):
                if n > 2:
                    child1[n] = child1[n] + ((-1)**minacceptmut)*np.random.choice(mutamtarray, p = mutprobarray)
                    child2[n] = child2[n] + ((-1)**minacceptmut)*np.random.choice(mutamtarray, p = mutprobarray)
                if child1[n] < 1:
                    child1[n] = 1
                if child1[n] > n:
                    child1[n] = n
                if child2[n] < 1:
                    child2[n] = 1
                if child2[n] > n:
                    child2[n] = n
            #replace losers
            agents[a[tsize-1]] = child1
            agents[a[tsize-2]] = child2
            
    dummyagent = []
    payoffs = []
    
    #calculate the winners
    k= 0
    for k in range(population):
        dummyagent.append(k)
        payoffs.append(agents[k][22])
    #sort the population
    for passnum in range(len(payoffs)-1,0,-1):
                for i in range(passnum):
                    if payoffs[i]<payoffs[i+1]:
                        temp = payoffs[i]
                        payoffs[i] = payoffs[i+1]
                        payoffs[i+1] = temp
                        temp2 = dummyagent[i]
                        dummyagent[i] = dummyagent[i+1]
                        dummyagent[i+1] = temp2
    #take the best agent and put it in the winners list
    winners.append(agents[dummyagent[0]])
    
    if verbose == 1:        
        print (r)
    #sort the winners
    for passnum in range(len(winners)-1,0,-1):
                    for i in range(passnum):
                        if winners[i][3]<winners[i+1][3]:
                            temp = winners[i]
                            winners[i] = winners[i+1]
                            winners[i+1] = temp
    print ("Cost:", cost)
    w = 0
    
    winneraverageproposals = []
    winnerproposalcis =[]
    for q in range(resource):
        x = 0.0
        y = 0.0            
        for u in range(len(winners)):
            x += winners[u][q]
        avgx = x/len(winners)
        winneraverageproposals.append(avgx)
        for i in range(len(winners)):
            y += (avgx - winners[i][q])**2
        stdx = np.sqrt(y/(len(winners)))
        confx = 1.96*stdx/np.sqrt(len(winners))
        winnerproposalcis.append(confx)
    wdemands = []
    wminaccepts = []
    for q in range(len(winners)):
        wdemands.append(winners[q][21])
        wminaccepts.append(winners[q][20])
#    
#    w = np.arange(0,resource)
#    plt.figure()
#    plt.title('Absorbance level vs Time')
#    plt.axis([0,resource,0,resource])
#    plt.xlabel("generation x10")
#    plt.ylabel("Absorbance")
#    plt.errorbar(w,winneraverageproposals, yerr = winnerproposalcis, color = 'blue')    
#    plt.scatter(w,winneraverageproposals, color = 'red')
    
  # Generate a plot in `plt`
    x = np.arange(0,runs/1000,1)
    plt.figure()
    plt.title('Cost = 1, Standard Mutation Rate, Blue = P, Green = MA, Red = D')
    plt.axis([0, runs/1000, 0,20])
    plt.xlabel("Games")
 #   plt.errorbar(x, gameproposalaverages, yerr = gameproposalcis, color = 'blue')#proposal
    plt.errorbar(x, minacceptingmean, yerr = minacceptingci,color = 'green')#minaccept
    plt.errorbar(x, demandingmean, yerr = demandingci, color = 'red')#demand
    plt.savefig('run.join(map(str, r)).png', bbox_inches='tight')
    plt.close()

main()
