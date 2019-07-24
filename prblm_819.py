

# https://leetcode.com/problems/most-common-word/


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        banned = [word.lower() for word in banned]
        
        para_list = paragraph.split() # splitting the sentence " " space wise
        
        temp = []
        for word in para_list: # splitting further "!?',;." any one of the character wise
            if ',' in word:
                temp = temp + word.split(',')
            elif ';' in word:
                temp = temp + word.split(';')
            elif '.' in word:
                temp = temp + word.split('.')
            elif "\'" in word:
                temp = temp + word.split('\'')
            elif '!' in word:
                temp = temp + word.split('!')
            elif '?' in word:
                temp = temp + word.split('?')
            else:
                temp.append(word)
        
        para_list = temp
                
        para_list = [word.strip('') for word in para_list if word.strip('') != '']
        para_list = [word.lower() for word in para_list] # lowercassing all to make case insensitive sentence
        
        dictionary = dict() # dict to hold wods with correspoding freq of occurence
        
        for word in para_list:
            if word in banned:
                continue
            
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
        
        freq = 0
        freq_word = ''
        
        for key in dictionary:
            
            if dictionary[key] > freq:
                freq = dictionary[key]
                freq_word = key
                
        return freq_word # return wod with highest occurence
            