import ollama

def run_chat():
    # Das Modell definieren (muss vorher via 'ollama pull' geladen sein)
    model_name = "hf.co/bartowski/Llama-3-SauerkrautLM-8b-Instruct-GGUF"
    
    # System-Prompt setzen: Hier erklärst Du die Rolle des Bots.
    system_prompt = (
        "Du bist ein geduldiger Tutor für Schüler. "
        "Die Schüler machen gerade einen Kurs bei VISION26 an der Evangelischen Schule Berlin Zentrum (ESBZ). "
        "Begrüße den Schüler zu Beginn des Dialogs. "
    )

    # Der Chat-Verlauf enthält die Nachrichten zwischen Nutzer und Bot.
    # Er beginnt immer mit dem System-Prompt.
    chatverlauf = [
        {
            'role': 'system',
            'content': system_prompt
        }
    ]

    print(f"Chatbot gestartet mit {model_name}. (Zum Beenden 'exit' tippen)")

    while True:
        user_input = input("\n👤 Du: ")
        
        if user_input.lower() in ["exit", "quit"]:
            break

        # User-Nachricht anhängen
        chatverlauf.append({'role': 'user', 'content': user_input})

        try:
            print("\n🤖 Bot: ", end="", flush=True)
            
            # Streaming-Antwort generieren (fühlt sich schneller an auf CPU)
            stream = ollama.chat(model=model_name, messages=chatverlauf, stream=True)
            
            full_response = ""
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end="", flush=True)
                full_response += content
            
            print() # Neue Zeile am Ende
            
            # Bot-Antwort für den Kontext speichern
            chatverlauf.append({'role': 'assistant', 'content': full_response})

        except Exception as e:
            print(f"\nFehler: {e}")

if __name__ == "__main__":
    run_chat()
