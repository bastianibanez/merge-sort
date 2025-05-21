from random import randint
class RandomArray:

    @staticmethod
    def get(n=10):
        arr = []
        for _ in range(n):
            arr.append(randint(-50,50))
        return arr

        