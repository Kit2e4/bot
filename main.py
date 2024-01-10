import telebot
from telebot import types

bot = telebot.TeleBot('6523388800:AAG2bmOT2EcSYbk2Z5osIsayl7qoQydjm0E')  

up = 0

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Аккредитивы')
    btn2 = types.KeyboardButton('Вклад')
    btn3 = types.KeyboardButton('Карты')
    btn4 = types.KeyboardButton('Кредиты')
    btn5 = types.KeyboardButton('Посылки')
    btn6 = types.KeyboardButton('Прайм')
    btn7 = types.KeyboardButton('Страховка')
    btn8 = types.KeyboardButton('Другое')
    btn9 = types.KeyboardButton('Расчитать')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    markup.add(btn9)

    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):

    if message.chat.type == 'private':
        if message.text == 'Аккредитивы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Открыл')
            btn2 = types.KeyboardButton('Раскрыл')
            btn3 = types.KeyboardButton('Домой')

            markup.add(btn1, btn2)
            markup.add(btn3)
            bot.send_message(message.chat.id, 'Что вы сделали с аккредитивами?', reply_markup=markup)
# Это для аккредитива
        elif message.text == 'Открыл':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id, 'Сколько вы открыли аккредитивов?', reply_markup=markup)
            bot.register_next_step_handler(message, process_opened_accr)
        elif message.text == 'Раскрыл':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы расскрыли аккредитивов?', reply_markup=markup)
            bot.register_next_step_handler(message, process_rask_accr)
# Это для вклада
        elif message.text == 'Вклад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id,'Сколько выдали вкладов?', reply_markup=markup)
            bot.register_next_step_handler(message, otk_vkl)
            
# Это для карт            
        elif message.text == 'Карты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Дебетовая')
            btn2 = types.KeyboardButton('Кредитная')
            btn3 = types.KeyboardButton('Детская')
            btn4 = types.KeyboardButton('Домой')

            markup.add(btn1, btn2,btn3,btn4)
            bot.send_message(message.chat.id,'Какая карта?', reply_markup=markup)
# Для дебетовых
        elif message.text == 'Дебетовая':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Выдал готовую карту')
            btn2 = types.KeyboardButton('Оформил именную карту')
            btn3 = types.KeyboardButton('Оформил моментальную карту')
            btn4 = types.KeyboardButton('Домой')

            markup.add(btn1, btn2,btn3)
            markup.add(btn4)

            bot.send_message(message.chat.id,'Что вы сделали?', reply_markup=markup)

        elif message.text == 'Выдал готовую карту':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы выдали готовых карт?',reply_markup=markup)
            bot.register_next_step_handler(message, vid_g_k)
        elif message.text == 'Оформил именную карту':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id, 'Сколько вы оформили именных карт?', reply_markup=markup)
            bot.register_next_step_handler(message, of_i_d_k)    
        elif message.text == 'Оформил моментальную карту':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили моментальных карт?', reply_markup=markup)
            bot.register_next_step_handler(message, of_m_d_k)
# Для кредитных 
        elif message.text == 'Кредитная':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Выдал готовую КК')
            btn2 = types.KeyboardButton('Оформил именную КК')
            btn3 = types.KeyboardButton('Оформил моментальную КК')
            btn4 = types.KeyboardButton('Домой')

            markup.add(btn1, btn2,btn3)
            markup.add(btn4)

            bot.send_message(message.chat.id,'Что вы сделали?', reply_markup=markup)

        elif message.text == 'Выдал КК':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id, 'Сколько вы выдали готовых карт?',reply_markup=markup)
            bot.register_next_step_handler(message, vid_k_k)

        elif message.text == 'Оформил именную КК':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id, 'Сколько вы оформили именных КК?',reply_markup=markup)
            bot.register_next_step_handler(message, of_i_k_k)    
        elif message.text == 'Оформил моментальную КК':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили моментальных карт?',reply_markup=markup)
            bot.register_next_step_handler(message, of_m_k_k)
# Для детских    
        elif message.text == 'Детская':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id,'Сколько выдали Детских карт?', reply_markup=markup)
            bot.register_next_step_handler(message, det_k)
