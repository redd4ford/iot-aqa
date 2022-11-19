import time

from config import Config
from pages.selenium_academy.auth import RegisterPage


def main():
    """
    Open registration page and input user data to perform registration.
    """
    page = RegisterPage(browser=Config.DRIVER)

    page.register(
        input_data={
            'first_name': 'Viktoriia',
            'last_name': 'Yehorova',
            'email': 'bamij44058@invodua.com',   # from temp-mail.org
            'password': '123456',
            'confirm_password': '123456'
        },
        sign_up_for_news=False
    )

    time.sleep(10)
    page.browser.quit()


if __name__ == '__main__':
    main()
