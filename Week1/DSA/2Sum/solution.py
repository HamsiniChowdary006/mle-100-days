class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i
        return []

def main():
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    target = int(input("Enter the target number: "))
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()
            