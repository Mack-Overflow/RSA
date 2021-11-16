'''
P-problems are deterministic: There is a path to a solution. An algorithm that can be used to find the answer.
NP-problems are non-deterministic: There is no clear solution
'''

def times(n):
    print(f"linear: {n}")
    print(f"polynomial: {n**5}")
    print(f"exponential: {2**n}")

times(5)

'''A decision problem L is NP if:
L is in NP, where a solution can be verified quickly, but there is no known efficient solution
Every problem in NP is reducible to L in polynomial (not exponential) time
'''