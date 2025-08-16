import streamlit as st
import json
import random
import string

def criar_senha():
        st.title("🔑Gerador de senhas!")
        st.subheader("Aqui você está no gerador de senha.")
            
        senha = []
        pool = ""
        tamanho = st.number_input("Na sua senha você deseja que tenha quantos caracteres?",min_value=0, step=1, value=10)
        
        #colocar caixa de selecionar
        minuscula = st.checkbox("letras minúsculas", value=True)
        maiscula = st.checkbox("letras maísculas", value=True)
        numeros = st.checkbox("números", value=True)
        simbolos = st.checkbox("simbolos", value=True)
        
        if st.button("Criar senha"):
            if minuscula:
                pool += string.ascii_lowercase
                senha.append(random.choice(string.ascii_lowercase))

            if maiscula:
                pool += string.ascii_uppercase
                senha.append(random.choice(string.ascii_uppercase))

            if numeros:
                pool += string.digits
                senha.append(random.choice(string.digits))

            if simbolos:
                pool += string.punctuation
                senha.append(random.choice(string.punctuation))

            tamanho_restante = tamanho - len(senha)
            
            if tamanho_restante > 0:
                for _ in range(tamanho_restante):
                    senha.append(random.choice(pool))

            random.shuffle(senha)

            senha_final = "".join(senha)
            senha_criada = True
            st.success("Senha gerada com sucesso!")
            st.info(senha_final)
        else:
            senha_criada = False
        
        if senha_criada:
            with st.expander("Crie um arquivo para sua senha"):
                st.write("Prefere em:")
                if st.button(".json"):
                    with open("Minha Senha segura.txt", "w") as arquivo:
                        arquivo.write(senha_final)
                if st.button(".txt"):
                    with open("Minha Senha segura.json", "w") as arquivo:
                        json.dump(senha_final, arquivo, indent=4, ensure_ascii=False)
                        

st.set_page_config(page_title="Gerador de senha", page_icon="🔒", layout="wide")
if 'page' not in st.session_state:
    st.session_state.page = 'principal'

if st.session_state.page == 'principal':
    criar_senha()
else:
    st.info("Erro.")
    st.rerun()

#veificador de nulos e melhorar a interface ver como fazer o download dos arquivos com a senha gerada
#ver melhor onde vai aparecer a st.info ou mudar de funçao e fazer um botao para copiar a senha gerada 
#centralizar o windget