import tkinter as tk

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

class MorseCodeTranslatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Morse Code Translator")

        self.input_label = tk.Label(master,bg="lavender", text="ENTER YOUR ENG STRING TO BE TRANSLATED",font=("Orbitron",15),pady=50)
        self.input_label.pack()

        self.input_textbox = tk.Text(master,bg="light blue" , height=6, width=80)
        self.input_textbox.pack()

        self.translate_button = tk.Button(master,bg="green", text="CLICK TO TRANSLATE", width=20,font=("Algerian"), pady= 20 , command=self.translate_text)
        self.translate_button.pack()

        self.output_label = tk.Label(master,bg="lavender", text="THE TRANSLATED TEXT", font=("Orbitron",15),pady=50)
        self.output_label.pack()

        self.output_textbox = tk.Text(master,bg="light blue" , height=6, width=80)
        self.output_textbox.pack()
        
    def translate_text(self):
        input_text = self.input_textbox.get("1.0", tk.END).strip().upper()

        output_text = ""
        for char in input_text:
            if char in MORSE_CODE:
                output_text += MORSE_CODE[char] + " "
            else:
                output_text += " "

        self.output_textbox.delete("1.0", tk.END)
        self.output_textbox.insert(tk.END, output_text)

root = tk.Tk()
translator_gui = MorseCodeTranslatorGUI(root)
root.config(bg="lavender")
root.mainloop()
