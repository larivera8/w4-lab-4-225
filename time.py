currentTimeStr = input("What is the current time (in hours 0-24)?")       # change 23 hours to 24
waitTimeStr = input("How many hours do you want to wait")                   # close parentheses added

'''
Name error
current_time_str ==> currentTimeStr
wait_time_str ==> waitTimeStr
finalTime_Int ==> finalTimeInt

Logic error: final time shows in hours 0-23
finalTimeInt = (currentTimeInt + waitTimeInt) %24
print(finalTimeInt)
'''

currentTimeInt = int(current_time_str)
waitTimeInt = int(wait_time_str)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTime_Int)
