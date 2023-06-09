from pitricks.utils import make_parent_top
make_parent_top()

import traceback
from typing import List, Union

import aiosmtplib

from .secret import (MAIL_PASSWORD, MAIL_SERVER_HOST, MAIL_USERNAME)

async def login_mail_async():
    smtp = aiosmtplib.SMTP(MAIL_SERVER_HOST, port=465, use_tls=True)
    await smtp.connect()
    await smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
    return smtp

smtp = None
async def send_verify_code(verify_code: str, receiver: Union[str, List[str]]):
    '邮箱发送验证码'
    global smtp
    if not smtp:
        smtp = await login_mail_async()

    message = (
        f'From: r00t <{MAIL_USERNAME}>\n'
        f'To: {receiver} <{receiver}>\n'
        f'Subject: r00t 2023 新生赛 注册验证码\n\n'
        f'您的验证码为：{verify_code}。有效期为24小时。'
    ).encode()
    try:
        await smtp.sendmail(MAIL_USERNAME, receiver, message)
        return True
    except Exception as e:
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import asyncio as ai
    ai.get_event_loop().run_until_complete(send_verify_code("异世相遇", "Koali233@qq.com"))
    # print(send_verify_code("不如打原神", "Koali233@qq.com"))
    # send_verify_code("123456", "pyy@r00team.cc")
