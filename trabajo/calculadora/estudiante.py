class Estudiante:
    def __init__(self, id_estudiante):
        self.id_estudiante = id_estudiante
        self.notas = []
        self.promedio = 0.0
        self.categoria = ""

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        self.promedio = sum(self.notas) / len(self.notas)
        if self.promedio < 3.0:
            self.categoria = "reprobado"
        elif 3.0 <= self.promedio <= 4.0:
            self.categoria = "regular"
        elif 4.0 < self.promedio <= 4.5:
            self.categoria = "bueno"
        else:
            self.categoria = "excelente"

    def ver_info(self):
        return f"Estudiante {self.id_estudiante}: Promedio {self.promedio:.2f} - Categoría: {self.categoria}"


class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def resumen_estadistico(self):
        reprobados = sum(1 for e in self.estudiantes if e.categoria == "reprobado")
        regulares = sum(1 for e in self.estudiantes if e.categoria == "regular")
        buenos = sum(1 for e in self.estudiantes if e.categoria == "bueno")
        excelentes = sum(1 for e in self.estudiantes if e.categoria == "excelente")
        return f"Resumen Estadístico:\nReprobados: {reprobados}\nRegulares: {regulares}\nBuenos: {buenos}\nExcelentes: {excelentes}"
