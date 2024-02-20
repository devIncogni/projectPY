# Printing Greeting According to Time
import time

currHour = int(time.strftime("%H"))

if (currHour >= 5 and currHour < 12):
    print("Good Morning")
elif (currHour >= 12 and currHour < 16):
    print("Good After Noon")
elif (currHour >= 16 and currHour < 20):
    print("Good Evening")
else:
    print("Good Night")

print(currHour)