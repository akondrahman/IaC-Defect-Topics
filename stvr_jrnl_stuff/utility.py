'''
utility file for
topic modeling in IaC scripts
Akond Rahman
Feb 26, 2017
'''
import time, datetime, os, sys, csv, pandas as pd
from collections import defaultdict
import numpy as np




def get_stop_words():
  lisToRet =  ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
  'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
  'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
  'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
  'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
  'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
  'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
  'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
  'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
  'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
  'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
  'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
  return lisToRet

def giveCommentFreeContentFromFile(fileNameParam, flag_=False):
  str2ret=""
  if (os.path.exists(fileNameParam)):
     for line_ in open(fileNameParam, 'rU'):
         plus_occu = line_.count('+')
         minus_occu = line_.count('-')
         at_occu = line_.count('@')
         li=line_.strip()
         # if ((not li.startswith("#")) and (plus_occu==1) and (minus_occu==1) and (at_occu == 0)):
         if ((not li.startswith("#"))):
            #print line.rstrip()
            str2ret = str2ret + line_.rstrip()

  return str2ret

def giveTimeStamp():

  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret
def readKeywordFile(fileName):
    listToRet = [] 
    fileO = open(fileName, 'rU')
    for line in fileO:
        line = line.strip('\n')
        line = line.strip('\t')
        listToRet.append(line)
    return listToRet 


def performCleanUp(fileParam):
    if os.path.isfile(fileParam):
       os.remove(fileParam)


def dumpTokens(def_tokens, non_def_tokens):
    def_str = ''
    non_def_str = ''
    def_filtered, non_def_filtered = [], []
    for tok_ in def_tokens:
        tokens_list = tok_.split(' ')
        for token_ in tokens_list:
            def_filtered.append(token_)
    for tok_ in non_def_tokens:
        tokens_list = tok_.split(' ')
        for token_ in tokens_list:
            non_def_filtered.append(token_)
    def_filtered     = np.unique(def_filtered)
    non_def_filtered = np.unique(non_def_filtered)
    for tok_ in def_filtered:
        def_str = def_str + tok_ + ',' + '\n'
    for tok_ in non_def_filtered:
        non_def_str = non_def_str + tok_ + ',' + '\n'
    dumpContentIntoFile(def_str, '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Semantics/results/ALL_DEF_TOKENS.csv')
    dumpContentIntoFile(non_def_str, '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Semantics/results/ALL_NON_DEF_TOKENS.csv')

# def createCorpusForLDA(listParam, fileNameParam):
#     ## first clean up previously created files
#     theMMFile        = fileNameParam + ".mm"
#     theDictFile      = fileNameParam + ".dict"
#     theMMIndexFile   = fileNameParam + ".mm.index"
#     performCleanUp(theMMFile)
#     performCleanUp(theDictFile)
#     performCleanUp(theMMIndexFile)
#     ## get any remaining stop words
#     stopWordList = get_stop_words()
#     #### two loops in one array syntax ! for all the documents do , get all those words whcih are not in the stop list
#     #texts = [[word for word in document.lower().split() if word not in stopWordList]
#     #          for document in modifiedDocList]
#     texts = [[word.lower() for word in docList if word not in stopWordList] for docList in listParam]
#     tokenFreq = defaultdict(int)
#     for text in texts:
#         for token in text:
#             tokenFreq[token] += 1

#     ##only add thsoe tokens that appear more than once in the documents
#     texts = [ [token for token in text if tokenFreq[token] > 1] for text in texts]

#     #pprint(texts)

#     txtDictionary = corpora.Dictionary(texts)
#     #pprint(txtDictionary)
#     txtDictionary.save(theDictFile)
#     #print(txtDictionary)


#     ## creating corpus
#     corpus = [txtDictionary.doc2bow(text) for text in texts]
#     #print "the .mm file", corpus
#     #print "Inside the .mm file "
#     #pprint(corpus)
#     corpora.MmCorpus.serialize(theMMFile, corpus)
#     print "Done Creating Corpus ... "



