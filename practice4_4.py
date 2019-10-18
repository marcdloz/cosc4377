# string expressions and operators
s1 = "hello"
s2 = "there"
combined = s1 + " " + s2
print(s1, s2)   # this also works as (s1, s2, sep=" ")
print(combined)
repeated = s1 * 3
print(repeated)

# ask for length of a string
print(len(combined))


# methods are functions inside an object
print(s1.upper())
print(s1.count("l"))    # counts how many of that letter is in the string.
print(s1.endswith("lo"))


# successfully convert a string to uppercase
s = combined.upper()
print(s)


# indexing individual characters of strings, can use negative indexing
print(s1[1], s1[-1])
print(s2[4], s2[-2])


# looping through a string, short way via Python
for c in combined:
    print(c, end="")    # use end="" to avoid println() new lines.
print()


rev_combined = ""
for i in range(len(combined)):
    rev_combined += combined[-1 - i]
print(rev_combined)


# String slicing aka substring
print(combined[0:4])
print(combined[3:8])
print(combined[2:])
print(combined[:2])


# converting characters to/from integer values
print(ord("a"))
print(chr(97))


# Rotation ciphering
def encode(word, amount):
    for letter in word:
        num = ord(letter) + amount  # shifts letter
        if num > ord('z'):          # wraps around if needed
            num -= 26
        elif num < ord('a'):
            num += 26
        print(chr(num), end="")
    print()


def main():
    encode("nintendo", 5)


main()


