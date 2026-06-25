# Projetos em Python 

Este repositório centraliza meus projetos de estudos práticos desenvolvidos em Python. O principal objetivo aqui é consolidar conceitos essenciais de programação e construir uma base sólida para a transição para a área de dados.

## Objetivos Principais

* **Lógica de Programação:** Estruturação de algoritmos eficientes e limpos.
* **Domínio da Linguagem:** Aprofundamento na sintaxe e nos recursos nativos do Python.
* **Pensamento Computacional:** Decomposição de problemas complexos em etapas menores e resolvíveis.
* **Resolução de Problemas:** Criação de soluções automatizadas para desafios do dia a dia.

---
# Portfólio de Projetos

## Gorjetas de Restaurantes

Uma ferramenta interativa desenvolvida para facilitar o cálculo do valor total de uma conta de restaurante. O programa recebe o valor total bruto e calcula o valor final a ser pago com base na porcentagem de gorjeta escolhida pelo usuário.

### Conceitos Aplicados e Aprendizados

* **Funções (`def`):** Modularização do código para garantir que cada bloco tenha uma única responsabilidade.
* **Tratamento de Erros (`try/except`):** Implementação de travas de segurança para evitar que o programa quebre caso o usuário digite um texto no lugar de números.
* **Automação do Sistema (Biblioteca `os`):** Uso do módulo nativo `os` para limpar o terminal a cada tela, melhorando consideravelmente a experiência e a navegação do usuário.

## Validador CPF

Um sistema desenvolvido para tratar, limpar e validar strings de CPF informadas pelo usuário. O projeto foca em garantir a integridade dos dados antes de qualquer processamento posterior.

### Conceitos Aplicados e Aprendizados

* **Expressões Regulares (Biblioteca `re`):** Utilização de máscaras de Regex para higienizar a entrada de dados, removendo pontuações (`.`, `,`, `-`) e caracteres indesejados de forma eficiente.
* **Composição de Funções (Dupla Verificação):** Arquitetura de código baseada em responsabilidade única, onde uma função é encarregada de limpar e garantir a tipagem dos dados (`validar_numero`) para só então acionar a função especialista em regras de negócio (`validar_cpf`).
* **Tratamento de Exceções (`try/except`):** Captura ativa de erros de conversão (`ValueError`), impedindo o travamento da aplicação caso dados alfabéticos sejam inseridos.
