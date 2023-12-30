from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup

from ..database import db


ayahModes = {
    "1": "Arabic + English",
    "2": "Arabic Only",
    "3": "English Only",
}

arabicStyles = {
    "1": "Uthmani",
    "2": "Simple",
}


async def updateSettings(u: Update, c):
    bot: Bot = c.bot
    userID = u.effective_user.id
    chatID = u.effective_chat.id

    if userID != chatID:  # if not private chat
        return

    user = db.getUser(userID)
    ayahMode = user["settings"]["ayahMode"]
    arabicStyle = user["settings"]["arabicStyle"]
    showTafsir = user["settings"]["showTafsir"]

    reply = f"""
<u><b>Settings</b></u>

<b>Ayah Mode</b>: {ayahModes[str(ayahMode)]}
<b>Arabic Style</b>: {arabicStyles[str(arabicStyle)]}
<b>Show Tafsir</b>: {["No", "Yes"][showTafsir]}
"""

    buttons = [
        [
            InlineKeyboardButton("Ayah Mode", callback_data="settings ayahMode"),
            InlineKeyboardButton("Arabic Style", callback_data="settings arabicStyle"),
        ],
        [
            InlineKeyboardButton("Show Tafsir", callback_data="settings showTafsir"),
        ],
    ]

    await bot.sendMessage(chatID, reply, reply_markup=InlineKeyboardMarkup(buttons))