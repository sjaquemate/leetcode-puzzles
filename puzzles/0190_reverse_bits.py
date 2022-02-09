"""


40. CLOSED  Reverse Bits - LeetCode

Reverse bits of a given 32 bits unsigned integer.
Note:

- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer `-3` and the output represents the signed integer `-1073741825`.


Example 1:

    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

    Input: n = 11111111111111111111111111111101
    Output:   3221225471 (10111111111111111111111111111111)
    Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.


Constraints:

- The input must be a binary string of length `32`


Follow up: If this function is called many times, how would you optimize it?

I have no clue how to go about this…

SOLVED WITH HINT, TESTED IN PYTHON:


    def reverse_bits(n: int):
        num = 0  # 32 zeros
        for i in range(32):
            print(i, to_binary(n >> i))
            print(i, bool((n >> i) & 1), to_binary((n >> i) & 1))
            # shift bits to 1 to right and check if last bit is zero or one
            # in other words, check if (last-i)'th bit is 1
            if (n >> i) & 1:
                # get the last bit
                num += ((n >> i) & 1) << (31 - i) # put this bit 31-i to the left (reversing the bits)
        return num


    def to_int(binary):
        return int(binary, 2)


    def to_binary(integer):
        return format(integer, '032b')


    input = "00000010100101000001111010011100"
    print(input)
    output = to_binary(reverse_bits(to_int(input)))
    print(output)

"""