with open("Ozhegov.txt", "r", encoding="UTF-8") as f:
    text = f.read
    line = f.readlines()
    word = line.split()
    for word in line:
        if len(word) > 20 or len(word) == 20:
            print(line)  
