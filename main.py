
# Task 1
from datetime import datetime, timedelta

# date_format = '%Y-%m-%d'

def get_days_from_today(date):
  date_now = datetime.now()
  try:
    date_received = datetime.strptime(date, date_format)
  except ValueError:
    print('date argument does not match expected date format "YYYY-MM-DD."')
    return None
  else:
    diff = date_now - date_received
    return diff.days

print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2025:10:09'))

# Task 2
import random

# >= 1
# <= 1000
# min >= q <= max
def get_numbers_ticket(min, max, quantity):
  if min < 1 or max > 1000 or quantity < min or quantity > max:
    return []
  
   # including 'max' in the range
  result = random.sample(range(min, max + 1), quantity)
  return sorted(result)

print(get_numbers_ticket(1, 49, 6))

# Task 3
import re

# +380501233234 - correct result
# country code => '+38'
def normalize_phone(phone_number):
  # remove all except numbers
  clean_number = re.sub(r"\D", '', phone_number)

  if clean_number.startswith('38'):
    return '+' + clean_number
  elif clean_number.startswith('0'):
    return '+38' + clean_number

  return clean_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized numbers:", sanitized_numbers)

# Task 4
date_format = '%Y.%m.%d'

def get_upcoming_birthdays(users):
  result = []

  for user in users:
    birthday = datetime.strptime(user['birthday'], date_format).date()

    today = datetime.today().date()
    birthday_this_year = birthday.replace(year=today.year)

    if today > birthday_this_year:
      birthday_this_year.replace(year=today.year + 1)
    
    if today <= birthday_this_year <= today + timedelta(days=7):
      if birthday_this_year.weekday() >= 5:
        # if birthday on weekends
        birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())
      
      result.append({
        'name': user['name'],
        'congratulation_date': birthday_this_year.strftime(date_format)
      })

  return result
  
users = [
    {"name": "John Doe", "birthday": "1985.12.29"},
    {"name": "Tim Cook", "birthday": "1999.07.29"},
    {"name": "Jane Smith", "birthday": "1990.08.03"}
]

print(get_upcoming_birthdays(users))
