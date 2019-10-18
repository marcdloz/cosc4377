
def multiprint(s, times):
    if times == 0:
        print("()")
    else:
        print("(" + s, end="")
        for i in range(times - 1):
            print("; " + s, end="")
        print(")")


multiprint("beetlejuice", 5)

# sentinel loop solution
total = 0
num = int(input("next integer (-1 to quit)? "))
while num != -1:
    total += num
    num = int(input("next integer (-1 to quit)? "))
print("total =", total)