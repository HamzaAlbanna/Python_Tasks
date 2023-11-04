s = input() # read input
# s = "1 4";
f = input()
# f = "x^3 + x^2 + x + 1"
(x,y) = s.split() # args
x=int(x)
y=int(y)
# print (x, y)
z=eval(f)
if (z == y):
    print ("True")
else:
    print ("False")