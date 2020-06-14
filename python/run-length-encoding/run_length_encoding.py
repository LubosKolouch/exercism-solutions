import re
def decode(string):
    print(string)
    dec_arr = re.split('(?=[A-Z][ ]*)', string)
    print(dec_arr)


def encode(string):
    pass
