#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from pyrogram import filters
from pyrogram.types import (
InlineKeyboardMarkup,
InlineKeyboardButton,
Message,
)

from YousefMusic import app
from YousefMusic.utils.database import get_lang, set_lang
from YousefMusic.utils.decorators import ActualAdminCB, language, languageCB
from config import BANNED_USERS
from strings import get_string, languages_present

def lanuages_keyboard(_):
buttons = []

for i in languages_present:
    buttons.append(
        [
            InlineKeyboardButton(
                text=languages_present[i],
                callback_data=f"languages:{i}",
            )
        ]
    )

buttons.append(
    [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
        ),
    ]
)

return InlineKeyboardMarkup(buttons)

@app.on_message(filters.command(["lang", "setlang", "language"]) & ~BANNED_USERS)
@language
async def langs_command(client, message: Message, ):
keyboard = lanuages_keyboard()
await message.reply_text(
_["lang_1"],
reply_markup=keyboard,
)

@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
try:
await CallbackQuery.answer()
except Exception:
pass

keyboard = lanuages_keyboard(_)
return await CallbackQuery.edit_message_reply_markup(
    reply_markup=keyboard
)

@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
langauge = CallbackQuery.data.split(":")[1]

old = await get_lang(CallbackQuery.message.chat.id)

if str(old) == str(langauge):
    return await CallbackQuery.answer(
        _["lang_4"],
        show_alert=True,
    )

try:
    _ = get_string(langauge)
    await CallbackQuery.answer(
        _["lang_2"],
        show_alert=True,
    )
except Exception:
    _ = get_string(old)
    return await CallbackQuery.answer(
        _["lang_3"],
        show_alert=True,
    )

await set_lang(
    CallbackQuery.message.chat.id,
    langauge,
)

keyboard = lanuages_keyboard(_)

return await CallbackQuery.edit_message_reply_markup(
    reply_markup=keyboard
)
