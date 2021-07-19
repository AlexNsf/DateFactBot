import random_date_generator as rdg
import random
import wikipediaapi


def make_date_for_wiki(date: str) -> str:
    return '_'.join(date.split())


def is_valid_fact(fact: str) -> bool:  # Почти все события в википедии имеют вид "год - событие", отсекаем именно такие
    if len(fact) < 6:
        return False
    if fact[4] == '—' or fact[5] == '—':
        return True
    return False


def add_date_to_fact(date: str, date_fact: str) -> str:  # Для благозвучия добавляем "В году"
    date_fact_list = date_fact.split()
    date_fact = date_fact_list[0] + ' ' + ' '.join(date_fact_list[2:])
    new_date_fact = date.split('_')[0] + ' ' + date.split('_')[1] + ' ' + date_fact
    return new_date_fact


def get_date_fact(date: str) -> str:
    if date[0] == 'л':
        date = rdg.make_random_date()
    wiki_wiki = wikipediaapi.Wikipedia('ru')
    date = (make_date_for_wiki(date))
    date_page = wiki_wiki.page(date)
    facts_section = ''
    for section in date_page.sections:
        if str(section)[:16] == 'Section: События':
            facts_section = str(section)
            break
    if facts_section == '':  # Если не была найдена секция с событиями, просим выбрать другую дату
        return 'Что-то пошло не так, попробуйте выбрать другую дату'
    facts_list = list(filter(is_valid_fact, facts_section.split('\n')))
    date_fact = random.choice(facts_list)
    date_fact = add_date_to_fact(date, date_fact)
    return date_fact

