import streamlit as st

st.title("Validador de CPF")
cpf = st.text_input("Digite o CPF (apenas números):")

if cpf:
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        st.error("CPF deve ter 11 dígitos.")
    elif cpf == cpf[0] * 11:
        st.error("CPF inválido.")
    else:

        nove_digitos = cpf[:9]
        contador_regressivo_dig1 = 10
        resultado_dig1 = 0
        for digito in nove_digitos:
            resultado_dig1 += int(digito) * contador_regressivo_dig1
            contador_regressivo_dig1 -= 1
        digito1 = (resultado_dig1 * 10) % 11
        if digito1 == 10:
            digito1 = 0

        dez_digitos = cpf[:10]
        contador_regressivo_dig2 = 11
        resultado_dig2 = 0
        for digito in dez_digitos:
            resultado_dig2 += int(digito) * contador_regressivo_dig2
            contador_regressivo_dig2 -= 1
        digito2 = (resultado_dig2 * 10) % 11
        if digito2 == 10:
            digito2 = 0

        if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
            st.success("CPF Válido!")
        else:
            st.error("CPF Inválido!")