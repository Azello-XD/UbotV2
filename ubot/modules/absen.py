from ubot import *


@PY.UBOT("test")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>apa jink?</b>")

@PY.UBOT("buy")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>di joviooo laa</b>")
    

@PY.UBOT("absen")
async def _(client: Client, message: Message):
    msg = await message.reply("<b>Hadir kontoI</b>")
    
