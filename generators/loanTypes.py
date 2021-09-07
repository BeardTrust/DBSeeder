#!/usr/bin/env python3

import random
import uuid

from models.loanType import LoanType

nicknames = ['Auto', 'Personal', 'Mortgage', 'Special']
months = [24, 48, 60, 72]

def generate_loan_type():
    id = uuid.uuid4()
    is_active = 'TRUE' if random.randint(0, 1) == 1 else 'FALSE'
    apr = random.random() * 10
    type_name = nicknames[random.randint(0, 3)]
    description = 'This is a meaningless set of words for development purpose. It is to be replaced with a true description of a loan when such functionality is necessary.'
    num_months = months[random.randint(0, 3)]

    loan_type = LoanType(id, is_active, apr, description, num_months, type_name)

    return loan_type