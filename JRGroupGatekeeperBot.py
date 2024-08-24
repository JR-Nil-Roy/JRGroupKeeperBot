from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram.ext import ContextTypes

# Token এবং URL
TOKEN = '7542037258:AAGMpDOX76FL2BhuZqqv8sXpC6H_T_o9cIQ'
SHARE_LINK = 'https://t.me/+MPJDzJTpeyc2MmQ9'

# Function to handle the /start command and any text message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Message text to be sent to the user
    response_message = (
        "Group Facility Not Available For You\n\n"
        "অনুগ্রহ করে লিংকটি ৩ জনের সাথে শেয়ার করুন।\n"
        "🔞 SHARE THE LINK🔞"
    )
    
    # Creating the keyboard with a share link button
    keyboard = [[InlineKeyboardButton("🔞 SHARE THE LINK🔞", url=SHARE_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Sending the message
    await update.message.reply_text(response_message, reply_markup=reply_markup)

def main() -> None:
    # Create the Application and pass it the bot's token
    application = Application.builder().token(TOKEN).build()

    # Add handler for /start command and any text message
    application.add_handler(CommandHandler('start', handle_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
