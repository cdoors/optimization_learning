"""
Since brute force is inefficient and the previous n-queens problem will search for eternity for solution,
this backtracking function solves the issue. It takes action, checks if the permutation can be extended and then backtracks
if it realizes that it is a dead end. This method is more compute efficient. The same n-queens problem is solved.

It can compute n = 20 in a matter of seconds, something impossible with the brute force method
"""

# def generate_permutations(perm, n):
#     if len(perm) == n:
#         print(perm)
#         return
    
#     for k in range(n):
#         if k not in perm:
#             perm.append(k)
#             generate_permutations(perm, n)
#             perm.pop()

def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)
            
            perm.pop()

extend(perm = [], n = 20)


