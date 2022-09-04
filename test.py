# binary search
# arr = [10, 20, 30, 50]
# x= 50
# def binarySearch(arr, x, low, high):
# 	while(low <= high):
# 		mid = low+((high - low)//2)
# 		# print("this is low and high",low,high)
# 		# print(mid)
# 		if(arr[mid] == x):
# 			return mid
# 		elif(arr[mid] < x):
# 			low = mid+1
# 		else:
# 			high = mid-1


# def binarySearch(arr, l, r, x):

#     while l <= r:

#         mid = l + (r - l) // 2
#         print(mid)
#         # Check if x is present at mid
#         if arr[mid] == x:
#             return mid

#         # If x is greater, ignore left half
#         elif arr[mid] < x:
#             l = mid + 1

#         # If x is smaller, ignore right half
#         else:
#             r = mid - 1

#     # If we reach here, then the element
#     # was not present
#     return -1
# ans = binarySearch(arr, 0, len(arr)-1, x)
# ans = binarySearch(arr,x,0,len(arr)-1)
# print(ans)


# print(bin(12))
# print(int("0b1100",2))

a = [5, 6, 7, 9, 1, 2, 3, ]
c = a
b = a.sort()
a[0] = 8
print(a)
print(b)
print(bool("a"))

for i, char in enumerate("helloooooo"):
    print(char)

print(type(type))
print(type(int))