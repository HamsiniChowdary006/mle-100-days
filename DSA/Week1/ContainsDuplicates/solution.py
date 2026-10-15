class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False

def main():
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()