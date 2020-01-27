def both_ends(s):
    if len(s) < 2:
        return str()
    return s[0] + s[1] + s[-2] + s[-1]


def fix_start(s):
    if len(s) > 0:
        return s[0] + s[1:].replace(s[0], "*")


def MixUp(a, b):
    return b[0] + a[1:] + " " + a[0] + b[1:]


def verbing(s):
    if len(s) >= 3:
        if s.endswith("ing"):
            return s + "ly"
        else:
            return s + "ing"
    return s


def not_bad(s):
    if s.index("not") < s.index("bad"):
        s.replace(s[s.index("not"):s.index("bad") + 3], "good")