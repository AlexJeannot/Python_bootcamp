from vector import Vector

vec_1 = Vector([1.0, 2.0, 3.0, 4.0])
vec_2 = Vector(7)
vec_3 = Vector((6.0, 13.0))

print("--- CHECK ADD ---\n")
print("vec_1    values = {0}      size = {1}\n".format(vec_1.values, vec_1.size))
print("vec_2    values = {0}      size = {1}\n".format(vec_2.values, vec_2.size))
print("vec_3    values = {0}      size = {1}\n".format(vec_3.values, vec_3.size))

print("--- CHECK CREATION EXEMPLE ---\n")
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 + 5
v3 = v1 * 5
v4 = v1 - 5
v5 = v1 / 5

print("v1 = {}".format(v1))
print("v2 = {}".format(v2))
print("v3 = {}".format(v3))
print("v4 = {}".format(v4))
print("v5 = {}".format(v5))
