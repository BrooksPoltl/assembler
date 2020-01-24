from numpy import binary_repr
def main(file):
    f = open(file)
    hack_file = file
    index = len(hack_file) - 1  
    while hack_file[index] in reversed(hack_file):
        if(hack_file[index] == "."):
            break
        hack_file = hack_file[:-1]
        index -= 1
    hack_file = "".join((hack_file, "hack"))
    h = open(hack_file, "w+")
    h.write(binary_repr(2, 16))

    print(hack_file)

    for line in f:
        break
main("./test/add/Add.asm")