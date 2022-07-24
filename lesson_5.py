data_types = ['hello', 'name', 123, 5, True, False, 2.5,  3.9]
strings = list()

print(data_types[0:4])
print(data_types[0:-1:2])

# print(data_types[])

data_types.append('ABC')
data_types.insert(1, 25)
data_types += '100'

print(data_types)

while len(strings) != 5:
    word = input('enter something:')
    strings.append(word)
    print(strings)
print(strings)
