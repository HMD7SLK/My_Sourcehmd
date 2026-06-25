
from YousefMusic.utils.database import (
    get_served_chats,
    get_served_users,
    get_client,
    set_must,
    get_must,
    del_must,
    get_must_ch,
    set_must_ch,
    get_active_chats,
    remove_active_video_chat,
    remove_active_chat,
    set_bot_name,
    get_bot_name,
)
from pyrogram.enums import ParseMode
import shutil
import asyncio
import random 

devs = filters.user([6094238403,6931657587,OWNER_ID])

@app.on_message(filters.command(["start"]) & filters.private & devs, group = 2)
async def start_dev(c, msg):
    keyboard = ReplyKeyboardMarkup([[("{ تعيين اسم البوت }")], [("{ مطورين السورس }")], [("{ قسم الاحصائيات }"), ("{ قسم المساعد }")], [("{ قسم الاشتراك الاجباري }"), ("{ قسم الاذاعه }")], [("{ حذف الكيبورد }")]], resize_keyboard=True)
    await msg.reply("<b>• اهلا بك حبيبي المطور◟</b>", reply_markup = keyboard)
    
@app.on_message(filters.command(["{ حذف الكيبورد }"],"") & filters.private & devs, group = 2)
async def delete_keyboard(c,msg):
    await msg.reply("<b>• تم ازالة الكيبورد عزيزي المطور ◟</b>", reply_markup = ReplyKeyboardRemove())

@app.on_message(filters.command(["{ قسم الاحصائيات }"],"") & filters.private & devs, group = 2)
async def stats_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم الاحصائيات ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• الكروبات •"), ("• المستخدمين •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))
    
@app.on_message(filters.command(["{ قسم المساعد }"],"") & filters.private & devs, group = 2)
async def asisstant_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم حساب المساعد ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• تغيير الاسم الاول •"), ("• تغيير الاسم الثاني •")], [("• تغيير البايو •")], [("• اضف صورة •"), ("• مسح الصورة •")], [("• اذاعة •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["{ قسم الاشتراك الاجباري }"],"") & filters.private & devs, group = 2)
async def force_sub_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم الاشتراك الاجباري ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• قناة الاشتراك •")], [("• اضف قناة/كروب •"), ("• حذف القناه/الكروب •")], [("• تفعيل الاشتراك •"), ("• تعطيل الاشتراك •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["{ قسم الاذاعه }"],"") & filters.private & devs, group = 2)
async def broadcast_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم الاذاعه ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• للكروبات •"), ("• للمستخدمين •")], [("• بالتوجيه للكروبات •"), ("• بالتوجيه للمستخدمين •")], [("• ترويج البوت •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["{ رجوع للقائمة الرئيسية }"],"") & filters.private & devs, group = 2)
async def start_dev(c, msg):
    keyboard = ReplyKeyboardMarkup([[("{ تعيين اسم البوت }")], [("{ مطورين السورس }")], [("{ قسم الاحصائيات }"), ("{ قسم المساعد }")], [("{ قسم الاشتراك الاجباري }"), ("{ قسم الاذاعه }")], [("{ حذف الكيبورد }")]], resize_keyboard=True)
    await msg.reply("<b>• اهلا بك حبيبي المطور◟</b>", reply_markup = keyboard)

from asyncio import gather

@app.on_message(filters.command(["• الكروبات •", "• المستخدمين •"], "") & filters.private & devs, group=2)
async def stat_bot(c: Client, msg):
    if msg.text == "• المستخدمين •":
        # استدعاء الدالة في الخلفية
        served_users, _ = await gather(
            get_served_users(c),
            get_served_chats(c)
        )
        return await msg.reply(f"<b>• عدد مستخدمين البوت : {len(served_users)} ◟</b>")
    else:
        _, served_chats = await gather(
            get_served_users(c),
            get_served_chats(c)
        )
        return await msg.reply(f"<b>• عدد كروبات البوت : {len(served_chats)} ◟</b>")

bot = [
    "<b>عوفني بحالي</b>",
    "<b>انت البوت امشي ولي 😂</b>",
    "<b>گول شرايد</b>",
    "<b>تحجي شرايد ؟ لو اكتمك 🌚</b>",
    "<b>قلب {}</b>",
    "<b>نعم يقلب {}</b>",
    "<b>شبيك ولك ؟ صار ساعه تصيح</b>",
    "<b>دكوم بيه</b>",
    "<b>نجب</b>",
    "<b>بذمتك اذا انت بدالي تقبل يسوون بيك هيج ؟</b>",
]

