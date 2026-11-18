# Relatório de Defesa e Reflexão sobre Malwares

Este documento faz parte da entrega do desafio prático de cibersegurança, complementando os scripts publicados neste repositório. O objetivo é documentar a experiência de simular malwares em ambiente controlado e, principalmente, refletir sobre as medidas de defesa no mundo real.

## 1. Estudo de Caso: Keylogger

Durante o desenvolvimento do keylogger em Python utilizando a biblioteca `pynput`, foi possível compreender como spywares conseguem interceptar as entradas de teclado do sistema.

**Adequação Ética e de Segurança:**
Inicialmente, o script previa o envio automático das teclas capturadas via e-mail (usando a biblioteca `smtplib`). No entanto, para garantir que o projeto estivesse em conformidade com as políticas do GitHub (que proíbe a distribuição de malwares funcionais) e mantivesse o foco 100% educacional, o código foi adaptado. A versão publicada neste repositório:
- Não envia dados pela rede;
- Não oculta o processo em segundo plano;
- Exige uma ação do usuário (tecla F9) para iniciar a captura;
- Salva os dados apenas em memória (buffer) para fins de demonstração.

## 2. Estudo de Caso: Ransomware

A simulação de Ransomware focou no entendimento da criptografia maliciosa. O script criado foi capaz de gerar arquivos de teste, criptografá-los e gerar uma mensagem de "resgate".
- **Aprendizado:** Foi possível entender como a criptografia simétrica (ex: AES) é utilizada para bloquear os dados da vítima e como a chave de descriptografia fica em posse do atacante.
- **Controle:** Todo o processo foi executado em ambiente isolado com arquivos de teste, garantindo que nenhum dado real fosse comprometido.

---

## 3. Reflexão sobre Defesa (Medidas de Prevenção)

Entender o ataque é o primeiro passo para a defesa. Abaixo, detalho como as principais ferramentas de segurança atuam contra essas ameaças:

###Antivírus e EDR (Endpoint Detection and Response)
- **Contra Keylogger:** O Antivírus detecta keyloggers através de assinaturas de código e análise comportamental. Ele consegue identificar quando um processo está tentando criar *hooks* de teclado (interceptar as teclas do sistema) e bloqueia a execução.
- **Contra Ransomware:** Ferramentas modernas (EDR) monitoram a velocidade com que os arquivos estão sendo modificados. Se um processo começa a criptografar centenas de arquivos em segundos, ele é interrompido e o computador é isolado da rede.

###Firewall
- **Contra Keylogger:** No script original, o keylogger tentava enviar dados via protocolo SMTP (e-mail). Um Firewall bem configurado pode bloquear a saída de tráfego da máquina para servidores de e-mail desconhecidos, impedindo a exfiltração dos dados capturados.
- **Contra Ransomware:** O Firewall bloqueia conexões de entrada não autorizadas. Além disso, regras de *outbound* (saída) podem impedir que o ransomware se comunique com o servidor do atacante (C2 - Command and Control).

###Sandboxing (Isolamento)
- É a técnica de executar um arquivo suspeito em um ambiente isolado e simulado (uma "caixa de areia"). Se o arquivo for um Ransomware, ele vai criptografar apenas os arquivos falsos da Sandbox. Se for um Keylogger, ele não terá acesso aos teclados reais do sistema. É a principal técnica usada por analistas de segurança.

###Conscientização do Usuário (A defesa mais importante)
Nenhuma ferramenta técnica é 100% infalível se o usuário não for treinado.
- **Phishing:** A maioria dos malwares é instalada porque o usuário clicou em um link malicioso ou abriu um anexo falso (como arquivos `.pyw` ou `.exe`).
- **Gerenciadores de Senha:** Usar um gerenciador evita que você digite senhas manualmente, protegendo contra keyloggers. Mesmo que o keylogger esteja rodando, ele capturará apenas a senha mestre do gerenciador, que não é o suficiente para acessar as contas.
- **Backups:** Contra Ransomware, a única garantia de recuperação sem pagar resgate é ter backups regulares em locais seguros (offline ou na nuvem).

## Conclusão
Este desafio demonstrou que implementar ameaças em Python é relativamente simples, mas entender o funcionamento das defesas e a importância da conscientização é o que separa um usuário vulnerável de um profissional de segurança.
