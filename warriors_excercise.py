"""
Simular una pelea entre los guerreros Z, en el cual van a tener las siguientes clases:

- Luchador: clase concreta de la cual van a instanciar todos los guerreros y va a contener

  - Atributos: 
    - Nombre (del luchador): str
    - Ki: int
    - SSJ: bool
    - Ataque: int
    - Defensa: int
    - Vida: int 
    
  - Metodos: 
    - Atacar
    
- Batalla: clase que vamos a utilizar como menu, donde va a recibir dos luchadores y va a comenzar la batalla por turnos

- Ejemplo
  - Goku:
    - nombre: Goku
    - ki: 9000
    - ssj: True
    - ataque: 1000
    - defensa: 500
    - vida: 1800
    
  - MajinBoo: 
    - nombre: majin boo
    - ki: 7500
    - ssj: False
    - ataque: 700 
    - defensa: 700
    - vida: 1500
"""

import time

class Fighter:
  def __init__(self, name, ki, ssj, attack, defense, life):
    self.name = name
    self.ki = ki
    self.ssj = ssj
    self.attack = attack
    self.defense = defense
    self.life = life
    print(name, 'is ready to fight!')
    
  def fighter_attack(self, enemy): # enemigo es el paso por referencia
    attack_difference = self.attack - enemy.defense
    enemy.life = enemy.life - attack_difference
     
    print(f'{self.name} attacked {enemy.name} with {attack_difference} of attack')
    
class Battle:
  turn = '1' # control para cambiar el turno del luchador
  
  def __init__(self, fighter_one, fighter_two):
    self.fighter_one = fighter_one
    self.fighter_two = fighter_two
    
  def start_battle(self):
    while self.fighter_one.life > 0 and self.fighter_two.life > 0: # mientras ambos sigan con vida
      time.sleep(0.5) # esto es para ver el tiempo de la batalla
      if self.turn == '1':
        self.fighter_one.fighter_attack(self.fighter_two)
        self.turn = '2' # cambia el control del turno 
      else:
        self.fighter_two.fighter_attack(self.fighter_one)
        self.turn = '1'
    if self.fighter_one.life <= 0:
      print(f'The winner is {self.fighter_one.name}')
    else:
      print(f'The winner is {self.fighter_two.name}')
            

goku = Fighter('Goku', 9000, True, 1000, 500, 1800)
majinboo = Fighter('Majin Boo', 7500, False, 700, 700, 1500)

Battle(goku, majinboo).start_battle()