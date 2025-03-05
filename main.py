import base64
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk, font

# Funzione per codificare in Base64
def encode_to_base64():
    input_string = input_text.get("1.0", "end-1c")  # Ottieni il testo dall'input
    if not input_string.strip():
        messagebox.showwarning("Input vuoto", "Inserisci una stringa da codificare.")
        return
    
    try:
        # Ottieni la codifica selezionata
        encoding = encoding_var.get()
        # Codifica in Base64
        byte_data = input_string.encode(encoding)
        base64_encoded = base64.b64encode(byte_data)
        base64_string = base64_encoded.decode('utf-8') + get_line_ending()
        output_text.delete("1.0", tk.END)  # Pulisci il campo di output
        output_text.insert(tk.END, base64_string)  # Inserisci il risultato
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la codifica: {e}")

# Funzione per decodificare da Base64
def decode_from_base64():
    base64_string = input_text.get("1.0", "end-1c")  # Ottieni il testo dall'input
    if not base64_string.strip():
        messagebox.showwarning("Input vuoto", "Inserisci una stringa Base64 da decodificare.")
        return
    
    try:
        # Ottieni la codifica selezionata
        encoding = encoding_var.get()
        # Rimuovi eventuali separatori di fine riga
        base64_string = base64_string.strip()
        # Decodifica da Base64
        base64_bytes = base64_string.encode('utf-8')
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode(encoding)
        output_text.delete("1.0", tk.END)  # Pulisci il campo di output
        output_text.insert(tk.END, decoded_string)  # Inserisci il risultato
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la decodifica: {e}")

# Funzione per ottenere il separatore di fine riga selezionato
def get_line_ending():
    ending = line_ending_var.get()
    if ending == "LF (Unix)":
        return "\n"
    elif ending == "CRLF (Windows)":
        return "\r\n"
    elif ending == "CR (Mac classico)":
        return "\r"
    else:
        return "\n"  # Default a LF

# Creazione della finestra principale
root = tk.Tk()
root.title("Codifica/Decodifica Base64")
root.geometry("640x480")
root.configure(bg="#2e2e2e")  # Sfondo scuro retrò

# Font pixelato
pixel_font = font.Font(family="TkFixedFont", size=10)

# Etichetta per l'input
input_label = tk.Label(root, text="Inserisci la stringa:", bg="#2e2e2e", fg="#ffcc00", font=pixel_font)
input_label.pack(pady=5)

# Campo di testo per l'input
input_text = scrolledtext.ScrolledText(root, height=5, width=60, bg="#1e1e1e", fg="#ffffff", font=pixel_font, bd=2, relief="groove")
input_text.pack(pady=5)

# Selettore per la codifica dei caratteri
encoding_frame = tk.Frame(root, bg="#2e2e2e")
encoding_frame.pack(pady=5)

tk.Label(encoding_frame, text="Codifica dei caratteri:", bg="#2e2e2e", fg="#ffcc00", font=pixel_font).pack(side=tk.LEFT)
encoding_var = tk.StringVar(value="UTF-8")  # Valore predefinito
encoding_options = ["UTF-8", "ASCII", "ISO-8859-1", "UTF-16"]
encoding_menu = ttk.Combobox(encoding_frame, textvariable=encoding_var, values=encoding_options, state="readonly", font=pixel_font)
encoding_menu.pack(side=tk.LEFT)

# Selettore per il separatore di fine riga
line_ending_frame = tk.Frame(root, bg="#2e2e2e")
line_ending_frame.pack(pady=5)

tk.Label(line_ending_frame, text="Separatore di fine riga:", bg="#2e2e2e", fg="#ffcc00", font=pixel_font).pack(side=tk.LEFT)
line_ending_var = tk.StringVar(value="LF (Unix)")  # Valore predefinito
line_ending_options = ["LF (Unix)", "CRLF (Windows)", "CR (Mac classico)"]
line_ending_menu = ttk.Combobox(line_ending_frame, textvariable=line_ending_var, values=line_ending_options, state="readonly", font=pixel_font)
line_ending_menu.pack(side=tk.LEFT)

# Pulsanti per codificare e decodificare
button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=10)

encode_button = tk.Button(button_frame, text="Codifica in Base64", command=encode_to_base64, bg="#ffcc00", fg="#000000", font=pixel_font, bd=2, relief="raised")
encode_button.pack(side=tk.LEFT, padx=5)

decode_button = tk.Button(button_frame, text="Decodifica da Base64", command=decode_from_base64, bg="#ffcc00", fg="#000000", font=pixel_font, bd=2, relief="raised")
decode_button.pack(side=tk.LEFT, padx=5)

# Etichetta per l'output
output_label = tk.Label(root, text="Risultato:", bg="#2e2e2e", fg="#ffcc00", font=pixel_font)
output_label.pack(pady=5)

# Campo di testo per l'output
output_text = scrolledtext.ScrolledText(root, height=5, width=60, bg="#1e1e1e", fg="#ffffff", font=pixel_font, bd=2, relief="groove")
output_text.pack(pady=5)

# Avvio del ciclo principale dell'interfaccia grafica
root.mainloop()