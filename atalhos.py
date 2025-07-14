import keyboard
import pyperclip
import time


#o script abaixo absorve um texto atrás do : e ao digitar esse texto a mensagem após o : é gerada
atalhos = {
    ".exemplo": "Bom dia, este é um exemplo",
}

def monitorar():
    buffer = ""

    while True:
        evento = keyboard.read_event()

        if evento.event_type == keyboard.KEY_DOWN:
            tecla = evento.name

            if tecla in ['space', 'enter', 'tab']:
                buffer = ""
                continue

            if tecla == 'backspace':
                buffer = buffer[:-1]
                continue

            if len(tecla) == 1:
                buffer += tecla

            for gatilho in atalhos:
                if buffer.endswith(gatilho):
                    texto = atalhos[gatilho]

                    for _ in gatilho:
                        keyboard.press_and_release('backspace')
                        time.sleep(0.01)

                    pyperclip.copy(texto)
                    keyboard.press_and_release('ctrl+v')

                    buffer = ""

print(" Rodando... digite qualquer atalho para colar a mensagem correspondente.")
print("Pressione Ctrl+C para sair.")
monitorar()
