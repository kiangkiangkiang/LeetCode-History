class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        while ")" in s:
            right_locate = s.index(")")
            left_locate = right_locate - 1
            while s[left_locate] != "(":
                left_locate -= 1
            s[left_locate + 1 : right_locate] = s[left_locate + 1 : right_locate][::-1]
            s.pop(right_locate)
            s.pop(left_locate)
            print(s)
        return "".join(s)


s = "(ed(et(oc))el)"
s = "a(bcdefghijkl(mno)p)q"
a = Solution()
print(a.reverseParentheses(s))
