# Printing Pattern
#Take an integer as input
#Boolean=True or False

# print("Star Pattern!")
# print("Enter the Value of num:")
# num=int(input())
# print("Enter the value'0' or '1'")
# a=int(input())
# b=bool(a)
# if(b==True):
#
#     for i in range (1,num+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#
#         print()
#
# elif(b==False):
#
#     for i in range (1,num+1):
#         for j in range (-1,num-i):
#             print("*",end=" ")
#
#         print()

for i in range (1,6):
    for j in range (6,i-1):
        print(j,end=" ")

    print()