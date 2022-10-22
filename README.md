## Application of Stack and Queue Data Structure: Shunting Yard Algorithm

### Question definition
Please implement a function parsing mathematical expressions specified in infix notation.

Sample input 1 : "(2 + 3) * 2"  
Sample Output 1: 10

Sample input 2 : "-4*-2/-(1-3)^2"  
Sample output 2: -2

[comment]: <> (請用 Python 實作數學運算字 parser ，並計算其結果。例： a = "&#40;2+3&#41; * 2"，要得到 10。  )

### Some Thoughts
This algorithm can be classified into two parts：  
>1.Transform the math equation(infix notation) into postfix notation.   
>2.Calculate the correct answer.

Some constraints about the input strings for this code:
>1.The math equations should be balanced, which means that all the parentheses are paired.   
>2.Decimals are not allowed in the input string, but the math result could be float numbers.
>3.Operators available in this code includes +, -, *, / and exponents(^).

### Things to be Improved
> 1.Add function to check whether math equations are balanced, and return warnings if not.
> 2.Fix constraint 2.  
> 3.Using Unit Testing to make sure all the calculation and warnings working well.

[comment]: <> (關於第二點的初步想法是利用re.findall&#40;&#41;，正確分隔輸入的string)
### Reference  
[Algorithm Introduction](https://youtu.be/HJOnJU77EUs)  
[Unary Minus Issue](https://stackoverflow.com/questions/16425571/unary-minus-in-shunting-yard-expression-parser)

