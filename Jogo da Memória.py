import tkinter as tk
from tkinter import messagebox
import random

NUM_ROWS = 4
NUM_COLS = 4
CARD_SIZE_W = 10  
CARD_SIZE_H = 5   

CARD_COLORS = [
    'green', 'orange', 'brown',  'grey', 
    'navy',  'olive', 'violet', 'turquoise'
]

BG_COLOR = '#272727'
FONT_COLOR = 'white'
FONT_STYLE = ('Arial', 12, 'bold')
MAX_ATTEMPTS = 20  
attempts = 0

def create_card_grid():
    colors = CARD_COLORS * 2  
    random.shuffle(colors)    
    grid = []
    for _ in range(NUM_ROWS):
        row = []
        for _ in range(NUM_COLS):
            color = colors.pop()  
            row.append(color)     
        grid.append(row)          
    return grid

def card_clicked(row, col):
    card = cards[row][col]
    color = card['bg']
    if color == 'black':  
        card['bg'] = grid[row][col]  
        revealed_cards.append(card)
        if len(revealed_cards) == 2:  
            check_match()

def check_match():
    card1, card2 = revealed_cards
    if card1['bg'] == card2['bg']:  
        card1.after(1000, card1.destroy)
        card2.after(1000, card2.destroy)
        matched_cards.extend([card1, card2])
        check_win()
    else:
        card1.after(1000, lambda: card1.config(bg='black'))
        card2.after(1000, lambda: card2.config(bg='black'))
    revealed_cards.clear()
    update_score()

def check_win():
    if len(matched_cards) == NUM_ROWS * NUM_COLS:
        messagebox.showinfo('Vitória!', 'Você venceu, parabéns!!!')
        window.quit()

def update_score():
    global attempts
    attempts += 1
    attempts_label.config(text='Tentativas: {}/{}'.format(attempts, MAX_ATTEMPTS))
    if attempts >= MAX_ATTEMPTS:
        messagebox.showinfo('Fim de Jogo', 'Você perdeu o jogo!')
        window.quit()

window = tk.Tk()
window.title('Jogo de Memória')
window.configure(bg=BG_COLOR)  

grid = create_card_grid()
cards = []
revealed_cards = []
matched_cards = []

for row in range(NUM_ROWS):
    row_of_cards = []
    for col in range(NUM_COLS):
        card = tk.Button(window, width=CARD_SIZE_W, height=CARD_SIZE_H, bg='black',
                        relief=tk.RAISED, bd=3, command=lambda r=row, c=col: card_clicked(r, c))
        card.grid(row=row, column=col, padx=5, pady=5)
        row_of_cards.append(card)
    cards.append(row_of_cards)

button_style = {'activebackground': '#f8f9fa', 'font': FONT_STYLE, 'fg': FONT_COLOR}
window.option_add('*Button', button_style)

attempts_label = tk.Label(window, text='Tentativas: {}/{}'.format(attempts, MAX_ATTEMPTS), fg=FONT_COLOR, bg=BG_COLOR, font=FONT_STYLE)
attempts_label.grid(row=NUM_ROWS, columnspan=NUM_COLS, padx=10, pady=10)  # Aqui define a cor de fundo da etiqueta de tentativas

window.mainloop()