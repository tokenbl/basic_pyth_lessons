import re

def email_parse(email_address):
    RE_EMAIL = re.compile(r'(?P<username>^[a-z0-9\_-]*)[@](?P<domain>(?<=@)\w*\.\w*)')
    if not RE_EMAIL.match(email_address):
        raise ValueError(f'wrong email: {email_address}')
    print(RE_EMAIL.match(email_address).groupdict())

email_parse('dfafgajhfgasfhkj@sdsadsadehkolyr.com')
email_parse('qwerty@qazwsx.su')