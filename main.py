import telebot
import datetime
import time
import threading
import random

BOT_TOKEN = '8054601472:AAHSX4eJYUDomEv1__SQlZGr-kb4yN0HsRA'
CHAT_ID = '1951801385'

bot = telebot.TeleBot(BOT_TOKEN)

def send_message(text):
    bot.send_message(CHAT_ID, text)

def format_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def schedule_reminders():
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        day = now.strftime("%A")

        # تذكيرات يومية
        if day in ["Friday", "Saturday"] and current_time == "04:00":
            send_message("صباح النور! قعدتي مع الأذان؟ يلا نبدأ إنجازنا من بدري.")

        if day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"] and current_time == "12:00":
            send_message("يلا نبدأ المذاكرة، شمس معك!")

        if current_time == "15:30":
            send_message("صلّيتي؟ لا تنسين الأذكار والموية.")

        if current_time == "22:30":
            send_message("وقت الراحة! اكتبي إنجازاتك اليوم ونامي مبسوطة.")

        if current_time in ["14:00", "18:00"]:
            support = random.choice([
                "شمس تقولك: تذكّري ليش بدأنا!",
                "كل صفحة تكتبينها اليوم، تفتح لك باب جديد.",
                "خذي نفس عميق… وتذكّري إنك قدها.",
                "شربي موية وتعالي نكمل سوا.",
                "فكري: وش تبين تحققين قبل النوم؟"
            ])
            send_message(support)

        if day == "Thursday" and current_time == "21:00":
            send_message("تقييم أسبوعك مع شمس:\n- وش أكثر شي فخورة فيه؟\n- وش اللي ما ظبط؟\n- وش تبين تطورينه الأسبوع الجاي؟")

        time.sleep(60)

# تشغيل الجدولة
threading.Thread(target=schedule_reminders).start()

# أوامر خاصة
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "هلا! أنا شمسك، صديقتك اللي تذكّرك وتسولف معك.")

@bot.message_handler(commands=['تقييمي'])
def send_review(message):
    bot.reply_to(message, "سؤال تقييم اليوم:\n1. كيف شعورك؟\n2. وش أكثر شي فخورة فيه؟\n3. وش تبين تحسنينه بكرة؟")

@bot.message_handler(commands=['جدولي'])
def send_schedule(message):
    bot.reply_to(message, "روتينك مع شمس:\n- صلاة وقرآن وموية\n- جلستين مذاكرة\n- بريك\n- إنجازات ونوم بسلام.")

@bot.message_handler(commands=['مكافأتي'])
def send_reward(message):
    rewards = [
        "كوب كوفي وفلم؟ تستاهلين!",
        "روحي تمشّي وانسي العالم شوي.",
        "أغنية تحبينها بصوت عالي؟ يلااا.",
        "افتحي تيك خفيف، بس دقايق.",
        "شمّي بخور تحبينه، تستاهلين راحة.",
        "رسمي شي بسيط، حتى لو خربوطة!",
        "غفي غفوة قصيرة، هذي فوز.",
        "اكتبي لنفسك رسالة حب.",
        "احضني مخدتك وشغّلي بودكاست حلو.",
        "شمس تقول: حتى الراحة إنجاز."
    ]
    bot.reply_to(message, random.choice(rewards))

@bot.message_handler(commands=['نصيحتي'])
def send_tip(message):
    tips = [
        "الانضباط أهم من الحماس اللحظي.",
        "صفحة اليوم تبني ثقة بكرة.",
        "المقارنة تسرقك، راقبي نفسك بس.",
        "إذا تعبتي، خذي بريك مو استسلام.",
        "كل شي تبينه، تبينه لأسباب عظيمة.",
        "بدلي فكرة مزعجة بكلمة حلوة.",
        "ركزي على خطوة، مو السلم كامل.",
        "كوني حنونة مع نفسك أكثر من أي أحد.",
        "الهدف الكبير يصير سهل بخطوات صغيرة.",
        "كل إنجاز صغير يراكم نجاح كبير."
    ]
    bot.reply_to(message, random.choice(tips))

@bot.message_handler(commands=['فكرتي'])
def send_fun_idea(message):
    ideas = [
        "اربطِي المعلومة بقصة غريبة!",
        "اكتبيها بخط مجنون وخربشي حولها.",
        "ارقصي المعلومة، لو لحالك!",
        "سوي اختبار وهمي لنفسك.",
        "شرحي المعلومة لأختك الصغيرة، حتى لو مو فاهمة.",
        "لوني الجدول كأنك تسوين خريطة كنز.",
        "سجلي صوتك وانتي تشرحين، وارجعي اسمعيه.",
        "سوي عرض بوربوينت كأنك معلمة.",
        "خلي المعلومات شخصيات وتخيليهم يتكلمون.",
        "اكتبي نكتة مرتبطة بالمعلومة!"
    ]
    bot.reply_to(message, random.choice(ideas))

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    now = format_time()
    bot.reply_to(message, f"سمعتك الساعة {now}، وش تبين أقول لك؟")

print("شمسك جاهزة طول اليوم!")
bot.infinity_polling()
reminder_messages = [
    "وينك؟ شمس تشتاق لك!",
    "مرّ وقت كثير بدون إنجاز… ترجعين؟",
    "أنا هنا دايم، بس ودي أسمع صوتك.",
    "كل دقيقة تنحسب، نبدأ؟",
    "تدرين؟ حتى لو شوي، المهم نتحرك!",
    "قومي قولي لي وش بنسوي الحين؟",
    "تذكري: الوقت مثل الرمل… يطيح بدون ما نحس."
]
