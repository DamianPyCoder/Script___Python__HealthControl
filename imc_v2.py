import requests

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

def calcular_rango_peso_normal(altura):
    peso_minimo = 18.5 * (altura ** 2)
    peso_maximo = 24.9 * (altura ** 2)
    return peso_minimo, peso_maximo

def obtener_ejercicios():
    url = "https://wger.de/api/v2/exercise/?language=2"
    response = requests.get(url)
    return response.json()["results"]

def obtener_dieta():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    return response.json()["meals"][0]

def pedir_datos_personales():
    print("¡Bienvenido/a a la calculadora de IMC y planificador de ejercicios y dieta!")

    # Pedir datos personales al usuario
    edad = int(input("Ingresa tu edad: "))
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    genero = input("Ingresa tu género (hombre/mujer): ").lower()

    return edad, peso, altura, genero

def main():
    edad, peso, altura, genero = pedir_datos_personales()

    # Calcular el IMC y el estado de salud
    imc = calcular_imc(peso, altura)
    estado = estado_salud(imc)

    print(f"\nTu IMC es: {imc:.2f}")
    print(f"Según el IMC, tienes {estado}.")

    # Calcular rango de peso normal
    peso_minimo, peso_maximo = calcular_rango_peso_normal(altura)
    print(f"Tu peso debería estar entre {peso_minimo:.2f} kg y {peso_maximo:.2f} kg para alcanzar un peso normal.")

    # Pedir los días de la semana en los que se puede entrenar
    dias_entrenamiento = input("\n¿Qué días de la semana puedes entrenar? (lunes, martes, miércoles, jueves, viernes, sábado, domingo) ").split(',')
    dias_entrenamiento = [dia.strip().capitalize() for dia in dias_entrenamiento]

    # Obtener ejercicios y dieta desde las APIs
    ejercicios = obtener_ejercicios()
    dieta = obtener_dieta()

    # Generar la tabla de ejercicios para los días seleccionados
    tabla_ejercicios = {}
    for dia in dias_entrenamiento:
        tabla_ejercicios[dia] = [ejercicio["name"] for ejercicio in ejercicios if dia.lower() in ejercicio["name"].lower()]

    # Mostrar la tabla de ejercicios
    print("\n¡Felicidades! A continuación, te presentamos una tabla de ejercicios:")
    for dia, ejercicios in tabla_ejercicios.items():
        print(f"\n{dia}:")
        if ejercicios:
            for ejercicio in ejercicios:
                print(f"- {ejercicio}")
        else:
            print("- Descanso")

    # Mostrar la tabla de dieta
    print("\nA continuación, te presentamos una tabla de dieta:")
    print(f"\nNombre: {dieta['strMeal']}")
    print("Ingredientes:")
    for i in range(1, 21):
        ingrediente = dieta[f"strIngredient{i}"]
        if ingrediente:
            print(f"- {ingrediente}")
    print("\nInstrucciones:")
    print(dieta["strInstructions"])

if __name__ == "__main__":
    main()
