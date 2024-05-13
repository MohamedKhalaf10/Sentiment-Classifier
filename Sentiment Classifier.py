# check 16.10 for project description and steps
'''
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
'''
##################################################### Global Variables ########################################################################
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
positive_words = []
negative_words = []
resulting_data = {}
#################################################### Function Definitions ######################################################################

def strip_punctuation (s: str) -> str:
    ''' Function that removes puncuations from a given string then return it '''

    for c in punctuation_chars:
        s = s.replace(c, "")
    
    return s

def get_pos (s: str) -> int:
    ''' Function count number of positive words in a sentance and return the number '''

    numOfPos = 0
    wordsList = s.split()

    for word in wordsList:
        if strip_punctuation(word).lower() in positive_words:
            numOfPos += 1

    return numOfPos

def get_neg (s: str) -> int:
    ''' Function count number of negative words in a sentance and return the number '''

    numOfNeg = 0
    wordsList = s.split()

    for word in wordsList:
        if strip_punctuation(word).lower() in negative_words:
            numOfNeg += 1

    return numOfNeg
#################################################### Application #############################################################################

# Store Positive Words
with open('positive_words.txt', 'r') as pos_f:
    for line in pos_f:
        if line[0] != ";" and line[0] != "\n":
            positive_words.append(line.strip())

# Store Negative Words
with open('negative_words.txt', 'r') as neg_f:
    for line in neg_f:
        if line[0] != ";" and line[0] != "\n":
            negative_words.append(line.strip())


# Count the number of Positive and Negative Words in the data tweets and store this data
with open('project_twitter_data.csv', 'r') as tweets_f:
    dataRows = tweets_f.readlines()[1:]

    for rowIdx, rowValue in enumerate(dataRows):
        rowValueList = rowValue.strip().split(",")
        resultValuesLst= []
        resultValuesLst.append(rowValueList[1])                             # Number of Retweets
        resultValuesLst.append(rowValueList[2])                             # Number of Replies
        resultValuesLst.append(get_pos(rowValueList[0]))                    # Positive Score
        resultValuesLst.append(get_neg(rowValueList[0]))                    # Negative Score
        resultValuesLst.append(resultValuesLst[2] - resultValuesLst[3])     # Net Score


        resulting_data["Tweet No."+ str(rowIdx + 1)] = resultValuesLst

# Transfer the data into a csv file
with open('resulting_data.csv', 'w') as results_f:
    results_f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

    for v in resulting_data.values():
        results_f.write("{}, {}, {}, {}, {}\n".format(v[0], v[1], v[2], v[3], v[4]))