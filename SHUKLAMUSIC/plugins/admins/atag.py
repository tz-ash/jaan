from SHUKLAMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
import config
from SHUKLAMUSIC.core.userbot import Userbot
from SHUKLAMUSIC import app
from pyrogram.types import ChatPermissions

userbot = Userbot()
spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝗘𝗹𝗹𝗮𝗿𝘃𝗮𝗿𝘂𝗺 𝗼𝗱𝗶 𝘃𝗮𝘆𝗼🤗🥱** ",
           " **𝗢𝗶𝗶 𝗸𝗼𝗶𝗶 𝗲𝘃𝗱𝗮 𝗮𝗿𝘂𝗺𝗶𝗹𝗹𝗲😊** ",
           " **𝗚𝗿𝗼𝘂𝗽 𝗶𝗹 𝘃𝗮𝘆𝗼😃** ",
           " **𝗔𝗿𝘂 𝗲𝗻𝗴𝗶𝗹𝘂𝗺 𝗶𝗻𝗱𝗼..??🥲** ",
           " **𝗘𝗻𝘁𝗲 𝗺𝗮𝗸𝗸𝗹𝗲 𝘃𝗮𝗮🥺** ",
           " **𝗞𝘂𝘁𝘁𝗶𝗸𝗮𝗹𝗲 𝗼𝗱 𝘃𝗮𝗮𝗮🤭** ",
           " **𝗡𝗶𝗻𝗮𝗸 𝗲𝗻𝘁𝗵𝗮 𝗱𝗮 𝗴𝗿𝗼𝘂𝗽𝗹 𝗶𝗹 𝘃𝗮𝗻𝗻𝗮..??🤨** ",
           " **𝗢𝗵𝗼 𝗻𝗲𝘆𝘂𝗺..??🙂** ",
           " **𝗘𝘁𝘁𝗮𝘆𝗶 𝗖𝗼𝗳𝗳𝗲𝗲..??🥲** ",
           " **𝗼𝗱 𝘃𝗮 𝗴𝗿𝗼𝘂𝗽 𝗶𝗹..??😋** ",
           " **𝗘𝗹𝗹𝗮𝗿𝗺 𝘃𝗮 𝗺𝗮𝗻𝘂𝗸𝘂 𝗽𝗼𝗹𝗶𝗸𝗮😍** ",
           " **𝗔𝗿𝘂𝗲𝗻𝗴𝗶𝗹𝘂𝗺 𝗼𝗻𝗹𝗶𝗻𝗲 𝗶𝗻𝗱𝗼😅😅** ",
           " **𝗚𝗿𝗼𝘂𝗽 𝗶𝗹 𝘃𝗮 𝗮𝗹𝗹𝗲 𝗶𝗻𝗱𝗮𝗹𝗼..??🤔** ",
           " **𝗘𝗱𝗮 𝗸𝗵𝗼𝘇𝗶🙄🙄** ",
           " **𝗡𝗲 𝗼𝗸𝗸𝗲 𝗼𝗿𝘂 𝗳𝗿𝗶𝗲𝗻𝗱 𝗮𝗻𝗻𝗼😕** ",
           " **𝗕𝗮𝗸𝗸𝗶 𝗲𝗹𝗹𝗮𝗿𝗺 𝗲𝘃𝗱𝗮..??🙃** ",
           " **𝗛𝗲𝗹𝗹𝗼 𝗮𝗿𝗶𝘆𝗼😛** ",
           " **𝗘𝗱𝗮 𝗺𝘄𝗼𝗻𝗲 𝗻𝗲 𝗼𝗼..?🤔** ",
           " **𝗡𝗲𝗻𝗮𝗸 𝗲 𝗴𝗿𝗽 𝗶𝗻𝘁𝗲 𝗼𝘄𝗻𝗲𝗿 𝗮𝗿𝗶𝘆𝗼.?** ",
           " **𝗘𝗱𝗮 𝗼𝗻𝗻𝘂 𝘃𝗮𝗱𝗮.🤗** ",
           " **𝗚𝗿𝗼𝘂𝗽 𝗼𝗻𝗻𝘂 𝗽𝗼𝘄𝗲𝗿 𝗮𝗸𝗸𝗶𝘆𝗲😇** ",
           " **𝗘𝗱𝗮 𝘁𝗵𝗼𝗿𝗮𝗽𝗽𝗮 𝗻𝗲𝘆𝗮🤭** ",
           " **𝗔𝗹𝗹𝗲𝗻𝗴𝗶𝗹𝘂𝗺 𝗺𝗮𝗹𝗹𝗲 𝗮𝗿𝗸𝘂𝗺 𝗯𝗲𝗻𝗱𝗮🥺🥺** ",
           " **𝗘 𝗸𝗼𝗰𝗵𝗶𝗻𝗲 𝗮𝗿𝗶𝘆𝗼😶** ",
           " **𝗜𝗻𝗻𝘂 𝗱𝘂𝘁𝘆 𝗶𝗹𝗹𝗲..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝗢𝗶𝗶 𝗰𝘂𝘁𝗲𝗲🙂** ",
           " **𝗡𝗲 𝘀𝘂𝗽𝗲𝗿 𝗮𝗵 𝗱𝗮😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝗜 𝗺𝗶𝘀𝘀 𝘂🥲** ",
           " **𝗔𝗿𝗮𝗱𝗮 𝗲𝘃𝗻...??😅** ",
           " **𝗡𝗲 𝗼𝗿𝘂 𝗸𝗶𝗹𝗹𝗮𝗱𝗶 𝘁𝗵𝗮𝗻𝗻𝗮..?😅** ",
           " **𝗢𝗱𝗶𝗸𝗼 𝗲𝘃𝗻 𝘃𝗮𝘁𝘁𝗾😆😆😆** ",
           " **𝗣𝗶𝗹𝗹𝗲𝗿 𝗼𝗸𝗸𝗲 𝗸𝗲𝗻𝗷𝗮𝘃 𝗮𝗮😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝗘𝗱𝗮.??🙉** ",
           " **𝗡𝗲 𝗰𝗵𝗶𝗻𝗴𝗮𝗺 𝗮𝗻𝗻𝗼..?😹** ",
           " **𝗡𝗲 𝗼𝗿𝘂 𝗸𝗼𝗰𝗵𝘂 𝗸𝗶𝗹𝗹𝗮𝗱𝗶😻** ",
           " **𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗶𝗱 𝘁𝗵𝗲𝗿𝗼𝗼..??🙃** ",
           " **𝗘𝗱𝗮 𝗶 𝗹𝗼𝘃𝗲 𝘆𝗼𝘂..?😕** ",
           " **𝗘𝗻𝘁𝗲 𝘃𝗲𝗹𝗮𝗸𝗮𝗿 𝗷𝗮𝗻𝗻𝘂..?🙃** ",
           " **𝗡𝗲 𝗼𝗸𝗸𝗲 𝗼𝗿𝘂 𝗻𝗲𝗻𝗯𝗮𝗻 𝗮𝗻𝗻𝗼..?🙃** ",
           " **𝗘𝗻𝗻𝗮 𝗶𝘀𝘁𝗵𝗮𝗺 𝗮𝘆𝗼😊** ",
           " **𝗡𝗲 𝗰𝗵𝘂𝗻𝗱𝗮𝗿𝗻 𝗮𝗵𝗻🧐** ",
           " **𝗢𝗱 𝗰𝗵𝗮𝗱𝗶 𝘃𝗮𝗮..?** ",
           " **𝗡𝗲 𝗼𝗸𝗸𝗲 𝘀𝗲𝘁𝗵 𝗽𝗼𝗼😠** ",
           " **𝗡𝗲𝗻𝗮𝗸 𝗲𝗻𝗻𝗲 𝗶𝘀𝘁𝗵𝗮𝗺 𝗮𝗻𝗻𝗼..?❤** ",
           " **𝗼𝗱𝘂 𝗻𝗼𝗼𝗯𝗲𝗲..?👱** ",
           " **𝗘𝗱𝗮 𝗺𝘄𝗼𝗻𝗲 🤧❣️** ",
           " **𝗡𝗻𝗷𝘂𝗺 𝗸𝗶𝗹𝗹𝗮𝗱𝗶😏😏** ",
           " **𝗡𝗲 𝗺𝗶𝗻𝗱𝗮𝗿𝘂𝘁𝗵🤐** ",
           " **𝗘𝗱𝗮 𝗸𝗼𝗰𝗵𝘂 𝗰𝗵𝗲𝗿𝘂𝗸𝗸𝗮😒** ",
           " **𝗔𝘆𝗼 𝗽𝗮𝗺𝗯😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝗘𝗹𝗹𝗮𝗿𝗸𝘂𝗺 𝗰𝗵𝘂𝗴𝗮𝗹𝗹𝗲 🙈** ",
           " **𝗡𝗲 𝘀𝗲𝘁𝗵 𝗽𝗼𝗼** ",
           " **𝗘𝗱𝗮 𝗴𝗿𝗼𝘂𝗽 𝗶𝗹 𝗮𝗿𝗺𝘂𝗹𝗹𝗮🥺🥺** ",
           " **𝗘𝘃𝗱𝗮 𝗲𝗻𝘁𝗵𝗮 𝗻𝗮𝗱𝗮𝗸𝗻𝗲👀** ",
           " **𝗚𝗼𝗱 𝗲𝗹𝗹𝗮𝗺 𝘀𝗲𝗲 𝗰𝗵𝗲𝘆𝘂𝘃𝗮🙂** ",
           " **𝗢𝗼𝗱𝘂 𝗼𝗿𝘂 𝗰𝗵𝗮𝗱𝘂..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
           " **𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:-[@art_loop]  𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫{ @amkidbot}🥰** ",
           " **𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
           ]

