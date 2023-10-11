'''Merge strings alternatively leetcode(1768)'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=[]
        i,j=0,0
        min_length=min(len(word1),len(word2))
        for i range(min_length) and j in range(min_length):
            merged.append(word1[i])
            merged.append(word2[j])
            i=i+1
            j=j+1
        while i<len(word1):
            merged.append(word1[i])
            i=i+1
        while j<len(word2):
            merged.append(word2[j])
            j=j+1
        return ''.join(merged)

        