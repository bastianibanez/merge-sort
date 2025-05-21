from MergeSorter import MergeSorter

def main():
    arr = [1,5,24,62,72,42,0,24,3,-15,3,-99]
    arr = MergeSorter.merge_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()