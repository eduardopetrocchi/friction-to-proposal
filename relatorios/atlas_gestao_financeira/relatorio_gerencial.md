# Atlas Gestão Financeira | Inteligência Financeira e Controladoria
**Relatório Executivo Consolidado & Fechamento Gerencial**  
*Cliente Analisado:* **TechServices LTDA (DADOS SIMULADOS - PME do Setor de Serviços)**  
*Responsável:* Especialista de Controle Financeiro (Atlas Gestão Financeira)

---

## 1. DRE Gerencial Resumido

> *Período: Fechamento Mensal Competência Atual*

| Rubrica DRE Gerencial | Valor (R$) | % da Receita Líquida |
| :--- | :---: | :---: |
| **Receita Bruta de Vendas/Serviços** | **R$ 150.000,00** | -- |
| (-) Deduções e Impostos Incidentes (Simples Nacional - 8%) | (R$ 12.000,00) | -- |
| **(=) Receita Líquida** | **R$ 138.000,00** | **100,00%** |
| (-) Custos Variáveis (Insumos/Terceirizados/Comissões) | (R$ 45.000,00) | 32,61% |
| **(=) MARGEM DE CONTRIBUIÇÃO** | **R$ 93.000,00** | **67,39%** |
| (-) Despesas Fixas (Folha de Pagamento, Aluguel, BPO, Softwares) | (R$ 62.000,00) | 44,93% |
| **(=) EBITDA Gerencial (Lucro Operacional)** | **R$ 31.000,00** | **22,46%** |
| (-/+) Resultado Financeiro (Taxas bancárias, juros, tarifas) | (R$ 3.000,00) | 2,17% |
| **(=) LUCRO LÍQUIDO GERENCIAL** | **R$ 28.000,00** | **20,29%** |

---

## 2. Indicadores Financeiros Calculados

* **PMR / DSO (Prazo Médio de Recebimento):** **45 dias**
  * *Análise:* Concessão de prazos faturados longos aos tomadores de serviço.
* **PMP / DPO (Prazo Médio de Pagamento aos Fornecedores):** **30 dias**
  * *Ciclo Financeiro:* **+15 dias** (PMR - PMP). A empresa financia 15 dias de operação antes de receber pelas vendas.
* **Margem de Contribuição (%):** **67,39%** (R$ 93.000,00)
  * *Análise:* Margem robusta para absorção dos custos fixos.
* **Ponto de Equilíbrio Operacional (Break-even Point):**
  * *Fórmula:* $\text{Custos e Despesas Fixas} \div \text{\% Margem de Contribuição}$
  * $\text{PE} = \text{R\$ 62.000,00} \div 0,6739 = \mathbf{R\$ 91.999,55}$ em **Receita Líquida** *(equivalente a ~R$ 100.000,00 em Receita Bruta)*.
  * *Análise:* A operação gera lucro a partir de R$ 100 mil faturados. O faturamento atual de R$ 150 mil supera o ponto de equilíbrio em 50%.

---

## 3. Projeção de Fluxo de Caixa (30 / 60 / 90 Dias)

> *Premissa: Saldo Inicial de Caixa Conciliado = R$ 25.000,00*

| Visão Projetada | D30 (Mês 1) | D60 (Mês 2) | D90 (Mês 3) |
| :--- | :---: | :---: | :---: |
| **Saldo Inicial** | **R$ 25.000,00** | **R$ 50.000,00** | **R$ 52.000,00** |
| (+) Entradas de Caixa Projeção (Recebimentos) | R$ 135.000,00 | R$ 120.000,00 | R$ 140.000,00 |
| (-) Saídas Fixas Projeção (Folha, Aluguel, BPO) | (R$ 62.000,00) | (R$ 62.000,00) | (R$ 62.000,00) |
| (-) Saídas Variáveis & Fornecedores | (R$ 45.000,00) | (R$ 53.000,00) | (R$ 48.000,00) |
| (-) Despesas Financeiras & Impostos (DAS) | (R$ 3.000,00) | (R$ 3.000,00) | (R$ 15.000,00)* |
| **(=) Fluxo Líquido do Período** | **+ R$ 25.000,00** | **+ R$ 2.000,00** | **+ R$ 15.000,00** |
| **(=) SALDO FINAL ACUMULADO** | **R$ 50.000,00** | **R$ 52.000,00** | **R$ 67.000,00** |

*\*Nota D90: Inclui provisão de parcela de ajuste fiscal/13º salário e oscilação sazonal de tributos.*

---

## 4. Riscos de Liquidez & Plano de Ação

### ⚠️ 3 Riscos de Liquidez Identificados
1. **Desperdício de Caixa pelo Descasamento do Ciclo Financeiro (PMR > PMP):** Como os recebimentos ocorrem em 45 dias e os pagamentos em 30 dias, há um pico de pressão sobre o caixa no D60, reduzindo a folga operacional líquida para R$ 2.000,00 no período.
2. **Inadimplência Concentrada de Clientes-Chave:** O DSO elevado (45 dias) expõe a empresa ao risco de caixa negativo no intervalo D30-D60 caso 2 ou mais clientes atrasem a liquidação de suas duplicatas.
3. **Inconsistências na Conciliação Fiscal x Fluxo Financeiro:** Falhas ou atrasos no cruzamento de NF-e com escrituração geram distorções no cálculo do Simples Nacional (DAS) ou risco de duplicidade em agendamentos de pagamentos.

