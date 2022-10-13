import re 

VALID_TIME_CONTROL = [
    "rapid",
    "bullet",
    "blitz"
]

VALID_MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def has_valid_month(date_string):
    match_month = re.findall("\s[a-zA-z]+\s",date_string).start()
    is_valid_month = match_month != None and len(match_month) != 0 and match_month[0] in VALID_MONTHS
    return is_valid_month

def is_valid_date_string(date_string):
    match_full = re.findall("^[0-9]{2}\s{1}[a-zA-Z]+,\s{1}[0-9]{4}$",date_string)
    return match_full != None and len(match_full) != 0 and has_valid_month

def is_valid_time_control(time_control_string):
    return time_control_string.lower() in VALID_TIME_CONTROL

def check_date_string(func):
    def inner1(*args):
        date_string = args[1] 
        func(date_string)
    return inner1