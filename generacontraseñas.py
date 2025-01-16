import random

Characters = ["+", "-", "*", "/", "^", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "&", "?", ">", "<", "=", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

longitud = input("Ingrese la longitud de la contraseña: ")

contraseña = longitud

for i in range(int(longitud)):
    contraseña += random.choice(Characters)
    
print(contraseña)
