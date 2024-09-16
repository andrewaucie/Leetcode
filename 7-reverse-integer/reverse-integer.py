class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        stringX = str(x)
        if x < 0:
            stringX = stringX[1:]
        reversedX = ""
        i = len(stringX)-1
        while i >= 0:
            if stringX[i] != "0":
                break
            i -= 1
        while i >= 0:
            reversedX += stringX[i]
            i -= 1 
        reversedIntX = int(reversedX)
        if x < 0:
            reversedIntX *= -1
        if reversedIntX < -2**(31) or reversedIntX >= 2**(31):
            return 0
        return reversedIntX
        
