class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict={}
        my_lst=[]
        for word in strs:
            ana_word="".join(sorted(word))
            if ana_word not in my_dict:
                my_dict[ana_word]=[word]
            else:
                my_dict[ana_word].append(word)
        for value in my_dict.values():
            my_lst.append(value)
        return my_lst
                


                

                