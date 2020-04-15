class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        s_list = list(s)
        n = len(s_list)
        num = 0
        for i in range(n):
            if i != n-1:
                if dic[s_list[i]] < dic[s_list[i+1]]:
                    num += -dic[s_list[i]]
                else:
                    num += dic[s_list[i]]
            else:
                num += dic[s_list[i]]
        return num


a = Solution().romanToInt("MCMXCIV")
print(a)
