import keyboard  # Biblioteca para monitorar eventos de teclado
import pyperclip  # Biblioteca para copiar/colar texto via área de transferência
import time  # Usada para pausas curtas entre ações


#o script abaixo absorve um texto atrás do : e ao digitar esse texto a mensagem após o : é gerada
atalhos = {
    ".exemplo": "Bom dia, este é um exemplo",
}

# Função principal que monitora o teclado em tempo real
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
           # Cola o texto correspondente
                    pyperclip.copy(texto)
                    keyboard.press_and_release('ctrl+v')

                    buffer = ""

print(" Rodando... digite qualquer atalho para colar a mensagem correspondente.")
print("Pressione Ctrl+C para sair.")
monitorar()
