class AlarmClock:
    def __init__(self,curr_time) -> None:
        self.current_time = curr_time
        self.alarm_on = False
        self.alarm_time = "5:30 PM"
      

    def change_current_time(self, new_current_time):
        self.change_current_time = new_current_time
        print(f"The current time has been changed from {self.current_time} to {new_current_time}")
        
    def turn_alarm_on(self):
    
        if self.alarm_on == False:
            activate_alarm = input(" Your alarm is not ON. Would you like to turn it ON?")
            if activate_alarm == "y":
                self.alarm_on = True
                print(f"Your alarm is on and set for {self.alarm_time}. ")
            else:
                print(f" You alarm will remain off.")
        else:
             print()
             print(f" Your alarm is ON and set for {self.alarm_time}.") 
             print()
             activate_alarm = input(f" Would you like to turn this alarm off? Press 'y' for yes and 'n' for no:")
             if activate_alarm == "y":
                self.alarm_on = True
                print(f"Your alarm is on and set for {self.alarm_time}. ")
             else:
                print(f" You alarm will remain off.")

    def change_alarm_time(self, new_alarm_time):
        self.alarm_time = new_alarm_time
        print(f" You have set the alarm time to {self.alarm_time}")
        
