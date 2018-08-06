# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:28:20 2017

@author: Homework
"""
programmerName = "Matthew Zhong"
honorCode = "I have neither given nor received unauthorized assistance on this assignment."

import random
import time
import sys

#typeTable uses offensive type as key 1, defensive type as key 2, and returns
#damage multiplier
typeTable = {}
typeTable["normal"] = {"normal": 1, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 1,
         "fighting": 1,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 1,
         "bug": 1,
         "rock": 0.5,
         "ghost": 0,
         "dragon": 1,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["fire"] = {"normal": 1, 
         "fire": 0.5, 
         "water": 0.5, 
         "electric": 1, 
         "grass": 2,
         "ice": 2,
         "fighting": 1,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 1,
         "bug": 2,
         "rock": 0.5,
         "ghost": 1,
         "dragon": 0.5,
         "dark": 1,
         "steel": 2,
         "typeless": 1}
    
typeTable["water"] = {"normal": 1, 
         "fire": 2, 
         "water": 0.5, 
         "electric": 1, 
         "grass": 0.5,
         "ice": 1,
         "fighting": 1,
         "poison": 1,
         "ground": 2,
         "flying": 1,
         "psychic": 1,
         "bug": 1,
         "rock": 2,
         "ghost": 1,
         "dragon": 0.5,
         "dark": 1,
         "steel": 1,
         "typeless": 1}
    
typeTable["electric"] = {"normal": 1, 
         "fire": 1, 
         "water": 2, 
         "electric": 0.5, 
         "grass": 0.5,
         "ice": 1,
         "fighting": 1,
         "poison": 1,
         "ground": 0,
         "flying": 2,
         "psychic": 1,
         "bug": 1,
         "rock": 1,
         "ghost": 1,
         "dragon": 0.5,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["grass"] = {"normal": 1, 
         "fire": 0.5, 
         "water": 2, 
         "electric": 1, 
         "grass": 0.5,
         "ice": 1,
         "fighting": 1,
         "poison": 0.5,
         "ground": 2,
         "flying": 0.5,
         "psychic": 1,
         "bug": 0.5,
         "rock": 2,
         "ghost": 1,
         "dragon": 0.5,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["ice"] = {"normal": 1, 
         "fire": 0.5, 
         "water": 0.5, 
         "electric": 1, 
         "grass": 2,
         "ice": 0.5,
         "fighting": 1,
         "poison": 1,
         "ground": 2,
         "flying": 2,
         "psychic": 1,
         "bug": 1,
         "rock": 0.5,
         "ghost": 1,
         "dragon": 2,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["fighting"] = {"normal": 2, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 2,
         "fighting": 1,
         "poison": 0.5,
         "ground": 1,
         "flying": 0.5,
         "psychic": 0.5,
         "bug": 0.5,
         "rock": 2,
         "ghost": 0,
         "dragon": 1,
         "dark": 2,
         "steel": 2,
         "typeless": 1}
    
typeTable["poison"] = {"normal": 1, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 2,
         "ice": 1,
         "fighting": 1,
         "poison": 0.5,
         "ground": 0.5,
         "flying": 1,
         "psychic": 1,
         "bug": 1,
         "rock": 0.5,
         "ghost": 0.5,
         "dragon": 1,
         "dark": 1,
         "steel": 0,
         "typeless": 1}
    
typeTable["ground"] = {"normal": 1, 
         "fire": 2, 
         "water": 1, 
         "electric": 2, 
         "grass": 0.5,
         "ice": 1,
         "fighting": 1,
         "poison": 2,
         "ground": 1,
         "flying": 0,
         "psychic": 1,
         "bug": 0.5,
         "rock": 2,
         "ghost": 1,
         "dragon": 1,
         "dark": 1,
         "steel": 2,
         "typeless": 1}
    
typeTable["flying"] = {"normal": 1, 
         "fire": 1, 
         "water": 1, 
         "electric": 0.5, 
         "grass": 2,
         "ice": 1,
         "fighting": 2,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 1,
         "bug": 2,
         "rock": 0.5,
         "ghost": 1,
         "dragon": 1,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["psychic"] = {"normal": 1, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 1,
         "fighting": 2,
         "poison": 2,
         "ground": 1,
         "flying": 1,
         "psychic": 0.5,
         "bug": 1,
         "rock": 1,
         "ghost": 1,
         "dragon": 1,
         "dark": 0,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["bug"] = {"normal": 1, 
         "fire": 0.5, 
         "water": 1, 
         "electric": 1, 
         "grass": 2,
         "ice": 1,
         "fighting": 0.5,
         "poison": 0.5,
         "ground": 1,
         "flying": 0.5,
         "psychic": 2,
         "bug": 1,
         "rock": 2,
         "ghost": 0.5,
         "dragon": 1,
         "dark": 2,
         "steel": 0.5,
         "typeless": 1}

typeTable["rock"] = {"normal": 1, 
         "fire": 2, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 2,
         "fighting": 0.5,
         "poison": 1,
         "ground": 0.5,
         "flying": 2,
         "psychic": 1,
         "bug": 2,
         "rock": 1,
         "ghost": 1,
         "dragon": 1,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["ghost"] = {"normal": 0, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 1,
         "fighting": 1,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 2,
         "bug": 1,
         "rock": 1,
         "ghost": 2,
         "dragon": 1,
         "dark": 0.5,
         "steel": 1,
         "typeless": 1}
    
typeTable["dragon"] = {"normal": 1, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 1,
         "fighting": 1,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 1,
         "bug": 1,
         "rock": 1,
         "ghost": 1,
         "dragon": 2,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["dark"] = {"normal": 1, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 1,
         "fighting": 0.5,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 2,
         "bug": 1,
         "rock": 1,
         "ghost": 2,
         "dragon": 1,
         "dark": 0.5,
         "steel": 1,
         "typeless": 1}
    
typeTable["steel"] = {"normal": 1, 
         "fire": 0.5, 
         "water": 0.5, 
         "electric": 0.5, 
         "grass": 1,
         "ice": 2,
         "fighting": 1,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 1,
         "bug": 1,
         "rock": 2,
         "ghost": 1,
         "dragon": 1,
         "dark": 1,
         "steel": 0.5,
         "typeless": 1}
    
typeTable["typeless"] = {"normal": 1, 
         "fire": 1, 
         "water": 1, 
         "electric": 1, 
         "grass": 1,
         "ice": 1,
         "fighting": 1,
         "poison": 1,
         "ground": 1,
         "flying": 1,
         "psychic": 1,
         "bug": 1,
         "rock": 1,
         "ghost": 1,
         "dragon": 1,
         "dark": 1,
         "steel": 1,
         "typeless": 1}

class Move:
    def __init__(self, typeString, damageAttribute, power, name):
        self.damageAttribute = damageAttribute #string
        self.power = power #float
        self.name = name #string
        self.typeString = typeString

class Pokemon: 
    
    def __init__(self, baseStatTotal, moves, type1String, type2String, name):
        self.type1 = type1String
        self.type2 = type2String
        self.moves = moves
        self.baseStatTotal = baseStatTotal
        self.isAlive = True
        self.name = name
        self.currentHP = baseStatTotal["HP"]
        
        
def weakTo(move, pokemon):
    offenseType = move.typeString
    
    defenseType1 = pokemon.type1
    defenseType2 = pokemon.type2
    
    multiplier1 = typeTable[offenseType][defenseType1]
    multiplier2 = typeTable[offenseType][defenseType2]
    
    damageMultiplier = multiplier1 * multiplier2
    
    return damageMultiplier

def victory(blueTeam, redTeam):
    
    numBlueRemaining = 0
    
    for poke in blueTeam:
        if blueTeam[poke].isAlive:
            numBlueRemaining+=1
    
    numRedRemaining = 0
    
    for poke in redTeam:
        if redTeam[poke].isAlive:
            numRedRemaining+=1
    
    if numBlueRemaining == 0:
        
        print("Blue: Dang it, I lost!")
        return False
    
    elif numRedRemaining == 0:
        
        print("Red: ...")
        print("**You lose...")
        return False
    
    return True

def damageCalculation(OffensivePokemon, DefensivePokemon, ChosenMove):
    
    rawDamage = 0
    multiplier = weakTo(ChosenMove, DefensivePokemon)
    
    if ChosenMove.damageAttribute == "physical":
        rawDamage = OffensivePokemon.baseStatTotal["ATK"] + ChosenMove.power - DefensivePokemon.baseStatTotal["DEF"]
        totalDamage = multiplier * rawDamage
        
    elif ChosenMove.damageAttribute == "special":
        rawDamage = OffensivePokemon.baseStatTotal["SPATK"] + ChosenMove.power - DefensivePokemon.baseStatTotal["SPDEF"]
        totalDamage = multiplier * rawDamage
        
    else:
        totalDamage = ChosenMove.power
        
    if totalDamage < 0:
        totalDamage = 0
    
    return totalDamage
    
def doDamage(TargetPokemon, damage, Move):
    
    if Move.damageAttribute == "physical" or Move.damageAttribute == "special":
        TargetPokemon.currentHP -= damage
    else:
        for statName in TargetPokemon.baseStatTotal.keys():
            if not (statName == "HP"):
                TargetPokemon.baseStatTotal[statName] *= damage
    pass

def displayEffectiveness(TargetPokemon, Move):
    multiplier = weakTo(Move, TargetPokemon)
    if multiplier > 1:
        time.sleep(1)
        print ("**It's super effective!")
        time.sleep(1)
    elif multiplier < 1:
        time.sleep(1)
        print("**It's not very effective...")
        time.sleep(1)
    pass
    

WingAttack = Move("flying", "physical", 60, "Wing Attack")
PsyBeam = Move("psychic", "special", 65, "PsyBeam")
Psychic = Move("psychic", "special", 95, "Psychic")
Reflect = Move("psychic", "auxillary", 0.8, "Reflect")
Leer = Move("normal", "auxillary", 0.8, "Leer")
TailWhip = Move("normal", "auxillary", 0.8, "Tail Whip")
HornDrill = Move("normal", "physical", 999, "Horn Drill")
Stomp = Move("normal", "physical", 65, "Stomp")
Barrage = Move("normal", "physical", 75, "Barrage")
DragonRage = Move("dragon", "special", 65, "Dragon Rage")
HydroPump = Move("water", "special", 110, "Hydro Pump")
HyperBeam = Move("normal", "special", 150, "Hyper Beam")
FireBlast = Move("fire", "special", 120, "Fire Blast")
Slash = Move("normal", "physical", 80, "Slash")
QuickAttack = Move("normal", "physical", 60, "Quick Attack")
Thunderbolt = Move("electric", "special", 90, "Thunderbolt")
Thunder = Move("electric", "special", 120, "Thunder")
MudSlap = Move("ground", "special", 20, "Mud-Slap")
Swift = Move("normal", "special", 60, "Swift")
Amnesia = Move("psychic", "auxilary", 2, "Amnesia")
BodySlam = Move("normal", "physical", 85, "Body Slam")
GigaDrain = Move("grass", "special", 90, "Giga Drain")
SolarBeam = Move("grass", "special", 150, "SolarBeam")
Flamethrower = Move("fire", "special", 90, "Flamethrower")
Blizzard = Move("ice", "special", 120, "Blizzard")
Surf = Move("water", "special", 90, "Surf")

moveDictionary = {"Wing Attack": WingAttack,
                  "PsyBeam": PsyBeam,
                  "Psychic": Psychic,
                  "Reflect": Reflect,
                  "Leer": Leer,
                  "Tail Whip": TailWhip,
                  "Horn Drill": HornDrill,
                  "Stomp": Stomp,
                  "Barrage": Barrage,
                  "Dragon Rage": DragonRage,
                  "Hydro Pump": HydroPump,
                  "Hyper Beam": HyperBeam,
                  "Fire Blast": FireBlast,
                  "Slash": Slash,
                  "Quick Attack": QuickAttack,
                  "Thunderbolt": Thunderbolt,
                  "Thunder": Thunder,
                  "Mud-Slap": MudSlap,
                  "Swift": Swift,
                  "Amnesia": Amnesia,
                  "Body Slam": BodySlam,
                  "Giga Drain": GigaDrain,
                  "SolarBeam": SolarBeam,
                  "Flamethrower": Flamethrower,
                  "Blizzard": Blizzard,
                  "Surf": Surf}

Pidgeot = Pokemon({"HP": 190, "ATK": 145, "DEF": 139, "SPATK": 134, "SPDEF": 134, "SPEED": 157}, [WingAttack], "flying", "normal", "Pidgeot")
Alakazam = Pokemon({"HP": 162, "ATK": 112, "DEF": 106, "SPATK": 135, "SPDEF": 85, "SPEED": 120}, [PsyBeam, Psychic, Reflect], "psychic", "typeless", "Alakazam")
Rhydon = Pokemon({"HP": 212, "ATK": 130, "DEF": 189, "SPATK": 106, "SPDEF": 106, "SPEED": 101}, [Slash, MudSlap, HornDrill], "ground", "rock", "Rhydon")
Exeggutor = Pokemon({"HP": 202, "ATK": 161, "DEF": 150, "SPATK": 194, "SPDEF": 128, "SPEED": 117}, [Stomp, Barrage], "grass", "psychic", "Exeggutor")
Gyarados = Pokemon({"HP": 202, "ATK": 194, "DEF": 144, "SPATK": 123, "SPDEF": 167, "SPEED": 81}, [DragonRage, HydroPump, HyperBeam, Leer], "water", "flying", "Gyarados")
Arcanine = Pokemon({"HP": 197, "ATK": 178, "DEF": 145, "SPATK": 167, "SPDEF": 145, "SPEED": 161}, [Leer, FireBlast, Flamethrower], "fire", "typeless", "Arcanine")

Pikachu = Pokemon({"HP": 142, "ATK": 117, "DEF": 90, "SPATK": 112, "SPDEF": 101, "SPEED": 156}, [QuickAttack, Thunderbolt, Thunder], "electric", "typeless", "Pikachu")
Espeon = Pokemon({"HP": 172, "ATK": 128, "DEF": 123, "SPATK": 200, "SPDEF": 161, "SPEED": 178}, [MudSlap, Swift, Reflect, Psychic], "psychic", "typeless", "Espeon")
Snorlax = Pokemon({"HP": 267, "ATK": 178, "DEF": 128, "SPATK": 128, "SPDEF": 178, "SPEED": 90}, [Amnesia, BodySlam], "normal", "typeless", "Snorlax")
Venusaur = Pokemon({"HP": 187, "ATK": 147, "DEF": 148, "SPATK": 167, "SPDEF": 167, "SPEED": 145}, [GigaDrain, SolarBeam], "grass", "poison", "Venusaur")
Charizard = Pokemon({"HP": 185, "ATK": 149, "DEF": 143, "SPATK": 177, "SPDEF": 150, "SPEED": 167}, [Flamethrower, WingAttack, FireBlast], "fire", "flying", "Charizard")
Blastoise = Pokemon({"HP": 186, "ATK": 148, "DEF": 167, "SPATK": 150, "SPDEF": 172, "SPEED": 143}, [Surf, Blizzard, HydroPump], "water", "typeless", "Blastoise")

blueTeam = {"Pidgeot": Pidgeot, 
            "Alakazam": Alakazam, 
            "Arcanine": Arcanine, 
            "Exeggutor": Exeggutor, 
            "Gyarados": Gyarados, 
            "Rhydon": Rhydon}
redTeam = {"Pikachu": Pikachu, 
           "Charizard": Charizard, 
           "Venusaur": Venusaur, 
           "Blastoise": Blastoise, 
           "Snorlax": Snorlax, 
           "Espeon": Espeon}

print("Blue: You're gonna lose, you little ameteur! I'm Blue, and I'm the champion of the Indigo League!")
time.sleep(1)
print("Red: ...")
time.sleep(1)
print("Blue: At a loss of words, I see. Well, let's get this over with!")
time.sleep(1)
print("**You are playing as Red.\n")
time.sleep(1)

battleEngaged = True

#Automatically send out the first pokemon in each team
blueCurrent = Pidgeot
redCurrent = Pikachu

blueCurrentAlive = True
redCurrentAlive = True

blueCurrentMoveList = []
redCurrentMoveList = []

for move in blueCurrent.moves:
    blueCurrentMoveList.append(move.name)

for move in redCurrent.moves:
    redCurrentMoveList.append(move.name)

time.sleep(1)
print("Blue: Go, Pidgeot!")
time.sleep(1)
print("Red: Go, Pikachu!")
time.sleep(1)

print("\n**Your team is:")

for name in redTeam.keys():
    print("*" + name)
    time.sleep(0.3)

time.sleep(0.5)
print("**Enter choices as they appear, with proper capitalization.")
time.sleep(0.5)

redRemaining = {}
blueRemaining = {}

while battleEngaged:
    
    #victory conditions
    
    battleEngaged = victory(blueTeam, redTeam)
    
    redRemaining = {poke 
                    for poke in redTeam
                    if redTeam[poke].isAlive}
    
    blueRemaining = {poke
                     for poke in blueTeam
                     if blueTeam[poke].isAlive}
    
    if len(redRemaining) == 0 or len(blueRemaining) == 0:
        print("The battle has finished!")
        battleEngaged = False
    
    #Battle information conditions
    #print("Blue has " + str(numBlueRemaining) + " pokemon remaining.")
    #print("Red has " + str(numRedRemaining) + " pokemon remaining.")
    
    #Swap to new pokemon randomly
    if not blueCurrent.isAlive:
        
        while not blueCurrent.isAlive:
            blueCurrentKey = random.choice(list(blueTeam))
            blueCurrent = blueTeam[blueCurrentKey]
        
        print("Blue: Go, " + blueCurrent.name + "!")
        time.sleep(1)
        
        blueCurrentMoveList = []
        for move in blueCurrent.moves:
            blueCurrentMoveList.append(move.name)
    
    #determine if battle continues, unused code
    #if not redCurrent.isAlive:
        
    #    while not redCurrent.isAlive:
    #        redCurrentKey = random.choice(list(redTeam))
    #        redCurrent = redTeam[redCurrentKey]
    #    
    #    print("Red: Go, " + redCurrent.name + "!")
    #    time.sleep(1)
        
    #    redCurrentMoveList = []
    #    for move in redCurrent.moves:
    #        redCurrentMoveList.append(move.name)


    while not redCurrent.isAlive:
        
        time.sleep(0.5)
        print("**Enter a pokemon which has not fainted you would like to switch to.")
        time.sleep(1)
        print("**Choices:")
        time.sleep(1)
        
        for poke in list(redRemaining):
            print("*" + poke)
            time.sleep(0.3)
        
        redCurrentKey = input("Choice: ")
        
        if redCurrentKey not in list(redRemaining):
            
            time.sleep(0.5)
            print("**Invalid input. Try again.")
            time.sleep(0.5)
            
        else:
            
            redCurrent = redTeam[redCurrentKey]
            
            time.sleep(0.5)
            print("Red: Go, " + redCurrent.name + "!")
            time.sleep(1)
            
            redCurrentMoveList = []
            for move in redCurrent.moves:
                redCurrentMoveList.append(move.name)
    
    #Make a move
    isValidMoveInput = False
    
    print("**Your " + redCurrent.name + " currently has " + str(int(100 * redCurrent.currentHP/redCurrent.baseStatTotal["HP"])) + "% HP remaining.")
    time.sleep(1)
    print("**Blue's " + blueCurrent.name + " currently has " + str(int(100 * blueCurrent.currentHP/blueCurrent.baseStatTotal["HP"])) + "% HP remaining.")
    time.sleep(1)
    
    while not isValidMoveInput:
        
        print("\nWhat will " + redCurrent.name + " do?")
        time.sleep(1)
        print("\nMoves: \n---------------------------------")
        
        for move in redCurrent.moves:
            print(move.name)
        
        time.sleep(1)
        redChosenMove = input("Choice: ")
        print()
        
        if redChosenMove in redCurrentMoveList:
            isValidMoveInput = True
        else:
            print("\nInvalid move. Try again.")
    
    #blue chosen move
    blueChosenMove = random.choice(blueCurrentMoveList)
    
    #damage calculation and turn decision tree
    redGoesFirst = (redCurrent.baseStatTotal["SPEED"] >= blueCurrent.baseStatTotal["SPEED"])
    
    damageAgainstBlue = damageCalculation(redCurrent, blueCurrent, moveDictionary[redChosenMove])
    damageAgainstRed = damageCalculation(blueCurrent, redCurrent, moveDictionary[blueChosenMove])
    
    if redGoesFirst: 
        
        print("**Your " + redCurrent.name + " is faster than Blue's " + blueCurrent.name + "!")
        time.sleep(1)
        print("**Your " + redCurrent.name + " attacks first!\n")
        time.sleep(1)
        print("**Your " + redCurrent.name + " uses " + redChosenMove + "!")
        time.sleep(2)
        
        doDamage(blueCurrent, damageAgainstBlue, moveDictionary[redChosenMove])
        displayEffectiveness(blueCurrent, moveDictionary[redChosenMove])
        
        print("**Your " + redCurrent.name + " deals " + str(int(100 * damageAgainstBlue/blueCurrent.baseStatTotal["HP"])) + "% of " + blueCurrent.name + "'s HP.")
        time.sleep(2)
        
        if blueCurrent.currentHP <= 0:
            
            time.sleep(1)
            print("**Blue's " + blueCurrent.name + " fainted!")
            time.sleep(1)
            print("Blue: Oh no! My " + blueCurrent.name + "!\n")
            time.sleep(1)
            
            blueCurrent.isAlive = False
            
        
        else:
            
            print("**Blue's " + blueCurrent.name + " uses " + blueChosenMove + "!")
            time.sleep(1)
            
            doDamage(redCurrent, damageAgainstRed, moveDictionary[blueChosenMove])
            displayEffectiveness(redCurrent, moveDictionary[blueChosenMove])
            time.sleep(2)
            
            print("**Blue's " + blueCurrent.name + " deals " + str(int(100 * damageAgainstRed/redCurrent.baseStatTotal["HP"])) + "% of " + redCurrent.name + "'s HP.\n")            
            
            if redCurrent.currentHP <= 0:
                
                time.sleep(1)
                print("**Your " + redCurrent.name + " fainted!")
                time.sleep(1)
                print("Red: ...\n")
                time.sleep(1)
                
                redCurrent.isAlive = False
            
    else:
        
        print("**Blue's " + blueCurrent.name + " is faster than Red's " + redCurrent.name + "!")
        time.sleep(1)
        print("**Blue's " + blueCurrent.name + " attacks first!\n")
        time.sleep(1)
        print("**Blue's " + blueCurrent.name + " uses " + blueChosenMove + "!")
        time.sleep(2)
        
        doDamage(redCurrent, damageAgainstRed, moveDictionary[blueChosenMove])
        displayEffectiveness(redCurrent, moveDictionary[blueChosenMove])
        time.sleep(2)
        
        print("**Blue's " + blueCurrent.name + " deals " + str(int(100 * damageAgainstRed/redCurrent.baseStatTotal["HP"])) + "% of " + redCurrent.name + "'s HP.\n")
        
        if redCurrent.currentHP <= 0:
            
            time.sleep(1)
            print("**Your " + redCurrent.name + " fainted!")
            time.sleep(1)
            print("Red: ...\n")
            time.sleep(1)
            
            redCurrent.isAlive = False
        
        else:
            
            time.sleep(1)
            print("**Your " + redCurrent.name + " uses " + redChosenMove + "!")
            time.sleep(2)
            
            doDamage(blueCurrent, damageAgainstBlue, moveDictionary[redChosenMove])
            displayEffectiveness(blueCurrent, moveDictionary[redChosenMove])
            time.sleep(2)
            
            print("**Your " + redCurrent.name + " deals " + str(int(100 * damageAgainstBlue/blueCurrent.baseStatTotal["HP"])) + "% of " + blueCurrent.name + "'s HP.\n")
            
            if blueCurrent.currentHP <= 0:
                
                time.sleep(1)
                print("**Blue's " + blueCurrent.name + " fainted!")
                time.sleep(1)
                print("Blue: Oh no! My " + blueCurrent.name + "!\n")
                time.sleep(1)
                
                blueCurrent.isAlive = False

sys.exit()    

