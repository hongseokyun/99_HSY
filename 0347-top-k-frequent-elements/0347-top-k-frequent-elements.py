class Solution(object):
    def topKFrequent(self, nums, k):
        dic = dict()
        # all components count
        for i in nums[:] :
            if i in dic.keys() :
                dic[i] += 1
            else :
                dic[i] = 1
        
        # sort based-on counts
        sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        arr = sort_dic[:k]
        result = []
        for i in arr :
            result.append(i[0])
        return result

