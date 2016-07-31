def convert_char(char, mod):
    buff = ''
    s = bin(ord(char))[2:]

    if len(s) < 7:
        s = '0' * (7 - len(s)) + s

    for c in s:
        if c == '0' and mod != 0:
            buff += ' 00 '
            mod = 0
        if c == '1' and mod != 1:
            buff += ' 0 '
            mod = 1

        buff += '0'

    return buff, mod

buff = ''
mod = -1

message = raw_input()

for char in message:
    tmp, mod = convert_char(char, mod)
    buff += tmp

print buff.strip()
