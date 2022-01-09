# QUESTION 1: Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.


# test cases
# 1. Cards is even in length and the card we are looking for is at the end
# 2. Cards is even in length and the card we are looking for is at the first
# 3. Cards is old in length and the card we are looking for is at the end
# 4. Cards is old in length and the card we are looking for is at the first
# 5. Card is not in the list
# 6. There are no cards in the list
# 7. There are more than 1 card with found but we must get the first occurrence
# 8. Card is found in the middle
# 9. Cards only contain one element

tests = [
    {
        "input": {
            "cards": [6,5,4,3,2,1],
            "query": 1
        },
        "output": 5
    },
    {
        "input": {
            "cards": [6,5,4,3,2,1],
            "query": 6
        },
        "output": 0
    },
    {
        "input": {
            "cards": [5,4,3,2,1],
            "query": 1
        },
        "output": 4
    },
    {
        "input": {
            "cards": [5,4,3,2,1],
            "query": 5
        },
        "output": 0
    },
    {
        "input": {
            "cards": [5,4,3,2,1],
            "query": 10
        },
        "output": -1
    },
    {
        "input": {
            "cards": [],
            "query": 5
        },
        "output": -1
    },
    {
        "input": {
            "cards": [5,4,4,4,4,3,2,1],
            "query": 4
        },
        "output": 1
    },
    {
        "input": {
            "cards": [5,4,3,2,1],
            "query": 3
        },
        "output": 2
    },
    {
        "input": {
            "cards": [5,4,3,2,1,0],
            "query": 2
        },
        "output": 3
    },
    {
        "input": {
            "cards": [5],
            "query": 5
        },
        "output": 0
    },
    {
        "input": {
            "cards": [5],
            "query": 4
        },
        "output": -1
    }
]


def find_card_position(cards, start, end, query):
    """
    Using a binary search algorithm, locate the position of the query in the cards array
    """
    while start <= end:
        mid = (start + end) //  2
        if cards[mid] == query:
            return mid
        elif cards[mid] > query:
            start = mid + 1
        else:
            end = mid - 1
    return -1 # not found


def locate_card(cards, query):
    """
    Locate the position of the card in the cards list
    :param: cards: cards list
    "param: query: card to be found
    :return: position of the card, -1 if not found
    """
    card_position = find_card_position(cards, 0, len(cards) - 1, query)

    # if there are multiple occurance of the card, we want to locate the first one
    while card_position > 0 and cards[card_position - 1] == query:
        card_position = find_card_position(cards, 0, card_position-1, query)
    return card_position


def evaluate(num1, num2):
    result = "PASS" if num1 == num2 else "FAIL"
    print(result)


if __name__ == "__main__":
    for test in tests:
        evaluate(locate_card(**test['input']), test['output'])