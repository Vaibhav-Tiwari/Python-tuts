import random


print("Welcome To The Game Of 'Snake,Water,Gun'")
print("Presented By: Vaibhav Tiwari\n")
lst=["snake","water","gun"]
choice=random.choice(lst)
val=10
# snake="s"
# water="w"
# gun="g"
pt=0
pr=0
sr=0
while(True):
    if(val>=1):
        print("Enter the value from 'snake','water','gun':")
        str = input()
        if str=="snake" and choice=="water":
             pt = pt + 1
             print("You Win!")
             print("You Got +1 Point")
            # print("Yor are left with:",val-1,"chances")
        elif str=="water" and choice=="snake":
            pr = pr + 1
            print("Computer Wins!")
            print("You Loose -1 Point")
            # print("Yor are left with:", val - 1, "chances")
        elif str=="gun" and choice=="snake":
            pt = pt + 1
            print("You Win!")
            print("You Got +1 Point")
            # print("Yor are left with:", val - 1, "chances")
        elif str=="snake" and choice=="gun":
            pr = pr + 1
            print("Computer Wins!")
            print("You Loose -1 Point")
            # print("Yor are left with:", val - 1, "chances")
        elif str=="water" and choice=="gun":
            pr = pr + 1
            print("Computer Wins!")
            print("You Loose -1 Point",)
            # print("Yor are left with:", val - 1, "chances")
        elif str=="gun" and choice=="water":
            pr = pr + 1
            print("Computer Wins!")
            print("You Loose -1 Point")
            # print("Yor are left with:", val - 1, "chances")
        elif str=="water" and choice=="water":
            sr = sr + 1
            print("match Draw!")
            print("No One Wins!")
            # print("Yor are left with:", val - 1, "chances")
        elif str=="gun" and choice=="gun":
            sr = sr + 1
            print("Match Draw!")
            print("No One Wins!")
            # print("Yor are left with:", val - 1, "chances")
        elif str=="snake" and choice=="snake":
            sr = sr + 1
            print("Match Draw!")
            print("No One Wins!")
            # print("Yor are left with:", val - 1, "chances")
        val=val-1
        print("Yor are left with:", val , "chances\n")
        # pt=pt+1
        # pr=pr+1
        # sr = sr + 1

    else:
        break

# pt=pt+1
# pr=pr+1
# sr=sr+1
print("The Total Number Of Matches Won By You:\n",pt)
print("The Total Number Of Matches Won By Computer:\n", pr)
print("Total Matches Get Draw:\n",sr)
if pt>pr:
    print("Congrats! You Win")
elif pt==pr:
    print("Match Draw!")
else:
    print("Computer Wins!")

