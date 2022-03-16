fhand = open('mbox-blow.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    words = line.split()
    #print('Debug:', words)
    if len(words) < 3 :
        continue
    if words[0] != 'From' :
        continue
    print(words[2])
