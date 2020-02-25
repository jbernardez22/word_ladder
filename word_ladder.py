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
    if(start_word == end_word):
        return [start_word]

    stack = []
    stack.append(start_word)
    q = deque()
    q.append(stack)

    while(q!=[]):
        newq = q.pop()
        for i in xs:
            if(_adjacent(i, newq[-1])):
                stack_copy = copy.deepcopy(newq)
                stack_copy.append(i)
                if(i == end_word):
                    for j in range(1, len(stack_copy) -2):
                        if _adjacent(edit[y-1], edit[y+1]):
                             stack_copy.pop(y)
                    return stack_copy
                q.appendleft(stack_copy)
                xs.remove(xs[i])
                

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    count=0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
        if(count>1):
            return False
    return True

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
print("hello")

#print(verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']))
#print(_adjacent('phone', 'phony'))
#print(_adjacent('stone', 'money'))
