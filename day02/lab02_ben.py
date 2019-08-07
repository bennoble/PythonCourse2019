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
      total_min = self.minutes + minutes
      while total_min >= 60:
        self.hour += 1
        total_min -= 60
        if self.hour > 12:
          self.hour = 1
        elif self.hour < 1:
          self.hour = 12
      self.minutes = 0
      self.minutes += total_min
      print(self)      
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
      total_min = self.minutes - minutes
      while total_min < 0:
        self.hour -= 1
        total_min += 60
        if self.hour > 12:
          self.hour = 1
        elif self.hour < 1:
          self.hour = 12
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
      if self.hour == other.hour and self.minutes == other.minutes:
        return False
      else:
        return True
      
# Instantiate clocks
clock1 = Clock(1, 45)
clock2 = Clock(2, 45)

# algebra
clock1 + 45
clock1 - 100

# logic
clock1 == clock2
clock1 != clock2