VC_TAG = [ "**𝗣𝗶𝗹𝗹𝗲𝗿𝗲 𝘃𝗰 𝘃𝗮🥲**",
         "**𝗩𝗰 𝘃𝗮𝗻𝗻𝗮 𝗺𝗶𝘁𝘁𝗮𝘆𝗶😬**",
         "**𝗘𝗱𝗮 𝘃𝗰 𝗶𝗹 𝗼𝗿𝘂 𝗸𝗼𝗰𝗵𝘂🏓**",
         "**𝗩𝗰 𝘃𝗮𝗮 𝗻𝗷𝗻 𝗶𝗻𝗱🥰**",
         "**𝗢𝗻𝗻𝘂𝗱𝗲 𝘃𝗶𝗹𝗶𝗸𝘂𝘃𝗮 𝘃𝗰 𝘃𝗮𝗮🤨**",
         "**𝗩𝗰 𝘃𝗮𝗻𝗻𝗶𝗹𝗲 𝘂𝗿𝘂𝗺𝗯 𝗸𝗮𝗱𝗶𝗸𝘂𝗺🤣**",
         "**𝗩𝗰 𝘃𝗮𝗮😁**",
         "**𝗩𝗰 𝗶𝗹 𝗮𝗿𝗼 𝗳𝗼𝗼𝘁𝗯𝗮𝗹𝗹 𝗸𝗮𝗹𝗶𝗸𝘂𝘃𝗮⚽**",
         "**𝗩𝗰 𝘃𝗮𝗱𝗮 𝗽𝗹𝘀🥺**",
         "**𝗘𝘆𝗼 𝘃𝗰 𝗶𝗹 𝘀𝗲𝗱 𝘀𝗼𝗻𝗴𝘀😥**",
         "**𝗡𝗷𝘂𝗺 𝗻𝗲𝘆𝘂𝗺 𝗺𝗮𝘁𝗵𝗿𝗲 𝗼𝗹𝗹𝗼 𝗩𝗰𝗶𝗹🙄**",
         "**𝗘𝗱𝗮 𝗲 𝗯𝗼𝘁 𝗲𝗻𝗴𝗻𝗮 𝘃𝗰 𝗶𝗹 𝗽𝗮𝗱𝗮𝗻𝗲?🤔**",
         "**𝗡𝗷𝗻 𝗼𝘁𝘁𝘆𝗸𝘂 𝗮𝗵 𝗱𝗮 𝗻𝗲 𝘃𝗰 𝘃𝗮𝗮🙂**",
        ]

last_checked_time = None

@app.on_message(filters.command(["atag"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    global last_checked_time
    try:
        # Start the Pyrogram client
        await userbot.one.start()
    except:
        pass

    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("This command only works in groups.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")

    if message.reply_to_message and message.text:
        return await message.reply("/atag 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/atag 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    else:
        return await message.reply("/atag 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /atagalloff , /stopavctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stopatag ||"
                await userbot.one.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(7)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["avctag"], prefixes=["/", ".", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /atagalloff , /stopavctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}\n\n|| ➥  ᴛᴀɢɢɪɴɢ ʙʏ  @SHIVANSH474||"
            await userbot.one.send_message(chat_id, txt)
            await asyncio.sleep(5)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["stopatagall", "cancelatagall", "offatagall", "atagallstop", "stopavctag", "stopatag", "atagalloff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝..♦")
