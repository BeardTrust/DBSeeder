#!/usr/bin/env python
import databases.beardtrust.accounts
from data.formats import Files
from databases.beardtrust.users import generate_multi_user_query, generate_users_file


def main():
    databases.beardtrust.accounts.generate_accounts_file()


if __name__ == '__main__':
    main()
