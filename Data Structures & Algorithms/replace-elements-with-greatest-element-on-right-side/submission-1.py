class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterate through the list of integers that are in the length of the array
        for i in range(len(arr)):
            # initialize to -1 for the max_num in the array 
            max_num = -1


            for j in range(i + 1, len(arr)):
                if arr[j] > max_num:
                    max_num = arr[j]

            arr[i] = max_num

        return arr

            
            
            




        