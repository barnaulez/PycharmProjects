with open("./Input/Names/invited_names.txt") as f:
    for line in f.readlines():
        l = line.strip('1234567890').strip()
        with open("./Input/Letters/starting_letter.txt") as f:
            text = f.read()
            output = text.replace("[name]", l)
            with open(f"./Output/ReadyToSend/letter_for_{l}.txt", mode="w") as f:
                f.write(output)

