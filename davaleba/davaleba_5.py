
#1
count = 0
nums = [1,2,3,4,5,6,7,8,9,10]

for num in nums:
    count = count + num

print(count)

#2
nums = [8,2,3,4,10,6,7,5,9,1]
nums.sort()
el = nums.pop()
print(el)
nums.sort(reverse=True)
j= nums.pop()
print(j)

#3
list1 = []
list2 = []
nums = [1,2,3,4,5,6,7,8,9,10]
for i in nums:
    if i % 2 == 1:
        continue
    list1.append(i)
print(list1)
for o in nums:
    if o % 2 == 0:
        continue
    list2.append(o)
print(list2)


#4

list = [1,2,3,4,5,6,7,8,9,10]
print(tuple (list))
print(list)

#5

nums = [1,2,9,3,2,4,5,3,6,6,7,8,9,10]

nums2 = []
for x in nums:
    if nums.count(x) >= 2:
        continue
    nums2.append(x)

print(nums2)









