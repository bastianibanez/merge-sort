DEBUG = False

class MergeSorter:
    @staticmethod
    def merge_sort(arr: list[int]):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr)//2
        l_arr, r_arr = arr[:mid], arr[mid:]

        MergeSorter.merge_sort(l_arr)
        MergeSorter.merge_sort(r_arr)
        
        solution = MergeSorter._merge(arr, l_arr, r_arr)
        
        if DEBUG:
            print(solution)
            print(l_arr)
            print(r_arr)
            print()

        return solution
     
    @staticmethod
    def _merge(arr, l_arr, r_arr):
        i, l_idx, r_idx = 0, 0, 0

        while l_idx < len(l_arr) and r_idx < len(r_arr):
            if l_arr[l_idx] < r_arr[r_idx]:
                arr[i] = l_arr[l_idx]
                l_idx += 1
                i += 1
                continue

            arr[i] = r_arr[r_idx]
            r_idx += 1
            i += 1

        while l_idx < len(l_arr):
            arr[i] = l_arr[l_idx]
            l_idx += 1
            i += 1

        while r_idx < len(r_arr):
            arr[i] = r_arr[r_idx]
            r_idx += 1
            i += 1

        return arr