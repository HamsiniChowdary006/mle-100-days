from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

def main():
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)

if __name__ == "__main__":
    main()
