import tkinter as tk
import random

# Thai consonants with pronunciation
thai_consonants = [
    ("ก", "gor kai"), ("ข", "kho khai"), ("ฃ", "kho kuat"), ("ค", "kho khwai"),
    ("ฅ", "kho khon"), ("ฆ", "kho ra-khang"), ("ง", "ngo ngu"), ("จ", "jo jaan"),
    ("ฉ", "cho ching"), ("ช", "cho chang"), ("ซ", "so so"), ("ฌ", "cho choe"),
    ("ญ", "yo ying"), ("ฎ", "do cha-da"), ("ฏ", "to pa-tak"), ("ฐ", "tho than"),
    ("ฑ", "tho montho"), ("ฒ", "tho phu-thao"), ("ณ", "no nen"), ("ด", "do dek"),
    ("ต", "to tao"), ("ถ", "tho thung"), ("ท", "tho thahan"), ("ธ", "tho thong"),
    ("น", "no nu"), ("บ", "bo baimai"), ("ป", "po pla"), ("ผ", "pho phueng"),
    ("ฝ", "fo fa"), ("พ", "pho phan"), ("ฟ", "fo fan"), ("ภ", "pho sam-phao"),
    ("ม", "mo ma"), ("ย", "yo yak"), ("ร", "ro rua"), ("ล", "lo ling"),
    ("ว", "wo waen"), ("ศ", "so sala"), ("ษ", "so ruesi"), ("ส", "so suea"),
    ("ห", "ho hip"), ("ฬ", "lo chu-la"), ("อ", "o ang"), ("ฮ", "ho nok-huk")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        self.root.configure(bg="white")

        self.current_card = None
        self.is_flipped = False

        # Flashcard display
        self.card_label = tk.Label(root, text="", font=("Arial", 50), bg="white")
        self.card_label.pack(expand=True, pady=20)

        # Buttons
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.new_card, font=("Arial", 14))
        self.next_button.pack(side=tk.RIGHT, padx=20, pady=10)

        # Load first card
        self.new_card()

    def new_card(self):
        """Select a new random Thai consonant and display it."""
        self.current_card = random.choice(thai_consonants)
        self.is_flipped = False
        self.card_label.config(text=self.current_card[0])  # Show Thai letter

    def flip_card(self):
        """Flip the card to show the pronunciation or return to Thai letter."""
        if self.current_card:
            if self.is_flipped:
                self.card_label.config(text=self.current_card[0])  # Show Thai letter
            else:
                self.card_label.config(text=self.current_card[1])  # Show pronunciation
            self.is_flipped = not self.is_flipped

# Create the main window
root = tk.Tk()
game = FlashcardGame(root)
root.mainloop()

