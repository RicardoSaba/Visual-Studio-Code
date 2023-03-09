import random

#informationen
info = int(input("Um Informationen zu dem Spiel zu erhalten gib eine 1 ein, um mit dem Spiel zu starten eine 2. "))
if info == 1:
    print("Das Wesen eines Pokemons beschreibt seine Werte. Sanft. 120 hp, 15 angriff, 40 tempo| Grob. 80hp, 35 angriff, 60 tempo| Ausgeglichen 95hp, 25 angriff, 45 tempo")
else:
    print("Kampf beginnt!")
    
# Definieren der Variablen
pause = 0
p1_name = input("Wähle dein Pokemon! ")
p1_wesen = int(input("Wähle das Wesen! Sanft 1, Grob = 2, Ausgeglichen = 3| "))
p1_hp = 0
p1_attack = 0
p1_tempo = 0

p2_name = input("Wähle das Gegner Pokemon! ")
p2_wesen = int(input("Wähle das Wesen für das Gegner Pokemon! Sanft 1, Grob = 2, Ausgeglichen = 3| "))
p2_hp = 0
p2_attack = 0
p2_tempo = 0

print("Es kämpfen:",p1_name,"mit dem Wesen",p1_wesen,"gegen",p2_name,"mit dem Wesen ",p2_wesen,"! ")
pause = input()

#Definieren der Wesen
sanft = [120, 15, 40]
grob = [80, 35, 60]
ausgeglichen = [95, 25, 45]

#Werte zuweisen p1
if p1_wesen == 1:
    p1_hp = sanft[0]
    p1_attack = sanft[1]
    p1_tempo = sanft[2]
    
if p1_wesen == 2:
    p1_hp = grob[0]
    p1_attack = grob[1]
    p1_tempo = grob[2]
    
if p1_wesen == 3:
    p1_hp = ausgeglichen[0]
    p1_attack = ausgeglichen[1]
    p1_tempo = ausgeglichen[2]

#Werte zuweisen p2
    
if p2_wesen == 1:
    p2_hp = sanft[0]
    p2_attack = sanft[1]
    p2_tempo = sanft[2]
    
if p2_wesen == 1:
    p2_hp = sanft[0]
    p2_attack = sanft[1]
    p2_tempo = sanft[2]
    
if p2_wesen == 1:
    p2_hp = sanft[0]
    p2_attack = sanft[1]
    p2_tempo = sanft[2]
    
#Bestimmung der Reihenfolge
if random.randint(0, 1) == 0:
    print(p1_name + " beginnt!")
    current_pokemon = p1_name
    other_pokemon = p2_name
else:
    print(p2_name + " beginnt!")
    current_pokemon = p2_name
    other_pokemon = p1_name

# Kampfschleife 
while p1_hp > 0 and p2_hp > 0:
    # Der aktuelle Angreifer wird ausgewählt
    if current_pokemon == p1_name:
        attacker_name = p1_name
        defender_name = p2_name
        attacker_hp = p1_hp
        attacker_attack = p1_attack
        defender_hp = p2_hp
    else:
        attacker_name = p2_name
        defender_name = p1_name
        attacker_hp = p2_hp
        attacker_attack = p2_attack
        defender_hp = p1_hp
    
    # Angriffswerte berechnen und ausgeben
    attack_damage = attacker_attack
    defender_hp -= attack_damage
    print(attacker_name + " greift an und fügt " + defender_name + " " + str(attack_damage) + " Schaden zu!")

    # Angriffswechsel
    if current_pokemon == p1_name:
        current_pokemon = p2_name
        other_pokemon = p1_name
        p2_hp = defender_hp
    else:
        current_pokemon = p1_name
        other_pokemon = p2_name
        p1_hp = defender_hp
        
  # Siegerprüfung
    if defender_hp <= 0:
        print(defender_name + " ist besiegt!")
        break        
#Ende
