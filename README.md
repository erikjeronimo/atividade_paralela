# Processamento Paralelo de Imagens em Python

Projeto desenvolvido para a atividade da 2ª Unidade de Programação Paralela e Distribuída.

## 1. Sobre o projeto

Este projeto implementa um processamento de imagens em lote para comparar o desempenho entre uma execução sequencial e uma execução paralela.

O objetivo é demonstrar como a programação paralela pode reduzir o tempo de processamento de tarefas computacionalmente intensivas, distribuindo o trabalho entre diferentes núcleos do processador.

O programa utiliza filtros de imagem, como desfoque e detecção de bordas, para realizar o processamento.

## 2. Tecnologias utilizadas

- **Python 3:** linguagem de programação utilizada no projeto.
- **Pillow:** biblioteca para leitura, manipulação e aplicação de filtros em imagens.
- **Multiprocessing:** módulo nativo do Python utilizado para distribuir tarefas entre múltiplos processos.
- **Git e GitHub:** ferramentas utilizadas para versionamento e publicação do código.

## 3. Estrutura do projeto

```text
atividade_paralela/
├── entrada/
│   └── imagens de entrada
├── saída/
│   └── imagens processadas
├── filtro_paralelo.py
└── README.md
```

A pasta `entrada` contém as imagens que serão processadas. A pasta `saída` é destinada às imagens resultantes do processamento.

## 4. Requisitos

Para executar o projeto, é necessário ter:

- Python 3 instalado.
- Biblioteca Pillow instalada.
- Imagens de entrada disponíveis na pasta `entrada`.

## 5. Como executar

### Passo 1 — Baixar o projeto

Clone o repositório:

```bash
git clone https://github.com/erikjeronimo/atividade_paralela.git
```

Entre na pasta do projeto:

```bash
cd atividade_paralela
```

### Passo 2 — Instalar a biblioteca Pillow

No terminal, execute:

```bash
py -m pip install Pillow
```

### Passo 3 — Preparar as imagens

Coloque as imagens que deseja processar na pasta `entrada`, seguindo a estrutura do projeto.

### Passo 4 — Executar o programa

Execute o seguinte comando:

```bash
py filtro_paralelo.py
```

O programa realizará o processamento sequencial e, em seguida, o processamento paralelo.

Ao final, serão apresentados no terminal os tempos de execução e o ganho de desempenho obtido.

## 6. Resultados obtidos

O teste foi realizado com 30 imagens, utilizando 12 núcleos da CPU na execução paralela.

| Modo de execução | Tempo |
|---|---:|
| Sequencial — 1 núcleo | 35,60 segundos |
| Paralelo — 12 núcleos | 13,91 segundos |

**Speedup obtido: 2,56×**

Neste teste, a execução paralela foi aproximadamente 2,56 vezes mais rápida que a execução sequencial.

O speedup foi calculado pela divisão do tempo sequencial pelo tempo paralelo.

## 7. Conceito de programação paralela

A programação paralela permite dividir uma tarefa em partes que podem ser executadas simultaneamente por diferentes núcleos do processador.

Neste projeto, cada imagem é enviada para processamento por meio do módulo `multiprocessing`, utilizando um conjunto de processos gerenciado por `Pool`.

Dessa forma, várias imagens podem ser processadas ao mesmo tempo, reduzindo o tempo total de execução em comparação com o processamento sequencial.

## 8. Autor

**Aluno:** ERIK JERONIMO 