# def performLDA(corpusFileParam, topicNumParam):
#     dictFileToRead  = corpusFileParam+'.dict'
#     mmFileToread    = corpusFileParam + '.mm'
#     dictToUse       = corpora.Dictionary.load(dictFileToRead)
#     corpToUse       = corpora.MmCorpus(mmFileToread)
#     print "Doing LDA model ..."
#     ## the follwong line take a lot of time for large number of documents
#     fittedLDAModel  = models.LdaModel(corpToUse, num_topics=topicNumParam, id2word=dictToUse)
#     corpus_LDA      = fittedLDAModel[corpToUse] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
#     ### let us print the words that constitue a topic
#     topic_distr_to_print  = fittedLDAModel.print_topics(topicNumParam)
#     return topic_distr_to_print, corpus_LDA



def processDataset(datasetAsAListOfLists):
  str2Return=""
  for list_ in datasetAsAListOfLists:
    for elem in list_:
        str2Return = str2Return + elem + ','
    str2Return = str2Return +  '\n'
  return str2Return



def dumpContentIntoFile(strP, fileP):
  fileToWrite = open( fileP, 'w')
  fileToWrite.write(strP )
  fileToWrite.close()
  return str(os.stat(fileP).st_size)





def dump_topic_modeling_metrics(datasetP, ndtDictP, ntDictP, tmDictP, dtmDictP, outputFileP):
  dataset_to_write = []
  with open(datasetP, 'rU') as f:
     reader_ = csv.reader(f)
     next(reader_, None)
     for row_ in reader_:
        file_name_  = row_[1]
        if ((file_name_ in ndtDictP) and (file_name_ in ntDictP) and (file_name_ in tmDictP) and (file_name_ in dtmDictP)):
            row2Write_ = []
            ## 1. NDT OF  A FILE, LIST OF VALUES
            NDT_Of_File = str(len(ndtDictP[file_name_]))
            ## 2. NT OF  A FILE, LIST OF VALUES
            NT_Of_File  = str(len(ntDictP[file_name_]))
            ## 3. TM OF  A FILE, LIST OF VALUES
            TM_Of_file  = tmDictP[file_name_]
            TM_Of_file  = [str(x_) for x_ in TM_Of_file]
            ## 4. DTM OF  A FILE, LIST OF VALUES
            DTM_Of_file = dtmDictP[file_name_]
            DTM_Of_file = [str(y_) for y_ in DTM_Of_file]
            ## 5. REMOVE THE FILE NAME FROM THE ROW
            row_ = [elem for elem in row_ if elem!=file_name_]
            #print "After removing file name:", row_
            ## 6. REMOVE THE ORG NAME FROM THE ROW, WE DONT NEED IT AS THE DATASETS ARE SEPERATE
            org_ = row_[0]
            row_.remove(org_)
            #print "After removing org. name:", row_
            ## 7. convert list to a string of values
            staticMetricsToWrite_ = [str(x_) for x_ in row_]
            row2Write_.append(file_name_)
            row2Write_.append(NDT_Of_File)
            row2Write_.append(NT_Of_File)
            row2Write_            = row2Write_ + TM_Of_file + DTM_Of_file + staticMetricsToWrite_
            #print "Row to write:", row2Write_
            dataset_to_write.append(row2Write_)
  str2Dump = processDataset(dataset_to_write)
  #print "This is what we will dump: \n", str2Dump
  dump_stat = dumpContentIntoFile(str2Dump, outputFileP)
  return dump_stat


def dumpComparisonMetrics(listOfVecs, wordCountParam, file_to_save):
  str2Dump = ''
  header   = 'TOKEN, D_TF, ND_TF, D_IDF, ND_IDF, D_RAW_OCCUR, ND_OCCUR, D_TFIDF, ND_TFIDF, D_ENTROPY, ND_ENTROPY,'
  for cnt_ in xrange(wordCountParam):
    for vector_ in listOfVecs:
      str2Dump = str2Dump + str(vector_[cnt_]) + ','
    str2Dump = str2Dump + '\n'
  str2Dump = header + '\n' + str2Dump
  dump_status = dumpContentIntoFile(str2Dump, file_to_save)
  print "Dumped a file of {} bytes".format(dump_status)





'''
for converting docuemnt trm amtrix to python pandas df
'''
def dumpTransformedTokenMatrixToCSV(transformed_features_param, feature_param, output_file_param ):
    df2ret = pd.DataFrame(transformed_features_param.toarray().transpose(), index = feature_param)
    df2ret.to_csv(output_file_param)
    return df2ret
