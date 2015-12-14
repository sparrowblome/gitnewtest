name = raw_input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 2: continue
    if words[0] != 'From': continue
    mail = words[1]
    counts[mail] = counts.get(mail,0) + 1    

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount        