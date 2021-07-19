import random

months_31 = ['января', 'марта', 'мая', 'июля', 'августа',  'октября', 'декабря']
months_30 = ['апреля', 'июня', 'сентября', 'ноября']
months_29 = ['февраля']


def make_random_date() -> str:
    month_category = random.randint(0, 2)
    if month_category == 0:
        day = random.randint(1, 31)
        month = random.choice(months_31)
    elif month_category == 1:
        day = random.randint(1, 30)
        month = random.choice(months_30)
    else:
        day = random.randint(1, 29)
        month = random.choice(months_29)
    return str(day) + ' ' + month
