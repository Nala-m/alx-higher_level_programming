#!/ysr/bin/pthon3
def uniq_add(my_list=[]):
    new = set(my_list)
    res = 0
    for i in new:
        res += 1
    return res
