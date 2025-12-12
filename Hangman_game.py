import random

HANGMAN_6_FACE = [
    r"""
      +---+
      |   |
      |   O
      |  /|\
      |  / \
      |  
   😵 DEAD
   
=========
""",
    r"""
      +---+
      |   |
      |   O
      |  /|\
      |    
      |  
   😨 SCARED
=========
""",
    r"""
      +---+
      |   |
      |   O
      |  /|
      |    
      |  
   😢 CRYING
=========
""",
    r"""
      +---+
      |   |
      |   O
      |   |
      |    
      |  
   😟 WORRIED
=========
""",
    r"""
      +---+
      |   |
      |   O
      |    
      |    
      |  
   🙂 NEUTRAL
=========
""",
    r"""
      +---+
      |   |
      |    
      |    
      |    
      |  
=========
""",
]


lives = 5
word_list = ["apple", "mouse", "lion"]
word = random.choice(word_list)

print("WORD (for debugging):", word)

game_over = False
correct_letters = []

while not game_over:

    character = input("Enter your guess: ").lower()

    display = ""

    for char in word:
        if char == character:
            correct_letters.append(char)
            display += char
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    # FIXEDBUG
    if character not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")
            print(HANGMAN_6_FACE[lives])
            break

    if "_" not in display:
        game_over = True
        print("You win")

    print(HANGMAN_6_FACE[lives])
