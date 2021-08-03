class Permutation:
    def __init__(self) -> None:
        self.permutatedList = []

    def stringPermutation(self, word: str, left: int, right: int) -> None:
        if left == right-1:
            self.permutatedList.append(word)
        else:
            for i in range(left, right):
                word = self.swap(word, left, i)
                self.stringPermutation(word, left+1, right)
                word = self.swap(word, left, i)

    def swap(self, word: str, i: int, j: int) -> str:
        word = list(word)
        word[i], word[j] = word[j], word[i]
        return "".join(word)


obj = Permutation()
obj.stringPermutation("abc", 0, 3)
print(obj.permutatedList)
