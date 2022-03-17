words = [x for x in(input().split(' '))]
words.sort()
ds = list(set(words))
print(','.join(ds))