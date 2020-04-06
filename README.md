# python-cvm

Pequena aplicação em python para baixar arquivos com cotação diária dos fundos registrados na CVM.

Fonte dos dados: http://dados.cvm.gov.br

Os arquivos referentes ao mês corrente (M) e anterior (M-1) são atualizados diariamente com as eventuais reapresentações. 
A atualização ocorre de terça a sábado, às 08:00h, com os dados recebidos pelo CVMWeb até as 23:59h do dia anterior.
Os arquivos referentes aos meses M-2 e M-3 são atualizados semanalmente com as eventuais reapresentações.
Os arquivos referente aos meses M-4, M-5, ..., até M-11 são atualizados mensalmente com as eventuais reapresentações.
