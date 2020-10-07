def binary_search(arr, val):
    low = 0 
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == val:
            print("The value is in Index : {} \n...".format(mid+1))
            return mid
        if val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return "NO MATCH"

arr = (1,2,3,7,9,12,13,18,20)
val = 18
binary_search(arr,val)