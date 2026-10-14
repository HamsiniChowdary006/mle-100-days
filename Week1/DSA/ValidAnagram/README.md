# Valid Anagram

## Approach 1: Using Counter
- Import Counter from collections module in python
- Counter counts the frequency of each character in a string and stores the results in a dictionary-like object
- Create a counter for both strings
- Compare the two counters, if they are equal then the strings are anagrams of each other then return True, otherwise return False

## Why do we use Counter?
Checking whether two strings contain the same characters is not enough, we must also check how many times each character appears.

## Complexity Analysis
- Time complexity: O(n + m) counting the characters and comparing the counters takes linear expected time, where n and m are the lengths of two strings.
- Space complexity: O(k) the counter stpre distinct charactes, where k is the number of distinct characters across both strings.


## Approach 2: Sorting
- Sort the characters of both strings using the built-in sorted() function
- Join the sorted character into two strings
- Compare the resulting strings
- If they are equal then return True, otherwise return False

## Complexity Analysis
- Time Complexity: O(nlogn + mlogm) since sorting both strings take O(logn) and O(mlogm) time
- Space Complexity: O(n + m); 
sorted() creates new character lists, and joining them creates new strings


## Approach 3: Using a character frequency array
- Check whether the strings have different lengths, if they do return False immediately because anagrams must have the same number of characters
- Create an array of size 26 initialized to 0s, each position represents lowercase english letters
- Traverse both strings at the same time
- For each character in s, increment its frequency in the array
- For each character in t, decrement its frequency in the array
- After processing both strings, check the array. If every value is zero, the frequencies match and strings are anagrams, otherwise they are not 