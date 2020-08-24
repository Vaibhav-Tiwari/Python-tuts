# Healthy Programmer

# 9am-5pm
# water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - Every 30 mins - eydone -log
# Physical activity - physical.mp3 (every- 45 mins) - Exdone - log
#
# Rules
# pygame module to play audio


import time
initial=time.time()
import datetime

# from pygame import mixer

def get_time():
    return datetime.datetime.now()


print("......A PLAN FOR HEALTHY PROGRAMMER!......")
print("A plan For 9am to 5pm")
localtime=time.asctime(time.localtime(time.time()))
print(localtime)


# print("Which Process Do You Want To Execute!")
# print("If You want to enter the Data Press '1'")
# print("If You want to open the file ans Simple read the data press '2'")
# var=int(input())
#
# if var == 1:
from pygame import mixer

def Drinking_water():

    time.sleep(1)

    mixer.init()
    mixer.music.load("The Chainsmokers - Closer ft. Halsey (Official).mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

     # infinite loop
    while True:
        # time.sleep(1)
        print("print 'Drank' to stop the song!")
        # print("Press 'e' to exit the program")
        query = input(" ")

        if query == 'Drank':
            # Pausing the music
            mixer.music.stop()

        if query != 'Drank':
            print("Please enter a valid Input!")

        if query == "Drank":
            with open("water.txt","a") as f:
                f.write(f"{get_time()}"+" Drank water!\n")
            # continue
        break
Drinking_water()

def Eye_exercise():
    time.sleep(10)

    mixer.init()
    mixer.music.load("One Call Away - Charlie Puth.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

    # infinite loop
    while True:
        # time.sleep(10)
        print("print 'Doneexe' to stop the song!")

        query = input(" ")

        if query == 'Doneexe':
            # Pausing the music
            mixer.music.stop()

        if query != 'Doneexe':
            print("Please enter a valid Input!")

        if query=='Doneexe':
            with open("eye.txt","a") as f:
                f.write(f"{get_time()}"+" Done with the eyes exercise!\n")

        break
Eye_exercise()

def Physical_exercise():
    time.sleep(20)

    mixer.init()
    mixer.music.load("Imagine Dragons - Believer.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

    # infinite loop
    while True:
        # time.sleep(20)
        print("print 'Done' to stop the song!")

        query = input(" ")

        if query == 'Done':
            # Pausing the music
            mixer.music.stop()

        if query != 'Done':
            print("Please enter a valid Input!")

        if query=='Done':
            with open("physicalactivity.txt","a") as f:
                f.write(f"{get_time()}"+"Done with the Physical Exercise!\n")

        break
Physical_exercise()

# elif var == 2:
#     print("press '1' to read the drinking water data file", "press '2' to read the Eye exercise data file!",
#           "press '3' to read the Physical activity data file")
#     num=int(input())
#     if num == 1:
#         with open("water.txt","r") as f:
#             content=f.read()
#             # return print(content)
#
#     elif num == 2:
#         with open("eye.txt","r") as f:
#             content=f.read()
#             # return print(content)
#
#     elif num == 3:
#         with open("physicalactivity.txt","r") as f:
#             content=f.read()
#             # return print(content)


