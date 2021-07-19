months_31 = ['января', 'марта', 'мая', 'июля', 'августа',  'октября', 'декабря']
months_30 = ['апреля', 'июня', 'сентября', 'ноября']
months_29 = ['февраля']


def check_message(message: str) -> bool:
    message = message.lower()
    if message == 'любая дата':
        return True
    if len(message.split()) != 2:
        return False
    day, month = message.split()
    if month not in months_31 and month not in months_30 and month not in months_29:
        return False
    if int(day) < 1:
        return False
    if month in months_31:
        if int(day) > 31:
            return False
    if month in months_30:
        if int(day) > 30:
            return False
    if month in months_29:
        if int(day) > 29:
            return False
    return True


