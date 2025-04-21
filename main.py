import datetime

def send_reminder():
    now = datetime.datetime.now()
    print(f"تذكير بالمذاكرة! الوقت الحالي: {now.strftime('%Y-%m-%d %H:%M:%S')}")

send_reminder()
