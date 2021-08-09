class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2, carry, ans = len(num1) - 1, len(num2) - 1, 0, []
        while l1 >= 0 or l2 >= 0 or carry:
            d1 = int(num1[l1]) if l1 >= 0 else 0
            d2 = int(num2[l2]) if l2 >= 0 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            ans += [str(digit)]
            l1, l2 = l1 - 1, l2 - 1
        
        return "".join(ans[::-1])