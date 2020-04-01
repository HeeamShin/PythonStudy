#############################
# single quote & double quote
print("I said 'Hello'")
print('I said "Hello"')

# escape character (\)
print("I said \"Hello\"")
print('I said \'Hello\'')
print("Hello\nHello")
print("Hello\tHello")
print("Hello\\Hello")

## table using \t
print("Name\tAge\tLocation")
print("John\t26\tWinterfell")
print("Cersei\t38\tCasterly Rock")

## multi line string
print("""I am a boy
You are a girl
We are friends""")

## multi line with escape character
print("""\
I am a boy
You are a girl
We are friends\
""")

##################
# string operators

## concetenation (+)
print("Hell" + "o")

## repetition (*)
print("Hello" * 3)

## indexing ([])
print("Hello"[2])
print("Hello"[-1])

### IndexError(index out of range)
# print("Hello"[10])

## slicing ([:])
print("Hello"[1:3])
print("Hello"[:3])
print("Hello"[1:])

# len()
print(len("Hello"))