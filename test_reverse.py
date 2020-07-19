class Solution:
    def reverse_func(self, text):
        result = []
        for i in range(len(text) - 1, -1, -1):
            result.append(text[i])
        return result

    def reverse_func_while(self, firstList):
        secondList = []
        counter = len(firstList) - 1
        while counter >= 0:
            secondList.append(firstList[counter])
            counter -= 1
        return secondList


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.reverse_func([1, 2, 3]))
    # print(Sol.reverse_func(['hi', 'hello', 'this', 'that', 'is', 'of']))
    print(Sol.reverse_func_while([1, 2, 3]))

