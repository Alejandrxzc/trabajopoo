class Producto:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = ""

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def verificar_stock(self):
        if self.cantidad < 10:
            self.estado = "crítico"
        elif 10 <= self.cantidad <= 50:
            self.estado = "bajo stock"
        else:
            self.estado = "suficiente"

    def ver_info(self):
        return f"Producto: {self.nombre} (Cod: {self.codigo}) | Disponibles: {self.cantidad} | Estado: {self.estado}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def reporte_consolidado(self):
        critico = sum(1 for p in self.productos if p.estado == "crítico")
        bajo = sum(1 for p in self.productos if p.estado == "bajo stock")
        suficiente = sum(1 for p in self.productos if p.estado == "suficiente")
        return f"Reporte Consolidado:\n- Crítico: {critico}\n- Bajo Stock: {bajo}\n- Suficiente: {suficiente}"