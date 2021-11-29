from libs import alarm

def main():
    alarm.currentTime()
    correct_input = alarm.correctInput(str(input('Time you want your alarm to ring (Format: H:M [24-Hour-Format]): ')))
    seconds_til_alarm_rings = alarm.alarm(correct_input)
    picked_sound = alarm.pickSound()
    alarm.clearConsole()
    alarm.currentTime()
    print("Given time when the Alarm will ring: " + correct_input[0] + ":"  + correct_input[1])
    print("Alarm-Tone you picked: " + picked_sound[2])
    alarm.countdown(seconds_til_alarm_rings)
    alarm.clearConsole()
    alarm.playsound(picked_sound)


if __name__ == "__main__":
    main()