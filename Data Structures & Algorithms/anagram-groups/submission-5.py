class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict={}
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord("a")]+=1
            key=tuple(count)
            if key in my_dict:
                my_dict[key].append(word)
            else:
                my_dict[key]=[word]  
        return list(my_dict.values())