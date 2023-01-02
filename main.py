import telebot
import random
# ідентифікатори повідомлень
# message.from_user.first_name - перше ім'я користувача (ім'я)
# message.from_user.last_name - друге ім'я користувача (прізвище)
# message.from_user.username - псевдонім користувача
# message.text - отримати текст з посилання

# Створюємо об'єкт бота
bot = telebot.TeleBot("5815303250:AAEyVTo1g1xwMO96NabBULGwiiOLXHD0-OA")
# Обробник повідомлень
@bot.message_handler(commands=["start", "hello"])
# Створюємо функцію обробника
def bot_start(message):
    # Відправник повідомлень
    bot.send_message(message.chat.id, "Hello, User! My name is IntensiveRandomBot!", reply_markup = keyboard)
    bot.register_next_step_handler(message, all_commands)
# Створюємо кнопку Play
button_play = telebot.types.KeyboardButton("Play")
# Створюємо клавіатуру
keyboard = telebot.types.ReplyKeyboardMarkup()
# Додаємо до клавіатури створену кнопку
keyboard.add(button_play)
#
space = " "
# Функція що виконує команди бота
def all_commands(message):
    if message.text.lower() == "play":
        number = random.randint(1,2)
        button_1 = telebot.types.KeyboardButton("1")
        button_2 = telebot.types.KeyboardButton("2")
        keyboard_2 = telebot.types.ReplyKeyboardMarkup()
        keyboard_2.add(button_1, button_2)
        bot.send_message(message.chat.id, f"Game started!\n{space*50}/hi", reply_markup = keyboard_2)
        # Реєструємо наступний крок користувача, який натискає на один з варіантів видповідей
        bot.register_next_step_handler(message, win_lose, number)
    if message.text.lower() == "/hi":
        bot.send_message(message.chat.id, f"Nice, to meet you! {message.from_user.username}!")
    bot.register_next_step_handler(message, all_commands)
# Створюємо функцію що перевіряє виграв чи програв користувач
def win_lose(message, number):
    # Якщо вгадали число, то перемогли
    if message.text.lower() == str(number):
        bot.send_message(message.chat.id, f"Congratulations {message.from_user.first_name}, you guessed!", reply_markup = keyboard)
    # Якщо не вгадав число, то програв
    if message.text.lower() != str(number):
        bot.send_message(message.chat.id, f"Sorry {message.from_user.first_name}, you don`t guessed!", reply_markup = keyboard)
    
# Опитування всіх чатів
bot.polling()