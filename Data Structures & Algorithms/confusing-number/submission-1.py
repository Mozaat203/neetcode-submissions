class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotated ={0:0,1:1,6:9,8:8,9:6 }
        original= n
        rotated_num=0

        if n == 0:
            return False

        while n>0:

            digit = n % 10

            if digit not in rotated:
                return False
            
            rotated_num = (rotated_num * 10) + rotated[digit]
            n//=10

        return original != rotated_num
            



