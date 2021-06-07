class Solution:
    def customSortString(self, S: str, T: str) -> str:
        """
        Time complexity: NxM
        Space complexity: N+M
        """
        unique_set = set(S) # M
        character_occurrence = {}   # N
        new_str = ""    # N
        insertions = 0

        for ch in T:    # N
            if ch in unique_set:
                if ch in character_occurrence:
                    character_occurrence[ch] += 1
                else:
                    character_occurrence[ch] = 1
                insertions += 1  
            else:
                new_str += ch


        for ch in S:    # M
            if ch in character_occurrence:
                occurrence = character_occurrence[ch]
                # new_input = ch * occurrence
                # new_str += new_input
                while character_occurrence[ch] > 0: # N
                    new_str += ch
                    character_occurrence[ch] -= 1
                    
        return new_str


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        """
        Time complexity: NxM
        Space complexity: N+M
        """
        S = list(S) 
        T = list(T)
        temporary = []
        for i in range(len(S)):
            for j in range(len(T)):
                if S[i] == T[j]:
                    temporary.append(T[j])
        
        pending = [item for item in T if item not in temporary]
        
        return "".join(temporary + pending)


# BEST SOLUTION
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        """
        Time complexity: N+M
        Space complexity: M
        """
        char_map = {}
        
        for ch in T:    # M
            if ch in char_map:
                char_map[ch] += 1
            else:
                char_map[ch] = 1
                
        result = []
        
        for ch in S:    # N
            if ch in char_map:
                result.append(ch * char_map[ch])
                del char_map[ch]    # entry from hash table
        
        # add the remaining elements
        for ch in char_map:
            result.append(ch * char_map[ch])
        
        
        return "".join(result)