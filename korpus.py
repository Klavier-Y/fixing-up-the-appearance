datefile = open('gehoeren.txt', encoding='UTF-8')

for line in datefile:
  line = line.rstrip()
  line = line.lstrip()

  print(line) 