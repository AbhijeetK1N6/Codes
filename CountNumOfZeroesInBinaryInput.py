"""
Sample Input:-
7
1 1 0 0 0 1 0

Sample Output:-
4
"""

def count_zeros(number):
    return str(number).count('0')
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
n=int(input())
num=list(map(str,input().split()))
ak=listToString(num)
print(count_zeros(ak))
