from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

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

reciterNames = {"1": "Mishary Rashid Al-Afasy", "2": "Abu Bakr Al-Shatri"}


async def updateSettings(u: Update, c):
    """Sends the settings message to change preferences"""
    message = u.effective_message
    userID = u.effective_user.id
    chatID = u.effective_chat.id
    isGroup = chatID == userID

    if chatID != userID:  # if not private chat
        #await message.reply_html("<b>Only works in private chat!</b>")
        return

    user = db.getUser(userID)

    settings = user["settings"]
    ayahMode = settings["ayahMode"]
    arabicStyle = settings["arabicStyle"]
    showTafsir = settings["showTafsir"]
    reciter = settings["reciter"]

    reply = f"""
<u><b>Settings</b></u>

<b>Ayah Mode</b>: {ayahModes[str(ayahMode)]}
<b>Arabic Style</b>: {arabicStyles[str(arabicStyle)]}
<b>Show Tafsir</b>: {["No", "Yes"][showTafsir]}
<b>Reciter</b>: {reciterNames[str(reciter)]}
"""

    buttons = [
        [
            InlineKeyboardButton("Ayah Mode", callback_data="settings ayahMode"),
            InlineKeyboardButton("Arabic Style", callback_data="settings arabicStyle"),
        ],
        [
            InlineKeyboardButton("Show Tafsir", callback_data="settings showTafsir"),
            InlineKeyboardButton("Reciter", callback_data="settings reciter"),
        ],
    ]

    await message.reply_html(reply, reply_markup=InlineKeyboardMarkup(buttons))
