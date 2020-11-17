# https://leetcode-cn.com/problems/queue-reconstruction-by-height/
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
from typing import List


class Solution:
    # 从小到大排列
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 对于同身高的人，位置越大的说明前面的人越多，说明有其他同身高的人在他之前，所以用 -x[1] 来对同身高的位置排序，
        # 即同身高的多个人，按照位置大小逆序插入队伍，也就是 k 值越 大 的越早插入队伍。
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            # 因为是按从小到大的顺序插入队列的，所以当 person 这个人插入队列中时，一定是第 k + 1 位置，
            # 前面一定有 k 个大于等于他的人。
            spaces = person[1] + 1
            # 开始数位置，这些位置要留给大于他的人。
            for i in range(n):
                # 因为是从小到大的顺序插入队列的，所以如果一个位置有值，则一定是小于 h 的数，spaces 不减少
                # 不会等于因为按 k 的逆序排序，k 值最大的 person 一定最先排
                if not ans[i]:
                    # 如果减少，则一定是比他大的数。
                    spaces -= 1
                    # 当前面比 i 大的数字都数出来时，新的位置就是 i 的位置。
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans


class Solution2:
    # 从大到小排列
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按从大到小的顺序排列，身高相同时 k 值越 小 的越早插入队伍
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = list()
        # 因为比 person 小的不会影响 person，因此它可以直接插入 k 值的位置。
        # 直接插入 k 位置的原因：
        # k 代表有 k 个人在 person 之前，所以只要插入到 k 位置，就是符合 k 的定义的，其他比他小的数字不需要关心。
        # 因为是从大到小插入的，所以插入到位置 k 时，一定有 k 个数比 person 大
        # （如果不够会自动向前补位，而所给条件是一定能排序成功的，所以不用担心 k 会被撑爆的问题）
        for person in people:
            # ans[person[1]:person[1]] = [person] 与 ans.insert(person[1], person) 相同
            # 但 ans[0:1] = [person] 和 ans.insert(0, person) 就不同了，因为此时会把 ans 的两个位置用 person 替换，如果
            # person 数量小于 ans 要替换的位置则后面自动补上，超出则自动扩展。
            # 如果插入的位置大于列表实际长度，则会插入到末尾位置
            ans[person[1]:person[1]] = [person]
        return ans
