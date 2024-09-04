def all_variants(text):
    interval = 1
    while interval < len(text)+1:
        for i in range(len(text)):
            if (interval+i) > (len(text)):
                continue
            else:
                b = text[i:i+interval]
                yield b
        interval += 1



a = all_variants("abc")
for i in a:
    print(i)

# d= 'abc'
# print(d[:2])
# print(d[1:])