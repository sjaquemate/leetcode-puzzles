"""

69. CLOSED (1) Sum of Two Integers - LeetCode


Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

Example 1:

    Input: a = 1, b = 2
    Output: 3

Example 2:

    Input: a = 2, b = 3
    Output: 5


Constraints:

- `-1000 <= a, b <= 1000`

….
a+b = a*b(1/b+1/a) =a + b
know that a%b remainder if a>b, and a//b the how amany times:
a//b * b = a - a%b, a=5, b=2
a//b / b = b - a%b, 10. 7
1 / 7 =

2 * 2 = 5 - 1
b//a * a = b - b%a
0 = 2 -2

so sum(a, b) = a*b(sum(1/a, 1/b))

WITH HINT

    public int getSum(int a, int b) {

       while(b!=0){
           int c = a&b;
           a=a^b;
           b=c<<1;
       }

       return a;
    }

let’s try to understand:
a = 1, b = 2, a = 01, b= 10

1. c = 00, a = 11, b=00, note ^ is xor
2. b = 0 return a=11=3

a^b different bits of a and b
a&b same bits of a and b
<< 1 is carry the one, thus (a&b) << 1 is powerful

a becomes whatever we can add comfortably
b becomes whatever we need to carry
and we continue this logic

I UNDERSTAND!

SO IN PYTHON:

def add(a, b):


    result = a^b
    carry = (a&b)<<1
    while carry != 0:  # until there is nothing to carry
        next_carry = (result &carry) <<1  # what we have to carry next
        result = result | carry  # whatever we needed to carry
        carry = next_carry
    return result

"""