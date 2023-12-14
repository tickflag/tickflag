#1
a, b = map(int, input().split())
n = min(a, b)
m = max(a, b)
print((n + m) * (m - n + 1) // 2)

#3
def check_string(s):
    stack = []
    opening_brackets = '({[<'
    closing_brackets = ')}]>'
    bracket_map = {')': '(', '}': '{', ']': '[', '>': '<'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return not stack

n = int(input())
out = ''

for i in range(n):
    inp = input()
    out += str(int(not check_string(inp)))

print(out)

knight_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
def knight(p1, p2):
    p1 = list(p1)
    p1[1] = int(p1[1])
    p2 = list(p2)
    p2[1] = int(p2[1])
    places = [p1]
    pos = get_possible_moves(places=places)
    for tries, _ in enumerate(range(5000), start=1):
        if p2 in pos: 
            return tries
        pos = get_possible_moves(places=pos)
    
    
#4
def get_possible_moves(places):

    possible_moves = []
    for place in places:
        x = place[0]
        y = place[1]
        for dx, dy in knight_moves:
            new_x = x + dx
            new_y = y + dy
            if 1 <= new_x <= n and 1 <= new_y <= n and [new_x, new_y] not in possible_moves:
                possible_moves.append([new_x, new_y])

    return possible_moves

n = int(input())
fr = map(int, input().split())
to = map(int, input().split())
print(knight(fr, to))

#5
from math import gcd
a1, a2, b1, b2 = map(int, input().split())
print(gcd(b1 - a1, b2 - a2) + 1)


letter = str(input())
s = str(input())

out = ''
coeff = ((ord(letter) - ord(s[0])))
if coeff < 0: coeff = 26 + coeff
coeff -= 1

if s:
    for i in s:
        if 
        if i.isalpha():
            if i.isupper():
                out += chr((ord(i) + coeff - 64) % 26 + 65)
            else:
                out += chr((ord(i) + coeff - 96) % 26 + 97)
        else:
            out += i

print(out)
