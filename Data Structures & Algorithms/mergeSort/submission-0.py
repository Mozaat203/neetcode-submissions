# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        m = len(pairs) // 2
        leftHalf = pairs[:m]
        rightHalf = pairs[m:]

        leftSorted = self.mergeSort(leftHalf)
        rightSorted = self.mergeSort(rightHalf)

        return self.merge(leftSorted, rightSorted)

    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:   # compare by key
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result