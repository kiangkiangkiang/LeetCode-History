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

#21. Merge Two Sorted Lists
# Definition for singly-linked list.
from collections import deque
from ctypes import sizeof
from typing import Counter


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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



