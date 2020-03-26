class Solution:
    def romanToInt(self, s: str) -> int:
        a = s.replace("IV", "4+").replace("IX", "10+").replace("XL", "40+").replace("XC", "90+").replace("CD", "400+").replace("CM", "900+")
        a = a.replace("I", "1+").replace("V", "5+").replace("X", "10+").replace("L", "50+")
        a = a.replace("C", "100+").replace("D", "500+").replace("M", "1000+")
        sum = eval(a[:-1])
        return sum


a = Solution().romanToInt("MCMXCIV")
print(a)
