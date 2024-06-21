juice=100
print("Enter your age and money:")
age=int(input())
money=int(input())
if money<juice and age<20 and age>60:
    print("Here is your juice")
elif money<juice and age>30 and age<50:
    print("See you later")
else:
    print("Here is your juice")
    change=juice-money
    print("here is your change",change)
print("Visit again")