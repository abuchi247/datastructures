class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        
        i = 0
        j = 0
        
        result = []
        
        while i < len(firstList) and j < len(secondList):
            if len(firstList[i]) < 2:
                i += 1
                continue
            if len(secondList[j]) < 2:
                j += 1
                continue 
                
            lower_bound = max(firstList[i][0], secondList[j][0])            
            higher_bound = min(firstList[i][1], secondList[j][1])
            
            if higher_bound == firstList[i][1]: 
                i += 1
            
            if higher_bound == secondList[j][1]: 
                j += 1
                
            if lower_bound > higher_bound:
                continue
                
            result.append([lower_bound, higher_bound])
            
        return result