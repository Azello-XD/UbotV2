from ubot import *


@PY.UBOT("test")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>apa sayang?</b>")

@PY.UBOT("buy bot")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>di joviooo laa</b>")
    

@PY.UBOT("absen")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>hadir maniszz😋😋</b>")
    
@PY.UBOT("p")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>salam memek🖕</b>")

@PY.UBOT("dana")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>089525340368 \n Aria Putra Pratama</b>")
    
@PY.UBOT("q")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>pong🔥</b>")
