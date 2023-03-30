
from alarm_clock import AlarmClock



   
my_clock = AlarmClock("12:00 PM")
print(f" The clock is currently reading: {my_clock.current_time}")


my_clock.change_current_time(input("What time is the new time?: "))

my_clock.turn_alarm_on()

my_clock.change_alarm_time(input(f" Currently you alarm is set for {my_clock.alarm_time}. What time do you want to change this to?"))


