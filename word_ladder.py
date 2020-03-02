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
    print("stack 1 = ", stack) # check
    q = deque() # check
    q.appendleft(stack)
    count = 0
    dicCount = 0
   # while(q!=[]): # maybe different method
    while (q):
        s = q.pop()
       # if (count > 5):#debug
          #  return 0#debug
        print(s)
        xs_copy = copy.deepcopy(xs)
        for i in xs_copy:
            dicCount = dicCount + 1
            if(_adjacent(i, s[-1])):  #confusedhere
                count  = count + 1
                stack_copy = copy.deepcopy(s)
                stack_copy.append(i)
                if(i == end_word): #code not getting here, add print statements inside of while loop and for loop
                    
                    print(i, "end word")
                   # print(q)
                    print("stack:", stack)
                   # stack.append(i)
                    print("count" +str(count))
                    print("diccount"+str(dicCount))
                    print("stack after append", stack)
                    return stack_copy
               # stack_copy = copy.deepcopy(s)
               # print("stack copy is", stack_copy, "i is", i)
               # print(i)
              #  stack_copy.append(i)
                q.appendleft(stack_copy)
              #  print(stack_copy)
                xs.remove(i)
    print("exited loop")
               
                
                 
                
def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
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

#print(verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']))
#print(_adjacent('phone', 'phony')
#print(_adjacent('bonny', 'money'))
word_ladder('stone','money')
