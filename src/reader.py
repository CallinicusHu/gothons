with open("text.txt", 'r', encoding="UTF8") as file:
    lines = file.readlines()

#removes /n
#for index, line in enumerate(lines):
#    lines[index] = line[:len(line)-1:]

look_for_this = "-The Bridge-\n"
def give_me_my_part():
    try:
        ndx = lines.index(look_for_this)
        part = ""
        counter = 0

        if lines.count(look_for_this) != 2:
            raise ValueError("Rossz a forrásfile vagy amit keresni próbálsz.")

        while True:
            counter += 1
            add_part = lines[ndx+counter]
            if add_part == look_for_this:
                break
            part = part + add_part
            if counter == 1000:
                raise ValueError("Végtelenített")
        return part

    except:
        "Nem nincs elfogyott."


print(give_me_my_part())


