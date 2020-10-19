import random as rd
from random_words import RandomWords
import board


while(True):
    rw= RandomWords()
    word= rw.random_words()
    player1_choose= rd.choice(word)
    random_word=[]
    draw_dash=[]
    wrong_guess=[]

    chance=0
    for i in player1_choose:
        random_word.append(i)
        draw_dash.append("_")
    print(str(draw_dash)[1:-1].replace(',',''))
    for tot_chance in range(len(player1_choose) + len(board.board(6))):
        player2_guess = input("guess: ")
        for guessed_letter in range(len(player1_choose)):
            if player1_choose[guessed_letter] == player2_guess:
                draw_dash[guessed_letter]=player2_guess

        if player2_guess in random_word:
            draw_dash[random_word.index(player2_guess)]=player2_guess
            print("correct: ",str(draw_dash)[1:-1].replace(',',''))
            print("wrong: ", str(wrong_guess)[1:-1].replace(',', ''))
            correct_guess=random_word
            if draw_dash[0:] == random_word[0:]:
                print(f'"The correct word was: {player1_choose}. You have Won. Swap the turn"')
                break

        elif chance<len(board.board(6)):
            wrong_guess.append(player2_guess)
            print("wrong letters reminder: ",str(wrong_guess)[1:-1].replace(',',''))
            print(board.board(chance))
            print(str(draw_dash)[1:-1].replace(',',''))
            chance+=1
            if chance==7:
                print("wrong: ", str(wrong_guess)[1:-1].replace(',',''))
                print(board.board(6))
                print(f'"The correct word was: {player1_choose}.You have Lost. Swap the turn"')
                break
