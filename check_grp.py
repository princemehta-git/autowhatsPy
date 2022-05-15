def check_grp(num):

    try:
        int(num[-4:])
        out = 'number'

    except:
        out = 'group'

    return out

