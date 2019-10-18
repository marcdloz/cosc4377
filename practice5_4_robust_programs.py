
# try to convert string to int and catch an exception
w = "hello"
try:
    n = int(w)
    print("I converted it successfully!", n)
except ValueError:
    # print("s is a non-integer value.")
    pass    # do nothing


def is_integer(s):
    try:
        s = int(s)
        return True
    except ValueError:
        return False


def get_int(prompt):
    line = input(prompt)
    while not is_integer(line):
        print("Not an integer; try again.")
        line = input(prompt)
    return int(line)


def main():
    age = get_int("How old are you? ")
    retire = 65 - age
    print("Retire in", retire, "years.")


main()