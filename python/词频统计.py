import re, collections, sys


words = "".join([line for line in sys.stdin])
words = re.compile(r"\w+").findall(words.lower()).split()
words = [each.strip() for each in words]
words = list(set(words))
counter = collections.Counter(words)
rank = sorted(counter.items(), key=lambda each: (-each[1], each[0]), reverse=False)
print(len(rank))
for each in rank[0:int(0.1 * len(rank))]:
    print("{} {}".format(each[0], each[1]))

