# Test case 4, 5, 6, 1, 2, 3

def findRotationHelper(arr, low, high):
    if(high<low):
        return "No match!"
    mid = int(low + ((high - low) // 2))
    if(mid<high and arr[mid+1]<arr[mid]):
        return (mid+1)
    if(mid>low and arr[mid]<arr[mid-1]):
        return mid
    if(arr[high] > arr[mid]):
        return findRotationHelper(arr, low, mid-1)
    return findRotationHelper(arr, mid+1, high)

arr = (4, 5, 6, 1, 2, 3)
error = findRotationHelper(arr, 0, len(arr)-1)
print("Array error at index : {}".format(error))
