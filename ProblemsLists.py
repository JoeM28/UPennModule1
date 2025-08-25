def concatenate(strings):
    """
    Concatenates the given list of strings into a single string.
    Returns the single string.
    If the given list is empty, returns an empty string.

    For example:
    - If we call concatenate(["a","b","c"]), we'll get "abc" in return
    - If we call concatenate([]), we'll get "" in return
    """
    return "".join(strings)


print(concatenate(["a","b","c"]))  # "abc"
print(concatenate([]))             # ""



def all_but_last(seq):
    """
    Returns a new list containing all but the last element in the given list.
    If the list is empty, returns None.
    """
    if not seq:       # checks if list is empty
        return None
    return seq[:-1]   # slicing removes the last element

print(all_but_last([1,2,3,4,5]))        # [1,2,3,4]
print(all_but_last(["a","d",1,3,4,None])) # ["a","d",1,3,4]
print(all_but_last([]))                 # None


def remove_duplicates(lst):
    """
    Returns the given list without duplicates.
    The order of the returned list doesn't matter.
    """
    return list(set(lst))


print(remove_duplicates([1,2,1,3,4]))  # [1, 2, 3, 4] (order may vary)
print(remove_duplicates([]))           # []


#️ Note: The order is not preserved (since sets are unordered).
# If you need to preserve the original order, you can do it like this:

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def reverse_word(word):
    """
    Reverses the order of the characters in the given word.
    """
    return word[::-1]


print(reverse_word("abcde"))    # "edcba"
print(reverse_word("a b c d e"))  # "e d c b a"
print(reverse_word("a  b"))     # "b  a"
print(reverse_word(""))         # ""

print("Python"[::-1])   # "nohtyP"
print([1,2,3,4][::-1]) # [4, 3, 2, 1]  (works on lists too!)


def divisors(n):
    """
    Returns a list with all divisors of the given number n.
    """
    return [i for i in range(1, n+1) if n % i == 0]


print(divisors(10))  # [1, 2, 5, 10]
print(divisors(1))   # [1]
print(divisors(12))  # [1, 2, 3, 4, 6, 12]


def divisors(n):
    """
    Returns a list with all divisors of the given number n.
    As a reminder, a divisor is a number that evenly divides another number.
    The returned list should include 1 and the given number n itself.
    The order of the returned list doesn't matter.

    For example:
    - If we call divisors(10), we'll get [1,2,5,10] in return
    - If we call divisors(1), we'll get [1] in return
    """
    # your code here
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result


print(divisors(10))  # [1, 2, 5, 10]
print(divisors(1))   # [1]
print(divisors(12))  # [1, 2, 3, 4, 6, 12]


def capitalize_or_join_words(sentence):
    """
    If the given sentence starts with *, capitalizes the first and last letters of each word,
    and returns the sentence without *.
    Else, joins all the words in the given sentence with commas.
    """
    if sentence.startswith("*"):
        words = sentence[1:].split()  # remove * and split into words
        result_words = []
        for w in words:
            if len(w) == 1:
                result_words.append(w.upper())
            else:
                result_words.append(w[0].upper() + w[1:-1] + w[-1].upper())
        return " ".join(result_words)
    else:
        words = sentence.split()  # handles multiple spaces automatically
        return ",".join(words)

def move_zero(lst):
    """
    Moves all non-zero numbers to the beginning of the list and
    moves all zeros to the end. Modifies the list in place.
    """
    non_zeros = [x for x in lst if x != 0]   # collect non-zero numbers
    zeros = [0] * (len(lst) - len(non_zeros))  # fill the rest with zeros
    lst[:] = non_zeros + zeros   # replace contents of lst in place

nums = [0,1,0,2,0,3,0,4]
move_zero(nums)
print(nums)   # [1, 2, 3, 4, 0, 0, 0, 0]

nums = [0,1,2,0,1]
move_zero(nums)
print(nums)   # [1, 2, 1, 0, 0]

nums = [1,2,3,4,5,6,7,8]
move_zero(nums)
print(nums)   # [1,2,3,4,5,6,7,8]

nums = []
move_zero(nums)
print(nums)   # []



def main():
    """
    Calls all the functions above to see whether they've been implemented correctly.
    """

    # test concatenate
    print("test concatenate")
    word = concatenate(["b", "e", "a", "t", "l", "e", "s"])
    print(word == "beatles")
    print("=" * 50)

    # test all_but_last
    print("test all_but_last")
    seq = all_but_last(["john", "paul", "george", "ringo", "tommy"])
    print(seq == ["john", "paul", "george", "ringo"])
    print("=" * 50)

    # test remove_duplicates
    print("test remove_duplicates")
    res = remove_duplicates([1, 3, 4, 2, 1])
    print(res == [1, 3, 4, 2])
    print("=" * 50)

    # test reverse_word
    print("test reverse_word")
    res = reverse_word("alphabet")
    print(res == "tebahpla")
    print("=" * 50)

    # test divisors
    print("test divisors")
    res = divisors(120)
    print(set(res) == set([1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]))
    print("=" * 50)

    # test capitalize_or_join_words
    print("test capitalize_or_join_words")
    print("Result for String Start With *: ")
    # Should return "I LovE CodinG AnD I'M HavinG FuN"
    res = capitalize_or_join_words("*i love coding and i'm having fun")
    print(res == "I LovE CodinG AnD I'M HavinG FuN")

    print("Result for Other String: ")
    # Should print "I,love,coding,and,I'm,having,fun"
    res = capitalize_or_join_words("I love coding and I'm having fun")
    print(res == "I,love,coding,and,I'm,having,fun")
    print("=" * 50)

    # test move_zero
    print("test move_zero")
    lst = [0, 1, 0, 2, 0, 3, 4, 0]
    print("Before move,the list looks like\n", lst)
    move_zero(lst)
    print("After move,the list looks like\n", lst)
    print("=" * 50)

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()



print(capitalize_or_join_words("*i love python"))   # "I LovE PythoN"
print(capitalize_or_join_words("i love python"))    # "i,love,python"
print(capitalize_or_join_words("i love    python  ")) # "i,love,python"
print(capitalize_or_join_words("*a b c"))           # "A B C"