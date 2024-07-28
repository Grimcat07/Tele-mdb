import os
from dotenv import load_dotenv
import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Load environment variables from .env file
load_dotenv()

OMDB_API_KEY = os.getenv('OMDB_API_KEY')
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)



# Function to start the bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I am your movie bot. Send me a movie or series name, and I will fetch its details for you.")

# Function to search for movie or series information
def search_item(message, query, type='movie'):
    response = requests.get(f'http://www.omdbapi.com/?s={query}&type={type}&apikey={OMDB_API_KEY}')
    data = response.json()

    if data['Response'] == 'True':
        markup = InlineKeyboardMarkup()
        for item in data['Search']:
            title = item['Title']
            year = item['Year']
            imdb_id = item['imdbID']
            poster_url = item['Poster'] if item['Poster'] != 'N/A' else "No poster available"
            button_text = f"{title} ({year})"
            markup.add(InlineKeyboardButton(button_text, callback_data=f"details:{imdb_id}"))
        bot.send_message(message.chat.id, "Select a title:", reply_markup=markup)
    else:
        bot.reply_to(message, 'No results found!')

# Function to show detailed item information
def show_details(message, imdb_id):
    response = requests.get(f'http://www.omdbapi.com/?i={imdb_id}&plot=full&apikey={OMDB_API_KEY}')
    data = response.json()

    if data['Response'] == 'True':
        poster = data['Poster'] if data['Poster'] != 'N/A' else "No poster available"
        reply = (
            f"Title: {data.get('Title', 'N/A')}\n"
            f"Year: {data.get('Year', 'N/A')}\n"
            f"Rated: {data.get('Rated', 'N/A')}\n"
            f"Released: {data.get('Released', 'N/A')}\n"
            f"Runtime: {data.get('Runtime', 'N/A')}\n"
            f"Genre: {data.get('Genre', 'N/A')}\n"
            f"Director: {data.get('Director', 'N/A')}\n"
            f"Writer: {data.get('Writer', 'N/A')}\n"
            f"Actors: {data.get('Actors', 'N/A')}\n"
            f"Plot: {data.get('Plot', 'N/A')}\n"
            f"Language: {data.get('Language', 'N/A')}\n"
            f"Country: {data.get('Country', 'N/A')}\n"
            f"Awards: {data.get('Awards', 'N/A')}\n"
            f"IMDB Rating: {data.get('imdbRating', 'N/A')}\n"
            f"IMDB Votes: {data.get('imdbVotes', 'N/A')}\n"
            f"Box Office: {data.get('BoxOffice', 'N/A')}\n"
            f"Production: {data.get('Production', 'N/A')}\n"
        )
        bot.send_photo(message.chat.id, poster, caption=reply)
    else:
        bot.reply_to(message, 'Details not found!')

# Function to show plot only
def show_plot(message, imdb_id):
    response = requests.get(f'http://www.omdbapi.com/?i={imdb_id}&plot=full&apikey={OMDB_API_KEY}')
    data = response.json()

    if data['Response'] == 'True':
        reply = (
            f"Title: {data.get('Title', 'N/A')}\n"
            f"Plot: {data.get('Plot', 'N/A')}\n"
        )
        bot.send_message(message.chat.id, reply)
    else:
        bot.reply_to(message, 'Plot not found!')

# Define a function to handle text messages
@bot.message_handler(func=lambda message: True)
def ask_search_option(message):
    query = message.text
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Search Movie", callback_data=f"search_movie:{query}"),
               InlineKeyboardButton("Search Series", callback_data=f"search_series:{query}"),
               InlineKeyboardButton("Get Plot (Movie)", callback_data=f"plot_movie:{query}"),
               InlineKeyboardButton("Get Plot (Series)", callback_data=f"plot_series:{query}"))
    bot.send_message(message.chat.id, "What would you like to do?", reply_markup=markup)

# Define a function to handle callback queries
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    action, query = call.data.split(":")
    if action == "search_movie":
        search_item(call.message, query, type='movie')
    elif action == "search_series":
        search_item(call.message, query, type='series')
    elif action == "plot_movie":
        search_plot(call.message, query, type='movie')
    elif action == "plot_series":
        search_plot(call.message, query, type='series')
    elif action == "details":
        show_details(call.message, query)
    elif action == "plot":
        show_plot(call.message, query)

# Function to search for plot only
def search_plot(message, query, type):
    response = requests.get(f'http://www.omdbapi.com/?s={query}&type={type}&apikey={OMDB_API_KEY}')
    data = response.json()

    if data['Response'] == 'True':
        markup = InlineKeyboardMarkup()
        for item in data['Search']:
            title = item['Title']
            year = item['Year']
            imdb_id = item['imdbID']
            button_text = f"{title} ({year})"
            markup.add(InlineKeyboardButton(button_text, callback_data=f"plot:{imdb_id}"))
        bot.send_message(message.chat.id, "Select a title for plot:", reply_markup=markup)
    else:
        bot.reply_to(message, 'No results found!')

# Run the bot
bot.polling()