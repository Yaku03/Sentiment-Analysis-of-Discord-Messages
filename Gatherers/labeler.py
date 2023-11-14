dest = open('../Datasets/backup.csv', 'a', encoding='utf-8')
x = 0
while True:
     source = open('../Datasets/dataset.csv', 'r', encoding='utf-8') 
     lines = source.readlines()
     line = lines[0]
     line = line.strip('\n')
     if len(lines) - 1 == 0:
          break
     print(line, '\n')
     i = input()
     if i == "exit":
          break
     else:
          print(line + f"{i}", file=dest)
          with open('../Datasets/dataset.csv', 'w', encoding='utf-8') as source:
               source.writelines(lines[1:])
          x += 1
