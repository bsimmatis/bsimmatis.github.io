# Github Assignment
*BIOL812*
***

### 1. When should you use Git for a project?
* When you need to collaborate on code to run repetitive tasks with datasets.

### 2. What kind of files/info should be saved in a Git repository? What types of files/info should not be included in a Git repo?
* Code and text files can be saved to a Git repository.
* Private or confidential files and information should not be included.

### 3. What are the commands to undo a commit?
* You can "undo" a commit by returning to the previous version using "git checkout HEAD~1"

### 4. One of your repositories is in a "detached HEAD" state. How do you fix this?
* The detached head state means that you aren't on the current commit. So, you can use "git checkout master" to return to the most recent commit.

### 5. Your boss has no idea what Git is or why you are using it. 
   Explain the pros / cons of using Git for your research project.
   Explain the pros / cons of hosting your project in a public 
   (or private) repository on Github/Bitbucket/Gitlab/etc. 
* Using Git for a research project is an easy way to back up code for repetitive data analysis remotely, so you won't lose anything stored with Git if you lose local files.
* It is easy to collaborate on code with many people at the same time, and all changes are easily tracked.
* Public repositories are open to view, so confidential information shouldn't be stored in Git, nor is it able to handle very large files or datasets.
* Storing code in a public repository will allow for open collaboration between programmers around the world and is free.
* Private hosting is available for a fee, but allows for more privacy on sensitive projects.
