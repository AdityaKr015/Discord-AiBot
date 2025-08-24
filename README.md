# Discord Gemini AI Bot

Hello world,this is my first personal project where i build a Discord Bot which is just powered by Google's Gemini Ai. Its basically Gemini Ai but in Discord bot format.I used Google's Gemini AI (`gemini-1.5-pro-002`) to generate intelligent conversations based on user inputs, with short-term memory support.

## Features
- 🤖 Powered by Gemini Pro AI (Google Generative AI API)
- 🧠 Remembers last 5 messages per user for smarter conversations
- 💬 Responds to users via `!ask` command
- 🕒 Shows "typing..." indicator while processing
- 🔒 Secure API key and token management using `.env` file

## Requirements
- Python 3.8 or higher
- `discord.py`
- `google-generativeai`
- `python-dotenv`

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2. **Install dependencies:**

   pip install -r requirements.txt

3. **Create a .env file in the project root and add your keys:**
 
   DISCORD_TOKEN=your_discord_bot_token_here
  
   GEMINI_API_KEY=your_gemini_api_key_here

5. **Run the bot:**

   python main.py     
