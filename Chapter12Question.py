"""Write a program and open three different text if any of the file is not present a message will display without crasing
the program """


def filename(fname):
    try:
        with open(fname, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {fname} is not found")


filename('mfile.txt')
