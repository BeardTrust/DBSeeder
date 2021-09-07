#!/usr/bin/env python3

from models.user import User

table_name = 'users'
columns = ['user_id', 'dob', 'email', 'first_name', 'last_name', 'password', 'phone', 'role', 'username']


class Insert:
    def __init__(self, user: User):
        fields = [user.user_id, user.dob, user.email, user.first_name, user.last_name, user.password, user.phone,
                  user.role, user.username]
        self.query = "INSERT INTO `users`(`user_id`, `dob`, `email`, `first_name`, `last_name`, `password`, `phone`, " \
                     "`role`, `username`) VALUES"
        self.values = "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(fields[0], fields[1],
                                                                                                fields[2], fields[3],
                                                                                                fields[4], fields[5],
                                                                                                fields[6], fields[7],
                                                                                                fields[8])

    def run(self) -> str:
        return self.query + self.values + ';'
