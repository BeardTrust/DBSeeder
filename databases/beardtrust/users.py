#!/usr/bin/env python3

import data.formats
import databases.beardtrust.query as query


def generate_users_file(min_users=1, max_users=101, file_format=data.formats.Files.sql):
    file_name = '/home/cahlien/Documents/beardtrust'
    file_name += '.sql' if file_format == data.formats.Files.sql else ''
    file_name += '.txt' if file_format == data.formats.Files.txt else ''

    outfile = open(file_name, 'w')

    for x in range(min_users, max_users):
        user = query.User()
        outfile.write(user.query.run() + '\n')

    outfile.close()


def generate_multi_user_query(min_users=1, max_users=101, file_format=data.formats.Files.sql):
    usernames = {''}
    user_ids = {''}
    phones = {''}

    file_name = '/home/cahlien/Documents/beardtrust'
    file_name += '.sql' if file_format == data.formats.Files.sql else ''
    file_name += '.txt' if file_format == data.formats.Files.txt else ''

    outfile = open(file_name, 'w')

    duplicates = 0

    for x in range(min_users, max_users):
        user = query.User()

        if user.user_id not in user_ids and user.username not in usernames and user.phone not in phones:
            usernames.add(user.username)
            user_ids.add(user.user_id)
            phones.add(user.phone)

            if x == 1:
                outfile.write(user.query.run() + '\n')
            else:
                outfile.write(user.query.values)

                if x == max_users - 1:
                    outfile.write(';')
                else:
                    outfile.write(',\n')
        else:
            duplicates += 1

    outfile.close()
    print('Discarded ' + str(duplicates) + ' entries due to violation of unique constraints.')
