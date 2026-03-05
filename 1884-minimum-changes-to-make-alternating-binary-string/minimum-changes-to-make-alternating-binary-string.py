class Solution:
    def minOperations(self, s):
        count_start0 = 0
        count_start1 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    count_start0 += 1
                if s[i] != '1':
                    count_start1 += 1
            else:
                if s[i] != '1':
                    count_start0 += 1
                if s[i] != '0':
                    count_start1 += 1
        
        return min(count_start0, count_start1)