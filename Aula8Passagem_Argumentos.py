import sys

args = sys.argv #arg1 = metodo // arg2 = n1 // arg = n2

def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

if args[1] == "soma":
    resp = soma(float(args[2]), float(args[3]))
elif args[1] == "sub":
    resp = sub(float(args[2]), float(args[3]))

print(resp)