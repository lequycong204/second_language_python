import math
f = lambda x: x**2 + 2*x + 1
# def solver(f, a, b, e = 0.000001):
#     midpoint = int((a + b) / 2) 
#     if abs(f(midpoint)) <= e:
#         print(midpoint)
#         return midpoint
    
#     if f(a) * f(midpoint) < 0:
#         solver(f, a, int((a + midpoint) / 2), e)
#     else:
#         solver(f, midpoint + 1, b, e)
    


def solvera(f, a, b, e=0.000001):
    c = a
    while ((b-a) >= 0.01):

        # Find middle point
        c = (a+b)/2
 
        # Check if middle point is root
        if (f(c) == 0.0):
            return c
 
        # Decide the side to repeat the steps
        if (f(c)*f(a) < 0):
            b = c
        else:
            a = c     
    return c
  
        
print(solvera(f, -2, 1))