---

### 💡 3 Ações Imediatas (Plano de Trabalho Atlas)
1. **Implantação de Régua de Cobrança Automatizada e Redução de DSO:** Reduzir o PMR de 45 para 30 dias via automação de alertas pré-vencimento e concessão pontual de desconto por antecipação.
2. **Renegociação do Prazo Médio com Fornecedores (Alinhamento de DPO):** Reestruturar prazos de pagamento com os 5 principais fornecedores de 30 para 45/60 dias, equalizando o Ciclo Financeiro.
3. **Automação da Conciliação Fiscal-Financeira via API ERP:** Finalizar a integração bancária diária via extrato OFX/API para eliminar checagens manuais e manter linha de crédito pré-aprovada a taxas reduzidas apenas para eventualidades no D60.

---

## 5. Esteira Fiscal-Financeira & Tratamento de Exceções

### Resumo das Etapas Operacionais da Esteira NF-e

| Etapa | Foco de Atuação | Tempo Manual Estimado (Semanal) | % Tempo |
| :--- | :--- | :---: | :---: |
| **Etapa 1** | Captura e Organização de XML/PDF/Scans | 03h 30min | 20,0% |
| **Etapa 2** | Triagem e Desduplicação de Documentos (Chave/Regra Tripla) | 02h 00min | 11,4% |
| **Etapa 3** | Validação de Controles Fiscais, Retenções e Alíquotas | 04h 30min | 25,7% |
| **Etapa 4** | Roteamento de Aprovações Operacionais e Pedidos | 02h 30min | 14,3% |
| **Etapa 5** | Conciliação Fiscal-Financeira e Escrituração | 05h 00min | 28,6% |
| **TOTAL** | **Ciclo Semanal de Validação Intensiva** | **17h 30min** | **100,0%** |

---

### Matriz de Tratamento de Exceções Fiscais

| Exceção Identificada | Causa Raiz | Procedimento Operacional / Tratamento |
| :--- | :--- | :--- |
| **1. Nota emitida sem XML** | Fornecedor envia apenas scan/PDF por e-mail. | Solicitar XML ao fornecedor ou realizar download direto via Chave na SEFAZ/Prefeitura. |
| **2. Retenção de IRRF/PCC incorreta** | Parametrização errada na emissão da NFS-e. | Bloquear pagamento no Contas a Pagar e solicitar cancelamento/reemissão ou Carta de Correção. |
| **3. Divergência valor NF-e x Pedido** | Frete extra ou reajuste contratual não avisado. | Paralisar aprovação e solicitar alinhamento entre gestor e fornecedor. |
| **4. NF-e duplicada** | Reenvio de documento ou duplicidade de e-mail. | Rejeitar segundo lançamento e arquivar com a tag "DUPLICADO". |
| **5. NF-e desconhecida emitida contra CNPJ** | Erro de digitação do emitente ou fraude fiscal. | Executar Manifestação do Destinatário como "Operação não Realizada" / "Desconhecimento". |
| **6. NF-e cancelada após aprovação** | Cancelamento pelo emitente na SEFAZ pós-entrega. | Estornar agendamento bancário e ajustar escrituração da competência. |

---

## 6. Estratégia Comercial & Expansão (Atlas Gestão Financeira)

### 6.1 Carrossel para Redes Sociais (7 Slides)
* **Slide 1 (Capa):** *Sua PME faturou R$ 150 mil e deu lucro, mas o caixa continua zerado?* (O problema é seu Ciclo Financeiro).
* **Slide 2 (O Paradox):** Comparativo DRE (Lucro de R$ 28k) vs Extrato no D60 (Saldo de R$ 2k).
* **Slide 3 (PMR vs PMP):** Explicação do descasamento (PMR 45d vs PMP 30d = Ciclo de +15d pagando para trabalhar).
* **Slide 4 (Break-even Real):** Mostrando o cálculo do Ponto de Equilíbrio em R$ 100k.
* **Slide 5 (Custo Operacional):** Exibindo o alerta das 17h30m gastas em processos manuais por mês.
* **Slide 6 (Plano de Virada):** 3 passos (Régua de cobrança, Renegociação DPO, Automação API).
* **Slide 7 (CTA):** Convite para Diagnóstico Financeiro Gratuito de 30 minutos.

---

