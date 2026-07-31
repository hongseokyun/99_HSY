class Solution(object):
    def uniquePaths(self, m, n):
        result = float(1)
        max_num = max(m,n)
        div_num = min(m,n)
        for i in range(max_num,m+n-1) :
            result *= i/float(div_num-1)
            print(result)
            div_num -= 1
            if div_num <= 1 :
                div_num = 2
        return int(round(result))
            