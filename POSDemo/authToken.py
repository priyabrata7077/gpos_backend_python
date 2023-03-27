import os
import secrets
import string


def gen_token():
    choices = string.ascii_letters + string.digits
    token = ''.join((secrets.choice(choices) for i in range(32)))
    return token

if __name__ == '__main__':
    tkn = gen_token()
    print(tkn)