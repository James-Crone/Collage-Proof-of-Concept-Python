Counter = 0
Highest = ""
Countgrade = []
Countnames = []

#checks value of grade and prints corrosponding grade and name
def check_grade(Grade, Studentname):#this is a subprogram it stores functions for later use 
    if Grade >= 0 and Grade <= 44:
        print(Studentname +"'s grade is Null")
    elif Grade >= 45 and Grade <= 49:
        print(Studentname +"'s grade is D")
    elif Grade >= 50 and Grade <= 59:
        print(Studentname +"'s grade is C")
    elif Grade >= 60 and Grade <= 69:
        print(Studentname +"'s grade is B")
    elif Grade >= 70 and Grade <= 100:
        print(Studentname +"'s grade is A")
    else: #output text if grade is non of the above
        print("Sorry incorrect please try again")
#

#start of program
testfile = open("grades.txt","r")#opens grades text file and reads from it
for line in testfile:#for loop
    myListOfSplitLine = line.strip('\n').split(" ")#splits each index by a space and strips new line characters 
    Studentname = myListOfSplitLine[0]#stores first index of list
    Coursemarks = int(myListOfSplitLine[1])#stores second index of list
    Prelimmarks = int(myListOfSplitLine[2])#stores third index of list
    Grade = int(Coursemarks + Prelimmarks) * 100 / 150#calculates the grade percentage
    check_grade(Grade, Studentname)#runs the subprogram above
    if Grade >= 70 and Grade <= 100:#determins if the grade currently stored in the varible is equal to A grade
        Counter = Counter + 1#if grade is equal to A grade counter will be multiplied by one
    Countgrade.append(Grade)
    Countnames.append(Studentname)
testfile.close()#closes the open file

Count = max(Countgrade)#finds the highest percent and stores it

if Countgrade[0] == Count:#checks Countgrade index with Countnames index and when both match stores the name index as Highest percentage student
    Highest = Countnames[0]
elif Countgrade[1] == Count:
    Highest = Countnames[1]
elif Countgrade[2] == Count:
    Highest = Countnames[2]
elif Countgrade[3] == Count:
    Highest = Countnames[3]
elif Countgrade[4] == Count:
    Highest = Countnames[4]
elif Countgrade[5] == Count:
    Highest = Countnames[5]
elif Countgrade[6] == Count:
    Highest = Countnames[6]
elif Countgrade[7] == Count:
    Highest = Countnames[7]
elif Countgrade[8] == Count:
    Highest = Countnames[8]
elif Countgrade[9] == Count:
    Highest = Countnames[9]
elif Countgrade[10] == Count:
    Highest = Countnames[10]
elif Countgrade[11] == Count:
    Highest = Countnames[11]
elif Countgrade[12] == Count:
    Highest = Countnames[12]
elif Countgrade[13] == Count:
    Highest == Countnames[13]
else:
    Highest == Countnames[14]

print ("\r\n", Highest, "Had the highest percentage at: ", Count, "\r\n")#prints Highest Percentage in class with name
print("Number of A grades in class is",Counter)#prints text and A count number
#