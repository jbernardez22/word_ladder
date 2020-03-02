#!/bin/python3

from collections import deque 
import copy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    with open(dictionary_file) as f:
        xs = f.readlines()
    for i in range(len(xs)-1):
        xs[i] = xs[i][0:-1]
    if(start_word == end_word):
        return [start_word]

    stack = []
    stack.append(start_word)
    print("stack 1 = ", stack) 
    q = deque()
    q.appendleft(stack)
    count = 0
    dicCount = 0
    while (q):
        s = q.pop()
        print(s)
        xs_copy = copy.deepcopy(xs)
        for i in xs_copy: 
            if(_adjacent(i, s[-1])):           
                stack_copy = copy.deepcopy(s)
                stack_copy.append(i)
                if(i == end_word):
                    return stack_copy
                q.appendleft(stack_copy)
                xs.remove(i)
                 
                
def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if(len(word1)!=len(word2)):
        return False
    if(word1 == word2):
        return False
    count=0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if(count==1):
        return True
    else:
        return False

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if(ladder == []):
        return False 
    for i in range(len(ladder)-1):
        word1 = ladder[i]
        word2 = ladder[i+1]
        print(word1)
        print(word2)
        if(_adjacent(word1, word2)!=True):
            return False
    return True

