# Prompt Improver - Guia de Uso

## 🚀 Como Usar

### Uso 1: Melhorar Prompt Simples

**Você pede:**
```
@prompt-improver Analise e melhore este prompt para meu bot de cupons:

"Você é um bot que mostra cupons e códigos desconto. 
Se o usuário pedir cupom, mostre cupons válidos.
Se não tiver cupom, diga que não tem."
```

**Skill Responde:**

```markdown
## 📊 ANÁLISE DO PROMPT ORIGINAL
- Clareza: 4/10 ❌ Muito vaga
- Especificidade: 2/10 ❌ Falta estrutura
- Bot Compatibility: ⚠️ Sem formatação
- Principais Issues:
  - Sem estrutura de resposta
  - Sem tratamento de erros
  - Sem limites de caracteres
  - Sem emojis/formatação

## 🎯 RECOMENDAÇÕES

1. **Adicionar Persona Clara**
   "Seu Objetivo: Ajudar usuários a encontrar cupons válidos"

2. **Estruturar Regras**
   Use listas numeradas com ✅/❌

3. **Definir Formato**
   JSON ou markdown estruturado

4. **Adicionar Constraints**
   Telegram: max 4096 caracteres

## ✨ PROMPT MELHORADO

Você é um **Bot de Cupons OfertaChina** especializado em encontrar códigos de desconto.

### Seu Objetivo:
- Buscar cupons válidos e ativos
- Mostrar desconto exato (% ou valor)
- Indicar validade e requisitos
- Ajudar usuários a economizar

### Regras Rigorosas:
✅ Apenas cupons verificados
✅ Mostrar data de expiração
✅ Indicar compra mínima
✅ Diferenciar novo/refill
❌ Nunca compartilhe cupons expirados
❌ Nunca prometa descontos falsos

### Formato de Resposta:
\`\`\`
🎟️ [CÓDIGO_CUPOM]
Desconto: [VALOR] (% ou R$)
Validade: [DATA_EXPIRAÇÃO]
Compra Mín: [R$]
Tipo: [Novo/Refill/Ambos]
Categoria: [Categoria]

[📋 Copiar Código] [🔗 Link Direto] [📱 Compartilhar]
\`\`\`

### Tratamento de Erros:
- "Cupom não encontrado. Tente: [sugestões]"
- "Cupom expirou em [data]. Tente outros: [lista]"
- "Sem cupons no momento. Volte amanhã!"

---

**Melhoria Esperada:** +6 pontos de clareza, estrutura profissional, melhor UX
```

---

### Uso 2: Otimizar para Plataforma

```
@prompt-improver Otimize este prompt para WhatsApp Bot (WAHA):

"Bot que faz busca de produtos e mostra resultados."
```

**Skill Responde:**

```markdown
## 🔄 OTIMIZAÇÃO PARA WHATSAPP (WAHA)

### Considerações WAHA vs Telegram:
❌ Sem inline keyboards (Telegram)
✅ Usa template messages
✅ Buttons (máx 3 por mensagem)
⚠️ Markdown limitado

### Prompt Otimizado:

Você é um Bot de Produtos para WhatsApp (WAHA).

**Restrições WhatsApp:**
- Max 4096 caracteres (igual Telegram, mas raramente atingido)
- Sem markdown complexo (apenas *negrito* e _itálico_)
- Máximo 3 botões por mensagem
- Templates para notificações em massa
- Sem inline keyboards (use buttons em lista)

**Formato de Resposta:**
Mensagem principal (até 1000 caracteres)
[Botão 1] [Botão 2] [Botão 3]

**Exemplo:**
*Produto encontrado!*
_iPhone 14_ 
Preço: ¥3.999 → R$1.999

[👁️ Ver Detalhes]
[💚 Favoritar]
[👥 Compartilhar]
```

---

## 📋 Tipos de Melhorias Disponíveis

| Tipo | Comando | Output |
|------|---------|--------|
| **Geral** | `@prompt-improver Melhore...` | Análise completa + versão melhorada |
| **Platform** | `@prompt-improver Otimize para [Telegram/WhatsApp]` | Adaptado para plataforma |
| **Flow Design** | `@prompt-improver Desenhe fluxo conversacional` | Estrutura multi-turno |
| **API Prep** | `@prompt-improver Prepare para API [Gemini/GPT]` | JSON schema + exemplos |
| **Audit** | `@prompt-improver Audite este prompt` | Checklist de qualidade |

---

## 🎯 Casos de Uso Comuns

