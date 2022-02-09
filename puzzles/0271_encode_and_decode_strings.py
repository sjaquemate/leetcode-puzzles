"""

62. CLOSED 659 · Encode and Decode Strings - LintCode

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement `encode` and `decode`

----------

Example1

    Input: ["lint","code","love","you"]
    Output: ["lint","code","love","you"]
    Explanation:
    One possible encode method is: "lint:;code:;love:;you"

Example2

    Input: ["we", "say", ":", "yes", "hoi:;hoi]
    Output: ["we", "say", ":", "yes", "hoi:;hoi"]
    Explanation:
    One possible encode method is: "we:;say:;hoi::;:;:;:hoi:;yes"

rocka((a))arock

SOLUTION ATTEMPT
We want to use any character as input. We know there is only one valid way of encoding if we use a certain separation character: “aaa”. Then first A can be an encoding for [“”, “”, “”, “”] or [a, “”, etc.] , this is why empty strings must be ignored in encoding imo. What if we place a ( ) around protected the clashing? well, what if:
sep_char = ‘:;’

encoded = word.replace(sep_char, ‘(‘+sep_char+’)’ for word in input]
Problem occurs here if we want to do: [“(“, “)”] → (:;)…

However we can encapsulate this in the same fashion again, knowing no empty strings are allowed:
encoded = ‘:'’.join([word.replace(sep_char, 3*sep_char) for word in input]

output = []
decode(encoded, cur_word = “”, output=[]):

    if len(encoded) == ..
        return

    if encoded.startswith(sep_char) and not encoded.startswith(sep_char*3):
        output.append(cur_word)
        encoded = encoded[len(sep_char):]
        cur_word = “”
    elif encoded.startswith(sep_char) and encoded.startswith(sep_char*3):


        cur_word += sep_char
    else:
        cur_word += encoded[0]
    decode(encoded[1:], cur_word)

…

rock:;, :;rock → rock:;:;:; :; :;:;:;rock NVM THIS DOES NOT WORK!

[rock, :;rock, rock]
rock:; :; rock  THIS COULD HAVE MULTIPLE INTERPRETATIONS. PROBLEM IS CLASHES WITH SEP CHAR
[rock, rock] → rockXrock
[rockX, rock] → rockXXrock which has two possible intepreations [rockX, rock] or [rock, Xrock]
One option: take two characters and end and start the word with that always…. What if we want one separator only?

WITH HINT: use length of string: this is trivially easy, i.e:

encoded = ‘’.join([ f’{len(word)}#{word}’ for word in input])
def decode(string):

    while len(string) > 0:
        sep_index = string.find(‘#’)
        length = int(string[:sep_index])
        start = sep_index + 1
        end = start + length
        word = string[start:end]
        output.append(word)
        string = string[end:]
"""