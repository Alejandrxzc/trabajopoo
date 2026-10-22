from estudiante import Estudiante, Curso

curso = Curso()
num_estudiantes = int(input("Ingrese el número de estudiantes de un curso: "))

for i in range(num_estudiantes):
    estudiante = Estudiante(i+1)
    for j in range(4):
        nota = float(input(f"Ingrese la calificación {j+1} para el estudiante {i+1}: "))
        estudiante.agregar_nota(nota)
        
    estudiante.calcular_promedio()
    print(estudiante.ver_info())
    curso.agregar_estudiante(estudiante)
    
print("\n--- Resumen Final ---")
print(curso.resumen_estadistico())
