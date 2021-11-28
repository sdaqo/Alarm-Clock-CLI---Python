from libs import alarm

def main():
    alarm.currentTime()
    correct_input = alarm.correctInput(str(input('Time you want your alarm to ring (Format: H:M): ')))
    seconds_til_alarm_rings = alarm.alarm(correct_input)
    alarm.clearConsole()
    alarm.currentTime()
    print("Given time when the Alarm will ring: " + correct_input[0] + ":"  + correct_input[1])
    alarm.countdown(seconds_til_alarm_rings)


if __name__ == "__main__":
    main()