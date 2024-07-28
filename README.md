```markdown
# Tele-mdb
Search for movies and series using a telegram bot 

# Movie Info Telegram Bot

This is a Telegram bot that allows users to search for movie and TV series information, including details like the cast, reviews, plot, and posters. The bot fetches data from the OMDB API.

## Features

- Search for movies and TV series by name.
- Retrieve detailed information about a specific movie or series, including the full plot, cast, and more.
- Display movie posters in the search results.
- Interactive inline keyboard for easy navigation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have a Telegram account.
- You have a bot token from the [Telegram BotFather](https://core.telegram.org/bots#6-botfather).
- You have an API key from [OMDB API](http://www.omdbapi.com/apikey.aspx).

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a `.env` file in the project directory and add your credentials:**

   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OMDB_API_KEY=your_omdb_api_key
   ```

## Usage

1. **Run the bot:**

   ```sh
   python bot.py
   ```

2. **Interact with the bot on Telegram:**

   - Search for movies or TV series by sending a message.
   - Use the inline keyboard to get detailed information or view posters.

## Project Structure

```plaintext
.
├── Tele.py
├── .env
├── .gitignore
├── README.md
```

- `Tele.py`: The main script that runs the Telegram bot.
- `.env`: File containing your bot token and API key (not included in the repository).
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file, providing an overview and instructions for the project.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [OMDB API](http://www.omdbapi.com/) for providing movie and TV series data.
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) for the Telegram bot API wrapper.

## Disclaimer

This project is created purely for fun and learning purposes. No further development or maintenance is planned.

Replace `"yourusername"`, `"your-repo-name"`, `"your_telegram_bot_token"`, and `"your_omdb_api_key"` with your actual GitHub username, repository name, and API tokens.
```
