# =====================================================================
# BLOQUE 1: FUNDAMENTOS BÁSICOS (Variables, Tipos de datos e Input)
# =====================================================================
print("==================================================")
print("   BIENVENIDOS AL TALLER DE PYTHON - CI NICARAGUA")
print("==================================================")

# 1. Variables y captura de datos por consola
nombre_participante = input("¿Cuál es tu nombre? ")
print(f"¡Hola, {nombre_participante}! Comencemos a programar.")

# 2. Operadores básicos y conversión de tipos
edad_str = input("¿Qué edad tienes? ")
edad = int(edad_str) # Convertimos el texto ingresado a número entero
proxima_edad = edad + 1
print(f"El próximo año cumplirás {proxima_edad} años.")


# =====================================================================
# BLOQUE 2: ESTRUCTURAS DE CONTROL (Condicionales y Bucles)
# =====================================================================
print("\n--- 2. CONTROL DE FLUJO Y LOGICA ---")

# Condicional (if / else)
nivel_experiencia = input("¿Tienes experiencia previa? (si/no): ").lower()

if nivel_experiencia == "si":
    print("-> ¡Excelente! Tienes bases para retos más avanzados.")
else:
    print("-> Perfecto. Este taller desde cero te dará bases sólidas.")

# Bucle (for) - Automatizando tareas repetitivas
print("\nIniciando sistema de carga de módulos:")
for modulo in range(1, 4):
    print(f">> Cargando módulo {modulo} de programación...")

print("¡Sistema listo y operativo! 🚀\n")


# =====================================================================
# BLOQUE 3: FUNCIONES (Modularización simple)
# =====================================================================
print("--- 3. FUNCIONES ---")

def calcular_precio_con_iva(precio_base):
    """Función para calcular el precio final aplicando un impuesto del 15%"""
    iva = precio_base * 0.15
    total = precio_base + iva
    return total

# Probando la función
precio_original = 100.0
precio_final = calcular_precio_con_iva(precio_original)
print(f"Precio base: ${precio_original} | Precio con IVA (15%): ${precio_final}")


# =====================================================================
# BLOQUE 4: CLASES, CONSTRUCTORES Y ENTIDADES (POO)
# =====================================================================
print("\n--- 4. MODELANDO ENTIDADES CON CLASES Y OBJETOS ---")

# Explicación previa a los estudiantes:
# Una "Clase" es el plano o molde. La "Entidad u Objeto" es el elemento real 
# creado a partir de ese plano que contiene sus propios datos y acciones.

class Producto:
    # 1. El Constructor: Método especial que inicializa los atributos de la entidad
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo      # Atributo de la entidad
        self.nombre = nombre      # Atributo de la entidad
        self.precio = precio      # Atributo de la entidad
        self.stock = stock        # Atributo de la entidad

    # 2. Método de comportamiento: Muestra la información de la entidad
    def mostrar_informacion(self):
        print(f"[{self.codigo}] Producto: {self.nombre} | Precio: ${self.precio} | Stock disponible: {self.stock}")

    # 3. Método para modificar el estado interno de la entidad
    def realizar_venta(self, cantidad_comprada):
        if cantidad_comprada <= self.stock:
            self.stock -= cantidad_comprada # Restamos del stock actual
            print(f"-> ¡Venta exitosa! Se vendieron {cantidad_comprada} unidad(es) de {self.nombre}.")
        else:
            print(f"-> ¡Error! No hay suficiente stock de {self.nombre} para completar la venta.")


# =====================================================================
# BLOQUE 5: INSTANCIACIÓN Y USO DE LAS ENTIDADES EN EL MUNDO REAL
# =====================================================================
print("\n--- Creando Instancias (Objetos) de nuestra Entidad ---")

# Creamos objetos reales (instancias de la clase Producto)
producto1 = Producto("PROD-01", "Laptop Core i5", 650.0, 5)
producto2 = Producto("PROD-02", "Teclado Mecánico RGB", 45.0, 10)

# Mostramos el estado inicial de ambas entidades
producto1.mostrar_informacion()
producto2.mostrar_informacion()

print("\n--- Ejecutando una transacción comercial ---")
# Interactuamos con los métodos de la entidad producto1
producto1.realizar_venta(2)

print("\n--- Estado actualizado de la Entidad después de la venta ---")
producto1.mostrar_informacion()