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

import time

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


def find_card_position_optimal(cards, start, end, query):
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


def locate_card_linear(cards, query):
    for index in range(len(cards)):
        if cards[index] == query:
            return index
    return -1


def locate_card_binary(cards, query):
    """
    Locate the position of the card in the cards list
    :param: cards: cards list
    "param: query: card to be found
    :return: position of the card, -1 if not found
    """
    card_position = find_card_position_optimal(cards, 0, len(cards) - 1, query)

    # if there are multiple occurance of the card, we want to locate the first one
    while card_position > 0 and cards[card_position - 1] == query:
        card_position = find_card_position_optimal(cards, 0, card_position-1, query)
    return card_position


def evaluate_test_case(func, arguments):
    """
    Evaluates test case using the function passed in
    """
    if not isinstance(arguments, dict):
        raise Exception("Argument must be a dictionary")

    if 'input' not in arguments.keys():
        raise Exception("Argument must have an input key")

    if 'output' not in arguments.keys():
        raise Exception("Argument must have an output key")

    for k in ['cards', 'query']:
        if k not in arguments.get('input').keys():
            raise Exception(f"input must have {k}")

    print("Input:")
    print(arguments.get('input'))

    print('Expected Output')
    print(arguments.get('output'))

    start = time.time()
    result = func(**arguments.get('input'))
    end = time.time()

    print('Actual Output')
    print(result)

    print("Execution Time:")
    print(f"{end-start:.4f} ms")

    print("Test Result:")
    message = "PASSED" if result == arguments['output'] else "FAILED"

if __name__ == "__main__":
    for test in tests:
        evaluate_test_case(locate_card_linear, test)
        evaluate_test_case(locate_card_binary, test)