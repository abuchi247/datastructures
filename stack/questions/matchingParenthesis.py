# checks if an expression has a matching opening and closing parenthesis

from stack.StackArray import StackArray


def is_balance(expression):
    opening = "({["
    closing = ")}]"

    s = StackArray()
    print(expression)

    for x in range(len(expression)):
        element = str(expression[x])
        if element in opening:
            s.push(element)
        elif element in closing:
            if s.is_empty():
                return False
            top = s.pop()
            # get the matching opening parenthesis for the closing paren
            matching_open = opening[closing.index(element)]
            # check if it matching the element in the stack
            if top != matching_open:
                return False

    return s.is_empty()


if __name__ == "__main__":
    print(is_balance("((a+b)*(c-d))"))
    print(is_balance("((a+b)*(c-d)])"))
    print(is_balance("((a+b)*(c-d])"))
