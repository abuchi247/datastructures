# Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out
# face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over
# as few cards as possible. Write a function to help Bob locate the card.

tests = [
    {   # empty cards
        "cards": [],
        "target": 10,
        "position": -1
    },
    {   # cards list with only 1 card
        "cards": [10],
        "target": 10,
        "position": 0
    },
    {   # cards list but card not found
        "cards": [8,7,6,5,4,3,2,1],
        "target": 10,
        "position": -1
    },
    {   # cards list with card found
        "cards": [8,7,6,5,4,3,2,1],
        "target": 6,
        "position": 2
    },
    {   # cards list with card found
        "cards": [8,7,6,5,4,3,2,1],
        "target": 8,
        "position": 0
    },
    {   # cards list with card found
        "cards": [8,7,6,5,4,3,2,1],
        "target": 1,
        "position": 7
    },
    {   # cards list with card found
        "cards": [8,8,8,6,5,4,3,2,1],
        "target": 0,
        "position": 8
    },
    {   # cards list with card found
        "cards": [8,8,8,6,5,4,3,2,2,2,1],
        "target": 2,
        "position": 7
    }
]


def evaluate_test(tests, func):
    for index, test in enumerate(tests):
        print(f"Executing test: {index}: {test['cards']}, finding: {test['target']}")
        result =  func(test['cards'], test['target'])
        if result != test['position']:
            print(f"Test {index} failed. result expected: {test['position']} but got {result}")


def locate_card(cards, target):
    start = 0
    end = len(cards) - 1

    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == target:
            return mid
        elif cards[mid] < target:
            end = mid-1
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    evaluate_test(tests, locate_card)
    # print(locate_card(tests[3]['cards'], tests[3]['target']))