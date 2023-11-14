from array import array


class Solution:
    def sort012(self, arr, num):
        count = [0, 0, 0]        
        for num in arr:
            count[num] += 1
        index = 0
        for i in range(3):
            for y in range(count[i]): 
                arr[index] = i
                index += 1

        return arr


# Create an object from Solution class
inp_ = Solution()
arr= [0, 2, 1, 2, 0]
sorted_arr = inp_.sort012(arr, 5)
print(sorted_arr)

