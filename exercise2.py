#Design a calculator which will give you the correct information except the following ones:
# 45 * 3= 555, 56 + 9=77, 56 / 6=4.
print("Welcome to my calculator")
print("1.Addition")
print("2.Multiplication")
print("3.Subtraction")
print("4.Division")
print("Enter the type which you wanna operation on:")
var1=int(input())
print("Enter the two numbers:")
num2=int(input())
num3=int(input())
if (var1==1):
    if (num2 == 56 and num3 == 9):
        print(77)
    else:
        print(num2+num3)
elif (var1==2):
    if (num2 == 45 and num3 == 3):
        print(555)
    else:
        print(num2*num3)
elif (var1==4):
    if ( num2 == 56 and num3 == 6):
        print(4)
    else:
        print(num2/num3)




