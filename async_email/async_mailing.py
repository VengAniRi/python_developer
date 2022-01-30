import sqlite3
import asyncio
from email.message import EmailMessage
import aiosmtplib
from more_itertools import chunked


async def send_message(data):
    message = EmailMessage()
    message["From"] = "root@localhost"
    message["To"] = data[3]
    message["Subject"] = "Thank You!"
    message.set_content(f"Уважаемый {data[1]}!\n"
                        "Спасибо, что пользуетесь нашим сервисом объявлений.")
    await aiosmtplib.send(message, hostname="127.0.0.1", port=1025)


async def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts')
    for chunk in chunked(cur.fetchall(), 5):
        tasks = []
        for rec in chunk:
            tasks.append(asyncio.create_task(send_message(rec)))
        await asyncio.gather(*tasks)


asyncio.run(main())