# Кредиты
        elif message.text == 'Кредиты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Выдача жилищного кредита')
            btn2 = types.KeyboardButton('Оформление заявки на получение ипотеки')
            btn3 = types.KeyboardButton('Оформление заявки на получение ПК')
            btn4 = types.KeyboardButton('Домой')

            markup.add(btn1, btn2, btn3)
            markup.add(btn4)
        elif message.text == 'Выдача жилищного кредита':
            bot.send_message(message.chat.id, 'Сколько вы оформили жилищных кредитов?')
            bot.register_next_step_handler(message, of_j_k)

        elif message.text == 'Оформление заявки на получение ипотеки':
            bot.send_message(message.chat.id, 'Сколько вы оформили ипотек?')
            bot.register_next_step_handler(message, of_ip)

        elif message.text == 'Оформление заявки на получение ПК':
            bot.send_message(message.chat.id, 'Сколько вы оформили заявок на получение ПК?')
            bot.register_next_step_handler(message, of_pk)
# Для посылок
        elif message.text == 'Посылки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id, 'Сколько посылок выдали и отправили?',reply_markup = markup)
            bot.register_next_step_handler(message, of_pos)

# Для прайма
        elif message.text == 'Прайм':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Прайм Старт')
            btn2 = types.KeyboardButton('Обычный прайм')
            btn3 = types.KeyboardButton('Прайм+ на год')
            btn4 = types.KeyboardButton('Прайм+ на месяц')
            btn5 = types.KeyboardButton('Домой')

            markup.add(btn1, btn2, btn3, btn4,btn5)

            bot.send_message(message.chat.id,'Что за прайм?)', reply_markup=markup)
# Прайм старт
        elif message.text == 'Прайм старт':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько подключили Прайм Старт?', reply_markup=markup)
            bot.register_next_step_handler(message, pr_st)

        elif message.text == 'Обычный прайм':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили праймов?', reply_markup=markup)
            bot.register_next_step_handler(message, pr)

        elif message.text == 'Прайм+ на год':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)

            bot.send_message(message.chat.id, 'Сколько вы оформили Прайм+ на год?', reply_markup=markup)
            bot.register_next_step_handler(message, prp)

        elif message.text == 'Прайм+ на месяц':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили Прайм+ на год?',reply_markup=markup)
            bot.register_next_step_handler(message, prpm)

# Для Страховок
        elif message.text == 'Страховка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Защита на любой случай (до 3000 руб.)')
            btn2 = types.KeyboardButton('Страхование жизни (ипотека)')
            btn3 = types.KeyboardButton('Страхование залога (ипотека)')
            btn4 = types.KeyboardButton('Страховой конструктор (2 опции)')
            btn5 = types.KeyboardButton('Домой')

            markup.add(btn1, btn2, btn3, btn4)
            markup.add(btn5)

            bot.send_message(message.chat.id,'Что ты сегодня сделал?', reply_markup=markup)

        elif message.text == 'Защита на любой случай (до 3000 руб.)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили Защита на любой случай (до 3000 руб.)?',reply_markup=markup)
            bot.register_next_step_handler(message, zls_d3000)

        elif message.text == 'Страхование жизни (ипотека)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили Страхование жизни (ипотека)',reply_markup=markup)
            bot.register_next_step_handler(message, sz_i)

        elif message.text == 'Страхование залога (ипотека)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили Страхование залога (ипотека)',reply_markup=markup)
            bot.register_next_step_handler(message, szs_i)

        elif message.text == 'Страховой конструктор (2 опции)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы оформили Страховой конструктор (2 опции)',reply_markup=markup)
            bot.register_next_step_handler(message, sk)

        elif message.text == 'Другое':
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Сбол IOS')
            btn2 = types.KeyboardButton('Домой')

            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(message.chat.id, 'Выберете действие',reply_markup=markup)

        elif message.text == 'Сбол IOS':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('Домой')

            markup.add(btn1)
            bot.send_message(message.chat.id, 'Сколько вы установили СБОЛ на Айфон?',reply_markup=markup)
            bot.register_next_step_handler(message, sbol)
        
        elif message.text == 'Расчитать':
                global up
                bot.send_message(message.chat.id, 'УП: {:.2f}'.format(up)) 

        elif message.text == 'Домой':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Аккредитивы')
            btn2 = types.KeyboardButton('Вклад')
            btn3 = types.KeyboardButton('Карты')
            btn4 = types.KeyboardButton('Кредиты')
            btn5 = types.KeyboardButton('Посылки')
            btn6 = types.KeyboardButton('Прайм')
            btn7 = types.KeyboardButton('Страховка')
            btn8 = types.KeyboardButton('Другое')
            btn9 = types.KeyboardButton('Расчитать')

            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
            markup.add(btn9)

            bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)
