import pyautogui
import keyboard
import time

def auto_type(text, delay=0.01):
    """Função para digitar texto automaticamente."""
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)  # Simula uma pausa entre caracteres

def main():
    print("Auto Typer - Digite o texto abaixo:")
    text_to_type = input("> ")

    print("\nPosicione o cursor no local desejado.")
    print("Pressione 'Ctrl + Alt + T' para iniciar a digitação...")
    
    # Aguarda o usuário apertar a combinação de teclas
    keyboard.wait('ctrl+alt+t')

    print("Iniciando a digitação...")
    auto_type(text_to_type)

    print("\nTexto digitado com sucesso!")

if __name__ == "__main__":
    main()

#pip install pyautogui keyboard
#python auto_typer.py