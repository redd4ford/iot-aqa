import math
import time

from config import Config
from pages.suninjuly_github import ExplicitWaitPage


def calculate_result(x_value: float) -> float:
    """
    Calculate ln(|12 * sin(x)|).
    """
    return math.log(
        abs(12 * math.sin(x_value)),
        math.e
    )


def main():
    """
    Open "Explicit Wait2 (Simple registration form)" page.
    Wait until the price is $100, then book the house, and solve captcha by 
    calculating the function from the previous lab task. Then submit the form.
    """
    page = ExplicitWaitPage(browser=Config.DRIVER)

    is_price_100 = page.wait_until_price_is_100()

    print(f'price is $100={is_price_100}')

    page.book()

    result = calculate_result(x_value=page.x_value)

    print(f'result={result}')

    page.answer(value=result, enter=False)

    time.sleep(10)
    page.browser.quit()


if __name__ == '__main__':
    main()
