class Solution(object):
    def searchInsert(self, nums, target):
        N = len(nums)
        kk = []
        d = []
        def search(arr,idx) :
            print(arr,idx)
            if len(arr) == 1 :
                if arr[0] == target :
                    kk.append(idx)
                    print(kk)
                    return
                else :
                    if arr[0] < target :
                        d.append(idx)
                    return
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]
            search(left,idx)
            search(right,len(arr)//2+idx) 
        search(nums,0)
        if kk :
            return kk[0]
        else :
            if d :
                return max(d) + 1
            else :
                return 0