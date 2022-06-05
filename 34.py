
try:

    with open('test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print('that file was not found')

else:
    print('that file is found')