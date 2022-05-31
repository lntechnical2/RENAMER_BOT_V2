from pyrogram import Client as IlluzX, filters 
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
import datetime
from helper.database import insert ,find_one
from pyrogram.file_id import FileId
CHANNEL = os.environ.get("CHANNEL", "")


@IlluzX.on_message(filters.private & filters.command(["start"]))
async def start(c , m):
    insert(int(m.chat.id))
    await m.reply_text(
        text="Hey 👋 Iam Renamer Bot I Can Rename Docs",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Settings", callback_data="stgs")
            ],[
             InlineKeyboardButton("Help", callback_data="help"),
             InlineKeyboardButton("About", callback_data="about")
             ]]
             )
         )
  
@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__You are not subscribed my channel__** ",reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("Join",url=f"https://t.me/{update_channel}") ]   ]))
       		return
       date = message.date
       _used_date = find_one(user_id)
       used_date = _used_date["date"]      
       c_time = time.time()
       LIMIT = 240
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:
       	await app.send_chat_action(message.chat.id, "typing")
       	await message.reply_text(f"```Sorry Dude am not only for YOU \n Flood control is active so please wait for {ltime}```",reply_to_message_id = message.message_id)
        else:
       	used_date = find(int(message.chat.id))
       	media = await client.get_messages(message.chat.id,message.message_id)
       	       	file = media.document or media.video or media.audio 
       	dcid = FileId.decode(file.file_id).dc_id
       	filename = file.file_name
       	filesize = humanize.naturalsize(file.file_size)
       	fileid = file.file_id
       	await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- {filesize}\n**Dc ID** :- {dcid} """,reply_to_message_id = message.message_id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename"),InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
