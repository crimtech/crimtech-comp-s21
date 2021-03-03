def sum(l, N):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == N:
                return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4) # Are we sure this one is correct?
    print("Success!")

if __name__ == "__main__":
    test()
