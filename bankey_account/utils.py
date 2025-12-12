# Format Python code here
import random
from datetime import date

from dateutil.relativedelta import relativedelta


def generate_account_number(dob=None):
    if dob is None:
        dob = date(1980, 1, 1)
    dob_part = dob.strftime("%Y%m%d")
    random_part = str(random.randint(100000, 999999))

    return dob_part + random_part


def generate_card_number():
    return f"{random.randint(0, 9999999999999999):016d}"


def generate_expiration_date():
    return date.today() + relativedelta(years=3)
