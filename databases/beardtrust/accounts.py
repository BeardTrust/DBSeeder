#!/usr/bin/env python3

import data.formats
import generators.accounts


def generate_accounts_file(file_format=data.formats.Files.sql):
    user_ids = generators.accounts.get_user_ids()
    admin_ids = generators.accounts.get_admin_ids()

    file_name = '/home/cahlien/Documents/beardtrust'
    file_name += '.sql' if file_format == data.formats.Files.sql else ''
    file_name += '.txt' if file_format == data.formats.Files.txt else ''

    outfile = open(file_name, 'w')
    first_account = True

    for user_id in user_ids:
        account = generators.accounts.generate_user_account(user_id)

        if first_account:
            outfile.write(account.query + '\n' + account.values)
            first_account = False
        else:
            outfile.write(account.values)

        outfile.write(',\n')

    for admin_id in admin_ids:
        account = generators.accounts.generate_admin_account(admin_id)
        outfile.write(account.values)
        outfile.write(';' if admin_id == admin_ids[len(admin_ids) - 1] else ',\n')

    outfile.close()

    print("Created " + str(len(admin_ids) + len(user_ids)) + ' account insertions.')
