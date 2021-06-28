# Binary search implementation using Python
def binary_search(arr,low, h, target):
    if low > h:
        return -1  # Element not present
    m = (low+h)//2
    if arr[m] == target:  # If element is present at the middle itself
        return m
    # Else the element can only be present in right subarray
    elif arr[m] < target:
        low = m+1
        return binary_search(arr, low, h, target)
    # If element is smaller than mid, then it can only
    # be present in left subarray
    elif arr[m] > target:
        h = m-1
        return binary_search(arr, low, h, target)
# The array should be sorted
arr = [1, 3, 4, 6, 7, 8, 9, 23, 45, 56, 112, 233, 444, 445, 446]
print("Here is your array :")
for i in arr:
    print(i, end=' ')
for i in range(2):
    target = int(input('\nEnter the element you want to search : '))
    # Function call
    target_index = binary_search(arr, 0, len(arr),target)
    if target_index == -1:
        print(f"The element  {target} was not found within the array")
    else:
        print(f"The index of the element {target} is {target_index}")
