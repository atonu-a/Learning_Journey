from datetime import datetime, timedelta

# today = datetime.today().date()
# tomorrow = today + timedelta(days=1)
# yesterday = today - timedelta(days=1)
# now = datetime.now()
# new_time = now + timedelta(hours=10, minutes=4, seconds=10)


# print(now , new_time)
# print(today, tomorrow, yesterday) #2026-09-28 2026-09-29 2026-09-27

now  = datetime.now()
meeting = datetime(2026, 9, 30)

diff = meeting - now
print(diff)