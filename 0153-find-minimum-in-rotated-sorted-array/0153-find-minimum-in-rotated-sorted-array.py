class Solution(object):
    def findMin(self, nums):
        kk = []
        def search(arr) :
            print(arr)
            if len(arr) == 1 :
                if kk :
                    if kk[0] > arr[0] :
                        kk.pop()
                        kk.append(arr[0])
                        return
                    else :
                        return
                else :
                    kk.append(arr[0])
                    return
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:] 
            print(left,right)
            search(left)
            search(right)
        search(nums)
        return kk[0]
        