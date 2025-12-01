import random


def generate_account_number(dob):
    dob_part = dob.strftime("%Y%m%d")
    random_acc_num = f"{random.randint(0, 9999):04d}"
    return random_acc_num + dob_part

def generate_card_number():
    return f"{random.randint(0, 9999999999999999):016d}"