#!/usr/bin/env python3

import uuid
import databases.beardtrust.query
from generators import user_details

TEST_PASSWORD = "$2a$10$bxMkN5JeemgTlrK7LMfm0eL5ljk0IvLWQVlclh20nxdREMlgMFwjy"


class User:
    """
    A class representing a BeardTrust web application user or administrator.
    """

    def __init__(self):
        """
        The constructor for the User class randomly generates all of the user data except system role.
        """
        self.__gender = user_details.generate_gender()
        self.__user_id = user_details.generate_user_id()
        self.__phone = user_details.generate_phone_number()
        self.__last_name = user_details.generate_surname()
        self.__first_name = user_details.generate_given_name(self.__gender)
        self.__password = TEST_PASSWORD
        self.__email = user_details.generate_email(self.__first_name, self.__last_name)
        self.__dob = user_details.generate_date(1900, 2007)
        self.__role = user_details.generate_role()
        self.__username = self.__first_name + '.' + self.__last_name
        self.__query = databases.beardtrust.query.Insert(self)

    @property
    def gender(self):
        return self.__gender

    @property
    def user_id(self):
        return self.__user_id

    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def role(self):
        return self.__role

    @property
    def username(self):
        return self.__username

    @property
    def query(self):
        return self.__query

    @property
    def dob(self):
        return self.__dob
