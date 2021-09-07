#!/usr/bin/env python3

from uuid import UUID


class Account:
    def __init__(self, account_id: UUID, user_id: str, active_status: int, dollars: int, cents: int,
                 is_negative: int, create_date: str, interest: float, nickname: str, account_type: str):
        self.__id = account_id
        self.__user_id = user_id;
        self.__active_status = active_status
        self.__dollars = dollars
        self.__cents = cents
        self.__is_negative = is_negative
        self.__create_date = create_date
        self.__interest = interest
        self.__nickname = nickname
        self.__account_type = account_type

        self.__query = "INSERT INTO `accounts` VALUES"
        self.__values = "('{0}', {1}, {2}, {3}, {4}, '{5}', {6}, '{7}', '{8}', '{9}')".format(account_id, active_status,
                                                                                              cents, dollars,
                                                                                              is_negative, create_date,
                                                                                              interest, nickname,
                                                                                              account_type,
                                                                                              user_id)

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def active_status(self):
        return self.__active_status

    @property
    def dollars(self):
        return self.__dollars

    @property
    def cents(self):
        return self.__cents

    @property
    def is_negative(self):
        return self.__is_negative

    @property
    def create_date(self):
        return self.__create_date

    @property
    def interest(self):
        return self.__interest

    @property
    def nickname(self):
        return self.__nickname

    @property
    def type(self):
        return self.__account_type

    @property
    def query(self):
        return self.__query

    @property
    def values(self):
        return self.__values

