from pathlib import Path

p = Path('/inodes')

n = 0;

while True:
    s = str(n)
    fname = s + ".txt"
    
    with(p/ fname).open('w') as file:
        file.write("hello")
        
    n += 1
    
#sudo -i first to run as root or just change the directory you are writing to
#The script will automatically stop because "No space left on device".
#Run df -h & df -hi. Compare the inode usage vs storage usage on the partition. You will notice that your drive is not out of space, the reason you can't create new files is because you have used up all of the inodes.