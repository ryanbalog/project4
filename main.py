'''
Project 4
CS2420
Ryan Balog
'''

from stack import Stack

SYMBOLS = ["*", "/", "+", "-"]


def in2post(line):
    '''converts infix expressions to postfix expressions'''
    operators = Stack()
    postfix = []

    if not isinstance(line, str):
        raise ValueError("Not a string expression")

    for token in line:
        if token == " ":
            pass
        elif token == "(":
            operators.push(token)
        elif token == ")":
            while operators.size() > 0 and operators.peek() != "(":
                postfix.append(operators.pop())
            if operators.size() <= 0:
                raise SyntaxError("Invalid Expression")
            operators.pop()

        elif token in SYMBOLS:
            if operators.size() == 0:
                operators.push(token)
            else:
                if (token == "+" or token == "-"):
                    while operators.size() > 0 and operators.peek() != "(":
                        x = operators.pop()
                        postfix.append(x)
                    operators.push(token)
                elif (token == "*" or token == "/") and (operators.peek() == "*" or operators.peek() == "/"):
                    while operators.size() > 0 and (operators.peek() == "*" or operators.peek() == "/"):
                        x = operators.pop()
                        postfix.append(x)
                    operators.push(token)
                else:
                    operators.push(token)
        else:
            postfix.append(token)
    while operators.size() > 0:
        postfix.append(operators.pop())

    return str(" ".join(postfix))


def eval_postfix(expression):
    '''evaluates a post fix expression'''
    evaluator = Stack()

    if not isinstance(expression, str):
        raise ValueError("Not a postfix string")

    for token in expression:
        if token == " ":
            pass
        elif token not in SYMBOLS:
            evaluator.push(token)
        else:
            if evaluator.size() >= 2:
                x = float(evaluator.pop())
                y = float(evaluator.pop())
                if token == "*":
                    evaluator.push(x * y)
                elif token == "/":
                    evaluator.push(y / x)
                elif token == "+":
                    evaluator.push(x + y)
                else:
                    evaluator.push(y - x)

            else:
                raise SyntaxError("Not valid postfix")

    return float(evaluator.pop())


def main():
    '''drive ingestion from file, data manipulation, and output'''
    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            print("infix: " + line)
            converted = in2post(line)
            print("postfix: " + converted.strip(" "))
            print("answer: " + str(eval_postfix(converted)) + "\n")


if __name__ == "__main__":
    main()
