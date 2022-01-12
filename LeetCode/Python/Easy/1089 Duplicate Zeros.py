class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        lenght = len(arr)
        i = 0
        while i <= lenght - 1:
            if arr[i] == 0:
                if i + 2 <= lenght - 1:
                    arr[i + 1], arr[i + 2] = arr[i + 2], arr[i + 1]
                    for j in range(i + 3, lenght):
                        arr[i + 1], arr[j] = arr[j], arr[i + 1]
                    arr[i + 1] = 0
                    i += 1
                elif i == lenght - 2:
                    arr[i + 1] = 0
            i += 1
