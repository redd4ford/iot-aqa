import random
import string


def generate_random_email(char_num: int = 10):
    return (
            ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
            + '@gmail.com'
    )
