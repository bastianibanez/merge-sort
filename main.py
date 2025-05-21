from MergeSorter import MergeSorter
from RandomArray import RandomArray

def main():
    arr = RandomArray.get()
    arr = MergeSorter.merge_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()
