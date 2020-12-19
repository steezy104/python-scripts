while True:
    try:
        lines = int(input("Enter how many lines you wish to write: "))
    except:
        continue
    if  lines > 0:
        break

text = []

for i in range(lines):
    text.append(input())

save_file = open("save_file.txt", "w")

for line in text:
    save_file.write(line+'\n')
    
save_file.close()