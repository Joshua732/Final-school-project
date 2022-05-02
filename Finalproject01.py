import time
# nothing here right now, Commit test 5
# add program to list that you want to check, right now it will only check one for now
Protectlist = [] #not used
#user inputs file
print("please enter name of file with .txt at the end to monitor")
Protect_file = input()
print("File has been opened and its being monitored")
#where its open by program
mainopen = open(Protect_file )
# where file is read and printed
readsfile = mainopen.read()
mainopen.close()
print(readsfile)
