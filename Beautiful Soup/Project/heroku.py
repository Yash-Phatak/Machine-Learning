from datetime import datetime
  
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

if current_time == "00:00:00":
    print("Tada!!!")
    print("Current Time =", current_time)