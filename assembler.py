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
    
    print(hack_file)
    for line in f:
        break
main("./test/add/Add.asm")