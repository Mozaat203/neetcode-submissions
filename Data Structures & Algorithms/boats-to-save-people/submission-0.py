class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left, right = 0, len(people) - 1
        numberOfBoats = 0
        while left <= right:
            
            if people[right] == limit:
                numberOfBoats += 1
                right -= 1
                continue

            elif people[right] + people[left] > limit:
                numberOfBoats += 1
                right -= 1

            else:
                numberOfBoats += 1
                left+=1
                right-=1
            
        return numberOfBoats