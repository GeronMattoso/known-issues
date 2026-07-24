# EST-002 - Falha no StackSpot Code Review da esteira

## Categoria

Esteira / StackSpot / GitHub

## Ambiente

Desenvolvimento

## Sistema afetado

Pipeline de CI/CD

## Sintoma

A etapa de StackSpot Code Review falha durante a execução da esteira e não permite remover arquivos da pasta `.github` do projeto.

## Mensagem de erro

```text
Code Review step failed
Unable to delete files from repository
```

## Causa

A etapa de validação interfere com arquivos gerenciados pelo fluxo do GitHub.

## Solução

Alterar diretamente o Git Flow da pipeline e desabilitar temporariamente a etapa de StackSpot Code Review.

## Workaround

Executar a esteira sem a etapa de validação.

## Tags

- stackspot
- github
- pipeline
- git-flow

## Responsável

Time de Desenvolvimento

## Data

2026-07-24
