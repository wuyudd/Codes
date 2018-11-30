# LC 825. Friends Of Appropriate Ages

# also pay attention to subarray problems:
#   547. Friend Circles

#####################################################################################
# my solution:
# idea: rolling sum / dict

# 1 rolling sum
class Solution(object):
    def numFriendRequests(self, ages):
        if not ages:
            return 0
        res = 0
        age_counter = [0] * 121
        age_counter_sum = [0]
        for age in ages:
            age_counter[age] += 1
        for i in range(1, 121):
            age_counter_sum.append(age_counter_sum[i-1] + age_counter[i])

        for j in range(15, 121):
            counter = age_counter_sum[j] - age_counter_sum[j // 2 + 7]
            res += (counter - 1) * age_counter[j]
        return res

# 2 dict
class Solution(object):
    def numFriendRequests(self, ages):
        if not ages:
            return 0
        age_num = {}
        res = 0
        for age in ages:
            age_num[age] = age_num.get(age, 0) + 1

        for age_1, num_1 in age_num.items():
            for age_2, num_2 in age_num.items():
                if age_1 <= age_2 * 0.5 + 7 or age_1 > age_2:
                    continue
                res += num_1 * num_2
                if age_1 == age_2:
                    res -= num_1
        return res


#####################################################################################