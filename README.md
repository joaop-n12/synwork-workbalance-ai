# WorkBalance AI - SynWork 🧠💼

O **WorkBalance AI** é um protótipo de sistema desenvolvido em Python focado em otimizar o bem-estar e a produtividade no ambiente de trabalho. O projeto analisa rotinas de trabalho de colaboradores, calcula métricas estatísticas de estresse e carga horária, gera alertas de desequilíbrio (risco de burnout) e fornece feedbacks automatizados e personalizados para a gestão de pessoas.

Este projeto foi desenvolvido como parte da **Global Solutions: Soluções Disruptivas de IA para o Futuro do Trabalho**.

---

## 🚀 Funcionalidades

* **Cadastro Automatizado:** Coleta de dados de rotina (Nome, Departamento, Horas Trabalhadas, Pausas, Nível de Estresse e Tarefas Concluídas).
* **Análise Estatística com NumPy:** Cálculo automatizado da média e desvio padrão das horas trabalhadas, além da média geral de estresse do time.
* **Alertas de Equilíbrio:** Identificação crítica de colaboradores operando com alto nível de estresse (>= 4) e poucas pausas (<= 1).
* **Módulo de Feedback:** Geração de diagnósticos de desempenho e bem-estar baseados no cruzamento de dados de produtividade e esgotamento.
* **Persistência de Dados:** Exportação automática do relatório consolidado e dos feedbacks para um arquivo externo (`relatorio_workbalance.txt`) com data e hora da execução.

---

## 📦 Estrutura do Repositório

Como o projeto foca na entrega limpa de código, o repositório contém apenas os arquivos essenciais de desenvolvimento:

* `workbalance_ai.py`: Script principal em Python com a lógica de execução via terminal.
* `workbalance_ai.ipynb`: Notebook Jupyter contendo os testes e a validação das células de código.

*Nota: O arquivo `relatorio_workbalance.txt` não está incluído no repositório por boas práticas de versionamento, sendo gerado automaticamente na máquina do usuário assim que o script é executado.*

---

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python 3 e a biblioteca **NumPy** instalados em sua máquina.
2. Baixe os arquivos `workbalance_ai.py` ou `workbalance_ai.ipynb`.
3. Execute o script principal:
```
   python workbalance_ai.py
```
4. Insira os dados solicitados para os 5 colaboradores no terminal.

5. Quando o sistema é executado com sucesso, ele gera um arquivo chamado `relatorio_workbalance.txt` estruturado da seguinte forma:
## 📄 Exemplo de Relatório Gerado

```text
RELATÓRIO WORKBALANCE AI
----------------------------------------
Média de horas trabalhadas: 12.6h
Desvio padrão de horas: 3.6h
Média de estresse: 3.0
Colaborador mais estressado: IVETE 
Colaboradores com 5+ tarefas: ['JOAO', 'ANTONIO']
Alerta de equilíbrio: ['IVETE ']

FEEDBACK INDIVIDUAL
----------------------------------------
JOAO: ritmo consistente! Pequenos ajustes podem ajudar.
IVETE : baixa entrega sob alto estresse. Faça pausas e respire.
ANTONIO: produtividade alta, mas o estresse está elevado. Considere reduzir o ritmo.
CAMILA: tudo dentro do esperado. Boa constância.
JOANA: você está tranquilo, mas precisa melhorar o foco para aumentar as entregas.

Relatório gerado em: 17/11/2025 17:21:04
````

👥 Integrantes do Grupo
João Pedro de Souza Nunes    
Guilherme Yuiti Matsushita Nakamura
