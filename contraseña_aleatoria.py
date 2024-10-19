import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud_de_contraseña = int(input("Cuantos caracteres de largo su contraseña va a ser?"))
contraseña_creada = ""

print(caracteres[1])

for i in range(longitud_de_contraseña):
    contraseña_creada = contraseña_creada + caracteres[random.randint(0, 73)]

print("Su contraseña generada es: " + contraseña_creada)