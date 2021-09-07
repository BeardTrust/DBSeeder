#!/usr/bin/env python
import databases.beardtrust.loan_types
from data.formats import Files
from databases.beardtrust.users import generate_multi_user_query, generate_users_file


def main():
    databases.beardtrust.loan_types.generate_loan_types_file()


if __name__ == '__main__':
    main()
