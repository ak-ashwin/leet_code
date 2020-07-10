from typing import List

# Example
# 1:
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example
# 2:
#
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


class Solution:
    def defangIPaddr(self, address: str) -> str:

        output = ""

        for i, num in enumerate(address):
            if num == ".":
                output = output + "[.]"
            else:
                output = output + num

        return output

# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".","[.]")


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.defangIPaddr("1.1.1.1"))
