import re
from collections import Counter

class analysedText(object):
    
    def __init__ (self, text):
        
        # format text, remove punctuation
        self.text = text       #declare a global variable, otherwise for loop will not save
        self.fmtText = self.text.lower()   #make text lower case

        #Remove special characters ',.!?' / Substring replacement        

        #loop implementation
        # chars_str = '.!,?'
        # for i in range(len(chars_str)):         #can't use len() alone b/c int obj is not iterable
        #     self.fmtText = self.fmtText.replace(chars_str[i], '')
            
        # list comprehension implementation
        # char_list = ['.', '!', ',', '?']
        # self.fmtText = ''.join(['' if i in char_list else i for i in self.fmtText])
        
        # list comprehension implementation (all inclusive)
        # self.fmtText = ''.join([i for i in self.fmtText if i.isalpha() or i.isspace()])
        
        #regular expression
        #replace all char not alphanumeric with ''
        self.fmtText = re.sub('[^A-Za-z0-9 ]', '', self.fmtText)
        
    def freqAll(self):        
        # Tokenizing a string and counting unique words - String tokenization 
        
        # Tokenize with string.split(), returns a list of delimiter separated words
        # wordList = self.fmtText.split(' ')
        
        # Tokenize with regular expression, re.split()
        wordList = re.split(r'\s', self.fmtText)
        
        # Use set() to filter out unique words
        # freqMap = {}  #create an empty dictionary with {}. Can't use it for set, use empty_set = set()
        # for word in set(wordList): # use set to remove duplicates in list
        #     freqMap[word] = wordList.count(word)
        # return freqMap          #returns a freqMap dictionary
        
        # Use dict.get() to count frequency
            # here if word is not in freqMap, get() returns 1, thus adding an entry key to dict
        # freqMap = {}
        # for word in wordList:
        #     freqMap[word] = freqMap.get(word, 1) 
        # return freqMap
        
        # Use Counter collection to return a Counter() dictionary of key(words): value(freq)
        return Counter(wordList)
    
    def mostCommonWord(self):
        # return the most common word + it's frequency in dictionary as tuple
        
        # Loop implementation
        # bigCount = None
        # bigWord = None
        # for word, count in self.freqAll():
        #     if bigCount() is None or count > bigCount():
        #         bigWord() = word
        #         bigCount() = count
        
        freqDict = self.freqAll()

        # https://www.programiz.com/python-programming/methods/built-in/max
        bigWord = max(freqDict, key = freqDict.get)     
        print(f'The most common word is {bigWord} and it appeared {freqDict.get(bigWord, None)} times')
        
        return bigWord, freqDict.get(bigWord, None)
        
    
    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()
        
        return freqDict[word] if word in freqDict else 0
    

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:                  #if True
       return 'Test Passed'
    else :
       return 'Test Failed'

print('Constructor: ')
try:
    samplePassage = analysedText('Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.')
    print(testMsg(samplePassage.fmtText == 'lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet'))
except:
    print('Error detected. Recheck your function ' )
print('freqAll: ')
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print('Error detected. Recheck your function ' )
print('freqOf: ')
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print('Error detected. Recheck your function  ' )