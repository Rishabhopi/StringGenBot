from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"𝐇𝐞𝐲 {message.from_user.first_name},\n\n๏ 𝐈 𝐀𝐦 {Anony.mention},\n\n𝐓𝐑𝐔𝐒𝐓𝐄𝐃 𝐒𝐓𝐑𝐈𝐍𝐆 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑 𝐁𝐎𝐓, \n\n 𝐅𝐔𝐋𝐋𝐘 𝐒𝐀𝐅𝐄 & 𝐒𝐄𝐂𝐔𝐑𝐄 𝐍𝐎 𝐀𝐍𝐘 𝐄𝐑𝐑𝐎𝐑..\n\n 𝐌𝐚𝐝𝐞 𝐁𝐲<a href=https://t.me/Rishu1286> ●⃝🇷ishu࿐♡ </a> ",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
