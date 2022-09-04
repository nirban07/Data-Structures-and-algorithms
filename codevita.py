# problem 1
# s = "abpcdefppp"
# k = 4
# count = 0
# for i in range(len(s)):
# 	if s[i] == "p":
# 		count+=1
# if(count == k):
# 	print("1")

# problem 2
# arr = [7, 3, 1, 3, 1 ]
# str = "111111111"
# cs = ""
# for i in range(len(arr)):
# 	print(cs)
# 	cs += "{0:b}".format(int(arr[i]))
# if str == cs:
# 	print("1")
# print(cs)
# # print("0")
# # 1111111
#

# problem 5
# arr = [1,2,3,4,5]
# a = arr
# a.pop()
# print(a)
# print(arr)
# for i in range(0,10,2):
# 	print(i)
# a = [1, 2, 2, 1]
# l = len(a)
# count = 0
# for i in range(l):
# 	if a[0] > a[len(a)-1]:
# 		if(i % 2 == 0):
# 			count += a[0]
# 		a.remove(a[0])
# 	else:
# 		if(i % 2 == 0):
# 			count += a[len(a)-1]
# 		a.remove(a[len(a)-1])

# v = [2,5,6,3,1]
# op = 0
# for i in range(len(v)):
#         a = v[i]
#         while(a):
#             a = a//2
#             op+=1
# print(op)
# a = [4,1,7,2]
# b = [2,1,3,4]
# k = 4
# count = 0
# for i in range(len(a)):
# 	for j in range(len(b)):
# 		if(a[i]-b[i]>b[j]-a[j]):
# 			count+=1
# 			if(count==k):
# 				print("1")
# 				print(i,j)
# 				break
# 	if(count==k):
# 		print("11")
# 		break


a = [1, 2, 2, 1]
l = len(a)
count = 0
for i in range(l):
	if a[0] > a[len(a)-1]:
		if(i % 2 == 0):
			count += a[0]
		a.remove(a[0])
	else:
		if(i % 2 == 0):
			count += a[len(a)-1]
		a.remove(a[len(a)-1])
print(count)