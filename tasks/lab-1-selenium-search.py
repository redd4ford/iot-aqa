import math
import time

from config import Config
from pages.suninjuly_github import RobotCaptchaPage


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
    Open "Robot Captcha" page.
    Calculate the function based on randomly generated x value, enter the result, and
    submit the form.
    """
    page = RobotCaptchaPage(browser=Config.DRIVER)

    print(f'x in page={page.x_value}')

    result = calculate_result(x_value=page.x_value)

    print(f'result={result}')

    page.answer(value=result, enter=False)

    time.sleep(10)
    page.browser.close()


if __name__ == '__main__':
    main()
