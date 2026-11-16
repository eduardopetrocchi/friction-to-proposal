### Rotina Operacional da Esteira de NF-e: Captura, Validação, Desduplicação e Conciliação Fiscal
**Cliente:** TechServices LTDA | **Responsável:** Analista Fiscal e de Processos (Atlas Gestão Financeira)

---

### 1. Visão Geral da Rotina Semanal
Como Analista Fiscal e de Processos responsável pela esteira de documentos fiscais da Atlas Gestão Financeira, minha prioridade nesta semana de fechamento é garantir a integridade absoluta dos dados das Notas Fiscais Eletrônicas (NF-e, NFS-e e CT-e) de entrada e saída da **TechServices LTDA**. A meta é zerar inconsistências e divergências de digitação que possam impactar o cálculo do Simples Nacional, a retenção na fonte de impostos e a composição da DRE Gerencial.

---

### 2. Fluxo em Etapas e Tempo Manual Simulado por Etapa

#### **Etapa 1: Captura e Recepção de Documentos Fiscais**
* **Descrição da Operação:** Varredura diária da caixa de e-mails dedicada (`fiscal@...`), recebimento de arquivos em múltiplos formatos (XML, PDF, imagens/scans) enviados por fornecedores e clientes, além da captura direta via Web Service da Secretaria da Fazenda (SEFAZ) e prefeitura.
* **Ações:** 
  * Download e organização de XMLs e PDFs em repositório centralizado por pasta/competência.
  * Transcrição/digitação manual ou via OCR de notas recebidas exclusivamente em formato imagem/PDF sem XML original.
* **Tempo Manual Simulado (Semanal/Fechamento):** **3 horas e 30 minutos** (média de 5 min por nota sem XML / organização de diretórios).

#### **Etapa 2: Triagem e Desduplicação de Documentos**
* **Descrição da Operação:** Aplicação das travas de segurança para impedir o registro duplo de despesas ou receitas no ERP/planilha de controle.
* **Controles de Desduplicação:**
  * **Chave de Acesso (44 dígitos):** Cruzamento automatizado da Chave de Acesso no banco de dados para NF-e/CT-e.
  * **Regra Tripla (para NFS-e sem chave padrão):** Validação combinada dos campos **[CNPJ do Emitente + Número da Nota + Valor Total]**. Se houver correspondência exata, o documento é segregado imediatamente como "Duplicado".
* **Tempo Manual Simulado (Semanal/Fechamento):** **2 horas** (conferência manual de divergências apontadas nas travas).

#### **Etapa 3: Validação de Controles Fiscais e Dados Críticos**
* **Descrição da Operação:** Conferência detalhada campo a campo dos dados do XML/PDF contra as regras fiscais vigentes da TechServices LTDA.
* **Controles de Validação Aplicados:**
  * **Dados Cadastrais:** Razão Social, CNPJ, Inscrição Municipal/Estadual do tomador e prestador.
  * **Enquadramento Tributário & Retenções:** Validação das alíquotas de retenção na fonte (IRRF, CSLL, PIS, COFINS, ISS) para serviços tomados/prestados.
  * **Classificação Fiscal:** Validação dos códigos CFOP, NCM, Código de Serviço e CNAE.
  * **Datas:** Validação da Data de Emissão vs. Data de Competência vs. Data de Faturamento.
* **Tempo Manual Simulado (Semanal/Fechamento):** **4 horas e 30 minutos** (conferência minuciosa de alíquotas e impostos retidos).

#### **Etapa 4: Processo de Aprovação Financeira e Fiscal**
* **Descrição da Operação:** Submissão das notas validadas aos responsáveis pelo centro de custo na TechServices LTDA (aprovação de medição/serviço) e amarração com os pedidos de compra/contratos.
* **Ações:**
  * Roteamento para aceite operacional do gestor do contrato.
  * Confirmação de recebimento do serviço para liberação do agendamento no Contas a Pagar / Contas a Receber.
* **Tempo Manual Simulado (Semanal/Fechamento):** **2 horas e 30 minutos** (cobrança de aprovações pendentes e validação de de para de pedidos).

#### **Etapa 5: Conciliação Fiscal-Financeira e Escrituração**
* **Descrição da Operação:** Cruzamento final dos dados fiscais com a movimentação bancária e preparação para o fechamento gerencial da controladoria.
* **Ações:**
  * Batimento da NF-e com o extrato bancário (OFX) e títulos liquidados/a liquidar.
  * Registro das NF-e de entrada e saída na planilha/sistema de escrituração fiscal.
  * Consolidação do relatório de faturamento bruto para cálculo da DAS (Simples Nacional - 8%) e apoio na elaboração da DRE Gerencial.
