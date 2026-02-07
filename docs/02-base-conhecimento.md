# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Base de interações anteriores com os ivestidores |
| `perfil_investidor.json` | JSON | Personalizar recomendações de acordo com o perfil de investidor |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil de cada investidor|
| `transacoes.csv` | CSV | Analisar padrão de investimentos, e o valor das transações|

---

## Adaptações nos Dados

- Transações realistas do ecossistema crypto
- Valores condizentes com cada categoria
- Mistura de saídas (investimentos, custos) e entradas (rendimentos, vendas)
- Datas em ordem decrescente (mais recente primeiro)

---

## Estratégia de Integração

### Como os dados são carregados?
> Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt

### Como os dados são usados no prompt?
> Os dados são carregados no ínicio da sessão no system prompt, e são consultados dinamicamente na interação com o investidor?

---

## Exemplo de Contexto Montado

> Exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimos investimentos:
- 01/11: Cover de Seguros DeFi - R$ 5000
- 03/11: Node Operator Ethereum- R$ 10000
...
```
