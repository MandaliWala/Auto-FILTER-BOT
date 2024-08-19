import datetime, time, asyncio
from pyrogram import Client, filters
from database.users_chats_db import db
from utils import broadcast_messages

@Client.on_message(filters.command("broadcast"))
async def pm_broadcast(bot, message):
    me = await bot.get_me()
    owner = await db.get_bot(me.id)
    if owner["user_id"] != message.from_user.id:
        return 
    b_msg = await bot.ask(chat_id = message.from_user.id, text = "Now Send Me Your Broadcast Message")
    try:
        users = await db.get_all_users()
        sts = await message.reply_text('Broadcasting your messages...')
        start_time = time.time()
        total_users = await clonedb.total_users_count()
        done = 0
        blocked = 0
        deleted = 0
        failed = 0
        success = 0
        async for user in users:
            if 'id' in user:
                pti, sh = await broadcast_messages(int(user['id']), b_msg)
                if pti:
                    success += 1
                elif pti == False:
                    if sh == "Blocked":
                        blocked += 1
                    elif sh == "Deleted":
                        deleted += 1
                    elif sh == "Error":
                        failed += 1
                done += 1
                if not done % 20:
                    await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")    
            else:
                # Handle the case where 'id' key is missing in the user dictionary 
                done += 1
                failed += 1
                if not done % 20:
                    await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")    

        time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
        await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users: {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")
    except Exception as e:
        print(f"error: {e}")