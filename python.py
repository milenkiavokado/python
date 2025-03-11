import random
import time
symbhol =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_symbhols = int(input("длина пароля"))
password = ""


for i in range(password_symbhols):
    password += (random.choice(symbhol))
    
    
print("сгенерированный пароль  ", password) 
