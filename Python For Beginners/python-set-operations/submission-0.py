from typing import List

def count_unique_words(words: List[str]) -> int:
    unique_words = set(words) # remove duplicates

    # now we want to count the number of unique words
    # i converterd the list to a set bc i want to get rid of duplicates
    # now im wondering the next step
    # im thinking of just converting it right back to a list

    uw = list(unique_words)

    return len(unique_words)


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
