# 2Sum problem

## Approach : HashMap
 
For this approach, we will use a HashMap to store the numbers we have seen so far and their corresponding indices.
As we iterate through the array, we calculate the complement i.e target - current number. If the complement exists in the HashMap, we have found a pair that sums up to the target.
Otherwise, we add the current number and its index to the HashMap and continue iterating through the array.

### Complexity Analysis

Time Complexity: O(n), because each element is processed once and the HashMap operations like insertion and lookup take O(1) time on average.

Space Complexity: O(n), because in the worst case we may store all n elements of the array in the HashMap.

### Test Cases

### Edge Cases
- Single element with no valid pair
- No valid pair in the array
- Zeroes in the array
- A valid pair involving the last element of the array
- A number must not be paired with itself unless it appears at two different indices

## Approach : Two Pointers

Two pointers can solve this question in O(n) time and O(1) auxiliary space when the array is sorted. However, the usual pointer moving logic is not reliable for unsorted arrays.


## Conclusion

The hash-map approach is more appropriate for unsorted array because it finds complements without needing the input to be sorted and returns the original indices.