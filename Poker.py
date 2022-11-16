import random

rounds = 100000
handysmbols = []
handvalues = []
hand = []
lastcard = []
statistic = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two pairs": 0,
    "Pair": 0,
    "High Card": 0
}

probabilites = {

    "Royal Flush": 0.000154 / 100,
    "Straight Flush": 0.00139 / 100,
    "Four of a Kind": 0.02401 / 100,
    "Full House": 0.1441 / 100,
    "Flush": 0.1965 / 100,
    "Straight": 0.3925 / 100,
    "Three of a Kind": 2.1128 / 100,
    "Two pairs": 4.7539 / 100,
    "Pair": 42.2569 / 100,
    "High Card": 50.1177 / 100


}


def getsymbol(numbers):
    numbers %= 4
    if numbers == 0:
        return "Heart"
    if numbers == 1:
        return "Club"
    if numbers == 2:
        return "Diamond"
    if numbers == 3:
        return "Spade"


def getcardnumber(number):
    number %= 13
    return number


def getcards(minimum, maximum, amount):
    cards = []
    for g in range(minimum, maximum + 1):
        cards.append(g)
    for j in range(amount):
        randindex = random.randrange(0, maximum - minimum + 1)
        lastPosition = len(cards) - 1 - j
        cards[randindex], cards[lastPosition] = cards[lastPosition], cards[randindex]
    return cards[-amount:]


def convertvalue(value):
    realvalue = value + 2
    if realvalue == 11:
        return "J"
    if realvalue == 12:
        return "Q"
    if realvalue == 13:
        return "K"
    if realvalue == 14:
        return "A"
    return realvalue

def getdifference(statistic, probabilites):
    difference = {}
    for k in statistic.keys():
        difference[k] = (probabilites[k] - (statistic[k] / rounds)) * 100
    return difference


def checkforpairs(values):
    duplicates = [number for number in values if values.count(number) > 1]
    uniques = list(set(duplicates))
    return len(duplicates), uniques


def checkforcombos(symbols, values):
    combo = False
    if symbols.count(symbols[0]) == len(symbols):
        symbols.sort()
        if values[0] == values[-1] - 4 and values[-1] == 12:
            statistic["Royal Flush"] += 1
            combo = True
        elif values[0] == values[-1] - 4:
            statistic["Straight Flush"] += 1
            combo = True
        elif not combo:
            statistic["Flush"] += 1
    if checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) == 1:
        statistic["Four of a Kind"] += 1
        combo = True
    elif checkforpairs(values)[0] == 5 and len(checkforpairs(values)[1]) >= 2:
        statistic["Full House"] += 1
        combo = True
    elif checkforpairs(values)[0] == 3:
        statistic["Three of a Kind"] += 1
        combo = True
    elif checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) >= 2:
        statistic["Two pairs"] += 1
        combo = True
    elif checkforpairs(values)[0] == 2:
        statistic["Pair"] += 1
        combo = True
    values.sort()
    if values[0] == values[-1] - 4 and len(checkforpairs(values)[1]) == 0:
        statistic["Straight"] += 1
        combo = True
    if not combo:
        statistic["High Card"] += 1


if __name__ == "__main__":
    for x in range(rounds):
        yourCards = getcards(1, 52, 5)
        for i in yourCards:
            handvalues.append(getcardnumber(i))
            handysmbols.append(getsymbol(i))
            hand.append([convertvalue(getcardnumber(i)), getsymbol(i)])
        checkforcombos(handysmbols, handvalues)
        handvalues = []
        handysmbols = []
    print("Statistik:\n")
    print(statistic)
    print("\nAbweichungen der Wahrscheinlichkeiten in %\n")
    print(getdifference(statistic, probabilites))