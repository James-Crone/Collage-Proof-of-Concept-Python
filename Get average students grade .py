total=0
grade=0
print ("Enter the number of Grades received")
grades = int(input())
for i in range(grades):
    print ("Input User grade")
    grade = int(input())
    total +=grade

if total >= 0 and total <= 49:
    print("\nStudent Grade is D")
elif total >= 50 and total <= 60:
    print("\nStudent Grade is C")
elif total >= 61 and total <= 69:
    print("\nStudent Grade is B")
elif total >= 70 and total <= 100:
    print("\nStudent Grade is A")
else:
    print("\nincorrect grades")

average = total / grades
print ("Average is", average)