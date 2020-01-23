def main(file):
    f = open(file)
    print(f)
    for line in f:
        print(line)

main("./test/add/Add.asm")