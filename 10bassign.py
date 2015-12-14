name = raw_input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 5: continue
    if words[0] != 'From': continue
    hour = words[5]
    times = hour.split(":")
    hour = times[0]
    counts[hour] = counts.get(hour,0) + 1
for k,v in sorted(counts.items()):
     print k, v    