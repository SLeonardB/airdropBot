from telegram.ext import Application, CommandHandler

import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Welcome to the FlowMint Airdrop giveaway Bot.")

async def airdrop(update, context):
    await update.message.reply_text(
            """
Register and verify your FM wallet.
Receive free airdrop and centidrop(tenth an airdrop) when you refer a user and they join.
Refer more users to receive more centidrops when they join.
            """)

async def balance(update, context):
    await update.message.reply_text(
            """
Name: {fm_username}
FM wallet address: {fm_wallet_address}
Referrals: {referrals}
Airdrop status: {airdrop_status}
Centidrops received: {centidrops_total}
Balance: {fm_balance}
            """)

async def help_cmd(update, context):
    await update.message.reply_text(
            """
Commands: /start /airdrop /balance.
Restart the bot in case of failure.
Email developer for support: sleonardbilly23@gmail.com
            """)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("airdrop", airdrop))
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("help", help_cmd))

app.run_polling()

