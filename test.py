# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f0 = 0
#         f1 = 1
#         f2 = 2
#         if n <= 0:
#             return f0
#         elif n == 1:
#             return f1
#         elif n == 2:
#             return f2
#         else:
#             result = 0
#             for i in range(3, n+1):
#                 result = f1 + f2
#                 f1 = f2
#                 f2 = result
#             return result


# 写个小程序，一个数组，长100，里边乱序分布数字1-100，在数组中随机挑选一个位置的数字，将其替换为-1，如何判断，被替换掉的数字是多少？
# def whichnum(n):
#     n.sort()
#     if n[len(n) // 2] == len(n) / 2:
#         if n[len(n) // 4 * 3] == len(n) / 4 * 3:
#             for i in range(len(n) // 4 * 3 + 1, len(n) + 1):
#                 if n[i] == i:
#                     pass
#                 else:
#                     return i
#         else:
#             for i in range(len(n) // 2, len(n) / 4 * 3 + 1):
#                 if n[i] == i:
#                     pass
#                 else:
#                     return i
#     else:
#         if n[len(n) // 4] == len(n) / 4:
#             for i in range(len(n) // 4, len(n) // 2 + 1):
#                 if n[i] == i:
#                     pass
#                 else:
#                     return i
#         else:
#             for i in range(1, len(n) / 4 + 1):
#                 if n[i] == i:
#                     pass
#                 else:
#                     return i
#
#
# print(whichnum([1, 2, 5, 4, -1, 6, 7, 8]))

# 挑选出重复数
# class Solution:
#     def num(self, n:list)->int:
#         new = []
#         for i in n:
#             if i not in new:
#                 new.append(i)
#             else:
#                 return i
#
#
# print(Solution.num(0, [1, 2, 2, 3]))

# 给两个字符串A和B，找出A对于B的最长前缀。
# while True:
#     try:
#         s1=input()
#         s2=input()
#         if len(s1)>len(s2):#总体思路：从短的字符串中取子串，看其在长字符串中是否存在
#             s1,s2=s2,s1
#         length=0
#         for i in range(len(s1)):
#             for j in range(i+1,len(s1)):
#                 sub=s1[i:j]
#                 if sub in s2 and j-i>length:
#                     res=sub
#                     length=j-i
#         print(res)
#     except:
#         break

# class Solution:
#     def whichnum(self, n:list) -> int:
#         n.sort()
#         if n[int(len(n) / 2)] == int(len(n) / 2):
#             if n[int(len(n) / 4 * 3)] == int(len(n) / 4 * 3):
#                 for i in range(int(len(n) / 4 * 3), len(n) + 1):
#                     if n[i] == i:
#                         pass
#                     else:
#                         return i
#             else:
#                 for i in range(int(len(n) / 2), int(len(n) / 4 * 3 + 1)):
#                     if n[i] == i:
#                         pass
#                     else:
#                         return i
#         else:
#             if n[int(len(n) / 4)] == int(len(n) / 4):
#                 for i in range(int(len(n) / 4 + 1), int(len(n) / 2 + 1)):
#                     if n[i] == i:
#                         pass
#                     else:
#                         return i
#             else:
#                 for i in range(1, int(len(n) / 2 + 1)):
#                     if n[i] == i:
#                         pass
#                     else:
#                         return i
#
#
# print(Solution.whichnum(0, [1, 3, 2, 4, -1, 5, 8, 7]))


# def outputnum(self):
#     n = int(input())
#     A = input().split()
#     newlist = []
#     A.sort()
#     for i in range(n):
#         if A[i] not in newlist and i + 1 < n and A[i] == A[i+1]:
#             pass
#         elif A[i] not in newlist and A[i] == A[i-1]:
#             pass
#         elif A[i] not in newlist and i+1 < n and A[i] != A[i+1] and A[i] != A[i-1]:
#             print(A[i])
#             newlist.append(A[i])
#         elif A[i] not in newlist and i + 1 == n and A[i] != A[i - 1]:
#             print(A[i])
#             newlist.append(A[i])
#         else:
#             pass
#
#     print(newlist)
#     print(int(len(newlist)/2))
#
#
# outputnum(0)


# class Solution:
#     def twoSum(self, nums, target):
#         hashtable = dict()
#         for i, num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num], i]
#             hashtable[nums[i]] = i
#         return []

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         #取出两个链表的数值
#         s1 = ''
#         while l1 is not None:
#             s1 = s1 + str(l1.val)
#             l1 = l1.next
#         s2 = ''
#         while l2 is not None:
#             s2 = s2 + str(l2.val)
#             l2 = l2.next
#         #两个链表的值相加求和
#         s3 = int(s1[::-1]) + int(s2[::-1])
#         s3 = [int(i) for i in str(s3)][::-1]
#         #创建新链表
#         #root作为根节点
#         root = ListNode(s3.pop(0))
#         #current指针用于创建接下来的节点
#         current = root
#         while s3 != []:
#             current.next = ListNode(s3.pop(0))
#             current = current.next
#         return root
print(987654321%4)