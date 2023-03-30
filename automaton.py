
# 5-tupla
states = [] #lista de strings
alphabets = [] #lista de strings
start_state = ""
final_states = [] #lista de strings
transition = {} #dicionário

# entrada que vai ser verificada
input_string = ""

# Os estados e os alfabetos estão representados por uma lista de strings
print("Insira os estados do automato separados por espaço: ", end="")
states = input().split()

print("\nInsira o alfabeto do automato separados por espaço: ", end="")
alphabets = input().split()

# Estados iniciais e estados aceitos pelo automato
print("\nInsira o estado inicial do automato: ", end="")
start_state = input()

print("\nInsira os estados finais do automato separado por espaços: ", end="")
final_states = input().split()

# Funções de transição é um dicionario onde:
# key = (current_state(estado atual), input(entrada))
# value = next_state (None para estados rejeitados)

print("\nInsira o próximo estado para prosseguir \n")
for state in states:
    for alpha in alphabets:
        print(f"\t {alpha}")
        print(f"{state}\t---->\t", end="")
        dest = input()

        #Estados rejeitados são representados por None no dicionario
        if dest == ".":
            transition[(state, alpha)] = None
        else:
            transition[(state, alpha)] = dest

# Etapa em que busca a sequência de entrada

while(True):
    print("\nInsira a cadeia para iniciar o automato: ", end="")
    input_string = input()

    # Analisa a entrada com o estado atual como estado inicial
    current_state = start_state

    for char in input_string:
        # Faz a transição para o proximo estado usando o estado atual e o alfabeto de entrada 
        current_state = transition[(current_state, char)]
        
        # Verifica se a cadeia é rejeitado
        if current_state is None:
            print("Rejeitado")
            break
    else:
        # Quando a string inteira for analisada, verifica se o estado final é um estado aceito
        if (current_state in final_states):
            print("Aceito")
        else:
            print("Rejeitado")
    
            