marks = ""

print("Please enter student test marks the equivilent grades will be returned")
marks = int(input())

if marks >= 0 and marks <= 49:
    print("Student Grade is D")

elif marks >= 50 and marks <= 60:
     print("Student Grade is C")

elif marks >= 61 and marks <= 69:
    print("Student Grade is B")

elif marks >= 70 and marks <= 100:
    print("Student Grade is A")
    
else:
    print("Incorrect grade please check and retry")