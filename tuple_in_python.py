tuple_a = (1,2,3,4, "Amrit", True, 9.955)
tuple_b= (44, 72, "Gunjan",False, 1.01)
tuple_c = ("abc", "def", "ghi")
print(tuple_a, tuple_b, tuple_c)
tuple_d = ((tuple_a), (tuple_b), (tuple_c))
print(len(tuple_d))
print(tuple_d[2][1])
print(type(tuple_a))
print(tuple_a[-4])
print(tuple_a)