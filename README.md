# pokemon-ripoff-version
A simple recreation of an iconic battle in the Pokemon games, with user input

## Installation
Simply run `python PokemonRipoffVersion.py` from the command line. This version supports Python 3.

## Usage
The Pokemon games have a turn-based battle system based on a more complex version of rock-paper-scissors. In this application, there are two teams:

1.) Blue

Blue is the opponent of this game. He has a team of:

```
Alakazam, Eggsecutor, Arcanine, Gyarados, Rhydon, Pidgeot
```

2.) Red

You play as Red in this game. Your team is:

```
Pikachu, Espeon, Charizard, Blastoise, Venusaur, Snorlax
```

After the initial battle prompt, here is what your command line will show:

```
Blue: You're gonna lose, you little ameteur! I'm Blue, and I'm the champion of the Indigo League!
Red: ...
Blue: At a loss of words, I see. Well, let's get this over with!
**You are playing as Red.

Blue: Go, Pidgeot!
Red: Go, Pikachu!

**Your team is:
*Pikachu
*Charizard
*Venusaur
*Blastoise
*Snorlax
*Espeon
**Enter choices as they appear, with proper capitalization.
**Your Pikachu currently has 100% HP remaining.
**Blue's Pidgeot currently has 100% HP remaining.

What will Pikachu do?

Moves:
---------------------------------
Quick Attack
Thunderbolt
Thunder
Choice:
```

Each move has a different type. Each Pokemon has different types. Experiment with which types do more damage against which Pokemon! A full type-effectiveness table can be found on https://bulbapedia.bulbagarden.net/wiki/Type#Type_effectiveness .

In this case, Electric type moves like Thunderbolt are a great choice against Pidgeot, so I enter the following:

```
What will Pikachu do?

Moves:
---------------------------------
Quick Attack
Thunderbolt
Thunder
Choice: Thunderbolt
```

The program then determines which Pokemon goes first, calculates the potential damage eahc Pokemon would have dealt to the opposing side, and adjusts their current HP (HitPoints) properly.

```
**Blue's Pidgeot is faster than Red's Pikachu!
**Blue's Pidgeot attacks first!

**Blue's Pidgeot uses Wing Attack!
**It's not very effective...
**Blue's Pidgeot deals 40% of Pikachu's HP.

**Your Pikachu uses Thunderbolt!
**It's super effective!
**Your Pikachu deals 71% of Pidgeot's HP.

**Your Pikachu currently has 59% HP remaining.
**Blue's Pidgeot currently has 28% HP remaining.

What will Pikachu do?

Moves:
---------------------------------
Quick Attack
Thunderbolt
Thunder
Choice:
```

Let's suppose I've defeated the other Pidgeot, like so:

```
**Blue's Pidgeot is faster than Red's Pikachu!
**Blue's Pidgeot attacks first!

**Blue's Pidgeot uses Wing Attack!
**It's not very effective...
**Blue's Pidgeot deals 40% of Pikachu's HP.

**Your Pikachu uses Thunder!
**It's super effective!
**Your Pikachu deals 103% of Pidgeot's HP.

**Blue's Pidgeot fainted!
Blue: Oh no! My Pidgeot!
```

Blue will automatically send out the next Pokemon he has, if it is available.

```
Blue: Go, Exeggutor!
**Your Pikachu currently has 19% HP remaining.
**Blue's Exeggutor currently has 100% HP remaining.

What will Pikachu do?

Moves:
---------------------------------
Quick Attack
Thunderbolt
Thunder
Choice:
```

After a while, your Pokemon in battle may faint. When this happens, the following prompt is shown:

```
**Your Pikachu is faster than Blue's Exeggutor!
**Your Pikachu attacks first!

**Your Pikachu uses Quick Attack!
**Your Pikachu deals 13% of Exeggutor's HP.
**Blue's Exeggutor uses Stomp!
**Blue's Exeggutor deals 95% of Pikachu's HP.

**Your Pikachu fainted!
Red: ...

**Enter a pokemon which has not fainted you would like to switch to.
**Choices:
*Snorlax
*Blastoise
*Charizard
*Espeon
*Venusaur
Choice:
```

In this case, Charizard is a great Fire Pokemon against Eggsecutor, a Grass/Psychic Pokemon. It follows that my choice is:

```
Choice: Charizard
```

The battle will continue to cycle until either Red or Blue has no more remaining Pokemon left to fight. Experiment with which Pokemon are great against which others!
