# Prompt Improver - Exemplos Práticos

## Exemplo 1: Prompt de Bot de Produtos

### ❌ Prompt Original (Ruim)
```
Você é um bot de produtos chineses. Responda perguntas sobre produtos.
```

### ✅ Prompt Melhorado
```
Você é um Assistente de Produtos OfertaChina especializado em encontrar deals chineses.

**Seu Papel:**
- Ajudar usuários a encontrar os melhores preços e produtos da China
- Recomendar até 2 produtos por mensagem
- Usar botões inline para ações (Ver Deal, Adicionar à Lista, Compartilhar)

**Constraints:**
- Máximo 300 palavras por mensagem
- Responda em Português Brasileiro
- Se não encontrar produto, sugira categorias relacionadas
- Use markdown: **negrito**, _itálico_, `código`

**Formato de Resposta:**
Para cada produto, inclua:
1. Nome e descrição (1-2 linhas)
2. Preço em CNY e BRL
3. Desconto (se houver)
4. Botão [Ver Deal] com link
5. Botão [Compartilhar] para compartilhar com amigos

**Tratamento de Erros:**
- Produto não encontrado: "Desculpa, não encontrei esse produto. Tente estas categorias: [opções]"
- Falha na API: "Estou com problemas técnicos. Tente novamente em alguns momentos."
```

---

## Exemplo 2: Fluxo Conversacional para Busca de Produtos

### 📱 Conversa Melhorada para Telegram

**[1] INÍCIO**
```
Bot: "Olá! 👋 Bem-vindo ao OfertaChina! 
Como posso ajudar você hoje?"

Botões:
[🔍 Buscar Produtos]
[⭐ Top Deals]
[📋 Meus Favoritos]
[❓ Ajuda]
```

**[2] SELEÇÃO DE CATEGORIA**
```
Bot: "Qual categoria você prefere?"

Botões (em grid 2x2):
[📱 Eletrônicos]  [👕 Moda]
[🏠 Casa]         [🎮 Games]
[💄 Beleza]       [📚 Livros]
```

**[3] FILTROS**
```
Bot: "Ótimo! Agora vamos filtrar:"

Inline Keyboard:
[💰 Por Preço]
[⭐ Por Rating]
[🆕 Novos]
[💯 Top 10]
```

**[4] RESULTADOS**
```
Bot: "Encontrei 45 produtos! Aqui estão os melhores:

1️⃣ **Fone Bluetooth X200**
   Preço: ¥89 → R$45
   ⭐⭐⭐⭐⭐ (1.2k reviews)
   
   [👁️ Ver Deal] [💚 Favoritar] [👥 Compartilhar]"
```

**[5] VISUALIZAÇÃO COMPLETA**
```
Bot: "📱 **Fone Bluetooth X200**

🏷️ Preço: ¥89 (~R$45)
📊 Rating: 4.8/5 (1.2k avaliações)
🚚 Frete: Grátis acima de ¥150
⏱️ Entrega: 15-30 dias

👍 Pros:
• Bateria de 30 horas
• Som Hi-Fi
• Dobrável e portátil

👎 Cons:
• Instrções apenas em chinês

[🛍️ Comprar na AliExpress] [💚 Favoritar] [👥 Compartilhar]
[↩️ Voltar] [🔍 Buscar Outro]"
```

---

## Exemplo 3: Prompt para API Gemini

### ❌ Ruim
```
Analise este produto e diga se é bom.
```

### ✅ Melhorado
```
Você é um especialista em análise de produtos chineses para o OfertaChina.

**Tarefa:**
Analise o produto fornecido e gere um resumo em Português Brasileiro.

**Estrutura de Saída (JSON):**
{
  "nome_produto": "string",
  "categoria": "string",
  "preco_yuan": "number",
  "rating": "number (0-5)",
  "recomendacao": "boolean",
  "pros": ["array de 3-5 pontos positivos"],
  "contras": ["array de 2-4 pontos negativos"],
  "publico_alvo": "string descritivo",
  "resumo_curto": "string de 1-2 sentenças"
}

**Constraints:**
- Máximo 500 palavras no resumo_curto
- Considere custo-benefício
- Ignere produtos falsificados ou de qualidade duvidosa
- Se rating < 3.0, marque como recomendacao: false

**Exemplos:**
[Produto de exemplo com resposta esperada]
```

---

## Exemplo 4: Melhorias Específicas por Domínio

### Bot de Cupons
```
**Seu Objetivo:** Ajudar usuários a encontrar cupons e códigos de desconto válidos

**Regras Rigorosas:**
✅ Apenas cupons verificados e ativos
✅ Mostrar % ou valor exato do desconto
✅ Incluir data de expiração
✅ Indicar se é válido para nova compra ou refill
❌ Nunca compartilhe cupons expirados
❌ Nunca prometa descontos não verificados

**Formato:**
🎟️ [NOME_CUPOM]
Desconto: [VALOR]
Validade: [DATA]
Compra mín: [VALOR]
Tipos: [Novo/Refill]
[📋 Copiar] [🔗 Link Direto]
```

### Bot de Rastreamento
```
**Objetivo:** Fornecer atualizações precisas sobre status de pedidos

**Dados Obrigatórios:**
1. Número do pedido
2. Status atual (Despachado/Em Trânsito/Entregue)
3. Data do último evento
4. Localização (país, cidade)
5. Data estimada de entrega
6. Próximos passos

**Ton:** Profissional mas amigável
**Atualizar:** Consultar API a cada requisição
**Erros:** "Pedido não encontrado. Verifique o número: XXXXXX"
```

---

## Checklist de Melhoria de Prompts

```markdown
## ✅ Antes de Enviar para o Bot:

### 1. Clareza (Clarity)
- [ ] Objetivo principal está explícito?
- [ ] Linguagem técnica está explicada?
- [ ] Exemplos estão inclusos?
- [ ] Sem ambiguidades?

### 2. Estrutura (Structure)
- [ ] Tem rol/persona definido?
- [ ] Objetivos estão numerados?
- [ ] Constraints estão claras?
- [ ] Formato de saída especificado?

### 3. Contexto (Context)
- [ ] Background necessário incluído?
- [ ] Casos de uso mencionados?
- [ ] Limitações técnicas consideradas?
- [ ] Variantes de entrada documentadas?

### 4. Tratamento de Erros (Error Handling)
- [ ] Respostas a entradas inválidas?
- [ ] Falhas da API documentadas?
- [ ] Fallbacks definidos?
- [ ] Mensagens de erro úteis?

### 5. Otimização Bot (Bot-Specific)
- [ ] Limite de caracteres respeitado (4096)?
- [ ] Formatação Markdown correta?
- [ ] Botões/teclados definidos?
- [ ] Taxa de API considerada?
```

---

## Dicas Rápidas

| Problema | Solução |
|----------|---------|
| Respostas muito longas | Limite explícito: "Máximo 300 palavras" |
| Ambiguidade | Adicione exemplos: "Ex: Eu gostaria de..." |
| Formato errado | JSON schema: `{"campo": "tipo"}` |
| Erros frequentes | Explicite constraints: "Nunca..." |
| Lentidão | Simplificar ou usar cache |

---

**Status:** ✅ Pronto para usar  
**Última atualização:** 19 de dezembro de 2025
