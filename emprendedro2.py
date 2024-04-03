
p = int(input("ingrese el precio de subs: "))
u = int(input("ingrese la cantidad de usuarios: "))
up = int(input("ingrese la cantidad de usuarios premium: "))
gt = int(input("ingrese el gasto total: "))

usuario_premium = 1.5 * p

up = up * usuario_premium

utilidades = p * u + up - gt




print(f"Las utilidades son {utilidades}")