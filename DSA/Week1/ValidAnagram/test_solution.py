from solution import Solution
# all three of these solutions can't handle upper case
# the question only mentions lower case letters
def test_1():
    assert Solution().isAnagram("anagram", "nagaram") == True

def test_2():
    assert Solution().isAnagram("anagraM", "NaGaram") == True