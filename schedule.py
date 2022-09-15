import telebot
from telebot import types
import config
from datetime import date, datetime, timedelta

#VARIABLES
bot = telebot.TeleBot(config.TOKEN)
time_schedule = ["1. 08:00 - 08:45", "2. 08:55 - 09:40", "3. 09:50 - 10:35", "4. 10:45 - 11:30", "5. 11:40 - 12:25", "6. 12:35 - 13:20", "7. 13:30 - 14:15", "8. 14:25 - 15:10", "9. 15:20 - 16:05", "10. 16:15 - 17:00", "11. 17:10 - 17:55", "12. 18:05 - 18:50"]
schedule = [[["АУДО (31)", "АУДО (31)", "Коррупция (факульт)(56)", "Физра", "Обед", "ПС (31)", "ПС(31)", "-", "-", "-", "-", "-"], 
["ПС (31)", "ПС (31)", "БУ (23)", "БУ (23)", "Компьютерные сети (32а)", "Компьютерные сети (32а)", "Обед", "АУДО", "АУДО", "Экономика (23)", "Экономика (23)", "-"], 
["-", "-", "-", "АУДО (31)", "АУДО (31)", "СУБД (31)", "Физра", "Обед", "СУБД (31)", "Экономика (23)", "Экономика (23)", "-"], 
["-", "-", "Экономика (23)", "Экономика (23)", "БУ (23)", "БУ (23)", "Обед", "АУДО (31)", "АУДО (31)", "СУБД (31)", "СУБД (31)", "-"], 
["-", "-", "-", "Компьютерные сети (32а)", "Обед", "АУДО (31)", "АУДО (31)", "Компьютерные сети (32а)", "Физра (факульт)", "СУБД (31)", "СУБД (31)", "-"], 
["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], 
["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]],
[["АУДО (31)", "АУДО (31)", "Коррупция (факульт)(56)", "Физра", "Обед", "ПС (31)", "ПС (31)", "БУ (23)", "БУ (23)", "Экономика (23)", "Экономика (23)", "-"], 
["-", "-", "БУ (23)", "БУ (23)", "Компьютерные сети (32а)", "Компьютерные сети (32а)", "Обед", "ПС (31)", "ПС (31)", "Экономика (23)", "Экономика (23)", "-"], 
["-", "-", "-", "АУДО (31)", "АУДО (31)", "СУБД (31)", "Физра", "Обед", "СУБД (31)", "Экономика (23)", "Экономика (23)", "-"], 
["Экономика (23)", "Экономика (23)", "ПС (31)", "ПС (31)", "БУ (23)", "БУ (23)", "Обед", "АУДО (31)", "АУДО (31)", "СУБД (31)", "СУБД (31)", "-"], 
["-", "-", "-", "Компьютерные сети (32а)", "Обед", "АУДО (31)", "АУДО (31)", "Компьютерные сети (32а)", "Физра (факульт)", "СУБД (31)", "СУБД (31)", "-"], 
["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], 
["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]]
timeinterval = []
i=0
while i < len(time_schedule):
    ti = time_schedule[i][-13:].split(" - ")
    timeinterval.append([])
    j=0
    while j < 2:
        timeinterval[i].append(datetime.now().replace(hour=int(ti[j].split(":")[0]), minute=int(ti[j].split(":")[1]), second=0, microsecond=0))
        j+=1
    i+=1
print(timeinterval)

#[[08:00, 08:45], [08:55, 09:40]]
stable = [[], []]




#FUNCTIONS
def get_week_day(day):
    match day:
        case 0:
            return 'понедельник'
        case 1:
            return 'вторник'
        case 2:
            return 'среда'
        case 3:
            return 'четверг'
        case 4:
            return 'пятница'
        case 5:
            return 'суббота'
        case 6:
            return 'воскресенье'
        case _:
            return 'ХЗ'

def match_delta(delta):
    match delta:
        case -2:
            return 'Позавчера'
        case -1:
            return 'Вчера'
        case 0:
            return 'Сегодня'
        case 1:
            return 'Завтра'
        case 2:
            return 'Послезавтра'
        case _:
            return 'ХЗ'

def oneday(delta):
    global schedule, time_schedule, timeinterval
    # print(datetime.now().replace(hour=8, minute=0) < datetime.now() and datetime.now() < datetime.now().replace(hour=19, minute=0))
    day = str(datetime.now() + timedelta(days=delta)).split()[0].split("-")
    dt = date(int(day[0]), int(day[1]), int(day[2]))
    week = dt.isocalendar()[1]
    corz = 0
    txt = f'<b>{match_delta(delta)} {get_week_day(dt.weekday())}, {day[2]}.{day[1]}.{day[0]}, '
    if week%2!=0:
        corz = 0
        txt += "числитель.</b>\n"
    else:
        corz = 1
        txt += "знаменатель.</b>\n"
    dtnow = datetime.now()
    i=0
    while i<12:
        # "1. 08:00 - 08:45"
        # timeinterval = time_schedule[i][-13:].split(" - ")
        # j=0
        # while j < 2:
        #     timeinterval[j] = datetime.now().replace(hour=int(timeinterval[j].split(":")[0]), minute=int(timeinterval[j].split(":")[1]), second=0, microsecond=0)
        #     j+=1
        # print(timeinterval)
        if delta == 0:
            if i<11:
                if dtnow >= timeinterval[i][0] and dtnow <= timeinterval[i+1][0]:
                    txt += f"🚬<i><b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}</i>\n"
                elif dtnow >= timeinterval[i][0] and dtnow >= timeinterval[i+1][0]:
                    txt += f"🟢<i><b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}</i>\n"
                else:
                    txt += f"⚪️<b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}\n"
            else:
                if dtnow >= timeinterval[i][0] and dtnow <= timeinterval[i][1]:
                    txt += f"🚬<i><b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}</i>\n"
                elif dtnow >= timeinterval[i][0] and dtnow >= timeinterval[i][1]:
                    txt += f"🟢<i><b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}</i>\n"
                else:
                    txt += f"⚪️<b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}\n"
        elif delta < 0:
            txt += f"🟢<i><b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}</i>\n"
        else:
            txt += f"⚪️<b>{time_schedule[i]}</b>. {schedule[corz][dt.weekday()][i]}\n"
        i+=1
    return txt

def get_week():
    global schedule, time_schedule
    day = str(datetime.now() + timedelta(days=0)).split()[0].split("-")
    dt = date(int(day[0]), int(day[1]), int(day[2]))
    week = dt.isocalendar()[1]
    corz = 0
    txt = f'<b>Неделя '
    if week%2!=0:
        corz = 0
        txt += "числитель.</b>\n\n"
    else:
        corz = 1
        txt += "знаменатель.</b>\n\n"
    j=0
    while j<5:
        txt += f"<b>{get_week_day(j).capitalize()}</b>\n"
        i=0
        while i<12:
            txt += f"<b>{time_schedule[i]}</b>. {schedule[corz][j][i]}\n"
            i+=1
        j+=1
        txt += "\n"
    return txt

#PROCESS

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📅 Неделя")
    btn2 = types.KeyboardButton("⏺ Сегодня")
    btn3 = types.KeyboardButton("▶️ Завтра")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Привет!\n<i><b>{1.first_name}</b></i> - бот помогающий узнать расписание!\n Нажимай на кнопки которые появились внизу и узнавай какие у тебя пары :)'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📅 Неделя")
    btn2 = types.KeyboardButton("⏺ Сегодня")
    btn3 = types.KeyboardButton("▶️ Завтра")
    markup.add(btn1, btn2, btn3)
    if text.find("сегодня") != -1:
        bot.send_message(message.chat.id, oneday(0), parse_mode='html', reply_markup=markup)
    elif text.find("послезавтра") != -1:
        bot.send_message(message.chat.id, oneday(2), parse_mode='html', reply_markup=markup)
    elif text.find("завтра") != -1:
        bot.send_message(message.chat.id, oneday(1), parse_mode='html', reply_markup=markup)
    elif text.find("позавчера") != -1:
        bot.send_message(message.chat.id, oneday(-2), parse_mode='html', reply_markup=markup)
    elif text.find("вчера") != -1:
        bot.send_message(message.chat.id, oneday(-1), parse_mode='html', reply_markup=markup)
    elif text.find("неделя") != -1:
        bot.send_message(message.chat.id, get_week(), parse_mode='html', reply_markup=markup)
    elif text.find("пошел нахуй") != -1 or text.find("иди нахуй") != -1:
        bot.send_message(message.chat.id, f"{message.from_user.first_name} сам иди, петушок лохматый!", reply_markup=markup)
    else:
        pass

#STARTING
print("Bot successfully started!")
bot.polling(none_stop=True)