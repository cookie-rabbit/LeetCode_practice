class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
        ls = list(str(abs(x)))
        a = ls[::-1]
        a = "".join(a)
        a = int(a)
        if flag:
            a = 0 - a
        else:
            pass
        if -2147483648 <= a <= 2147483647:
            pass
        else:
            return 0
        return a


if __name__ == '__main__':
    b = Solution().reverse(-2023123123)
    print(b)
