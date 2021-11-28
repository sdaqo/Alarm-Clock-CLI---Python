import time
import os

allowed_24 = list(range(1,25))
allowed_60 = list(range(0, 60))

def correctInput(input_time):
    given = input_time.split(":")
    condition = False
    
    while True:
        if checkListForNumbers(given) == True:
            break
        else:
            input_time = str(input("Please only use numbers! Time: "))
            given = input_time.split(":")

    while condition == False: 
        if len(given) == 2 and int(given[0]) in allowed_24 and int(given[1]) in allowed_60: 
            condition = True
            break
        else:
            input_time = str(input('Please make sure your input has the correct format! (Format: H(1-24):M(1-60)): '))
            given = input_time.split(":")
            while True:
                if checkListForNumbers(given) == True:
                    break
                else:
                    input_time = str(input("Please only use numbers! Time: "))
                    given = input_time.split(":")   
    return given

def checkListForNumbers(input):
    if input[0].isnumeric() and input[1].isnumeric():
        x = True        
    else:
        x = False
    return x

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        
        if hours >= 0:
            timeformat = 'The Alarm Rings in {:02d} Hours {:02d} Minutes and {:02d} Seconds'.format(hours, mins, secs)
        else: 
            timeformat = 'The Alarm Rings in {:02d} Hours {:02d} Minutes and {:02d} Seconds'.format(hours + 24, mins, secs)
        
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

def alarm(time_given):
    t = time.localtime()
    current_time_h = int(time.strftime("%H", t))
    current_time_m = int(time.strftime("%M", t))
    current_time_s = int(time.strftime("%S", t))
    difference_h = int(time_given[0]) - current_time_h
    difference_m = int(time_given[1]) - current_time_m
    time_alarm_stops = []
    
    if difference_h >= 0:
        time_alarm_stops.append(difference_h)
    else:
        time_alarm_stops.append(difference_h + 24)

    if difference_m >= 0:
        time_alarm_stops.append(difference_m)
    else:
       devision = (difference_h * 60 + difference_m) / 60
       devision_reminder = (difference_h * 60 + difference_m) % 60 
       time_alarm_stops[0] = int(devision)
       time_alarm_stops.append(devision_reminder)
    
    
    seconds = int(time_alarm_stops[0]) * 3600 + int(time_alarm_stops[1]) * 60 - current_time_s
    
    return seconds

def currentTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    print("Current Time: " + current_time) 
    
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)