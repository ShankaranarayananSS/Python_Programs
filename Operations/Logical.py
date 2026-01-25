t, f = True, False
print("True Tables:")

print("\nAND OPERATOR:")
print(t, "\tand\t", t, "\t=\t", t and t)
print(t, "\tand\t", f, "\t=\t", t and f)
print(f, "\tand\t", t, "\t=\t", f and t)
print(f, "\tand\t", f, "\t=\t", f and f)

print("\nOR OPERATOR:")
print(t, "\tor\t", t, "\t=\t", t or t)
print(t, "\tor\t", f, "\t=\t", t or f)
print(f, "\tor\t", t, "\t=\t", f or t)
print(f, "\tor\t", f, "\t=\t", f or f)

print("\nNOT OPERATOR:")
print("not",t,"\t=\t", not t)
print("not",f,"\t=\t", not f)
