# discordのボットに必要なライブラリ
import discord
# 環境変数を読み込むのに必要なライブラリ
import os
import requests

# 各モジュールのインポート
from keep_alive import keep_alive

# このBOTが使う権限をデフォルトで設定
intents=discord.Intents.default()
# discordライブラリ Ver2.0 以降は必要
intents.message_content = True
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

# トークンを環境変数から取得
TOKEN = os.getenv("DISCORD_TOKEN")

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    await message.channel.send(message)
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if((message.content).startswith("exdc ") | \
       (message.content).startswith("EXDC ") | \
       (message.content).startswith("デイケア　")):
        #a = ps99calc.func(message.content)
        a ="にゃ"
        await message.channel.send(a)
        return
    
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)