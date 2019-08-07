## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
      return "The current time is %d:%02d" % (self.hour, self.minutes)
  
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
#Calculate the total minute value
      total_min = self.minutes + minutes
# While the total min value is greater than 60, add an hour to the time, then
# subtract 60. If the hours go above 12, reset hours to 1. If the hours go
# below 1, reset hours to 12.
      while total_min >= 60:
        self.hour += 1
        total_min -= 60
        if self.hour > 12:
          self.hour = 1
        elif self.hour < 1:
          self.hour = 12
# Reset self.min to 0. Then add the total minutes.
      self.minutes = 0
      self.minutes += total_min
      print(self)      
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
#Calculate the total minute value to be subtracted.
      total_min = self.minutes - minutes
# If the total minutes to be subtracted are less than 0, subtract an hour and 
# add 60 minutes. If the hours go above 12, reset hours to 1. If the hours go
# below 1, reset hours to 12.
      while total_min < 0:
        self.hour -= 1
        total_min += 60
        if self.hour > 12:
          self.hour = 1
        elif self.hour < 1:
          self.hour = 12
# set the minutes to the remaining total minutes.
      self.minutes = total_min
      print(self)
      
    ## Are two times equal?
    def __eq__(self, other):
      if self.hour == other.hour and self.minutes == other.minutes:
        return True
      else:
        return False

    ## Are two times not equal?
    def __ne__(self, other):
      not self.__eq__(other)
      
# Instantiate clocks
clock1 = Clock(1, 45)
clock2 = Clock(2, 45)

# algebra
clock1 + 100
clock1 - 45

# logic
clock1 == clock2
clock1 != clock2

