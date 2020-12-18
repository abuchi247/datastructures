# Given n non-negative integers a1, a2, ..., an , where each represents a
#  point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the 
# line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
# such that the container contains the most water.

def calculate_area(length, width):
    return length * width

def max_area(arr):
    """
    Returns pair of indexs container that holds the most water
    """
    maximum_area = 0
    result = {}

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            length = min(arr[i], arr[j])
            width = j - i
            new_area = calculate_area(length, width)
            if maximum_area <= new_area:
                maximum_area = new_area
                result = {maximum_area: [i, j]}
    return result[maximum_area] if maximum_area != 0 else None

if __name__ == "__main__":
    tests = int(input("Number of test cases: "))

    while tests > 0:
        arr = list(map(int, input("Enter an array to get the container with most water: ").split()))

        print(f"Array {arr} container {max_area(arr)} holds the most water")
        tests -= 1