from sensor import SensorTemperatura, Edificio

edificio = Edificio()
cantidad = int(input("Cantidad de sensores de temperatura instalados: "))

for i in range(cantidad):
    temp = float(input(f"Temperatura registrada para el sensor {i+1}: "))
    sensor = SensorTemperatura(i+1, temp)
    sensor.evaluar_temperatura()
    print(sensor.ver_info())
    edificio.agregar_sensor(sensor)
    
print(edificio.generar_resumen())
