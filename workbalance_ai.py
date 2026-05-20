import os
import numpy as np
from time import sleep
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- PARTE 2: FUNÇÕES CORRIGIDAS (Usando o parâmetro 'lista' corretamente) ---
def calcular_media_horas(lista):
    if not lista: return 0.0
    return float(np.mean([c['horas_trabalhadas'] for c in lista]))

def maior_estresse(lista):
    if not lista: return ""
    return max(lista, key=lambda c: c['estresse'])['nome']

def colaboradores_produtivos(lista):
    return [c['nome'] for c in lista if c['tarefas_concluidas'] >= 5]

def alerta_equilibrio(lista):
    return [c['nome'] for c in lista if c['estresse'] >= 4 and c['pausas'] <= 1]

# --- PARTE 5: FEEDBACK DETERMINÍSTICO (Sem Random/Aleatoriedade) ---
def feedback(colaborador):
    nome = colaborador['nome']
    estresse = colaborador['estresse']
    pausas = colaborador['pausas']
    tarefas = colaborador['tarefas_concluidas']

    # Regras lógicas baseadas em dados
    if tarefas >= 5 and estresse <= 2:
        return f'{nome}: excelente desempenho! Você mantém ritmo forte com bom equilíbrio.'
    elif tarefas >= 5 and estresse >= 4:
        return f'{nome}: produtividade alta, mas o estresse está elevado. Considere reduzir o ritmo.'
    elif tarefas <= 2 and estresse <= 2:
        return f'{nome}: você está tranquilo, mas precisa melhorar o foco para aumentar as entregas.'
    elif tarefas <= 2 and estresse >= 4:
        return f'{nome}: baixa entrega sob alto estresse. Faça pausas e respire.'
    elif estresse >= 4 and pausas <= 1:
        return f'{nome}: alta carga e poucas pausas. Tente intercalar descansos.'
    
    # Feedback padrão preditivo (Substituindo o Random por consistência de IA)
    subcarga = "Considere assumir novos desafios." if tarefas < 3 else "Mantenha o bom trabalho."
    return f'{nome}: ritmo estável e sob controle. {subcarga}'

# --- PARTE 4: TRATAMENTO DE ERROS ROBUSTO (Usando Raise para o estresse) ---
lista_colaboradores = []
for c in range(5):
    while True:
        try:
            clear_screen()
            print(f'=== CADASTRO DO COLABORADOR {c+1}/5 ===\n')

            nome = input('Digite seu nome: ').strip().upper()
            if not nome: raise ValueError("O nome não pode ser vazio.")
            
            departamento = input('Digite seu departamento: ').strip().upper()
            htd = float(input('Horas trabalhadas por dia: '))
            pausas = int(input('Pausas por dia (quantidade): '))

            nivel_estresse = int(input('Nível de estresse (1 a 5): '))
            if not (1 <= nivel_estresse <= 5):
                # Força o programa a ir para o bloco except com uma mensagem específica
                raise ValueError("O nível de estresse deve estar estritamente entre 1 e 5.")

            tarefas_concluidas = int(input('Tarefas concluídas: '))

            lista_colaboradores.append({
                'nome': nome,
                'departamento': departamento,
                'horas_trabalhadas': htd,
                'pausas': pausas,
                'estresse': nivel_estresse,
                'tarefas_concluidas': tarefas_concluidas
            })
            break  

        except ValueError as e:
            print(f'\n❌ Erro de validação: {e}')
            print('Por favor, refaça o cadastro deste colaborador.')
            sleep(3)

# --- PARTE 3 & 4: EXIBIÇÃO, GERAÇÃO DE TEXTO E SALVAMENTO DE ARQUIVO ---
horas = np.array([c['horas_trabalhadas'] for c in lista_colaboradores])
estresse = np.array([c['estresse'] for c in lista_colaboradores])

media_horas = np.mean(horas)
desvio_horas = np.std(horas)
media_estresse = np.mean(estresse)

agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
feedbacks = [feedback(c) for c in lista_colaboradores]

relatorio_texto = (
    'RELATÓRIO WORKBALANCE AI\n'
    '----------------------------------------\n'
    f'Média de horas trabalhadas: {media_horas:.1f}h\n'
    f'Desvio padrão de horas: {desvio_horas:.1f}h\n'
    f'Média de estresse: {media_estresse:.1f}\n'
    f'Colaborador mais estressado: {maior_estresse(lista_colaboradores)}\n'
    f'Colaboradores com 5+ tarefas: {colaboradores_produtivos(lista_colaboradores)}\n'
    f'Alerta de equilíbrio: {alerta_equilibrio(lista_colaboradores)}\n\n'
    'FEEDBACK INDIVIDUAL\n'
    '----------------------------------------\n' +
    '\n'.join(feedbacks) + '\n\n'
    f'Relatório gerado em: {agora}\n'
)

# Print na tela (Faltou no arquivo .py de vocês)
clear_screen()
print(relatorio_texto)

# Salvar no arquivo com tratamento de erro correto
try:
    caminho_relatorio = os.path.join(os.getcwd(), 'relatorio_workbalance.txt')
    with open(caminho_relatorio, 'w', encoding='utf-8') as f:
        f.write(relatorio_texto)
    print('✔ Relatório gerado e salvo com sucesso em "relatorio_workbalance.txt"!')
except (OSError, IOError) as e:
    print(f'❌ Falha ao gravar o arquivo em disco: {e}')