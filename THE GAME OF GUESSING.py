#no of guesses 9
#print the no. of guesses left
#and at the end we have to print the game over

print("Welcome to the Game Of Guessing")
print("You have only 5 chances to win this game")
n=20
c=5
while(1):
    print("Enter the value of your choice")
    num1 = int(input())
    if(num1 < n):
        if(c>1):
          print("enter the bigger number")
          c=c-1
          print(c,end=" Chances left\n")
        else:
            print("GAME OVER")
            break

        #else:
            #print("Game Over")
       # break

    elif(num1==n):
        print("Congrats you have a very good guessing ability")
        break
    elif(num1 > n):
        if(c>1):
            print("enter the smaller number than this")
            c=c-1
            print(c,end=" Chances left\n")
        else:
            print("Game Over")
            break



