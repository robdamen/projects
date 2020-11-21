import os
import time

os.system('clear')
name = input("Wat is je naam? \n")

print("Hallo " + name + ", tijd om galgje te spelen!")
print("")
name_speler = input("Wie gaat het woord raden? \n")
time.sleep(1)
print("")

#verzameld de gekozen keuzes door de speler, goed en verkeerd.
goede_keuzes = []
verkeerde_keuzes = []
woord_geraden = False
woord = str.lower(input("Kies een woord: "))

# Controle of alle letter geraden zijn en speler heeft gewonnen

def win_controle():
    counter = 0
    for letter in woord:
        if letter in goede_keuzes:
            counter += 1
    if int(counter) == len(woord):
        print("Je hebt het woord geraden! " + name_speler + " wint!!!\n")
        exit()
    else:
        pass

os.system('clear')

print("Okay, goede keuze! Nu mag " + name_speler + " raden... Het woord is " + str(len(woord)) + " letters lang.\n")

def letter_kiezen():
    letter = input("Kies een letter: ")

    if letter in woord:
        goede_keuzes.append(letter)
        os.system('clear')
        for teken in woord:
            if teken in goede_keuzes:
                print(teken)
            else:
                print("_")
        print("")
        win_controle()            
    else:
        verkeerde_keuzes.append(letter)
        print("Jammer... je hebt " + str(len(verkeerde_keuzes)) + " verkeerde keuzes gemaakt.\n")
    
    
    
# Hier worden de win of verlies voorwaarden bepaald
while len(verkeerde_keuzes) <= 11:
    if win_controle == True:
        print("\n" + name_speler + " je hebt gewonnen van " + name + " !!\n Goed gedaan.")
        break
    elif len(verkeerde_keuzes) == 10:
        print("\nHelaas " + name_speler + " je hebt het woord niet geraden en " + name + " is de winnaar!\n")
        break
    else:
        letter_kiezen()



