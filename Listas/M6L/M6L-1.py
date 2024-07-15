'''Faça um programa que leia uma frase, e duas letras quaisquer do usuário. A seguir,
troque na frase todas as ocorrências da primeira letra fornecida pela segunda e
imprima a nova frase'''

while True:
    phase = input("Write any sentence here: ")
    letter_1 = input("Write the letter in the sentence to be replaced: ")
    letter_2 = input("Write the letter in the sentence that will replace it: ")
    y = 0


    if letter_1 and letter_2 not in phase:
        print(f"The typed letter is not in the sentence, it remains the same")    
    else:
        phase_replaced = phase.replace(letter_1, letter_2)
        print(f"Now your sentence is:\n {phase_replaced}")
    

#Loop for make more sentences
    verify = input("Do you want continue? [Y/N]")
    if verify.lower().strip() == y:
        break