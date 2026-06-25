from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_chat_member_updated(group=847)
async def WelcomeDev(client: Client, response: ChatMemberUpdated):
    dev_id = 2012962190  # ايدي المطور

    if not response.new_chat_member:
        return

    if response.from_user and response.from_user.id == dev_id:
        try:
            info = await client.get_users(dev_id)

            name = info.first_name or "Developer"
            bio = getattr(info, "bio", None) or "No Bio"

            markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton(name, user_id=dev_id)]]
            )

            await client.send_photo(
                chat_id=response.chat.id,
                photo="https://te.legra.ph/file/1fcf060f8caa21b8b5179.jpg",
                caption=f"⚡ لقد انضم مطور السورس\n\nالاسم: {name}\nالبايو: {bio}",
                reply_markup=markup
            )

        except Exception as e:
            print(f"WelcomeDev Error: {e}")
