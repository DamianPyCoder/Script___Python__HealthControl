def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def estado_salud(imc):
    if imc < 18.5:
        return "bajo peso"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obesidad"

def generar_tabla_ejercicios(dias_entrenamiento):
    tabla_ejercicios = {
        "Lunes": ["Sentadillas", "Flexiones de brazos", "Planchas"],
        "Martes": ["Caminata rápida", "Abdominales", "Estiramientos"],
        "Miércoles": ["Levantamiento de pesas", "Burpees", "Yoga"],
        "Jueves": ["Correr", "Saltos de cuerda", "Estiramiento"],
        "Viernes": ["Natación", "Zancadas", "Ejercicios de brazos"],
        "Sábado": ["Ciclismo", "Planche", "Estiramientos"],
        "Domingo": ["Descanso activo", "Yoga", "Paseo al aire libre"],
    }
    
    entrenamiento_semana = {}
    for dia_entrenamiento in dias_entrenamiento:
        entrenamiento_semana[dia_entrenamiento] = tabla_ejercicios[dia_entrenamiento]
    
    return entrenamiento_semana

def generar_tabla_dieta():
    tabla_dieta = {
        "Desayuno": ["Avena con frutas", "Yogur griego", "Frutos secos"],
        "Almuerzo": ["Ensalada de pollo", "Arroz integral", "Vegetales al vapor"],
        "Cena": ["Salmón a la parrilla", "Ensalada verde", "Pan integral"],
        "Snack mañana": ["Fruta fresca", "Nueces", "Té verde"],
        "Snack tarde": ["Batido de proteínas", "Galletas de arroz", "Zumo natural"],
    }
    return tabla_dieta

def main():
    print("Bienvenido a la calculadora de IMC y planificador básico de ejercicios y dieta")
    edad = int(input("Ingresa tu edad: "))
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    genero = input("Ingresa tu género (hombre/mujer): ").lower()

    imc = calcular_imc(peso, altura)
    estado = estado_salud(imc)

    print(f"\nTu IMC es: {imc:.2f}")
    print(f"Según el IMC, tienes {estado}.")

    dias_entrenamiento = input("\n Qué días de la semana puedes entrenar? (lunes, martes, miércoles, jueves, viernes, sábado, domingo) ").split(',')
    dias_entrenamiento = [dia.strip().capitalize() for dia in dias_entrenamiento]

    # Generar y mostrar tablas ejercicios y dieta
    tabla_ejercicios = generar_tabla_ejercicios(dias_entrenamiento)
    tabla_dieta = generar_tabla_dieta()
    print("\n A continuación, te presentamos una tabla de ejercicios:")
    for dia, ejercicios in tabla_ejercicios.items():
        print(f"\n{dia}:")
        for ejercicio in ejercicios:
            print(f"- {ejercicio}")
    print("\n A continuación, te presentamos una tabla de dieta:")
    for comida, alimentos in tabla_dieta.items():
        print(f"\n{comida}:")
        for alimento in alimentos:
            print(f"- {alimento}")

if __name__ == "__main__":
    main()
