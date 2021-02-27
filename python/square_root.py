import math

def square_root(n):
    # Write your code here!
    if n >= 0 and isinstance(n, int):
        return math.sqrt(n)
    else:
        return -1

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()