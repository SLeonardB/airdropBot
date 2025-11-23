# Telegram Airdrop Bot Version 1
  _At an Initial Coin Offering(ICO), this code can create a telegram bot to automate an airdrop giveaway to users who are interested in the currency.
  New users can register with the bot, receive and verify their FM wallets and are required to refer at least one other user. The referrer receives centidrops( a tenth of the FM airdrop) when the referred user(s) joins.
  Existing users can refer new users and do receive centidrops once the new register and verify their FM wallets._

  ## Running the bot
  ### With python and pip installed, clone the repository. Move into the git directory.
  ```
  $ python -m venv botEnv;
    source botEnv/bin/activate; source botEnv/Scripts/activate on Windows;
    pip install -r requirements.txt;
    python bot/main.py
  ```
  ### Tested on: _Linux, Termux_
  ### Technologies used:
  - _Telegram Bot API through python-telegram-bot module._
  - _Python FastAPI for asynchronous backend logic._
  - _Sqlite database for bot and user data._
  - _Linux cron for persistence on deployment server._
  - _ReactJs for interactive web dashboard._
  - _Telegram mini web app similar in function to the web dashboard._

  ## Any Other Business:
  - The code can be _altered_ to meet similar use cases with various giveaway flows.
  - The sample crypto-currency coin used: _FlowMint(FM) Coin_.
  - The sample coin Telegram channel link for proof of concept: [_Official FlowMint Coin Announcements Channel._](https://t.me/flowmintcoin)
  - The sample Telegram bot username to check out for deployed bot: _@FlowMintDropBot_
  - Email improvements to [_developer_.](https://sleonardb.github.io/home/)
  - Ideas to expand the bot are welcome especially concerning smart contract and Blockchain functionality.
  - This code is for _demonstration_ purposes only. A real crypto-currency network is to be used in more sophisticated versions of the Bot.
  
  ### Author
  * _Leonard Billy Ssekanjako_
  * _Date: Sunday, 23rd November, 2025 at 01 30 hours._
