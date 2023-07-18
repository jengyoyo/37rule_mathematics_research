import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from random import shuffle
from time import time

ST = time()

PickedList = []
list1 = [a for a in range(100)]
percentage = 37


def Rule37(List):

    The37 = max(List[:percentage])

    for a in List[percentage:]:
        if a > The37:
            return a
    else:
        return List[-1]


RepeatTimes = 10000

for times in range(RepeatTimes):
    shuffle(list1)
    PickedList.append((Rule37(list1)))


print(f"min value in PickedList: {min(PickedList)}")
print(f"max value in PickedList: {max(PickedList)}")
print(f"average in PickedList: {round(sum(PickedList) / len(PickedList), 2)}")
print(
    f"The percentage of picking the maximum: { PickedList.count(99) / RepeatTimes }")
print("================================================")

ET = time()
print(ET - ST)
print("================================================")


X_numbers = [a for a in range(min(PickedList), max(PickedList) + 1)]
Y_times = [PickedList.count(a) for a in X_numbers]

X_numbers = list(map(lambda x: str(x), X_numbers))
x = np.array(X_numbers)
y = np.array(Y_times)

Data = pd.DataFrame({"number": X_numbers,
                     "times": Y_times
                     })
print(Data)

# plt.plot(x, y)
# plt.show()
