

# computes the average(mean) of the numbers in the given list
def average(numbers):
    sum = 0
    count = 0
    for n in numbers:
        sum += n
        count += 1
    return int(sum / count)


def squares(n):
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result


# returns a new list of just unique words from the passing list
def unique_words(words):
    unique_word_list = []
    for word in words:
        if word not in unique_word_list:
            unique_word_list.append(word)
    return unique_word_list


def last_index(list, target):
    for i in range(len(list) - 1, -1, -1):  # remember, start, stop, step
        if list[i] == target:
            return i
        raise ValueError(str(target) + " is not in list")


def count_between(numbers, min, max):
    count = 0
    for number in numbers:
        if min <= number <= max:
            count += 1
    return count


# index only returns first occurence
def replace(list, target, replacement):
    if target in list:
        index = list.index(target)
        list[index] = replacement
    return list


def replace_all(list, target, replacement):
    for i in range(len(list)):
        if list[i] == target:
            list[i] = replacement
    return list


def reverse(list):
    for i in range(len(list) // 2):
        j = len(list) - i - 1
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
    return list


def rotate_left(data):
    first = data[0]
    for i in range(len(data) - 1):
        data[i] = data[i + 1]
    data[-1] = first
    return data


def rotate_right(data):
    last = data[-1]
    for i in range(len(data) - 1, 0, -1):
        data[i] = data[i - 1]
    data[0] = last
    return data


def main():
    numbers = [1, 7, 3, 9, 7]
    avg = average(numbers)
    print("average of", numbers, "is", avg)
    nums = squares(7)
    print("result is", nums)

    print(10 in numbers)
    print(7 in numbers)

    words = ["hello", "there", "hello", "hi"]
    words = unique_words(words)
    print(words)

    print(numbers.index(7))
    print(numbers.index(3, 1, 3))   # search between index 1 and 3

    print(last_index(numbers, 7))
    """print(last_index(numbers, 5))"""
    print(count_between(numbers, 2, 8))

    words = ["to", "be", "or", "not", "to", "be"]
    print(replace(words, "be", "beep"))
    print(replace_all(words, "be", "beep"))

    # demonstrates reversed function
    rev = list(reversed(numbers))   # need to cast as list since reversed returns as an object, not a list
    print(rev)
    print(reverse(words))
    print(rotate_left(numbers))
    print(rotate_right(numbers))

    print(numbers[1:] + numbers[:1])
    print(numbers[-1:] + numbers[:-1])

    data = [5, 4, 3, 2, 1]
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                print("(", data[i], ",", data[j], ")", sep="")

    # create list of the squares of 1-5 using list comprehension
    data2 = [n * n for n in data]
    print(data2)


main()
