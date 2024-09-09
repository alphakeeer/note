class Solution: #解一，略微丑陋了
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        l = len(s)
        s = s+" "
        ans = 0
        i = 0
        while i < l:
            if s[i]+s[i+1] in roman:
                ans += roman[s[i]+s[i+1]]
                i = i+2
                continue
            ans += roman[s[i]]
            i = i+1
        return ans

class Solution: #解二，同12

    THOUSANDS = ["", "M", "MM", "MMM"]
    HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    def intToRoman(self, num: int) -> str:
        return Solution.THOUSANDS[num // 1000] + \
            Solution.HUNDREDS[num % 1000 // 100] + \
            Solution.TENS[num % 100 // 10] + \
            Solution.ONES[num % 10]

a = "MMM"
solution = Solution()
result = solution.romanToInt(a)
print(result)
