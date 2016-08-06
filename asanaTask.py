"""
If you have a task that you need to complete on a regular basis, you can set it up in Asana as a recurring task.
One option is to schedule the task to repeat every k weeks on specified days of the week.

It would be useful to be able to view the first n dates for which the task is scheduled.
Given the first date for which the task is scheduled, return an array of the first n dates.

In this task, you'll likely need month lengths and weekday names, provided here:

Month lengths from January to December: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

During leap years February has 29 days.
Names of weekdays: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday".

January 1, 2015 was a Thursday.

Example

For firstDate = "01/01/2015", k = 2, daysOfTheWeek = ["Monday", "Thursday"] and n = 4, the output should be

recurringTask(firstDate, k, daysOfTheWeek, n) =
   ["01/01/2015", "05/01/2015", "15/01/2015", "19/01/2015"]

firstDate falls on a Thursday. The first Monday after it is "05/01/2015".
Since k = 2, the next two days for which the task is scheduled are Thursday, January 15, and Monday, January 19.

Array containing the first n dates (including the first one) on which the task is scheduled in the chronological order.

--------------------------------------------------------------------------------

AsanaTaskDates are Objects with 4 values - (Day of Week, Month, Day, Year)

Given an initializing AsanaTaskDate, find all dates for a repeating Task accounting for leap years
"""

class AsanaTaskDate:
  def __init__(self, dayOfWeek, day, month, year):
    #Integers
    self.day = day
    self.month = month
    self.year = year

    #Integer representing Day of Week
    self.dayOfWeek = dayOfWeek

    self.dayOfWeekDict = {
      0: "Monday",
      1: "Tuesday",
      2: "Wednesday",
      3: "Thursday",
      4: "Friday",
      5: "Saturday",
      6: "Sunday"
    }

    self.monthDayDict_Regular = {
      1: 31,
      2: 28,
      3: 31,
      4: 30,
      5: 31,
      6: 30,
      7: 31,
      8: 31,
      9: 30,
      10: 31,
      11: 30,
      12: 31
    }

    self.monthDayDict_Leap = self.monthDayDict_Regular.copy()
    self.monthDayDict_Leap[2] = 29

  def getMonthDayDict(self):
    if self.isLeapYear():
      return self.monthDayDict_Leap
    return self.monthDayDict_Regular

  def isLeapYear(self):
    if self.year % 4 == 0:
      return True
    return False

  def toString(self):
    return "%s, %s/%s/%s" % (self.dayOfWeekDict[self.dayOfWeek], self.day, self.month, self.year)

  def printAsanaTaskDate(self):
    print self.toString()

  def getData(self):
    return (self.dayOfWeek, self.day, self.month, self.year)

  def copy(self):
    return AsanaTaskDate(self.dayOfWeek, self.day, self.month, self.year)

  def incrementDays(self, n):
    while n > 0:
      self.dayOfWeek = (self.dayOfWeek + 1) % 7

      monthDayDict = self.getMonthDayDict()

      if self.day < monthDayDict[self.month]:
        self.day += 1

      else:
        self.day = 1
        if self.month == 12:
          self.month = 1
          self.year += 1
        else:
          self.month += 1

      n -= 1

  def incrementWeeks(self, n):
    while n > 0:
      self.incrementDays(7)
      n -= 1

class AsanaTaskCalendar:
  def __init__(self, initDate):
    self.initDate = initDate

  def getRecurringTaskDates(self, firstDate, k, daysOfTheWeek, n):
    startDateList = self.findStartDates(firstDate, daysOfTheWeek)
    taskDateList = []
    count = 0

    while count < n:
      taskDateList.extend([date.toString() for date in startDateList])
      self.incrementDates(startDateList, k)
      count += len(startDateList)

    print taskDateList[:n]

  def findStartDates(self, firstDate, daysOfTheWeek):
    startDateList = []

    currDate = firstDate.copy()
    remainingDaysOfTheWeek = set(daysOfTheWeek)

    while len(remainingDaysOfTheWeek) > 0:
      if currDate.dayOfWeek in remainingDaysOfTheWeek:
        startDateList.append(currDate.copy())
        remainingDaysOfTheWeek.remove(currDate.dayOfWeek)

      currDate.incrementDays(1)
    return startDateList

  def incrementDates(self, currDateList, k):
    for date in currDateList:
      date.incrementWeeks(k)

d1 = AsanaTaskDate(3, 1, 1, 2015)
atc = AsanaTaskCalendar(d1)
atc.getRecurringTaskDates(d1, 2, [0,3], 100000)
