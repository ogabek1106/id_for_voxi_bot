import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 🔐 Use your bot token directly or with environment variable
TOKEN = "7613232669:AAFcN-5qh6wX9uGlxUsFnFNV-_fA7VCg0ug"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def handle_docs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    if doc:
        await update.message.reply_text(
            f"📁 File ID:\n`{doc.file_id}`",
            parse_mode="Markdown"
        )
        logger.info(f"Received file: {doc.file_name} | ID: {doc.file_id}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, handle_docs))

logger.info("Bot started.")
app.run_polling()
