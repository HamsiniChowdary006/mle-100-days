class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1
        for c in cnt:
            if c != 0:
                return False
        return True

def main():
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)

if __name__ == "__main__":
    main()