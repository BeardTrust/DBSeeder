#!/usr/bin/env python3

from uuid import UUID


class LoanType:
    def __init__(self, id: UUID, is_active: int, apr: float, description: str, 
                 num_months: int, type_name: str):
        self.__id = id
        self.__type_name = type_name;
        self.__is_active = is_active
        self.__description = description
        self.__num_months = num_months

        self.__query = "INSERT INTO `loan_types` VALUES"
        self.__values = "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(id, is_active,
                                                                                              apr,
                                                                                              description,
                                                                                              num_months,
                                                                                              type_name)

    @property
    def id(self):
        return self.__id

    @property
    def type_name(self):
        return self.__type_name

    @property
    def apr(self):
        return self.__apr

    @property
    def is_active(self):
        return self.__is_active

    @property
    def description(self):
        return self.__description

    @property
    def num_months(self):
        return self.__num_months

    @property
    def query(self):
        return self.__query

    @property
    def values(self):
        return self.__values