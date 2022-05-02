import time
# Just the Main loop
Mainloop = 2
# nothing here right now, Commit test 5
# add program to list that you want to check, right now it will only check one for now
Protectlist = [] #not used
#user inputs file
print("please enter name of file with .txt at the end to monitor")
Protect_file = input()
print("File has been opened and its being monitored")
#where its open by program
mainopen = open(Protect_file)
# where file is read and printed
readsfile = mainopen.read()
mainopen.close()
while Mainloop == 2:
    oldread = readsfile
    tempopen = open(Protect_file)
    newread = tempopen.read()
    mainopen.close()

    if oldread != newread:
        print(Protect_file + " " + "FILE HAS BEEN MODIFIED")
        break
    else:
        time.sleep(3)
