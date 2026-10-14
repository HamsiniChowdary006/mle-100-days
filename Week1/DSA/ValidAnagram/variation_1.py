class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))
        return new_s == new_t

def main():
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)

if __name__ == "__main__":
    main()