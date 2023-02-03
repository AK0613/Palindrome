# Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case sensitivity

# "aabaa" True
# "aabbaa" True
# "abc" False
# "a" True
# "" True

def two_pointers_outside(input):
    length = len(input)
    a = 0
    b = length - 1
    equal = False
    if 0 <= length <= 1:
        equal = True

    if length > 2:
        if length % 2 == 0:
            while a < b:
                if input[a] == input[b]:
                    a += 1
                    b -= 1
                    equal = True
                else:
                    equal = False
                    break
        else:
            while a <= b:
                if input[a] == input[b]:
                    a += 1
                    b -= 1
                    equal = True
                else:
                    equal = False
                    break
    return equal


def two_pointers_middle(input):
    length = len(input)
    equal = False
    a = b = 0

    if 0 <= length <= 1:
        equal = True
        return equal
    if length > 2:
        if length % 2 == 0:
            a = (length // 2) - 1
            b = length // 2
            while a >= 0 and b < length:
                if input[a] == input[b]:
                    equal = True
                else:
                    equal = False
                    break
                a -= 1
                b += 1
        else:
            a = b = length // 2
            while a >= 0 and b < length:
                if input[a] == input[b]:
                    equal = True
                else:
                    equal = False
                    break
                a -= 1
                b += 1
    return equal


# Compare against reverse approach
def reverse_approach(input):
    length = len(input)
    equal = False

    if 0 <= length <= 1:
        equal = True
        return equal
    if length > 2:
        if length % 2 == 0:
            middle = length // 2
            a = input[0:middle:]
            b = ''.join(reversed(input[middle::]))
            if a == b:
                equal = True

        else:
            middle = (length - 1) // 2
            a = input[0:middle:]
            # List splicing leaves the middle value in limbo since it never reaches middle in the previous line and +1 moves it past the middle
            b = ''.join(reversed(input[middle + 1::]))
            if a == b:
                equal = True
    return equal


# Next problem: If a string is almost a palindrome by being off by a single digit/character
# raceacar -> true either by removing the e or the a.
# abccdba -> True by removing the extra c
# abcdefdba -> False cause removing a single char is not enough to palindrome
# "" and "a" are true
# "ab" is also true since removing a letter yields a palindrome


def almost_palindrome(input):
    length = len(input)
    equal = False
    a = 0
    b = length - 1
    if 0 <= length <= 2:
        return True
    else:
        while a <= b:
            if input[a] == input[b]:
                a += 1
                b -= 1
                equal = True
            else:
                equal = False
                str_a = input[0:b:] + input[b + 1::]
                str_b = input[0:a:] + input[a + 1::]
                print(str_a, str_b)
                if reverse_approach(str_a) or reverse_approach(str_b):
                    equal = True
                break
    return equal


str = "abccdba"
input = ''.join(item for item in str if item.isalnum()).lower()
print(almost_palindrome(input))
# print(reverse_approach(input))
# print(two_pointers_outside(input))
# print(two_pointers_middle(input))
