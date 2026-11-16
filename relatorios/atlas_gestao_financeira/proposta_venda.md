# Proposta Comercial
## Soluções de Automação e Inteligência Artificial

**Apresentada por:** IdeiaFlui  
**Destinatário:** Atlas Gestão — BPO Financeiro, Controladoria e Processos para PMEs

---

## 1. Apresentação

A **IdeiaFlui** é um estúdio especializado em Inteligência Artificial, automação de processos, criação digital e inteligência de dados. Nosso objetivo é transformar rotinas operacionais manuais em fluxos eficientes e automatizados, permitindo que empresas de alto desempenho escalem suas entregas sem aumentar a carga de trabalho braçal.

Com base na análise do relatório gerencial da **Atlas Gestão**, identificamos gargalos operacionais relevantes na execução de tarefas repetitivas de conciliação e processamento de dados, além de oportunidades para impulsionar a aquisição de clientes. 

Esta proposta apresenta um plano de atuação focado na implementação de tecnologia de automação para otimizar a operação da Atlas Gestão, posicionando nossa empresa como sua parceira tecnológica estratégica.

---

## 2. Diagnóstico e oportunidades identificadas

O relatório gerencial aponta que a rotina operacional consome **20h 00min / semana** (equivalente a 80 horas por mês) da equipe em tarefas manuais, repetitivas e propensas a falhas. 

Abaixo detalhamos as principais oportunidades operacionais mapeadas:

| Ordem de Impacto | Gargalo Operacional Mapeado | Natureza do Problema | Impacto Identificado |
| :---: | :--- | :--- | :--- |
| **1º (Maior Impacto)** | Conciliação Bancária Manual e Batimento do Extrato com Títulos Fiscais | Manual & Propensa a erro | Consumo de **5h 00min / semana**. Risco de erros no Simples Nacional e atrasos no Fluxo de Caixa. |
| **2º** | Conferência Manual de Retenções Fiscais (IRRF, PCC, ISS) em XML/PDF | Manual & Propensa a erro | Consumo de **4h 30min / semana**. Risco de pagamentos incorretos de guias fiscais e multas. |
| **3º** | Captura, Download e Organização Manual de XMLs, PDFs e Scans Fiscais | Manual & Repetitiva | Consumo de **3h 30min / semana**. Varredura manual em e-mails e portais de prefeituras. |
| **4º** | Consolidação Manual de Planilhas de Fluxo de Caixa e DRE Gerencial | Manual & Repetitiva | Consumo de **2h 30min / semana**. Risco de quebra de fórmulas e perda de dados históricos. |
| **5º** | Follow-up Manual para Roteamento de Aprovações | Repetitiva & Manual | Consumo de **2h 30min / semana**. Gargalos no Contas a Pagar e risco de perda de vencimentos. |
| **6º** | Triagem e Checagem Manual de Duplicidade de Documentos | Repetitiva & Propensa a erro | Consumo de **2h 00min / semana**. Risco residual de agendamentos em duplicidade. |

Além do impacto operacional interno, identificou-se no relatório a necessidade de estruturação de materiais de comunicação e páginas de conversão para alavancar a estratégia comercial de captação de clientes BPO.

---

## 3. Soluções propostas pela IdeiaFlui

Para maximizar o retorno operacional imediato, a IdeiaFlui estabeleceu **UM fluxo prioritário de maior impacto** para o escopo principal desta proposta.

### Fluxo Prioritário Selecionado: Automação da Conciliação e Entrada de Dados Financeiros
* **Solução:** **Operação Automatizada em 15 Dias (Dados, Planilhas & Automação n8n)**
* **Descrição:** Estruturação de uma esteira automatizada utilizando o n8n e Google Sheets para substituir a digitação manual e a checagem linha a linha de extratos e títulos. O fluxo captura os dados de entrada, executa as validações necessárias, popula a planilha gerencial e dispara notificações e alertas automáticos sobre inconsistências ou atualizações de saldo.

---

### Etapas futuras (fora deste escopo)
Os demais processos e oportunidades identificados no diagnóstico poderão ser contratados em etapas subsequentes mediante novas propostas comerciais:
1. **Automação da Captura e Triagem de XMLs/PDFs Fiscais:** Automação para varredura de documentos fiscais e checagem de retenções.
2. **Máquina de Aquisição (Página de Vendas + Lote Editorial):** Estruturação da Landing Page de alta conversão para captação de leads qualificados (conforme o briefing comercial do relatório) e produção de 30 dias de conteúdos estratégicos (carrosséis, reels e posts) para redes sociais.

