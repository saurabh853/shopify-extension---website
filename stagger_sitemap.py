import re
import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

start = datetime.strptime('2026-05-20', '%Y-%m-%d')
end = datetime.strptime('2026-06-28', '%Y-%m-%d')

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_date(match):
    rand_d = random_date(start, end)
    return f'<lastmod>{rand_d.strftime("%Y-%m-%d")}</lastmod>'

new_content = re.sub(r'<lastmod>.*?</lastmod>', replace_date, content)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Sitemap dates staggered successfully.")
