def rm_smallest(d):
    # Your code here!
    keys = list(d.keys())
    if len(keys) == 0:
        return d
    cur_min = d[keys[0]]
    cur_key = keys[0]
    for k in d.keys():
        if cur_min > d[k]:
            cur_key = k
            cur_min = d[k]
    del d[cur_key]
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
