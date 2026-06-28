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

---

## Validador CPF

Um sistema desenvolvido para tratar, limpar e validar strings de CPF informadas pelo usuário. O projeto foca em garantir a integridade dos dados antes de qualquer processamento posterior.

### Conceitos Aplicados e Aprendizados

* **Expressões Regulares (Biblioteca `re`):** Utilização de máscaras de Regex para higienizar a entrada de dados, removendo pontuações (`.`, `,`, `-`) e caracteres indesejados de forma eficiente.
* **Composição de Funções (Dupla Verificação):** Arquitetura de código baseada em responsabilidade única, onde uma função é encarregada de limpar e garantir a tipagem dos dados (`validar_numero`) para só então acionar a função especialista em regras de negócio (`validar_cpf`).
* **Tratamento de Exceções (`try/except`):** Captura ativa de erros de conversão (`ValueError`), impedindo o travamento da aplicação caso dados alfabéticos sejam inseridos.

---

## Contagem de Vogais

Um programa focado em manipulação de strings que analisa um texto fornecido pelo usuário, identificando e contabilizando a quantidade total de vogais presentes.

### Conceitos Aplicados e Aprendizados

* **Operadores de Associação (`in`):** Uso do operador `in` combinado com estruturas condicionais (`if`) para verificar a existência de caracteres de forma direta dentro de uma coleção de vogais.
* **Manipulação de Strings (`.lower()`):** Aplicação de métodos de padronização de texto para converter a entrada do usuário em letras minúsculas, garantindo a precisão da contagem independente da formatação original.
* **Otimização de Estruturas:** Compreensão sobre a diferença de performance ao buscar elementos dentro de sequências, evoluindo o uso de listas (`list`) para conjuntos (`set`) buscando maior eficiência.

---

## Filtro de Palavras Longas

Um script desenvolvido para analisar strings e extrair palavras complexas (com 10 ou mais caracteres). É um excelente exemplo de como realizar processos de tokenização e filtragem de textos.

### Conceitos Aplicados e Aprendizados

* **Manipulação de Listas (`.append()`):** Utilização de estruturas de repetição (`for`) para varrer coleções e isolar dados específicos dentro de uma nova lista dinâmica.
* **Higienização de Strings (Tokenização):** Divisão de strings em blocos de palavras (`.split()`) combinada com substituição de caracteres para evitar que pontuações interfiram na contagem de caracteres.
* **Saída de Dados Formatada:** Uso do operador de desempacotamento (`*`) junto ao parâmetro `sep` no método `print` para exibir listas de forma limpa e legível no terminal.

---

## Gerador de Senhas Aleatórias

Um script desenvolvido para automatizar a criação de senhas fortes e aleatórias, combinando letras (maiúsculas e minúsculas), dígitos numéricos e caracteres especiais.

### Conceitos Aplicados e Aprendizados

* **Mapeamento de Caracteres (Biblioteca `string`):** Uso de constantes nativas do Python para criar um banco completo e seguro de caracteres sem a necessidade de digitação manual de arrays.
* **Seleção Aleatória Multipla (`random.choices`):** Aplicação de amostragem aleatória com reposição para selecionar múltiplos elementos de forma simultânea com base em um tamanho predefinido.
* **Conversão de Dados (`.join()`):** Conversão eficiente de uma estrutura de lista (`list`) de caracteres para uma string unificada e pronta para exibição.