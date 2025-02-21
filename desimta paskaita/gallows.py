import os
import random
import time

words = [
    {'content':'dog', 'hint':"It's an animal"},
    {'content':'pepsi', 'hint':"It's a product"},
    {'content':"mercedes", "hint":"It's a car"}
]

words_categories = {
    'animals':{'content':'dog', 'hint':"It's an animal"},
    'cars': {'content':'mercedes', 'hint':"It's a car"}
}

def generate_word():
    return random.choice(words)

def clear():
    os.system('cls')
    
def print_game_state(health:int, hint:int, word:dict, selected_letters:set[str]):
    clear()
    print(f"Health - {health}")
    print(f"Hint - {word['hint']}")
    print(f"You have {hint} hints left")
    print(f"Current - {return_word(word['content'], selected_letters).lower()}")

# def return_word(word:str, selected_letters:set[str]):
#     result = ""
#     for letter in word:
#         if letter in selected_letters:
#             result+= letter
#         elif letter == ' ':
#             result+= letter
#         else:
#             result+="_"
#     return result


def return_word(word:dict, selected_letters:set[str]):
    return ''.join(letter if letter in selected_letters else '_' for letter in word)

def handle_add(letter:str, word:dict, selected_letters: set[str]):
    if letter in word['content']:
        selected_letters.add(letter)
        return True
    else:
        return False
    
def handle_hint(hint:int, health:int, word:dict, selected_letters:set[str]):
    if hint == 0 or health == 1:
        return False
    else:
        selected_letters.add(random.choice(word['content']))
        return True
        
        
    
if __name__ == "__main__":
    clear()
    print("Hello, welcome to Gallows!")
    print("Press enter to start...")
    input("")
    
    while True:
        health = 7
        hint = 1
        word = generate_word()
        selected_letters = set()
        
        while True:
            print_game_state(health, hint, word, selected_letters)
            
            try:
                letter = input("Please enter a letter: ")
                if letter == 'hint':
                    if handle_hint(hint, health, word, selected_letters):
                        hint = 0
                        health-=1
                        continue
                    else:
                        raise ValueError
                        
                elif len(letter) != 1 or not letter.isalpha():
                    raise ValueError
                
            except ValueError:
                continue
            
            if handle_add(letter, word, selected_letters):
                if return_word(word['content'], selected_letters) == word['content']:
                    clear()
                    print(f"You won with {health} health left!")
                    print(f"Answer is {word['content']}")
                    time.sleep(5)
                    break
            else:
                health -=1
                if health == 0:
                    print_game_state(health,hint ,  word, selected_letters)
                    print('Game over, you lost all health.')
                    print(f'Answer: {word['content']}')
                    time.sleep(5)
                    break
            
        