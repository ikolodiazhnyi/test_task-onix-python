while (True):
    filePath = input("Enter a path to the file: ")
    try:
        with open(filePath) as file:
            for str in file:
                print(str, end='')
        print()
    except IOError as e:
        print(e.strerror)