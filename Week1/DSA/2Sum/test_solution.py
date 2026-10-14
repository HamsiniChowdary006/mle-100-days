from solution import Solution
def test_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_2():
    assert Solution().twoSum([-1, -2, -3, -4], -6) == [1, 3]

def test_3():
    assert Solution().twoSum([5], 10) == []

def test_4():
    assert Solution().twoSum([1, 2, 5, 9], 14) == [2, 3]

# this is the test case where two pointers fail
def test_5():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]