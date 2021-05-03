time_sec = int(input("Enter the time in sec: "))
hours = time_sec // 3600
minutes = (time_sec - hours * 3600) // 60
seconds = time_sec - (hours * 3600 + minutes * 60)
print(f"The time is:  {hours} : {minutes} : {seconds}")
