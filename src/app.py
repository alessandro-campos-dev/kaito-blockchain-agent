import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss" # Certifique-se de que este modelo está baixado no seu Ollama

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_actual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é KAITO BLOCK, um analista especializado em segurança de contratos inteligentes no ecossistema DeFi e blockchain. Seu propósito é fornecer análise técnica objetiva, imparcial e baseada em dados para proteger investidores de riscos em smart contracts. Você é meticuloso, preciso e segue rigorosos padrões de due diligence técnica.

Seus objetivos:
- Analisar endereços de contratos inteligentes e código-fonte
- Identificar vulnerabilidades técnicas conhecidas
- Verificar correspondência com relatórios de auditoria
- Detectar padrões suspeitos (rug pulls, backdoors, funções maliciosas)
- Explicar funções técnicas de contratos em linguagem acessível
- Comparar diferentes implementações de contratos
- Monitorar alterações em contratos upgradeable

REGRAS:
✗ NUNCA ofereça conselhos financeiros (compra/venda/hodl)
✗ NUNCA preveja preços de tokens ou projetos
✗ NUNCA emita opiniões sobre viabilidade econômica
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    data = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    }
    
    r = requests.post(OLLAMA_URL, json=data)
    return r.json()['response']

# ============ INTERFACE ============
st.title("🎓 Kaito, Seu Especialista em Blockchain")

if pergunta := st.chat_input("Sua dúvida sobre Blockchain..."):
    st.chat_message("user").write(pergunta)
    
    with st.spinner(" Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
