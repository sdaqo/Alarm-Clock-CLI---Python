import time
import os
import glob
import threading
from platform import system
from playsound import _playsoundWin, _playsoundNix, _playsoundOSX

allowed_hours = list(range(1,25))
allowed_minutes = list(range(0, 60))
allowed_sounds = list(range(1, 23))
keep_going = True
system = system()

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
        if len(given) == 2 and int(given[0]) in allowed_hours and int(given[1]) in allowed_minutes: 
            condition = True
            break
        else:
            input_time = str(input('[False Input] Time you want your alarm to ring (Format: H:M [24-Hour-Format]): '))
            given = input_time.split(":")
            while True:
                if checkListForNumbers(given) == True:
                    break
                else:
                    input_time = str(input("Please only use numbers! Time: "))
                    given = input_time.split(":")   
    return given

def checkListForNumbers(input):
    input = list(input)
    if len(input) == 2:
        if input[0].isnumeric() and input[1].isnumeric():
            x = True        
        else:
            x = False
    else:
        try:
            if input[0].isnumeric():
                x = True
            else:
                x = False
        except:
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


def pickSound():
    alarms = glob.glob('alarms/*.mp3')
    while True:
        pick_alarm = input("Pick your Alarm-Tone (1-22): ")
        
        while True:
            if checkListForNumbers(pick_alarm) == True and int(pick_alarm) in allowed_sounds:
                break
            else:
                pick_alarm = input("[False Input] Pick your Alarm-Tone (1-22): ")
                continue

        if system == "Windows":    
            _playsoundWin("{0}".format(str(alarms[int(pick_alarm) - 1])))
        elif system == "Darwin":
            _playsoundOSX("{0}".format(str(alarms[int(pick_alarm) - 1])))
        else:
            _playsoundNix("{0}".format(str(alarms[int(pick_alarm) - 1])))
        
        
        confirm = False
        
        while True:
            confirm = input("Do you want to pick this Sound? (y/N): ")
            
            if confirm == "y"or confirm == "Y":
                confirm = True
                break
            elif confirm == "n" or confirm ==  "N":
                confirm = False
                break
            else:
                continue
 
        if confirm == True:
            break
        else:
            pass
    name = alarms[int(pick_alarm) - 1].replace("alarms", "").replace(".mp3", "").replace("\\", "")
    return int(pick_alarm), alarms, name

def key_capture_thread():
    global keep_going
    input()
    keep_going = False
    

def playsound(picksound_out):
    threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    
    while keep_going:
        print("To exit press the ENTER key.", end="\r")
        
        if system == "Windows":    
            _playsoundWin("{0}".format(str(picksound_out[1][int(picksound_out[0]) - 1])))
        elif system == "Darwin":
            _playsoundOSX("{0}".format(str(picksound_out[1][int(picksound_out[0]) - 1])))
        else:
            _playsoundNix("{0}".format(str(picksound_out[1][int(picksound_out[0]) - 1])))
        