from math import pi, sin

f = lambda x: x*sin(x)  
a = 0                   
b = pi/2               

n = 6                   
h = (b - a) / n         


S = (f(a) + f(b))
for i in range(1, n, 3):                        
    S += 3 *(f(a + i*h) + f(a + (i+1)*h))
for i in range(3, n, 3):                     
    S += 2 * f(a + i*h)
I = 3/8 * h * S

print("Integral of the equation, I = %f" % I)
