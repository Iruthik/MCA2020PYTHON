# 4. Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to # find sum of 2 time.

class time:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def __add__(self, other):
      hou = self.__hour + other.__hour
      mi = self.__minute + other.__minute
      se = self.__second + other.__second
      print("Sum of Time: "+str(hou)+"hour "+str(mi)+"minute "+str(se)+" seconds")
hr1 = int(input("Enter Hour in first clock:"))
min1 = int(input("Enter minute in first clock:"))
sec1 = int(input("Enter second in first clock:"))

hr2 = int(input("Enter Hour in second clock:"))
min2 = int(input("Enter minute in second clock:"))
sec2 = int(input("Enter second in second clock:"))

t1 = time(hr1,min1,sec1)
t2 = time(hr2,min2,sec2)
print(t1+t2)