### 1. Bot de Produtos
```
@prompt-improver Melhore este prompt para bot de produtos:
[seu prompt aqui]

Contexto adicional:
- Plataforma: Telegram
- Usuários: 50k/mês
- Resposta: Max 300 palavras
```

### 2. Bot de Suporte
```
@prompt-improver Desenhe fluxo conversacional para bot de suporte

Requisitos:
- Categorizar problema
- Esclarecer tipo de pedido
- Fornecer solução ou escalar
```

### 3. Prompt para API
```
@prompt-improver Prepare prompt para integração com Gemini

Tarefa: Análise de produtos chineses
Entrada: JSON com dados do produto
Saída: Recomendação + análise detalhada
```

### 4. Validação de Qualidade
```
@prompt-improver Audite qualidade deste prompt:
[prompt atual]

Critérios:
- Clareza
- Compatibilidade Telegram
- Tratamento de erros
```

---

## ⚡ Dicas Rápidas

### ✅ BOM
```
"Máximo 300 palavras, sempre use markdown, formato JSON"
```

### ❌ RUIM
```
"Responda bem, use formatação, seja profissional"
```

---

### ✅ BOM (Exemplo)
```
Para cada produto, responda:
{
  "nome": "string",
  "preco": "number",
  "link": "url"
}
```

### ❌ RUIM
```
"Mostre produto e preço e link"
```

---

## 🔗 Integração com outras Skills

### Com Frontend Analyzer
```
1. Frontend Analyzer extrai cores/fontes
2. Prompt Improver otimiza instruções de UI
3. Resultado: Bot responde com UI tokens corretos
```

### Com Telegram UI Design
```
1. Telegram UI desenha keyboard
2. Prompt Improver escreve instruções
3. Resultado: Bot implementa UI corretamente
```

---

## 📊 Métricas de Melhoria

```markdown
## Antes vs Depois

### Prompt Original: "Bot de produtos"
- Clareza: 2/10
- Tokens (est.): 450
- Taxa erro: ~40%

### Prompt Melhorado
- Clareza: 9/10 (+350%)
- Tokens (est.): 600 (+33%)
- Taxa erro: ~5% (-87.5%)

**Benefício:** Mais clareza com custo aceitável de tokens
```

---

## 🚫 Anti-Patterns (Evite!)

| Anti-Pattern | Problema | Solução |
|--------------|----------|---------|
| "Seja criativo" | Impreciso, respostas inconsistentes | "Responda com exatamente..." |
| "Use emojis" | Bot não sabe quando usar | "Use 1 emoji por linha: 🎯" |
| "Seja profissional" | Significado ambíguo | "Tom: formal, respeitoso, conciso" |
| "Responda tudo" | Respostas muito longas | "Máximo [N] palavras" |

---

## 💬 Chat Patterns

### Padrão 1: Análise + Melhoria (Mais comum)
```
Você: "Melhore este prompt: [X]"
Skill: [Análise + Melhorias + Versão Nova]
Você: "Use mais emojis"
Skill: [Versão atualizada com mais emojis]
```

### Padrão 2: Design de Fluxo
```
Você: "Desenhe fluxo conversacional para..."
Skill: [Diagrama ASCII + Prompts para cada turno]
Você: "Adicione filtros de preço"
Skill: [Fluxo atualizado com nova branch]
```

### Padrão 3: Validação Iterativa
```
Você: "Audite este prompt"
Skill: [Análise de 10 critérios]
Você: "Corrija os 3 issues críticos"
Skill: [Versão corrigida]
Você: "Pronto?"
Skill: "✅ Pronto para produção!"
```

---

## 🎓 Template para Seus Próprios Prompts

Copie este template e preencha:

```
### 🤖 Seu Robô [Nome]

**Seu Objetivo:**
- [Objetivo 1]
- [Objetivo 2]

**Seu Público:**
[Descrever usuários]

**Constraints:**
✅ [Rule 1]
✅ [Rule 2]
❌ [Never 1]
❌ [Never 2]

**Formato de Resposta:**
[Estrutura esperada: JSON, markdown, etc]

**Exemplos:**
[1-2 exemplos de entrada/saída]

**Tratamento de Erros:**
- Caso 1: [Resposta]
- Caso 2: [Resposta]
```

---

**Próximos Passos:**
1. Escolha um prompt seu
2. Passe para @prompt-improver
3. Itere até ficar satisfeito
4. Use em produção
5. Colete feedback de usuários

---

**Última atualização:** 19 de dezembro de 2025  
**Status:** ✅ Production Ready
