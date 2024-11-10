import streamlit as st

# Título de la aplicación
st.title("Calculadora Básica - TSCDeIA")

# Entrada de números
num1 = st.number_input("Ingrese el primer número:", step=1.0)
num2 = st.number_input("Ingrese el segundo número:", step=1.0)

# Selección de la operación
operation = st.selectbox("Seleccione la operación:", ("Suma", "Resta", "Multiplicación", "División"))

# Resultado
resultado = None
if st.button("Calcular"):
    if operation == "Suma":
        resultado = num1 + num2
    elif operation == "Resta":
        resultado = num1 - num2
    elif operation == "Multiplicación":
        resultado = num1 * num2
    elif operation == "División":
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error("Error: División por cero no permitida.")

    st.success(f"Resultado: {resultado}")
    # Muestra el resultado
    if resultado is not None:
        st.write("true")
