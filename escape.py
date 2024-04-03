import math

radio = int(input("Ingrese el radio en kilómetros:"))
gravedad = float(input("Ingrese la constante g: "))


radio = radio * 1000
ve = math.sqrt(2*gravedad*radio)



print(f"La veolcidad de Escape es: {ve:.1f} [m/s]")
