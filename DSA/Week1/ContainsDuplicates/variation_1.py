class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False

def main():
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()