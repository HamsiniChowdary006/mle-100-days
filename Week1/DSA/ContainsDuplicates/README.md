# Contains Duplicate

## Approach : HashSet
- Create an empty hash set to store the elements encountered so far
- Iterate through each number in the array
- If the number already exists in the set, return True
- If the number does not exist in the set, add it to the set
- If no duplicates are found after the loop, return False

## Complexity Analysis
- Time Complexity: O(n), each element is checked and inserted into the set in average O(1) time.
- Space Complexity: O(n), in the worst case senario, all elements are unique and are stored in the set.

## Approach : Sorting
- Sort the array in ascending order
- Iterate through the sorted array starting from the second element
- Compare each element with the previous one
- If bothe elements are equal, return True
- If no adjacent elements are equal return False

## Complexity Analysis
- Time Complexity: O(n log n), due to sorting followed by linear scan
- Space Complexity: O(1) auxiliary space for an in-place sort, O(n) if new array is created for sorting
