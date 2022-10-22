""" Shunting-yard Algorithm in Python
Part I: Takes a string using infix notation and outputs it in postfix.
Part II: Evaluates a postfix expression and outputs the result

Suppose the input string is balanced
Only integer could be handled correctly, but decimal is considered during calculation
Great video to explain the idea of this algorithm: https://youtu.be/HJOnJU77EUs
Great stackoverflow website to illustrate the unary minus issue:
https://stackoverflow.com/questions/16425571/unary-minus-in-shunting-yard-expression-parser
"""

import operator
import re
from typing import List


def shunting_yard_algorithm(line:str)-> float:
    return evaluate(infix_to_postfix(line))


def is_unary_minus(char: str, idx: int, line: List[str]) -> bool:
    """Cases to become an unary minus:
    1. Be the first character of the string
    2. Preceded by another operator
    3. Preceded by a left parenthesis
    """
    if char == '-':
        if idx == 0 or is_operator(line[idx - 1]) or is_left_paren(line[idx + 1]):
            return True
    return False


def is_left_paren(char:str) -> bool:
    return char in ['(', '[', '{']


def is_right_paren(char:str) -> bool:
    return char in [')', ']', '}']


def find_open_paren(right: str) -> bool:
    paren_pair = {')': '(', ']': '[', '}': '{'}
    return paren_pair[right]


def is_operator(char: str) -> bool:
    return char in ['+', '-', '*', '/', '^']


def is_greater_precedence(a:str, b:str) -> bool:
    pred = {'^': 4, 'u': 3,
            '*': 2, '/': 2,
            '+': 1, '-': 1,
            '(': 0, '[': 0, '{': 0,
            }
    return pred[a] >= pred[b]

# Part I


def infix_to_postfix(line: str) -> str:
    """
    Infix_to_Postfix rules:

    1.Use stack(LIFO) to store operators
    2.Operator with higher precedence should be put at the top of stack

    :param line:
    :return: str in prefix notation
    """

    stack = []
    output = []

    line = line.replace(" ", "")
    line = re.findall('[+\-/*//()^]|\d+|.|\d+', line)

    for idx, char in enumerate(line):

        if char.isdigit():
            output.append(char)

        elif is_left_paren(char):
            stack.append(char)

        elif is_right_paren(char):
            while stack[-1] != find_open_paren(char):
                output.append(stack.pop())
            stack.pop()

        elif is_unary_minus(char, idx, line):
            stack.append('u')

        elif is_operator(char):
            if not stack:
                stack.append(char)
            else:
                while len(stack) != 0 and is_greater_precedence(stack[-1], char):
                    output.append(stack.pop())
                stack.append(char)
        else:
            raise ValueError("Found invalid operator!")


    while stack:
        output.append(stack.pop())

    return output
# Part II


def operator_transfom(o: str) :
    oper = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow}

    return oper[o]


def evaluate(postfix:List[str]) -> float:

    stack = []

    for char in postfix:

        if char.isnumeric():
            stack.append(char)

        elif char == 'u':
            a = float(stack.pop())
            stack.append(operator.sub(0,a))

        elif is_operator(char):  # char is operator
            fn = operator_transfom(char)
            if len(stack) >= 2:
                a, b = float(stack.pop()), float(stack.pop())
            stack.append(fn(b, a))

    return stack[0]


if __name__ == '__main__':
    test_case = ["2  +  1",
                 "1+(2*3-1)-2",
                 "1*2-3/4+5*6-7*8+9/10",
                 "-4*-2/-(1-3)^2"]

    for i in range(len(test_case)):
        print("Test case ", i+1, ": ", test_case[i])
        print("Result: ", shunting_yard_algorithm(test_case[i]))
