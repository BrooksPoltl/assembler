from numpy import binary_repr

def line_parser(hack_file, line):
    if(line[0] == "@"):
        print("reached")
        new_line = line[1:]
        new_line = int(new_line)
        hack_file.write(binary_repr(new_line, 16)+ '\n')
    if(line == "D=A"):
        hack_file.write("")


def main(file):
    f = open(file)
    hack_file = file
    index = len(hack_file) - 1  
    #create hackfile string
    while hack_file[index] in reversed(hack_file):
        if(hack_file[index] == "."):
            break
        hack_file = hack_file[:-1]
        index -= 1
    hack_file = "".join((hack_file, "hack"))


    h = open(hack_file, "w+")

    for line in f:
        line_parser(h, line)
main("./test/add/Add.asm")