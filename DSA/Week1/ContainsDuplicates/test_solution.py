from solution import Solution
def test_1():
    assert Solution().containsDuplicate([1, 2, 4, 6]) == False

def test_2():
    assert Solution().containsDuplicate([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 20]) == True

def test_3():
    assert Solution().containsDuplicate([-1, -2, -0, 4, 5, -1]) == True