---

## 4. Escopo e entregáveis

### Pacote Recomendado: Operação Automatizada em 15 Dias (Dados, Planilhas & Automação n8n)

#### Escopo incluso:
- Diagnóstico de 1 processo crítico (Fluxo de Conciliação Bancária e Entrada de Dados);
- Planilha base no Google Sheets com até 4 abas;
- 1 fluxo no n8n: entrada, validação, planilha, notificação;
- Alertas por e-mail, Telegram ou WhatsApp;
- Painel com até 6 KPIs;
- Até 3 regras de alerta;
- 1 modelo de relatório mensal;
- Documentação, export do fluxo e 1h de treinamento;
- 30 dias de suporte.

#### Fora do escopo:
- ERP legado sem API documentada;
- Mais de 1 fluxo principal;
- Custos de VPS e de APIs de mensageria.

#### Premissas:
- Dicionário de dados e KPIs aprovados previamente pela cliente (1 rodada de validação).
- Execução em VPS própria da cliente (ex.: cerca de R$ 30/mês) ou n8n Cloud, com esses custos pagos pela cliente.
- Integrações dependem de API pública documentada; ERP proprietário legado sem API fica fora do escopo.

---

## 5. Metodologia de implementação

A IdeiaFlui adota um processo estruturado em 4 etapas para garantir agilidade e aderência técnica:

1. **Diagnóstico & Entendimento**  
   Mapeamos o gargalo, os objetivos de negócio e o contexto operacional.
2. **Estratégia & Arquitetura**  
   Desenhamos a esteira da solução, escolhendo as ferramentas mais adequadas.
3. **Desenvolvimento & Testes**  
   Construímos, iteramos e validamos fluxos e interfaces sob critérios de qualidade.
4. **Entrega & Operação**  
   Entregamos a solução validada, documentada e pronta para uso na rotina.

---

## 6. Benefícios esperados

* **Redução de Trabalho Manual:** Eliminação do trabalho braçal de digitação e cruzamento linha a linha no fluxo prioritário de conciliação.
* **Mitigação de Erros:** Redução de falhas humanas na transferência de dados para a planilha gerencial.
* **Agilidade na Informação:** Disponibilização rápida de dados financeiros para tomada de decisão e acompanhamento de caixa.
* **Notificações em Tempo Real:** Recebimento de alertas automáticos via WhatsApp, Telegram ou e-mail sobre inconsistências e indicadores.
* **Liberdade Operacional:** Liberação de tempo da equipe técnica para atuação consultiva e estratégica de controladoria.

---

## 7. Investimento e condições comerciais

### Valor do Investimento
* **Pacote Operação Automatizada em 15 Dias:** R$ 2.990
* **Prazo de Execução:** 15 dias úteis, a contar do recebimento de acessos e dados.

### Condições de Pagamento
* **Forma de Pagamento:** PIX 50/50 (50% de entrada e 50% na aprovação da entrega) ou até 3x sem juros no cartão de crédito.

### Garantias
* **Garantia de escopo:** qualquer item acordado e não entregue é concluído sem custo adicional.
* **Propriedade intelectual:** código, domínio, artes em PNG e fluxos JSON pertencem ao cliente no encerramento.

---

## 8. Próximos passos

Para dar início à implantação do fluxo automatizado, convidamos a equipe da Atlas Gestão para uma reunião de alinhamento técnico e validação dos acessos.

**Canais de Contato:**
* **E-mail:** atendimento@ideiaflui.com.br
* **WhatsApp:** 48991633122

---

## 9. Considerações finais

A IdeiaFlui reafirma seu compromisso em atuar como parceira tecnológica estratégica da Atlas Gestão. Acreditamos que a automação dos processos operacionais repetitivos é o passo fundamental para permitir que sua empresa escala suas operações de BPO e Controladoria com máxima eficiência e precisão.

Ficamos à disposição para esclarecer dúvidas e iniciar o projeto.

**IdeiaFlui**  
*Estúdio de Inteligência Artificial, Automação e Dados*  
ideiaflui.com.br