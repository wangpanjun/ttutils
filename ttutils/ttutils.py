# coding=utf-8

from constant import TIME_CONSTANT, POSTAGE_CONSTANT


def trans_seconds(seconds):
    min, sec = seconds / 60, seconds % 60
    hour, min = min / 60, min % 60
    day, hour = hour / 24, hour % 24

    return reduce(lambda x, y: "%d%s" % (y[1], TIME_CONSTANT[y[0]]) + x if y[1] > 0 else x,
                 enumerate([sec, min, hour, day]), "")


def trans_byte(byte, byte_type='B'):
    assert byte_type in ['b', 'B'], '仅支持【b】或者【B】'
    byte = byte if byte_type == 'B'else byte >> 3
    ls = []
    flag = 0
    while flag < len(POSTAGE_CONSTANT) and byte > 0:
        ls.append(byte % (1 << 10))
        byte >>= 10
        flag += 1
    return reduce(lambda x, y: "%d%s " % (y[1], POSTAGE_CONSTANT[y[0]]) + x if y[1] > 0 else x, enumerate(ls), "")


if __name__ == '__main__':
    # trans_seconds(113200)
    print trans_byte(14 * 1024 * 1000*1000, byte_type='B')
