from matplotlib.axis import XAxis
from numpy import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = 100000
sum = 0
numRoundsToLoose = []

wallet = x*1000
money = 0

def settings():
    global account
    global counter
    global result
    global bet
    global lose
    account = 1000
    counter = 0
    result = 0
    bet = 1
    lose = True


print('----------check----------')

settings()
for i in range(x):
    if i % (x/1000) == 0:
        print("this is: ", i/(x/100), "%")
    while lose == True:
        counter += 1
        if account < bet:
            bet = account
            # print('va banque')
        # print("account: ",account, "bet:",bet)
        result = random.randint(1, 3)
        if result == 1:
            account -= bet
            bet = bet*2
            # print("lose: ","account: ",account,)
        else:
            account += bet
            # print("win: ", "account: ",account,)
        # print(counter)
        if account == 0:
            lose = False
        if  counter >= 50:
            lose = False

    money += account

    numRoundsToLoose.append(counter)
    sum += counter
    settings()


print('----------check----------')

n = np.array(numRoundsToLoose)
arr = np.sort(n)
aux = 0
xaxis = []
yaxis = []

# print(arr)

for i in range(arr[0], arr[len(arr)-1]+1):
    filter_arr = arr == i
    newarr = arr[filter_arr]
    if len(newarr) > 0:
        aux = newarr[0]
        xaxis.append(aux)
    else:
        xaxis.append(0)
    yaxis.append((len(newarr)/x)*100)
    # yaxis.append(len(newarr))

print(xaxis)
print('------------------------')
print(yaxis)
print('------------------------')
print(sum/x)

plt.title("średnia: {}".format(sum/x))
plt.xlabel("ilość rund do przegranej")
plt.ylabel("procent[%]")

plt.bar(xaxis, yaxis)
plt.show()

print('money   -- ',money)
print('account -- ',wallet)
print('diff -- ',(money - wallet)/wallet,'%')