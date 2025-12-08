import random
from datetime import date
from dateutil.relativedelta import relativedelta


def generate_account_number(dob):
    dob_part = dob.strftime("%Y%m%d")
    random_acc_num = f"{random.randint(0, 9999):04d}"
    return random_acc_num + dob_part


def generate_card_number():
    return f"{random.randint(0, 9999999999999999):016d}"


def generate_expiration_date():
    return date.today() + relativedelta(years=3)
