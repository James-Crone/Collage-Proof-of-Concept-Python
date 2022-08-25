Lst = []
Number = 1
Loop = 8

for i in range(Loop):
    print("Please enter Temperature Number for each day of the week:", Number)
    Input = float(input())
    if Input >= 0 and Input <= 100:
        Number = Number + 1
        Lst.append(Input)
    else:
        print("Please input a number between 0 and 100")

Weeklytotal = Lst[0] + Lst[1] + Lst[2] + Lst[3] + Lst[4] + Lst[5] + Lst[6]
print("Weekly Total Temperature =", Weeklytotal)
print("List Of Temperatures =", Lst)