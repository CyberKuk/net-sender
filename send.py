import asyncio
import telegram
import socket
import re
import uuid
from dotenv import dotenv_values

config = dotenv_values()


def get_host_name():
    return socket.gethostname()


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]


def get_mac_address():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def build_message():
    return 'I am alive!\n' + \
        'Host name: ' + get_host_name() + '\n' +\
        'Ip: ' + get_ip() +  '\n' +\
        'Mac: ' + get_mac_address()


async def send_message(text):
    bot = telegram.Bot(config['BOT_TOKEN'])
    async with bot:
        await bot.send_message(text=text, chat_id=int(config['SEND_ID']))


async def main():
    message = build_message()
    await send_message(message)


if __name__ == '__main__':
    asyncio.run(main())
