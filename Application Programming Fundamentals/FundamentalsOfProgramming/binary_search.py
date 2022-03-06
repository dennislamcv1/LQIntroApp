#!/usr/bin/python3


# This implements the Binary Search Algorithm
def binary_search(needle, haystack):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # Each time through the loop, print out the portion
        # of the data set we are still searching
        print(f"Searching {haystack[left:right+1]} for {needle}")
        if haystack[mid] == needle:
            return mid                 # FOUND IT!
        elif haystack[mid] < needle:
            left = mid + 1             # Discard left side
        elif haystack[mid] > needle:
            right = mid - 1            # Discard right side

    return -1                          # -1 indicates NOT FOUND


# This is a sample data set to search
haystack = [1, 3, 12, 14, 23, 34, 55, 65, 75, 78]

# We'll loop over every value in the haystack,
# plus a number that are not there, and show results
for needle in [0, 1, 3, 5, 12, 14, 15, 23, 30, 34, 42, 55, 65, 70, 75, 78, 99]:
    location = binary_search(needle, haystack)
    if location >= 0:
        print(f"Found {needle} in {haystack} at index {location}")
    else:
        print(f"Cannot find {needle} in {haystack}!")

    print("------------------------")
