import itertools
from time import time


# decorator idiom
def timeit(f):
    def wrap(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        print(f'Function: {f.__name__}, exec time={time()-start}')
    return wrap


@timeit
def how_long_to_read_dictionary():
    # file reading idiom, with is context manager
    with open('words_alpha.txt') as f:
        for line in f:
            pass


@timeit
def search_words(in_str, word_length):
    may_be_words = set()
    for t in itertools.permutations(in_str, word_length):
        may_be_words.add(''.join(t))
    print(len(may_be_words), may_be_words)

    with open('words_alpha.txt') as f:
        count = 0
        for word in f.read().split():
            if len(word) != word_length:
                continue
            if set([word]).issubset(may_be_words):
                print(f'Found: {word}')
                count += 1

    print(f'Found {count} words')

# idiom: it allows to impot this file without
#        executing what is below, good for testing
#        and playing from python prompt...
if __name__ == '__main__':
    how_long_to_read_dictionary()
    search_words(
        #input('your chars, pls? '),
        #int(input('word length, pls? ')),
        "pterodaptylpterodaptyl", 7
    )
