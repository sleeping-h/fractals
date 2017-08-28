import turtle
t = turtle.Turtle()
wn = turtle.Screen()

walk = lambda a, n: ''.join(x if x != a else walk(x, n-1) \
                              if n else 'F' for x in a)

## first curve

a = "a - a + + a - a".split() # Koch
a[0] = a[2] = a[5] = a[7] = a

s = walk(a, 3)
t.up()
t.back(200)
t.down()
t.speed(42)
cmd = { 'F': lambda: t.forward(4)
      , '+': lambda: t.right(60)
      , '-': lambda: t.left(60)
      }
for c in s:
    cmd[c]()

## second curve

a = "a - a + a + a a - a - a + a".split() # Minkovsky
a[0] = a[2] = a[4] = a[6] = a[7] = a[9] = a[11] = a[13] = a

s = walk(a, 2)
t.up()
t.forward(30)
t.down()
cmd = { 'F': lambda: t.forward(3)
      , '+': lambda: t.right(90)
      , '-': lambda: t.left(90)
      }
for c in s:
    cmd[c]()

wn.exitonclick()
