'''Answer History Unrecode
#Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums) - 1):
            for search in range(n+1, len(nums)):
                if nums[search] + nums[n] == target:
                    return([search, n])

class Solution(object):
    def __init__(self):
        self.answer = []
    def DeleteState(self, state, existState):
        deleteElement = []
        for i in range(len(existState)):
            diff = len(existState) - i
            deleteElement += [u * diff + existState[i] for u in [-1, 0, 1]]
        return [i for i in state if i not in deleteElement]
    def SolveNQueens(self, n, existState = []):
        state = [i for i in range(n)]
        if len(existState) > 0:
            state = self.DeleteState(state, existState)
        if len(existState) == n:
            self.answer.append(["".join((("."*n)[:i], "Q", ("."*n)[i+1:])) for i in existState])
            return existState
        for pos in state:
            self.SolveNQueens(n, existState + [pos])
        return(self.answer)

a = Solution()
s = a.SolveNQueens(5)
s


def DeleteState(state, existState):
    deleteElement = []
    for i in range(len(existState)):
        diff = len(existState) - i
        deleteElement += [u * diff + existState[i] for u in [-1, 0, 1]]
    return [i for i in state if i not in deleteElement]
def Queens(n, existState = []):
    state = [i for i in range(n)]
    if len(existState) == 0:
        global answer
        answer = []
    else:
        state = DeleteState(state, existState)
    if len(existState) == n:
        answer.append(["".join((("."*n)[:i], "Q", ("."*n)[i+1:])) for i in existState])     
    for pos in state:
        Queens(n, existState + [pos])
    return(answer)

exampleAnswer = Queens(1);exampleAnswer
exampleAnswer = Queens(4);exampleAnswer





class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def calculate(self, ans, upDigits):
        if len(ans) == 2:
            upDigits = int(ans[0])
            ans = int(ans[1])
        else:
            upDigits = 0
            ans = int(ans[0])
        return ans, upDigits
    def addTwoNumbers(self, l1, l2, upDigits = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 != None:
            ans = str(l2.val + upDigits)
            ans, upDigits = self.calculate(ans, upDigits)
            return ListNode(val = ans, next = self.addTwoNumbers(None, l2.next, upDigits))
        elif l1 != None and l2== None:
            ans = str(l1.val + upDigits)
            ans, upDigits = self.calculate(ans, upDigits)
            return ListNode(val = ans, next = self.addTwoNumbers(l1.next, None, upDigits))
        elif l1 == None and l2 == None:
            if upDigits == 0:
                return None
            else:
                return ListNode(val = upDigits, next = self.addTwoNumbers(None, None, 0))
        else:
            ans = str(l1.val + l2.val + upDigits)
            ans, upDigits = self.calculate(ans, upDigits)
            return ListNode(val = ans, next = self.addTwoNumbers(l1.next, l2.next, upDigits))


a = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 9)))
b = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 5, next = ListNode(val = 9))))
s = Solution()
sss = s.addTwoNumbers(a, b)
sss
print(sss.next.next.next.next.next)


from asyncio import sslproto
from queue import Queue
from typing import Counter


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        maximum = 1
        whichRepeat = []
        for i in range(len(s)):
            if len(s) - i < maximum:
                break
            times = 1
            words = s[i]
            for u in range(i + 1, len(s)):
                if len(whichRepeat) == 1:
                whichRepeat = [j for j in range(len(words)) if words[j] == s[u]]
                if len(whichRepeat) == 0:
                    times+=1
                    words += s[u]
                else:
                    whichRepeat = whichRepeat[0]
                    if times > maximum:
                        maximum = times
                    break
                if u == len(s)-1:
                    if times > maximum:
                        maximum = times
        return maximum

class Solution(object):
    def lengthOfLongestSubstring(self, s, maximum = 0, start = 1, times = 1, words = None):
        if len(s) == 0:
            return 0
        if len(s) <= maximum:
            return maximum
        if len(s) == 1:
            return 1
        if words == None:
            words = s[0]
        whichRepeat = []
        for i in s[start:]:
            whichRepeat = [u for u in range(len(words)) if words[u] == i]
            if len(whichRepeat) == 0:
                times += 1
                words += i
            else:
                if times > maximum:
                    maximum = times
                whichRepeat = whichRepeat[0]
                break
            if times == len(s):
                if times > maximum:
                    maximum = times
                return maximum
        return self.lengthOfLongestSubstring(s[(whichRepeat+1):], maximum, start = times - whichRepeat, times = times - whichRepeat)
        
class Solution(object):
    def lengthOfLongestSubstring(self, s, maximum = 0, start = 1, times = 1, words = None):
        while(True):
            if len(s) == 0:
                return 0
            if len(s) <= maximum:
                return maximum
            if len(s) == 1:
                return 1
            if words == None:
                words = s[0]
            whichRepeat = []
            for i in s[start:]:
                whichRepeat = [u for u in range(len(words)) if words[u] == i]
                if len(whichRepeat) == 0:
                    times += 1
                    words += i
                else:
                    if times > maximum:
                        maximum = times
                    break
                if times == len(s):
                    if times > maximum:
                        maximum = times
                    return maximum
                
            s = s[(whichRepeat[0]+1):]
            start = times - whichRepeat[0]
            times = times - whichRepeat[0]
            words = s[:start]


class Solution(object):
    def isPalindrome(self, x):
        if int(str(x)[::-1]) == x :
            return True
        else :
            return False

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        ans = sorted(nums1 + nums2)
        for i in range(len(ans)):
            if len(ans) % 2 == 0:
                if i+1 == len(ans)/2:
                    return float((ans[i] + ans[i+1]) / 2.0)
            else:
                if i+1 == (len(ans) + 1)/2.0:
                    return float(ans[i])

class Solution(object):
    def longestPalindrome(self, s):
        maximum = len(s)
        palindrome = ""
        if len(s) <= 1:
            return s
        for i in range(len(s)):
            for u in reversed(range(i, len(s))):
                if len(palindrome) >= maximum:
                    return palindrome
                if s[i] == s[u]:
                    if u-i+1 > len(palindrome):
                        if s[i:(u+1)] == s[i:(u+1)][::-1]:
                            palindrome = s[i:(u+1)]
            maximum -= 1
        return s[0]

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = {}
        string_index = 0
        for i in range(numRows):
            result[i] = ""
        while True:
            for i in range(numRows):
                result[i % numRows] += s[string_index]
                string_index += 1
                if string_index == len(s):
                    return "".join([i for i in result.values()])
            for i in range(numRows - 2):
                result[(numRows - 2) - (i % numRows)] += s[string_index]
                string_index += 1
                if string_index == len(s):
                    return "".join([i for i in result.values()])
            
class Solution(object):
    def reverse(self, x):
        if x > 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2 ** 31 - 1 else 0
        else:
            return int("-" + str(abs(x))[::-1]) if -2 ** (31) <= int("-" + str(abs(x))[::-1]) else 0
        
class Solution(object):
    def myAtoi(self, s):
        dig = [str(i) for i in range(10)]
        sign = ["-", "+"]
        result = "0"
        times = 0
        start = False
        for i in range(len(s)):
            if i == times:
                if s[i] == " ":
                    times+=1
                    continue
                if s[i] in sign or s[i] in dig:
                    result = ""
                    result += s[i]
                    start = True
            elif start:
                if s[i] in dig:
                    result += s[i]
                else:
                    break
            else:
                break
        if len(result) == 1 and result[0] in sign:
            return 0
        if int(result) >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif int(result) <= -2 ** 31:
            return -2 ** 31
        else:
            return int(result)

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if int(str(x)[::-1]) == x:
            return True
        else :
            return False


class Solution(object):
    def isMatch(self, s = "", p = ""):
        p_index = len(p) - 1 
        s_index = len(s) - 1
        isMatch = True
        while isMatch:
            if s[s_index] == p[p_index] or p[p_index] == ".":
                s_index -= 1
                p_index -= 1
                if s_index < 0 and p[p_index] != "*":
                    return True if p_index < 0 else False
                if p_index < 0:
                    return True if s_index < 0 else False
            elif p[p_index] == "*":
                p_index -= 1
                if p[p_index] == ".":
                    p_index -= 1
                    if p_index < 0: return True
                    #find p
                    while p_index >= 0:
                        if p[p_index] == "*":
                            p_index -= 2
                            if p_index < 0: return True
                        else:
                            break
                    #find s
                    while s_index >= 0:
                        if s[s_index] == p[p_index] or p[p_index] == ".":
                            isMatch = self.isMatch(s[:(s_index+1)], p[:(p_index+1)])
                            #print("isMatch: ", isMatch)
                            if isMatch:
                                return True
                        s_index -= 1
                    return False
                else:
                    while s_index >= 0:
                        if s[s_index] == p[p_index]:
                            s_index -= 1
                            if s_index < 0:
                                return self.isMatch(s[:(s_index+2)], p[:p_index]) if p_index > 0 else True
                        else:
                            p_index -= 1
                            if p_index < 0:
                                return True if s_index < 0 else False
        return isMatch

                     
#fail              
class Solution(object):
    def isMatch(self, s = "", p = ""):
        p_index = len(p) - 1 
        s_index = len(s) - 1
        isMatch = True
        while isMatch:
            if p[p_index] == "*":
                p_index -= 1
                if p[p_index] == ".": #deal with .*
                    p_index -= 1
                    if p_index < 0: return True
                    #find p
                    while p_index >= 0:
                        if p[p_index] == "*":
                            p_index -= 2
                            if p_index < 0: return True
                        else:
                            break
                    #find s
                    while s_index >= 0:
                        #print("s[s_index]: ", s[s_index])
                        #print("p[p_index]: ", p[p_index])
                        if s[s_index] == p[p_index] or p[p_index] == ".":
                            isMatch = self.isMatch(s[:(s_index+1)], p[:(p_index+1)])
                            #print("isMatch: ", isMatch)
                            if isMatch:
                                return True
                        s_index -= 1
                    return False
                else:
                    if s_index < 0:
                        return True if p_index-1 < 0 else False
                    while s_index >= 0:
                        if s[s_index] == p[p_index]:
                            s_index -= 1
                            if s_index < 0:
                                return self.isMatch('', p[:p_index]) if p_index > 0 else True
                        else:
                            p_index -= 1
                            if p_index < 0:
                                return True if s_index < 0 else False
            elif s[s_index] == p[p_index] or p[p_index] == ".":
                s_index -= 1
                p_index -= 1
                if s_index < 0 and p[p_index] != "*":
                    return True if p_index < 0 else False
                if p_index < 0:
                    return True if s_index < 0 else False
            else:
                return False
        return isMatch


class Solution(object):
    def maxArea(self, height):
        maximum = 0
        for x1 in range(len(height) - 1):
            for x2 in range(len(height)):
                 if maximum / height[x2] > len(height)
            candiList = [(x2 - x1) * height[x2] ]
            if len(candiList) == 0:
                break
            else:
                if max(candiList) > maximum:
                    maximum = max(candiList)
        return maximum

class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0 or changed.count(0) % 2 != 0:
            return []
        changed.sort()
        changedSet = list(set(changed))
        countChanged = Counter(changed).values()
        if changedSet[0] == 0:
            ans = [0] * (countChanged[0]/2)
            changedSet = changedSet[1:]
            countChanged = countChanged[1:]
        else:
            ans = []
        while len(changedSet) >= 1:
            if changedSet[0] * 2 in changedSet:
                whichDouble = changedSet.index(changedSet[0] * 2)
                ans += ([changedSet[0]] * countChanged[0])
                countChanged[whichDouble] -= countChanged[0]
                if countChanged[whichDouble] == 0:
                    countChanged.pop(whichDouble)
                    changedSet.pop(whichDouble)
                elif countChanged[whichDouble] < 0:
                    return []
                changedSet.pop(0)
                countChanged.pop(0)
            else:
                return []
        return ans

from collections import deque
class MyStack(object):
    def __init__(self):
        self.inputQuene = deque()
        self.number = 0

    def push(self, x):
        self.inputQuene.append(x)
        self.number  += 1
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        try:
            self.number -= 1
            return self.inputQuene.pop()
        except:
            return None

    def top(self):
        return self.inputQuene[self.number - 1] if self.number > 0 else None
    def empty(self):
        return True if self.number == 0 else False

        
'''