### 6.2 Roteiro de Reel (35 Segundos)
* **00:00 - 00:05:** *"Sua PME faturou R$ 150 mil, a planilha mostra R$ 28 mil de lucro, mas no final do mês você não tem dinheiro nem para o pro-labore?"* [Overlay: R$ 150k Faturados. Caixa ZERADO?]
* **00:05 - 00:15:** *"O erro é olhar só para a DRE e esquecer o Ciclo Financeiro. Se você dá 45 dias de prazo pro seu cliente e paga a folha em 30, você está bancando o seu cliente."* [Overlay: PMR 45d vs PMP 30d]
* **00:15 - 00:25:** *"Chega o mês seguinte, seu saldo despenca para R$ 2 mil e você precisa recorrer a cheque especial."* [Overlay: Aperto de Caixa no D60]
* **00:25 - 00:35:** *"Quer parar de gerir sua PME no escuro? Comente DIAGNÓSTICO aqui embaixo e receba uma análise gratuita do caixa da sua empresa com a Atlas."* [Overlay: Comente "DIAGNÓSTICO"]

---

### 6.3 Critérios de Qualificação de Leads (SQLs / ICP Atlas)
1. **Faturamento Bruto Mensal:** R$ 80.000,00 a R$ 500.000,00/mês.
2. **Modelo de Gestão Atual:** Baseado em planilhas manuais ou ERPs desintegrados.
3. **Ciclo Financeiro Composto:** Operações B2B/Serviços com vendas faturadas (PMR $\ge$ 30 dias).
4. **Interlocutor Decisor:** Sócio-proprietário, Director Executivo ou CEO.
5. **Dor Declarada:** Falta de visibilidade de caixa ou divergência entre lucro contábil e saldo bancário.

---

### 6.4 Estrutura da Reunião de Diagnóstico Gratuito (30 Minutos)
* **Bloco 1 (00:00 - 00:05):** Boas-vindas, alinhamento de agenda e autorização para análise.
* **Bloco 2 (00:05 - 00:15):** Investigação SPIN (Rotinas manuais, indicadores conhecidos, forma de cobertura de caixa).
* **Bloco 3 (00:15 - 00:22):** Simulação ao vivo de Break-even, Ciclo Financeiro e tempo perdido no processo fiscal.
* **Bloco 4 (00:22 - 00:27):** Apresentação da solução Atlas BPO & Controladoria.
* **Bloco 5 (00:27 - 00:30):** Fechamento e agendamento da reunião de proposta comercial.

---

## Gargalos Operacionais

Abaixo estão identificados os gargalos operacionais mapeados na rotina de inteligência e controle financeiro da empresa, classificados em **ordem decrescente de impacto** no negócio. Cada gargalo traz a especificação da natureza da falha (manual, repetitiva ou propensa a erro) e a estimativa de horas de trabalho perdidas por semana.

| Ordem de Impacto | Gargalo Operacional | Natureza da Tarefa | Descrição do Impacto Operacional e Financeiro | Estimativa Simulada de Horas Perdidas / Semana |
| :---: | :--- | :--- | :--- | :---: |
| **1º (Maior Impacto)** | **Conciliação Bancária Manual e Batimento do Extrato com Títulos Fiscais** | Manual & Propensa a erro | Digitação manual e cruzamento linha a linha de extratos OFX/PDF com títulos a pagar/receber. Alto risco de erro na apuração de impostos (Simples Nacional), divergências no fechamento e atraso no envio do Fluxo de Caixa aos sócios. | **5h 00min / semana** |
| **2º** | **Conferência Manual de Retenções Fiscais (IRRF, PCC, ISS) e Alíquotas em XML/PDF** | Manual & Propensa a erro | Validação individual de notas fiscais de serviços tomados/prestados. Falhas na revisão geram pagamentos incorretos de guias fiscais, multas por descumprimento de obrigações acessórias e retrabalho na escrituração. | **4h 30min / semana** |
| **3º** | **Captura, Download e Organização Manual de XMLs, PDFs e Scans Fiscais** | Manual & Repetitiva | Varredura em caixas de e-mail e portais de prefeituras/SEFAZ, seguida de download e digitação de dados de notas emitidas em formato imagem (sem XML). Atividade puramente operacional sem geração de valor. | **3h 30min / semana** |
| **4º** | **Consolidação Manual de Planilhas de Fluxo de Caixa (30/60/90 Dias) e DRE Gerencial** | Manual & Repetitiva | Extração de dados de múltiplos relatórios para montagem e atualização de planilhas dinâmicas de projeção de liquidez. Riscos de quebra de fórmulas e perda de histórico de dados. | **2h 30min / semana** |
| **5º** | **Follow-up Manual para Roteamento de Aprovações de Compras e Medicões** | Repetitiva & Manual | Cobrança ativa junto aos gestores de contrato da empresa para validação e aceite de notas fiscais antes do agendamento bancário. Gera gargalos no Contas a Pagar e risco de perda de vencimentos. | **2h 30min / semana** |
| **6º (Menor Impacto)** | **Triagem e Checagem Manual de Trava de Duplicidade de Documentos** | Repetitiva & Propensa a erro | Verificação manual de divergências em NFS-e sem chave padrão (aplicação manual de regra tripla [CNPJ + Nº Nota + Valor]). Risco residual de agendar pagamentos em duplicidade. | **2h 00min / semana** |
| **TOTAL** | **Gargalos Totais da Rotina Operacional Financeira** | -- | **Perda recorrente de capacidade operacional da equipe em tarefas sem valor estratégico.** | **20h 00min / semana** *(80 horas/mês)* |