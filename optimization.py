# optimization

from pandas import Series, DataFrame
from random import choice
from time import time

# record the started time
ST = time()


def CountAB(GuessNumber, CompareNumber):  # definite a CountAB function
    A = 0
    B = 0
    GuessNumber = str(GuessNumber)
    CompareNumber = str(CompareNumber)
    for a in range(0, 4):
        if CompareNumber[a] in GuessNumber:
            if CompareNumber[a] == GuessNumber[a]:
                A += 1
            else:
                B += 1
    return (A, B)


# find all suitable numbers
SuitableNumbers = []
for number in range(123, 1000):
    number = '0' + str(number)
    if len(set(number)) == 4:
        SuitableNumbers.append(number)

for number in range(1000, 10000):
    number = str(number)
    if len(set(number)) == 4:
        SuitableNumbers.append(number)


# creat a default dataframe
DefaultDataFrame = DataFrame({
    "SuitableNumbers": SuitableNumbers,
})

KindOfAnswerList = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (
    1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0)]
DefaultReplyAnswerDict = {}
for BasicSetting in KindOfAnswerList:
    DefaultReplyAnswerDict[BasicSetting] = 0
# {(0, 0): 0, (0, 1): 0 ...}

# AnswerNumber = choice(SuitableNumbers)  # set the answer number
AnswerNumber = 4713
print(f"answer number is {AnswerNumber}")

FirstGuessNumber = "0123"  # set the first guess number
FilterDataFrame = DataFrame({
    "FilteredNumber": SuitableNumbers,
})

ReplyAnswerList = []
# [(0, 0), (0, 0), (0, 1), (0, 2)]
for CheckedNumber in FilterDataFrame["FilteredNumber"]:
    ReplyAnswerList.append(CountAB(CheckedNumber, FirstGuessNumber))
FilterDataFrame["Reply"] = ReplyAnswerList

AnswerReply = CountAB(FirstGuessNumber, AnswerNumber)
FilterDataFrame = FilterDataFrame[FilterDataFrame.Reply == AnswerReply]


GuessTimes = 1
GuessNumber = 0

while True:

    SDDataFrame = DataFrame({
        "SuitableNumbers": SuitableNumbers,
    })  # statistic the standard deviation
    SDList = []

    for CandidateNumber in SuitableNumbers:

        ReplyAnswerDict = DefaultReplyAnswerDict.copy()
        # {(0, 0): 0, (0, 1): 0 ...}

        for CheckedNumber in FilterDataFrame["FilteredNumber"]:
            ReplyAnswer = CountAB(CandidateNumber, CheckedNumber)
            ReplyAnswerDict[ReplyAnswer] += 1

        SDList.append(Series(ReplyAnswerDict.values()).std())

    SDDataFrame["SD"] = SDList

    IndexNumber = SDDataFrame["SD"].idxmin()
    GuessNumber = SDDataFrame["SuitableNumbers"][IndexNumber]
    

    ReplyAnswerList = []
    # [(0, 0), (0, 0), (0, 1), (0, 2)]
    for CheckedNumber in FilterDataFrame["FilteredNumber"]:
        ReplyAnswerList.append(CountAB(CheckedNumber, GuessNumber))
    FilterDataFrame["Reply"] = ReplyAnswerList

    AnswerReply = CountAB(GuessNumber, AnswerNumber)

    if AnswerReply == (4, 0):
        print(f"Answer is {GuessNumber}")
        print(f"Guess {GuessTimes} times")
        break

    FilterDataFrame = FilterDataFrame[FilterDataFrame.Reply == AnswerReply]

    if len(FilterDataFrame["FilteredNumber"]) == 1:

        GuessNumber = FilterDataFrame["FilteredNumber"].to_string(index=False)
        GuessTimes += 1
        print(f"Answer is {GuessNumber}")
        print(f"Guess {GuessTimes} times")
        break

    GuessTimes += 1


ET = time()
print(round(ET - ST, 4))
