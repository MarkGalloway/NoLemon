import re
from django.core.validators import RegexValidator

__all__ = ['phone_validator']

phone_regex = re.compile(r'''
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

phone_validator = RegexValidator(regex=phone_regex, message="Phone number should include 3 digit area code, and 7 digit number.")
