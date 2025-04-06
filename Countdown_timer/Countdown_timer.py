import time

# Here we use time module which gives us functions like sleep() to pause the program

seconds = int(input("Enter time in seconds: "))

while seconds:
    mins, secs = divmod(seconds, 60)
# here divmod converts total seconds into minutes and seconds
# for example divmod(70, 60) → (1, 10)
# here the 70 sec convert into 1 min and 10 sec
    print(f"{mins:02}:{secs:02}")
# this formated print statement use to print the countdown   
    time.sleep(1) 
# use sleep(1) to make the timer wait for one second between updates
    seconds -= 1

print("Time's up!!! ⏰")
