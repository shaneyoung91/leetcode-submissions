class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
            
            result = 0

            for stone in stones:
                if stone in list(jewels):
                    result += 1
            
            return result