#New Section
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#21. Merge Two Sorted Lists
from collections import deque
import enum
import xxlimited


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val < list2.val:
            return ListNode(val = list1.val, next = self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(val = list2.val, next = self.mergeTwoLists(list1, list2.next))



#50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def cal(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n % 2 == 0:
                result = cal(x, n/2)
                return  result * result
            else:
                return x * self.myPow(x, n - 1)
        
        return cal(x, n) if n > 0 else 1/cal(x, abs(n))
       


#206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        test = 0
        while head:
            test += 1
            tmp = head.next
            head.next = prev

            prev = head
            head = tmp
            if test > 100:
                print("wrong")
                break
        return prev
        


#143. Reorder List (not yet finish)
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def helper(head):
            if head.next == None:
                pass
            else:
                tmp = head.val
                tmp2 = helper(head.next)
                head.val = tmp2.val
                tmp2.val = tmp
        helper(head)



#203. Remove Linked List Elements       
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            if current.val == val:
                current = current.next
                if prev == None:
                    head = current
                else:
                    prev.next = current
            else:
                prev = current
                current = current.next
        return head
                


#160. Intersection of Two Linked Lists
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c = headA
        setA = set()
        while c:
            setA.add(c)
            c = c.next
        
        c = headB
        while c:
            if c in setA:
                return c
            c = c.next
        return None         



#1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(a[:(i+1)]) for i in range(len(a))]



#724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: list[int], tmp = []) -> int:
        leftSum = 0
        rightSum = sum(nums[1::])
        n = len(nums)
        for i in range(n):
            if leftSum == rightSum :
                return i
            else:
                if i == n: return -1 
                rightSum -= nums[i+1]
                leftSum += nums[i]
        return -1



#11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        maximum = 0
        while left < right:
            h = min(height[left], height[right])
            maximum = max((right - left) * h, maximum)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maximum



#1. Two Sum
class Solution(object):
    def twoSum(self, nums: list[int], target: int):
        myHashMap = {}
        for i, v in enumerate(nums):
            find = target - v
            if find in myHashMap:
                return [myHashMap[find], i]
            else:
                myHashMap[v] = i
            
            

#15. 3Sum
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:  
        ans = []
        for t in range(len(nums)-1):
            target = -1*nums[t]
            input = nums[(t+1):]
            myHashMap= {}
            for i, v in enumerate(input):
                find = target - v
                if find in myHashMap:
                    tmp = sorted([find, v, nums[t]])
                    if tmp not in ans:
                        ans.append(tmp)
                else:
                    myHashMap[v] = v
        return ans



#2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
       


#704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        half = int(len(nums) / 2)
        index = list(range(len(nums)))
        while nums:
            if target > nums[half]:
                nums = nums[(half+1):]
                index = index[(half+1):]
                half = int(len(nums) / 2)
            elif target < nums[half]:
                nums = nums[:half]
                index = index[:half]
                half = int(len(nums) / 2)
            else:
                return index[half]
        return -1



#278. First Bad Version
class Solution:
    def firstBadVersion(self, n: int) -> int:
        half = int(n/2)
        l, r = 0, n
        while half > 0:
            if isBadVersion(half):
                r = half
                if r - l <= 1:
                    return half
            else:
                l = half
            half = int((r + l)/2)



#35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        indexList = list(range(len(nums)))
        half = int(len(nums)/2)
        while len(nums) > 1:
            print(nums)
            if target > nums[half]:
                nums = nums[half:]
                indexList = indexList[half:]
            elif target < nums[half]:
                nums = nums[:half]
                indexList = indexList[:half]
            else:
                return indexList[half]
            half = int(len(nums)/2)
        return indexList[0] if target <= nums[0] else indexList[0] + 1
           


#35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        half = (r + l) >> 1
        while r - l > 1:
            if target > nums[half]:
                l = half
            elif target < nums[half]:
                r = half
            else:
                return half
            half = (r + l) >> 1
        
        return l if target <= nums[l] else r



#1742. Maximum Number of Balls in a Box
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = []
        for ball_number in range(lowLimit, highLimit+1):
            ans.append(sum(map(lambda x: int(x), list(str(ball_number)))))
        return max(Counter(ans).values())



#2264. Largest 3-Same-Digit Number in String
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        numMap = Counter(num)
        numMap = dict(sorted(numMap.items(), key = lambda x:x[0], reverse=True))
        for k, v in numMap.items():
            if v < 3:
                continue
            else:
                ans = Counter()
                test = list(num)
                for i in range(v):
                    index = test.index(k)
                    ans[index] += 1
                    test.pop(index)
                if max(ans.values()) >= 3:
                    return str(k)*3
        return ""

   

#1093. Statistics from a Large Sample
class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        #key -> values: sample -> counts
        count = Counter(enumerate(count))
        count = dict(filter(lambda x: x[1] > 0, count))
        allKeys = list(count.keys())
        allVals = list(count.values())

        #mean, mode
        n = sum(allVals)
        mode = allKeys[allVals.index(max(allVals))]
        mean = sum([k*v for k, v in zip(allKeys, allVals)])/n

        #median
        median, k_prev, cumSum = n >> 1, None, 0
        for k, v in zip(allKeys, allVals):
            if k_prev is not None:
                median = (k + k_prev)/2 if n % 2 == 0 else k
                break
            if cumSum + v < median:
                cumSum += v
            elif cumSum + v > median:
                median = k
                break
            else:
                k_prev = k
        #minimum, maximum
        minimum = float(allKeys[0])
        maximum = float(allKeys[-1])

        return [minimum, maximum, mean, float(median), float(mode)]

   

#977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, nums))



#189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        [nums.insert(0, nums.pop()) for i in range(k)]
        


#14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""
        times = min([len(i) for i in strs])
        for word in range(times):
            check = ""
            for s in strs:
                if check != "":
                    if s[word] != check:
                        return ans
                else:
                    check = s[word]
            ans += check
        return ans



#17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myDict = {}
        repTimes = [3,3,3,3,3,4,3,4]
        for i, v in enumerate(["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]):
            myDict[str(i+2)] = v

        times, n = 1, len(digits)
        for i in range(n):
            times *= repTimes[int(digits[i]) - 2]
        
        result = []
        times2 = 1
        for i in range(n):
            ans = []
            times = int(times/repTimes[int(digits[i]) - 2])
            for s in myDict[digits[i]]:
                for c in s:
                    ans += c*times
            ans += ans * times2
            times2 = int(times2 * times)
            if result:
                for i in range(len(result)):
                    result[i] = result[i] + ans[i]
            else:
                result = ans
        return result

  

#19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:   
        c = head
        total = 0
        while c:
            total += 1
            c = c.next
        if total == n:
            return head.next
        remove = total - n
        c, now, prev = head, 0, head
        while c:
            if now == remove:
                prev.next = c.next
                break
            else:
                prev = c
                c = c.next
                now += 1
        return head



#20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {"(": ")", "[": "]", "{": "}"}
        s = list(s)
        l = []
        while s:
            if s[0] in myDict:
                l.append(s.pop(0))
            else:
                try:
                    if s[0] == myDict[l[-1]]:
                        l.pop()
                        s.pop(0)
                    else:
                        return False
                except:
                    return False
        return False if l else True
  


#28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle) 
        for i in range(n - m + 1):
            if haystack[i:(i+m)] == needle:
                return i
            


#26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] in nums[:i] + nums[i+1:]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)



#27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
            


#31. Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        domain = sorted(set(nums))
        sub_nums = []
        n = len(nums)
        for i in reversed(range(n)):
            if i == n:
                sub_nums.append(nums[i])
            else:
                tmp = list(filter(lambda x:nums[i] < x, sub_nums))
                if tmp != []:
                    #oK
                    tmp.sort() #tmp[0] is what i need
                    sub_nums.pop(sub_nums.index(tmp[0]))
                    sub_nums.append(nums[i])
                    sub_nums.sort()
                    nums[i] = tmp[0]
                    for u, j in enumerate(range(i+1, n)):
                        nums[j] = sub_nums[u]
                    return
                else:
                    sub_nums.append(nums[i])
        nums.sort()


#(not finished)
#46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def helper(myList):
            if len(myList) == 1:
                return myList
        
            for i in range(len(myList)):
                tmp = myList[i]
                myList.pop(i)
                ans.append([tmp] + helper(myList[0:i] + myList[i+1:]))
        return ans
        

#(not finished)
#98. Validate Binary Search Tree    
class Solution:
    def isValidBST(self, root: Optional[TreeNode], l = None, r = None) -> bool:
        if l:
            if root.val > l: l = root.val 
            if root.val < r: r = root.val
        else:
            l = root.val
            r = root.val

        if root.left and root.right:
            if root.left.val < root.val < root.right.val:
                return self.isValidBST(root.left) and self.isValidBST(root.right) 
            else:
                return False
        elif root.left and not root.right:
            if root.left.val < root.val:
                return self.isValidBST(root.left)
            else:
                return False
        elif not root.left and root.right:
            if root.val < root.right.val:
                return self.isValidBST(root.right)
            else:
                return False
        else:
            return True
        

