#!/usr/bin/env python3

import enum


class Role(enum.Enum):
    """
    This class represents the role of a user within a web application.
    """

    admin = 0
    user = 1
