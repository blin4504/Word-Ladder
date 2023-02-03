# name: Brian Lin
# assignment: Homework 1-P

import sys

BEGIN_CHAR = 97
END_CHAR = 122

"""
The function used to find the word ladder from a start word to end word using BFS
Arguments:
    start: word to start with
    end: word to end with
    d: the dictionary containing all valid words
"""
def solve(start, end, d):
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    while(len(queue) > 0):
        for _ in range(len(queue)):
            curr_word = queue.pop(0)
            curr_word_chars = list(curr_word)
            for j in range(len(curr_word_chars)):
                original = curr_word_chars[j]
                if curr_word_chars[j] == end[j]:
                    continue
                for k in range(BEGIN_CHAR, END_CHAR + 1):
                    if chr(k) == original:
                        continue
                    curr_word_chars[j] = chr(k)
                    new_word = "".join(curr_word_chars)
                    if new_word == end:
                        d[end] = curr_word
                        return
                    if (new_word in d and new_word not in visited):
                        visited.add(new_word)
                        d[new_word] = curr_word
                        queue.append(new_word)
                curr_word_chars[j] = original

"""
The function used to backtrack to generate the shortest path from the start word 
to end word.
Arguments:
    start: word to start with
    end: word to end with
    d: the dictionary containing all valid words
"""
def getPath(start, end, d):
    sol = []
    sol.insert(0, end)
    curr = end
    while(curr != start):
        sol.insert(0, d[curr])
        curr = d[curr]
    return sol

"""
The main function responsible for getting the file, start, and end word to put into
the solver to find the shortest path possible.
"""
def main():
    d = {}
    file = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    with open(file, 'r') as f:
        for line in f:
            key = line.strip()
            d[key] = None
    solve(start, end, d)
    if (d[end] == None):
        print("no solution")
    else:
        path = getPath(start, end, d)
        for i in path:
            print(i)

if __name__ == "__main__":
    main()
