class Solution: #解一
    def intToRoman(self, num: int) -> str:
        # 只有4，9出现时需要改变，其他皆可叠加
        roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        ans = ""
        for i, val in reversed(roman.items()):  # 反向取dict，先大后小
            a = num//i
            if a == 0:
                continue
            ans = ans+a*val
            num = num-a*i
        return ans

class Solution: #解二
    # 每位数的每个数字都能用相互独立的字母代替
    # 直接计算得到index
    THOUSANDS = ["", "M", "MM", "MMM"]
    HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    def intToRoman(self, num: int) -> str:
        return Solution.THOUSANDS[num // 1000] + \
            Solution.HUNDREDS[num % 1000 // 100] + \
            Solution.TENS[num % 100 // 10] + \
            Solution.ONES[num % 10]

a = 3749
solution = Solution()
result = solution.intToRoman(a)
print(result)
