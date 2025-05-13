stroka = "1h 45m,360s,25m,30m 120s,2h 60s"
new_stroka = stroka.replace(",", " ")
new_stroka = new_stroka.split(" ")
total_minutes = 0
for time in new_stroka:
    if time[-1] == "h":
        total_minutes += int(time[:-1]) * 60
    elif time[-1] == "m":
        total_minutes += int(time[:-1])
    elif time[-1] == "s":
        total_minutes += int(time[:-1]) // 60

print(total_minutes)