* **Tempo Manual Simulado (Semanal/Fechamento):** **5 horas** (conciliação linha a linha do extrato bancário com títulos fiscais).

---

### 3. Quadro Resumo do Tempo Manual Gasto por Etapa

| Etapa da Rotina | Foco de Atuação | Tempo Manual Estimado (Semanal) | % do Tempo Total |
| :--- | :--- | :---: | :---: |
| **Etapa 1** | Captura e Organização de XML/PDF/Imagens | 03h 30min | 20,0% |
| **Etapa 2** | Triagem e Desduplicação de Documentos | 02h 00min | 11,4% |
| **Etapa 3** | Validação de Controles Fiscais e Retenções | 04h 30min | 25,7% |
| **Etapa 4** | Roteamento de Aprovações Operacionais | 02h 30min | 14,3% |
| **Etapa 5** | Conciliação Fiscal-Financeira e Escrituração | 05h 00min | 28,6% |
| **TOTAL** | **Ciclo Semanal de Conciliação Intensiva** | **17h 30min** | **100,0%** |

---

### 4. Matriz de Exceções Identificadas e Tratamento Operacional

During the execution of the pipeline, the following exceptions are handled according to predefined fiscal standards:

```
+---------------------------------------------------------------------------------------------------+
| MATRIZ DE TRATAMENTO DE EXCEÇÕES FISCAIS                                                         |
+----------------------+----------------------------------+-----------------------------------------+
| Exceção Identificada | Causa Raiz                       | Procedimento Operacional / Tratamento   |
+----------------------+----------------------------------+-----------------------------------------+
| 1. Nota emitida sem  | Fornecedor envia apenas scan ou  | Notificar o fornecedor imediatamente    |
|    arquivo XML.      | PDF de RPS por e-mail.           | solicitando o arquivo XML. Caso não     |
|                      |                                  | envie, efetuar consulta via Chave na    |
|                      |                                  | SEFAZ/Prefeitura para download direto.  |
+----------------------+----------------------------------+-----------------------------------------+
| 2. Retenção de IRRF/ | Erro de parametrização do        | Bloquear o pagamento no Contas a Pagar. |
|    PCC incorreta no  | prestador na emissão da NFS-e.   | Solicitar o cancelamento e reemissão    |
|    serviço tomado.   |                                  | da NFS-e correta ou emitir Carta de     |
|                      |                                  | Correção (conforme legislação municipal)|
|                      |                                  | ajustando os impostos retidos.          |
+----------------------+----------------------------------+-----------------------------------------+
| 3. Divergência entre | Frete/taxa extra não informada   | Paralisar a aprovação. Contactar o      |
|    valor da NF-e e o | previamente ou reajuste contratual| gestor da conta na TechServices LTDA    |
|    pedido/boleto.    | não comunicado.                  | para aprovação de aditivo ou solicitar  |
|                      |                                  | complemento/desconto ao fornecedor.     |
+----------------------+----------------------------------+-----------------------------------------+
| 4. NF-e duplicada no | Reenvio do mesmo documento pelo  | Rejeitar o segundo lançamento, aplicar  |
|    mesmo vencimento. | fornecedor ou duplicidade no e-mail| a tag "DUPLICADO" no controle central e |
|                      |                                  | arquivar a nota duplicada sem gerar     |
|                      |                                  | lançamento financeiro.                  |
+----------------------+----------------------------------+-----------------------------------------+
| 5. NF-e emitida contra| Fraude fiscal, erro de CNPJ ou   | Realizar imediatamente a "Manifestação  |
|    a TechServices    | operação não efetuada.           | do Destinatário" como "Operação não     |
|    sem pedido válido. |                                  | Realizada" ou "Desconhecimento da       |
|                      |                                  | Operação" no portal da SEFAZ.           |
+----------------------+----------------------------------+-----------------------------------------+
| 6. NF-e cancelada    | Emitente cancelou a nota na SEFAZ| Notificar o departamento financeiro para|
|    após aprovação do | após a entrega do serviço/produto.| estornar o agendamento bancário e ajustar|
|    pagamento.        |                                  | a escrituração fiscal da competência.    |
+----------------------+----------------------------------+-----------------------------------------+
```

---

### 5. Encerramento e Encaminhamento à Controladoria
Com a conclusão deste fluxo operacional de 17h30min de validação intensiva:
1. Todas as entradas e saídas da TechServices LTDA estão **100% conciliares e livres de duplicidades**.
2. O montante de faturamento de **R$ 150.000,00** e os custos/despesas estão devidamente escriturados sem erros de digitação.
3. Os dados validados alimentam diretamente a DRE Gerencial e a projeção do Fluxo de Caixa, garantindo a acurácia necessária para a apresentação aos sócios.