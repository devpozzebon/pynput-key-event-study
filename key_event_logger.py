"""
key_event_logger.py

Estudo sobre pynput: captura de eventos de teclado com ativacao manual.

AVISO
-----
Este script e APENAS educacional. Ele:
- NAO salva em disco
- NAO envia dados pela rede
- So registra teclas quando voce ativa com F9
- Nao roda oculto (e .py, nao .pyw)

Use apenas em maquinas que voce possui ou tem autorizacao para testar.
"""

from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift, keyboard.Key.shift_r,
    keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
    keyboard.Key.alt_l, keyboard.Key.alt_r,
    keyboard.Key.caps_lock, keyboard.Key.cmd,
}

capturando = False
buffer = []


def on_press(key):
    global capturando, buffer

    if key == keyboard.Key.f9:
        capturando = not capturando
        print(f"\n[Captura {'ATIVADA' if capturando else 'DESATIVADA'}]\n")
        if not capturando and buffer:
            print("Teclas capturadas nesta sessao:")
            print("".join(buffer))
            buffer = []
        return

    if not capturando:
        return

    try:
        buffer.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            buffer.append(" ")
        elif key == keyboard.Key.enter:
            buffer.append("\n")
        elif key == keyboard.Key.tab:
            buffer.append("\t")
        elif key == keyboard.Key.backspace:
            buffer.append("[<]")
        elif key == keyboard.Key.esc:
            buffer.append("[ESC]")
        elif key in IGNORAR:
            pass
        else:
            buffer.append(f"[{key}]")


def main():
    print("Estudo de eventos de teclado (pynput)")
    print("F9 = ativar/desativar captura | ESC = sair\n")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
