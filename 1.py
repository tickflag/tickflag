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
coeff = (ord(s[0]) - ord(letter))

if s:
    for i in s:
        if 'a' <= i and i <= 'z':
            out += chr((ord(i) - coeff - ord('a') + 26) % 26 + ord('a'))
        elif 'A' <= i and i <= 'Z':
            out += chr((ord(i) - coeff - ord('A') + 26) % 26 + ord('A'))
        else:
            out += i

print(out)



import java.util.Scanner;

public class StringDecryption {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter letter: ");
        String letter = scanner.nextLine();

        System.out.print("Enter s: ");
        String s = scanner.nextLine();

        String out = "";
        int coeff = (int) (s.charAt(0) - letter.charAt(0));

        if (!s.isEmpty()) {
            for (int i = 0; i < s.length(); i++) {
                char currentChar = s.charAt(i);
                if ('a' <= currentChar && currentChar <= 'z') {
                    out += (char) ((currentChar - coeff - 'a' + 26) % 26 + 'a');
                } else if ('A' <= currentChar && currentChar <= 'Z') {
                    out += (char) ((currentChar - coeff - 'A' + 26) % 26 + 'A');
                } else {
                    out += currentChar;
                }
            }
        }

        System.out.println(out);
    }
}


type

  cell = record

  x, y: integer;

  end;

var

  queue: array[1..700] of cell;

  a: array[-1..27, -1..27] of integer;

  x1, y1, x2, y2, i, j, t, h, n: integer;

  p, p1: cell;

procedure push(p: cell);

begin

  queue[t] := p;

  inc(t);

end;

function pop(): cell;

begin

  pop := queue[h];

  inc(h);

end;

function isEmpty(): boolean;

begin

  isEmpty := false;

  if h = t then isEmpty := true;

end;

begin

  h := 1;

  t := 1;

  read(n, x1, y1, x2, y2);

  for i := 1 to n do

  for j := 1 to n do

  a[i, j] := -1;

  a[x1, y1] := 0;

  p. x := x1;

  p. y := y1;

  push(p);

  while not isEmpty() do

  begin

  p := pop();

  for i := -2 to 2 do

  for j := -2 to 2 do

  if (i * i + j * j = 5) and (a[p. x + i, p. y + j] = -1) then begin

  p1.x := p. x + i;

  p1.y := p. y + j;

  push(p1);

  a[p1.x, p1.y] := a[p. x, p. y] + 1;

  end;

  end;

  write(a[x2, y2]);

end.


import java.util.Scanner;

class Cell {
    int x, y;

    Cell(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class MazeSolver {
    static Cell[] queue;
    static int[][] a;
    static int x1, y1, x2, y2, i, j, t, h, n;

    static void push(Cell p) {
        queue[t] = p;
        t++;
    }

    static Cell pop() {
        Cell popped = queue[h];
        h++;
        return popped;
    }

    static boolean isEmpty() {
        return h == t;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        h = 1;
        t = 1;

        n = scanner.nextInt();
        x1 = scanner.nextInt();
        y1 = scanner.nextInt();
        x2 = scanner.nextInt();
        y2 = scanner.nextInt();

        queue = new Cell[700];
        a = new int[30][30];

        for (i = 1; i <= n; i++)
            for (j = 1; j <= n; j++)
                a[i][j] = -1;

        a[x1][y1] = 0;

        Cell p = new Cell(x1, y1);
        push(p);

        while (!isEmpty()) {
            p = pop();

            for (i = -2; i <= 2; i++)
                for (j = -2; j <= 2; j++)
                    if (i * i + j * j == 5 && a[p.x + i][p.y + j] == -1) {
                        Cell p1 = new Cell(p.x + i, p.y + j);
                        push(p1);
                        a[p1.x][p1.y] = a[p.x][p.y] + 1;
                    }
        }

        System.out.println(a[x2][y2]);
    }
}



