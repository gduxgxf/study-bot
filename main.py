import requests
import datetime

# توكن البوت
BOT_TOKEN = '8054601472:AAHSX4eJYUDomEv1__SQlZGr-kb4yN0HsRA'
# معرف المستخدم (User ID)
USER_ID = '1951801385'

def send_reminder():
    now = datetime.datetime.now()
    message = f"تذكير بالمذاكرة! الوقت الحالي: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": USER_ID,
        "text": message
    }
    requests.post(url, data=data)

send_reminder()
