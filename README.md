# pynput Key Event Study

Pequeno projeto de estudo sobre a biblioteca [`pynput`](https://pypi.org/project/pynput/):
como capturar e tratar eventos de teclado em Python.

## Aviso

Este projeto e **apenas para fins educacionais**. O codigo:

- **Nao** envia dados pela rede
- **Nao** salva registros em disco
- **Nao** roda oculto em segundo plano
- So captura teclas quando o usuario ativa explicitamente (F9)

Use apenas em maquinas que voce possui ou tem autorizacao para testar.
O autor nao se responsabiliza por uso indevido.

## O que o codigo demonstra

- Como usar `pynput.keyboard.Listener`
- Como diferenciar teclas normais (`key.char`) de teclas especiais (`keyboard.Key.*`)
- Como usar uma tecla de atalho (F9) para ligar/desligar a captura
- Tratamento de `AttributeError` ao acessar `key.char`

## Como executar

```bash
pip install pynput
python key_event_logger.py
