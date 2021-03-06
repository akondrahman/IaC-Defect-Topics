'''
enhanced pre-processing
to handle list oflists
Feb 27, 2017

'''
import utility, token_pre_processor
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
PuppetKeyWordFileName = 'PUPP_KW.txt'
PuppetKeywordList = utility.readKeywordFile(PuppetKeyWordFileName)



def removeNumeralsFromList(listParam):
    tempList=[]
    finalList=[]
    for list_ in listParam:
        for tokenStr in list_:
            modifiedTokenStr =  token_pre_processor.removeNumeralsFromWord(tokenStr)
            tempList.append(modifiedTokenStr)
        finalList.append(tempList)
        #print "List after numeral handling: ", tempList
        tempList = []
    return finalList



def removeSpecialCharsFromList(listParam):
    tempList=[]
    finalList=[]
    for list_ in listParam:
        for tokenStr in list_:
            modifiedTokenStr =  token_pre_processor.removeSpecialCharsFromWord(tokenStr)
            tempList.append(modifiedTokenStr)
        finalList.append(tempList)
        #print "List after special character handling: ", tempList
        tempList = []
    return finalList


def removeDelimitersFromList(listParam):
    tempList=[]
    finalList=[]
    for list_ in listParam:
        for tokenStr in list_:
            modifiedTokenStr =  token_pre_processor.removeDelimitersFromWord(tokenStr)
            tempList.append(modifiedTokenStr)
        finalList.append(tempList)
        #print "List after special character handling: ", tempList
        tempList = []
    return finalList


def splitUnderscores(listParam):
    tempList=[]
    finalList=[]
    underscoreStr="_"
    splittedTokenList = []
    for list_ in listParam:
        #print "List before underscore handling: ", listO
        for tokenStr in list_:
            if tokenStr is not None  and underscoreStr in tokenStr:
                splittedTokenList = token_pre_processor.splitUnderscores(tokenStr)
                tempList.extend(splittedTokenList)
            else:
                tempList.append(tokenStr)
        finalList.append(tempList)
        #print "List after underscore handling: ", tempList
        tempList = []
    return finalList



def splitSpaces(listParam):
    tempList=[]
    finalList=[]
    spaceStr=" "
    splittedTokenList = []
    for list_ in listParam:
        #print "List before space handling : ", listO ;
        for tokenStr in list_:
            if tokenStr is not None  and spaceStr in tokenStr:
                splittedTokenList = token_pre_processor.splitSpaces(tokenStr)
                tempList.extend(splittedTokenList)
            else:
                tempList.append(tokenStr)
        finalList.append(tempList)
        #print "List after space handling: ", tempList
        tempList = []
    return finalList



def handleCamelNPascalCaseInList(listParam):
    tempList=[]
    finalList=[]
    for list_ in listParam:
        for tokenStr in list_:
            modifiedTokenStr = token_pre_processor.splitCamelNPascalCase(tokenStr)
            tempList.append(modifiedTokenStr)
        finalList.append(tempList)
        #print "List after camel case handling: ", tempList
        tempList = []
    return finalList


def removeSmallLenghtedTokens(listParam, thresP):
    tempList=[]
    finalList=[]
    for list_ in listParam:
        for tokenStr in list_:
            if type(tokenStr) is str:
               if len(tokenStr) > thresP:
                  tempList.append(tokenStr)
        finalList.append(tempList)
        #print "List after removing small lenghted tokens: ", tempList
        tempList = []
    return finalList

def removeStopWords(listParam):
    #this method removes tokens that are basically stop words from the list
    tempList=[]
    finalList=[]
    for list_ in listParam:
        for tokenStr in list_:
            if tokenStr not in utility.get_stop_words():
                tempList.append(tokenStr)
        finalList.append(tempList)
        #print "List after removing stop words : ", tempList
        tempList = []
    return finalList


def removePuppKeywords(listParam):
    #this method removes tokens that are Java keywords, from the list
    tempList=[]
    finalList=[]
    for list_ in listParam:
        for tokenStr in list_:
            if tokenStr not in PuppetKeywordList :
                tempList.append(tokenStr)
        finalList.append(tempList)
        #print "List after removing Java keywords: ", tempList
        tempList = []
    return finalList


def format_using_stemmer(listParam):
  #print len(listParam)
  output_list = []
  formatted_list = []
  #stemmer_obj = PorterStemmer()
  stemmer_obj  = SnowballStemmer("english")
  for subList in listParam:
    formatted_list = [stemmer_obj.stem(token) for token in subList]
    output_list.append(formatted_list)
    formatted_list = []
  return output_list

def splitDots(listParam):
    tempList=[]
    finalList=[]
    dotStr="."
    splittedTokenList = []
    for list_ in listParam:
        for tokenStr in list_:
            if tokenStr is not None  and dotStr in tokenStr:
                splittedTokenList = token_pre_processor.splitDots(tokenStr)
                tempList.extend(splittedTokenList)
            else:
                tempList.append(tokenStr)
        finalList.append(tempList)
        tempList = []
    return finalList
def splitColons(listParam):
    tempList=[]
    finalList=[]
    colonStr=":"
    splittedTokenList = []
    for list_ in listParam:
        for tokenStr in list_:
            if tokenStr is not None  and colonStr in tokenStr:
                splittedTokenList = token_pre_processor.splitColons(tokenStr)
                tempList.extend(splittedTokenList)
            else:
                tempList.append(tokenStr)
        finalList.append(tempList)
        tempList = []
    return finalList
def splitSlashes(listParam):
    tempList=[]
    finalList=[]
    _Str="/"
    splittedTokenList = []
    for list_ in listParam:
        for tokenStr in list_:
            if tokenStr is not None  and _Str in tokenStr:
                splittedTokenList = token_pre_processor.splitSlashes(tokenStr)
                tempList.extend(splittedTokenList)
            else:
                tempList.append(tokenStr)
        finalList.append(tempList)
        tempList = []
    return finalList
def splitDashes(listParam):
    tempList=[]
    finalList=[]
    _Str="-"
    splittedTokenList = []
    for list_ in listParam:
        for tokenStr in list_:
            if tokenStr is not None  and _Str in tokenStr:
                splittedTokenList = token_pre_processor.splitDashes(tokenStr)
                tempList.extend(splittedTokenList)
            else:
                tempList.append(tokenStr)
        finalList.append(tempList)
        tempList = []
    return finalList




def convertToUTF(listParam):
  #print len(listParam)
  output_list = []
  formatted_list = []
  for subList in listParam:
    formatted_list = [token.decode('utf-8', 'ignore') for token in subList]
    output_list.append(formatted_list)
    formatted_list = []
  return output_list
