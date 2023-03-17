with open("my_file.txt",mode="rw") as f:
    contents = f.read()
    print(contents)
    f.write("New text")
    contents = f.read()
    print(contents)
