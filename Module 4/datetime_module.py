import datetime

now = datetime.datetime.now() #ekhon er date time microsecond soho ene debe
today_date = datetime.date.today() # Only date
now_time = datetime.datetime.now().time() #Only time

date = datetime.datetime(2026, 10, 21) #Custom date without time
time = datetime.datetime(2026, 10, 21, 5, 26) #Custom date with time

formatted_date = now.strftime("%Y/%m/%d %H:%M:%S") #Fromatting datetime
formatted_date1 = now.strftime("%y/%m/%d %H:%M:%S") # print 26 instead of 09 because of b
formatted_date2 = now.strftime("%y/%b/%d %H:%M:%S") # print sept instead of 2026 because of y
formatted_date3 = now.strftime("%y/%B/%d %H:%M:%S") # print September instead of 2026 because of y
formatted_date4 = now.strftime("%y/%B/%d %A %H:%M:%S") #Using A for Day (Monday) and a for short form (Mon)

formatted_time1 = now_time.strftime("%I:%M:%S") #Shows 12 hour formate instead of 24
formatted_time = now_time.strftime("%I:%M:%S %p") #using p it shows the am or pm

formatted_date5 = "26-09-2028 10:17:54"
parsed_date = datetime.datetime.strptime(formatted_date5, "%d-%m-%Y %I:%M:%S")



print(formatted_date5)
print(parsed_date)
# print(formatted_date1) #26/09/28 17:17:54
# print(time) #2026-10-21 05:26:00
# print(date) # 2026-10-21 00:00:00
# print(now_time) #17:17:54.129817
# print(now) # 2026-09-28 17:17:54.129774
# print(today_date) #2026-09-28