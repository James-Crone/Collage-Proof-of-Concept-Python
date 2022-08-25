
'''           INDEX
0.  Declare variables
1.  Ask user to input price of item
2.  Loop while price of item != -1
3.  Print item number and it�s price
4.  Add price to total
5.  Ask user to input next price of item
6.  End of loop
7.  Print the total
8.  Print the number of items
'''
#0
Userprice = ""
Number = 0
Total = 0
#1
print ("Please enter the price of item type -1 to stop")
Userprice = float(input())
#2
while Userprice != -1:
    Number = Number + 1
#3
    print (Number and ": " and Userprice)
#4
    Total += Userprice
#5
    print ("Please enter price of next item type -1 to stop")
    Userprice = float(input())
#6/7/8
print("Total Price of all items is: "+"{:.2f}".format(Total))
print("Amount of items is:", Number)