import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
from random import choice, shuffle
from time import time


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

# =======================================basicSettingCompleted======================================================
Testtimes = 30


GuessFrequency = []
GuessTimeList = []
percnetage = 0

# for time1000 in range(Testtimes):

# record the started time
ST = time()

AnswerNumber = choice(SuitableNumbers)  # set the answer number
print(f"answer number: {AnswerNumber}")

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
print(FirstGuessNumber, GuessTimes)
print(FilterDataFrame)
GuessNumber = 0

while True:

    shuffle(SuitableNumbers)

    GuessNumber = choice(SuitableNumbers)

    ReplyAnswerList = []
    # [(0, 0), (0, 0), (0, 1), (0, 2)]
    for CheckedNumber in FilterDataFrame["FilteredNumber"]:
        ReplyAnswerList.append(CountAB(CheckedNumber, GuessNumber))
    FilterDataFrame["Reply"] = ReplyAnswerList

    AnswerReply = CountAB(GuessNumber, AnswerNumber)

    if AnswerReply == (4, 0):
        print(GuessNumber, GuessTimes)

        break

    FilterDataFrame = FilterDataFrame[FilterDataFrame.Reply == AnswerReply]

    if len(FilterDataFrame["FilteredNumber"]) == 1:

        GuessNumber = FilterDataFrame["FilteredNumber"].to_string(
            index=False)
        GuessTimes += 1
        print(FilterDataFrame)
        print(GuessNumber, GuessTimes)
        break

    GuessTimes += 1
    print(GuessNumber, GuessTimes)
    print(FilterDataFrame)

ET = time()
SpendingTime = round(ET - ST, 0)

GuessFrequency.append(GuessTimes)
GuessTimeList.append(SpendingTime)

# with open("20220128record.txt", 'a') as f:
#     f.write(f"{percnetage}% \n", )
#     f.write(f"all GuessFrequency {GuessFrequency} \n")
#     f.write(f"sum of GuessFrequency {sum(GuessFrequency)} \n")
#     f.write(
#         f"average of GuessFrequency {sum(GuessFrequency) / Testtimes} \n")
#     f.write(
#         "======================================================================= \n")

# XFrequency = np.array([a for a in range(1, int(max(GuessFrequency))+1)])
# YFrequency = np.array([GuessFrequency.count(a) for a in XFrequency])

# plt.bar(XFrequency, YFrequency)
# plt.savefig(f"20220128{ percnetage }%Frequency.png")
# plt.close()

# with open("20220128record.txt", 'a') as f:
#     f.write(f"all GuessTimeList {GuessTimeList} \n")
#     f.write(f"sum of GuessTimeList {sum(GuessTimeList)} \n")
#     f.write(
#         f"average of GuessTimeList {sum(GuessTimeList) / Testtimes} \n")
#     f.write(
#         "======================================================================= \n")
#     f.write(
#         "======================================================================= \n")

# XTime = np.array([a for a in range(1, int(max(GuessTimeList))+1)])
# YTime = np.array([GuessTimeList.count(a) for a in XTime])

# plt.bar(XTime, YTime)
# plt.savefig(f"20220128{ percnetage }%Time.png")
# plt.close()
