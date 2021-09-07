#!/usr/bin/env python3
import random
import uuid

from generators.user_details import generate_date
from models.account import Account

nicknames = ['', 'my', 'first', 'new', 'our', 'big', 'old', 'latest', 'amazing', 'awesome', 'tiny', 'work', 'business',
             'personal', 'home', 'family']

def generate_admin_account(admin_id):
    account_id = uuid.uuid4()
    active_status = random.randint(0, 1)
    cents = random.randint(0, 99)
    dollars = random.randint(0, 100000)
    is_negative = random.randint(0, 1)
    create_date = generate_date(2021, 2022)
    interest = 0
    nickname = 'Work'
    account_type = 'Teller'

    account = Account(account_id, admin_id, active_status, dollars, cents, is_negative, create_date,
                      interest, nickname, account_type)

    return account


def generate_user_account(user_id):
    account_id = uuid.uuid4()
    active_status = random.randint(0, 1)
    cents = random.randint(0, 99)
    dollars = random.randint(0, 100000)
    is_negative = random.randint(0, 1)
    create_date = generate_date(2021, 2022)
    interest = random.random() * 10
    account_type = 'SuperSaver' if random.randint(0, 2) == 0 else 'CoolCash'
    nickname = nicknames[random.randint(0, len(nicknames) - 1)] + account_type

    account = Account(account_id, user_id, active_status, dollars, cents, is_negative, create_date,
                      interest, nickname, account_type)

    return account


def get_user_ids(file_name='/stor/Documents/Scripts/SeedBeardTrustDB/data/BeardTrust_Dev_users.csv') -> list[str]:
    in_file = open(file_name, 'r')
    user_ids = []

    for line in in_file:
        user_ids.append(line.strip('\n'))

    in_file.close()

    return user_ids


def get_admin_ids(file_name='/stor/Documents/Scripts/SeedBeardTrustDB/data/BeardTrust_Dev_admin.csv') -> list[str]:
    in_file = open(file_name, 'r')
    admin_ids = []

    for line in in_file:
        admin_ids.append(line.strip('\n'))

    in_file.close()

    return admin_ids


