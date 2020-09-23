

def dot(a,b):
    x1,y1,z1 = a ## deconstructing the tuple
    x2,y2,z2 = b
    return x1*x2 + y1*y2 + z1*z2

#tuples
vec = 2,4,1
vec2 = 1,1,1

print(dot(vec,vec2))