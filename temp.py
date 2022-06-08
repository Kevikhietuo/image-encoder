msg = 'kevikhietuo'

val1 = hash('k') % 255
val2 = ord('k') + 1
print(val1)
print(chr(val2))
print(hash(chr(val2)) % 255)