# ________________________________________________________________________________________________________________________________________
# Функция для обработки введенного пользователем количества открытых аккредитивов
def process_opened_accr(message):
    global o_a,up

    try:
        x_o_a = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return

    up_1 = 0.2
    o_a = x_o_a * up_1
    up += o_a

# Функция для обработки введенного пользователем количества раскрытых аккредитивов    
def process_rask_accr(message):
    global r_a,up

    try:
        x_r_a = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return

    up_2 = 0.3
    r_a = x_r_a * up_2 
    up += r_a
# Открытие вклада    
def otk_vkl(message):
    global o_a,up

    try:
        x_o_a = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return

    up_3 = 0.23
    o_a = x_o_a * up_3 
    up += o_a
# Выдача готовой карты
def vid_g_k(message):
    global v_g_k, up

    try:
      x_g_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_4 = 0.14
    vid_g_k = x_g_k * up_4
    up += vid_g_k
# Новая именная дебетовая карта
def of_i_d_k(message):
    global i_d_k, up

    try:
      x_v_d_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_5 = 0.29
    of_i_d_k = x_v_d_k * up_5
    up += of_i_d_k
def of_m_d_k(message):
    global m_d_k, up
# Новая моментальная дебетовая карта
    try:
      x_m_d_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_6 = 0.23
    of_m_d_k = x_m_d_k * up_6
    up += of_m_d_k
# Готовая КК
def vid_k_k(message):
    global v_k_k, up

    try:
      x_k_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_7 = 0.14
    vid_k_k = x_k_k * up_7
    up += vid_k_k
# Новая именная КК
def of_i_k_k(message):
    global i_k_k, up

    try:
      x_v_k_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_8 = 1.33
    of_i_k_k = x_v_k_k * up_8
    up += of_i_k_k
# Новая моментальная КК
def of_m_k_k(message):
    global m_k_k, up
    try:
      x_m_k_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_9 = 1.33
    of_m_k_k = x_m_k_k * up_9
    up += of_m_k_k 
# Для детских карт
def det_k(message):
    global det_k, up
    try:
      x_det_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_10 = 0.23
    v_det_k = x_det_k * up_10
    up += v_det_k
# Для оформления жилищного кредита
def of_j_k(message):
    global of_j_k, up
    try:
      x_j_k = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_11 = 1.8
    of_j_k = x_j_k * up_11
    up += of_j_k
# Для ипотек 
def of_ip(message):
    global of_ip, up
    try:
      x_ip = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_12 = 1.2
    of_ip = x_ip * up_12
    up += of_ip
# Для ПК 
def of_pk(message):
    global of_pk, up
    try:
      x_pk = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_13 = 1.0
    of_pk = x_pk * up_13
    up += of_pk
# Для посылок
def of_pos(message):
    global of_pos, up
    try:
      x_pos = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_14 = 0.06
    of_pos = x_pos * up_14
    up += of_pos
# Для прайма старт
def pr_st(message):
    global pr_st, up
    try:
      x_pr_st = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_15 = 0.2
    pr_st = x_pr_st * up_15
    up += pr_st
# Для прайма обычного
def pr(message):
    global pr, up
    try:
      x_pr = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_16 = 0.5
    pr = x_pr * up_16
    up += pr
# Для прайма+ на год
def prp(message):
    global prp, up
    try:
      x_prp = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_17 = 0.5
    prp = x_prp * up_17
    up += prp
# Для прайм+ на месяц
def prpm(message):
    global prpm, up
    try:
      x_prpm = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_18 = 0.2
    prpm = x_prpm * up_18
    up += prpm
# Для ЗЛС до 3000р.
def zls_d3000(message):
    global zls_d3000, up
    try:
      x_zls_d3000 = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_19 = 0.2
    zls_d3000 = x_zls_d3000 * up_19
    up += zls_d3000
# Для Страхование жизни (ипотека)
def sz_i(message):
    global sz_i, up
    try:
      x_sz_i = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_20 = 0.3
    sz_i = x_sz_i * up_20
    up += sz_i
# Для Страхование жизни (ипотека)
def szs_i(message):
    global szs_i, up
    try:
      x_szs_i = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_21 = 0.6
    szs_i = x_szs_i * up_21
    up += szs_i
# Для страхового конструктора
def sk(message):
    global sk, up
    try:
      x_sk = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_22 = 1
    sk = x_sk * up_22
    up += sk
# Для Сбол на ios
def sbol(message):
    global sbol, up
    try:
      x_sbol = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите целое число.')
        return
    up_23 = 0.12
    sbol = x_sbol * up_23
    up += sbol

bot.polling(none_stop=True)
