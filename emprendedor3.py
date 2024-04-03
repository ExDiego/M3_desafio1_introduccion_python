
p = int(input("ingrese el precio de subs: "))
u = int(input("ingrese la cantidad de usuarios: "))
gt = int(input("ingrese el gasto total: "))
utilidades_anteriores = int(input("Utilidades anteriores: "))



utilidades = p * u - gt
razon = utilidades_anteriores/utilidades



print(f"La razon de las utilidades son {razon:.2f}")