selections = [
    "<b>اسمي {} ولك</b>",
    "<b>كافي كتلك اسمي {}</b>",
    "<b>نعم</b>",
    "<b>گول</b>",
    "<b>راسي صار يوجعني من وراك امشي ولي</b>",
    "<b>يعم والله بحبك بس ناديلي {}</b>",
    "<b>تدري راح احبك اكتر لو ناديتلي {}</b>",
    "<b>اسكت كافي دوختني</b>",
    "<b>عيون {} </b>",
    "<b>ما فارغ لك ولي</b>",
    "<b>كالعادة مزعليه و يجي يمي 😔</b>",
    "<b>ولك احجي شرايد</b>",
    "<b>شكلها منكدا عليك وجاي تطلعهم علينا</b>",
    "<b>ورحمه ابويا اسمي {}</b>",
]

@app.on_message(filters.command("{ تعيين اسم البوت }", ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id,"<b> ⌔︙ ارسل اسم البوت الجديد الان .</b>", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("<b> ⌔︙ تم تعين اسم البوت بنجاح </b>.")
   
@must_join_ch
@app.on_message(filters.command(["بوت", "البوت"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    
    # تحقق من طول الرسالة
    print(f"Length of message: {len(bar)}")
    
    await message.reply_text(f"<a href='https://t.me/{bot_username}?startgroup=True'>{bar}</a>", disable_web_page_preview=True)

@app.on_message(filters.text)
async def bott(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    if message.text == BOT_NAME:
        bar = random.choice(bot).format(BOT_NAME)
        await message.reply_text(f"<a href='https://t.me/{bot_username}?startgroup=True'>{bar}</a>", disable_web_page_preview=True)
    message.continue_propagation()

@app.on_message(filters.command(["• تغيير الاسم الاول •","• تغيير البايو •","• اضف صورة •","• تغيير الاسم الثاني •","• مسح الصورة •"],"") & filters.private & devs, group = 2)
async def acc_bot(c,msg):
    if msg.text == "• اضف صورة •":
        try:
            m = await c.ask(msg.chat.id, "<b>• قم بإرسال الصوره عزيزي المطور ◟</b>")
            if m.text == "• اضف صورة •":
                m = await c.ask(msg.chat.id, "<b>•عذرا قم بإرسال صورة عزيزي المطور ◟</b>")
            photo = await m.download()
            client = await get_client(1)
            await client.set_profile_photo(photo=photo)
            await msg.reply("<b>• تم تغيير الصورة بنجاح ◟</b>")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    elif msg.text == "• تغيير البايو •":
        try:
            m = await c.ask(msg.chat.id, "<b> • قم بإرسال البايو عزيزي المطور ◟</b>")
            if m.text == "• تغيير البايو •":
                m = await c.ask(msg.chat.id, "<b>•عذرا قم بإرسال نص البايو عزيزي المطور ◟</b>")
            client = await get_client(1)
            await client.update_profile(bio=m.text)
            await msg.reply("• تم تغيير البايو بنجاح ◟")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    elif msg.text == "• تغيير الاسم الاول •":
        try:
            m = await c.ask(msg.chat.id, "<b>• قم بإرسال الاسم عزيزي المطور ◟</b>")
            if m.text == "• تغيير الاسم الاول •":
                m = await c.ask(msg.chat.id, "<b>•عذرا قم بإرسال نص الاسم عزيزي المطور ◟</b>")
            client = await get_client(1)
            await client.update_profile(first_name=m.text)
            await msg.reply("<b>• تم تغيير الاسم الاول بنجاح ◟</b>")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    elif msg.text == "• تغيير الاسم الثاني •":
        try:
            m = await c.ask(msg.chat.id, "<b>• قم بإرسال الاسم عزيزي المطور ◟</b>")
            if m.text == "• تغيير الاسم الثاني •":
                m = await c.ask(msg.chat.id, "<b>• عذرا قم بإرسال نص الاسم عزيزي المطور ◟</b>")
            client = await get_client(1)
            await client.update_profile(last_name=m.text)
            await msg.reply("<b>• تم تغيير الاسم التاني بنجاح ◟</b>")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    else:
        client = await get_client(1)
        if (await client.get_me()).photo:
            try:
                async for photo in client.get_chat_photos("me", limit = 1):
                    await client.delete_profile_photos(photo.file_id)
                await msg.reply("<b>• تم حذف صورة من الحساب المساعد بنجاح◟</b>")
            except Exception as e:
                await msg.reply(f"- حدث خطا -> {e}")
        else:
            await msg.reply("• لا يوجد صور لحذفها عزيزي المطور ◟")

@app.on_message(filters.command(["{ اذاعة }"],"") & filters.private & devs, group = 2)
async def broadcast_acc(c,msg):
    try:
        m = await c.ask(msg.chat.id, "• قم بإرسال الرسالة المراد نشرها عزيزي المطور ◟")
        if m.text == "• اذاعة •":
            m = await c.ask(msg.chat.id, "•عذرا قم بإرسال الرسالة المراد نشرها عزيزي المطور ◟")
        client = await get_client(1)
        x = 0
        async for ch in client.get_dialogs():
            try:
                if m.photo:
                    photo = await m.download()
                    await client.send_photo(ch.chat.id, photo=photo, caption=m.caption)
                elif m.video:
                    video = await m.download()
                    thumb = await app.download_media(m.video.thumbs[0].file_id)
                    await client.send_video(ch.chat.id, photo=video, caption=m.caption, duration=m.video.duration,thumb=thumb)
                else:
                    await client.send_message(ch.chat.id, text=m.text)
                x += 1
            except:
                pass
        await msg.reply(f"• تم ارسال الى {x} شات")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")

@app.on_message(filters.command(["{ اضف قناة }"],"") & filters.private & devs, group = 2)
async def add_must(c,msg):
    try:
        m = await c.ask(msg.chat.id, "•عذرا قم بإرسال يوزر القناها وليس رابط او الكروب وتاكد من رفع البوت بها عزيزي المطور ◟")
        try:
            chat = await c.get_chat(m.text)
        except:
            return await msg.reply("• تاكد عزيزي المطور من يوزر القناه او الكروب ◟")
        await set_must(c.me.username,chat.username)
        await msg.reply("• تم تعيين القناه بنجاح عزيزي المطور ◟")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")

@app.on_message(filters.command(["{ قناة الاشتراك }"],"") & filters.private & devs, group = 2)
async def get_ch_must(c,msg):
    db = await get_must(c.me.username)
    if db:
        return await msg.reply(f"• قناة الاشتراك : @{db} ◟")
    else:
        return await msg.reply("• لا يوجد عزيزي المطور قم باضافة قناة اولا ◟")

@app.on_message(filters.command(["{ حذف قناة الاشتراك }"],"") & filters.private & devs, group = 2)
async def rem_ch_must(c,msg):
    done = await del_must(c.me.username)
    if done:
        return await msg.reply("• تم حذف قناة الاشتراك الاجباري عزيزي المطور ◟")
    else:
        return await msg.reply("• لا يوجد عزيزي المطور لحذفه ◟")

@app.on_message(filters.command(["{ تفعيل الاشتراك }"],"") & filters.private & devs, group = 2)
async def en_ch_must(c,msg):
    status = await get_must_ch(c.me.username)
    if status == "معطل" :
        await set_must_ch(c.me.username,"enable")
        await msg.reply("• تم تفعيل الاشتراك الاجباري عزيزي المطور ◟")
    else:
        await msg.reply("• الاشتراك الاجباري مفعل ◟")

@app.on_message(filters.command(["{ تعطيل الاشتراك }"],"") & filters.private & devs, group = 2)
async def dis_ch_must(c,msg):
    status = await get_must_ch(c.me.username)
    if status == "مفعل" :
        await set_must_ch(c.me.username,"disable")
        await msg.reply("• تم تعطيل الاشتراك الاجباري عزيزي المطور ◟")
    else:
        await msg.reply("• الاشتراك الاجباري معطل ◟")

@app.on_message(filters.command(["{ مطورين السورس }"],"") & filters.private & devs, group = 2)
async def devs_source(c,msg):
    await msg.reply("• اهلا بك عزيزي المطور لرؤية معلومات المطورين قم بالضغط ع الاذرار بالاسفل ◟", reply_markup = ReplyKeyboardMarkup([[("• المطور الاول •"), ("• المطور الثاني •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["• مطورين السورس •"],"") & filters.private & devs, group = 2)
async def devs_source(c,msg):
    await msg.reply("• اهلا بك عزيزي المطورين لرؤية معلومات المطورين السورس قم بالضغط ع الاذرار بالاسفل ◟", reply_markup = ReplyKeyboardMarkup([[("• المطور الاول •"), ("• المطور الثاني •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["{ المطور الاول }", "{ المطور الثاني }"], "") & filters.private & devs, group=2)
async def dev_source(c, msg):
    if msg.text == "{ المطور الاول }":
        username = "Y_o_V"
    else:
        username = "aBoPhr"

    user = await c.get_users(username)
    text = f"<b>• 𝖭𝖺𝗆𝖾 : {user.mention}</b>\n<b>• 𝗂𝖣 : {user.id}</b>"
    
    if user.username:
        text += f"\n<b>• 𝖴𝗌𝖾r : @{user.username}</b>"
    
    chat = await c.get_chat(user.id)
    if chat.bio:
        text += f"\n<b>•𝖡𝗂𝗈 : {chat.bio}</b>"
    
    if user.photo:
        async for photo in app.get_chat_photos(user.id, limit=1):
            await msg.reply_photo(photo.file_id, caption=text)
    else:
        await msg.reply(text)



@app.on_message(filters.command(["• للكروبات •","• للمستخدمين •"],"") & filters.private & devs, group = 2)
async def broadcast_gr(c,msg):
    try:
        m = await c.ask(msg.chat.id, "• قم بارسال الرسالة التي تريد نشرها ◟")
        if m.text in ["• للكروبات •" ,"• للمستخدمين •"]:
            m = await c.ask(msg.chat.id, "•عذرا قم بارسال الرسالة التي تريد نشرها ◟")
        chats = await get_served_chats(c) if msg.text == "• للكروبات •" else await get_served_users(c)
        x = 0
        n = "chat_id" if msg.text == "• للكروبات •" else "user_id"
        for chat in chats:
            try:
                if m.photo:
                    photo = await m.download()
                    await app.send_photo(int(chat[n]), photo=photo, caption=m.caption)
                elif m.video:
                    video = await m.download()
                    thumb = await app.download_media(m.video.thumbs[0].file_id)
                    await app.send_video(int(chat[n]), photo=video, caption=m.caption, duration=m.video.duration,thumb=thumb)
                else:
                    await app.send_message(int(chat[n]), text=m.text)
                x += 1
                await asyncio.sleep(0.2)
            except:
                pass
        type = "كروب" if msg.text == "• للكروبات •" else "مستخدم"
        await msg.reply(f"• تم ارسال الى {x} {type}")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")    

@app.on_message(filters.command(["• بالتوجيه للكروبات •", "• بالتوجيه للمستخدمين •"],"") & filters.private & devs, group = 2)
async def broadcast_fr(c,msg):
    try:
        m = await c.ask(msg.chat.id, "• قم بارسال الرسالة التي تريد نشرها ◟")
        if m.text in ["• بالتوجيه للكروبات •", "• بالتوجيه للمستخدمين •"]:
            m = await c.ask(msg.chat.id, "•عذرا قم بارسال الرسالة التي تريد نشرها ◟")
        chats = await get_served_chats(c) if msg.text == "• بالتوجيه للكروبات •" else await get_served_users(c)
        x = 0
        n = "chat_id" if msg.text == "• بالتوجيه للكروبات •" else "user_id"
        for chat in chats:
            try:
                await m.forward(int(chat[n]))
                x += 1
                await asyncio.sleep(0.2)
            except:
                pass
        type = "كروب" if msg.text == "• بالتوجيه للكروبات •" else "مستخدم"
        await msg.reply(f"• تم ارسال الى {x} {type}")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")    

@app.on_message(filters.command(["{ ترويج للبوت }"],"") & filters.private & devs, group = 2)
async def broadcast_bot_(c: Client ,msg):
    try:
        owner = await c.get_users(int(OWNER_ID))
        chats = await get_served_chats(c) 
        x = 0
        for chat in chats:
            try:
                await c.send_message(int(chat["chat_id"]),f"<b>• بوت ميوزك قنوات كروبات ، البوت يعمل بسرعة وجودة خارقة ، بدون تهنيج ولا تقطيع لان البوت شغال علي سيرفر لوحدو◟</b>\n\n<b>• ارفع البوت فـ قناتك او كروبك وجرب سرعة البوت بنفسك وشوف المميزات◟</b>\n\n<b>• يوزر البوت : @{c.me.username} ◟ </b>\n<b>• يوزر المطور : @{owner.username if owner.username else owner.mention} ◟</b>", reply_markup=ikm([[ikb("𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .", url=f"https://t.me/{app.username}?startgroup=true")]]))
                x += 1
                await asyncio.sleep(0.2)
            except Exception as e:
                pass
        await msg.reply(f"• تم ارسال الى {x} كروب")
        users = await get_served_users(c) 
        x = 0
        for chat in users:
            try:
                await c.send_message(int(chat["user_id"]),f"<b>• بوت ميوزك قنوات كروبات ، البوت يعمل بسرعة وجودة خارقة ، بدون تهنيج ولا تقطيع لان البوت شغال علي سيرفر لوحدو◟</b>\n\n<b>• ارفع البوت فـ قناتك او كروبك وجرب سرعة البوت بنفسك وشوف المميزات◟</b>\n\n<b>• يوزر البوت : @{c.me.username} ◟ </b>\n<b>• يوزر المطور : @{owner.username if owner.username else owner.mention} ◟</b>", reply_markup=ikm([[ikb("𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .", url=f"https://t.me/{app.username}?startgroup=true")]]))
                x += 1
                await asyncio.sleep(0.2)
            except Exception as e:
                pass
        await msg.reply(f"• تم ارسال الى {x} مستخدم")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")
