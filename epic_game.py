import random
import time
from clear_screen import clear
from termcolor import colored
from colorama import init
from audio import *

init()

i_want_sleep = ['.', ',', '-','!','?', '~']

def n(text, color = "white", end = '\n'): #normal print no visual novel style
    print(colored(text, color), end = '')
    print(end=end, flush=True)

def lmao(text, color="white", end='\n'): #halo text visual novel mwehehehee
    for char in text:
        if char in i_want_sleep:
            print(colored(char, color), end='', flush=True)
            time.sleep(0.3)
        else:
            print(colored(char, color), end='', flush=True)
            time.sleep(0.05)
    print(end=end, flush=True)
    
class Character:
    def __init__(self, name, hp, atk, defense, crit_rate, crit_dmg, break_effect, element):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.original_hp = hp
        self.atk = atk
        self.original_atk = atk
        self.defense = defense
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg
        self.break_effect = break_effect
        self.energy = 0
        self.shield = 0
        self.buffs = {}
        self.dmg_bonus = 0
        self.element = element
        self.frozen = False
        self.shield_value = 0

    def check_stats(self):
        clear()
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.atk}")
        print(f"Defense: {self.defense}")
        print(f"Crit Rate: {self.crit_rate}%")
        print(f"Crit Damage: {self.crit_dmg}%")
        print(f"Break Effect: {self.break_effect}%")
        print(f"Shield: {self.shield}")
        print(f"Buffs: {self.buffs}")
        time.sleep(1)
        clear()

class FuXuan(Character):
    def __init__(self):
        super().__init__("Fu Xuan", 10000, 1000, 1000, 20, 80, 50 ,"Quantum")
        self.talent_counter = 1
        
    def energize(self, energy):
        self.energy += energy
        if self.energy > 135:
            self.energy = 135
        
    def basic_attack(self, target):
        clear()
        fuxuan_basicatk = random.choice(fu_xuan_basicatk)
        if fuxuan_basicatk == fu_xuan_basicatk1:
            fu_xuan_basicatk1.play()
            lmao("\"With all my power.. Scry the future!\"", color = "magenta")
        elif fuxuan_basicatk == fu_xuan_basicatk2:
            fu_xuan_basicatk2.play()
            lmao("\"In formation, in accordance!\"", color = "magenta")
        sound_effectfxb.play()
        sound_effectfxb2.play()
        
        damage = self.max_hp * 0.5
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
        
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))

        crit_roll = random.randint(0, 100)
        if crit_roll < self.crit_rate:
            damage += damage * (self.crit_dmg/100)
            
        target.hp -= damage
        print(f"{self.name} dealt {damage:.0f} damage to {target.name}!")
        target.toughness -= 10
        time.sleep(1)
        self.energize(20)
        check_others(game.fu_xuan, target)
    
    def skill(self, party):
        clear()
        fuxuan_skill = random.choice(fu_xuan_skill)
        if fuxuan_skill == fu_xuan_skill1:
            fu_xuan_skill1.play()
            lmao("\"Converge... and awaken!\"", color = "magenta")
        elif fuxuan_skill == fu_xuan_skill2:
            fu_xuan_skill2.play()
            lmao("\"Together... as one!\"", color = "magenta")
        sound_effectfxs.play()
            
        for target in party:
            if 'Matrix of Prescience' not in target.buffs:
                hp_increase = self.original_hp * 0.06
                target.max_hp += hp_increase
                target.hp += hp_increase
                target.crit_rate += 12
                target.buffs['Matrix of Prescience'] = 3
                print(f"{target.name}'s HP increased to {target.hp}, Crit Rate to {target.crit_rate}!")
                self.energize(30)
            
            else:
                target.buffs['Matrix of Prescience'] = 3
                print("Matrix of Prescience's effect has been refreshed!")
                self.energize(50)
                
        time.sleep(1)
                 
    def ultimate(self, party, target):
        clear()
        if self.energy == 135:
            fu_xuan_ultimate1.play()
            lmao("\"All things in this world have their laws.\"", color = "magenta")
            fu_xuan_ultimate2.play()
            lmao("\"Yet stratagems... constellations.. are human.. creations! Hmph!\"", color = "magenta")
            
            damage = self.max_hp
            
            if self.dmg_bonus > 0:
                damage += damage * self.dmg_bonus/100
                
            damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
            
            crit_roll = random.randint(0, 100)
            if crit_roll < self.crit_rate:
                damage += damage * (self.crit_dmg/100)
                    
            target.hp -= damage
            print(f"{self.name} dealt {damage:.0f} damage to {target.name}!")
            target.toughness -= 20
            
            for character in party:
                HP_recovery = self.max_hp * 0.05 + 133
                character.hp += HP_recovery
                if character.hp > target.max_hp:
                    character.hp = target.max_hp
                print(f"{character.name} recovers {HP_recovery} HP!")
                
            sound_effectfxu.play()
            sound_effectfxu2.play()
            time.sleep(1)
            self.energy = 0
            self.energize(5)
            self.talent_counter += 1
            if self.talent_counter > 2:
                self.talent_counter = 2
            self.talent()
            check_others(game.fu_xuan, target)
        
        else:
            n("Not enough energy!", color = "red")   
            time.sleep(1)
        
    def talent(self):
        if self.hp < self.max_hp * 0.5 and self.talent_counter > 0:
            missing_hp = self.max_hp - self.hp
            self.hp += missing_hp * 0.9
            print(f"{self.name} recovers {missing_hp * 0.9} HP!")
            self.talent_counter -= 1
              
    def skill_turn_check(self):
        for target in game.class_list:
            if "Matrix of Prescience" in target.buffs:
                target.buffs["Matrix of Prescience"] -= 1
                if target.buffs["Matrix of Prescience"] == 0:
                    target.crit_rate -= 12
                    target.max_hp -= self.original_hp * 0.06
                    if target.hp > target.max_hp:
                        target.hp = target.max_hp
                    del target.buffs["Matrix of Prescience"]
                    print(f"{target.name}'s Matrix of Prescience has expired!")
                    time.sleep(1)
                    
class Tingyun(Character):
    def __init__(self):
        super().__init__("Tingyun", 3000, 3000, 1000, 10, 70, 50, "Lightning")
        self.benediction = False
        self.benediction_target = None
        self.previous_target_atk_bonus = 0
        
    def energize(self, energy):
        self.energy += energy
        if self.energy > 130:
            self.energy = 130
        
    def basic_attack(self, target):
        clear()
        tingyun_basicatk.play()
        lmao("\"..Chill out!\"", color = "light_magenta")
        sound_effectqqb.play()
        
        damage = self.atk
        damage += damage * 0.4
    
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
            
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
        
        crit_roll = random.randint(0, 100)
        if crit_roll < self.crit_rate:
            damage += damage * (self.crit_dmg/100)
            
        target.hp -= damage
        print(f"{self.name} dealt {damage:.0f} damage to {target.name}!")
        target.toughness -= 10
        time.sleep(1)
        self.energize(20)
        self.talent(target)
    
    def skill(self, party):
        print("Choose a member by number: ")
        for i, character in enumerate(party, start=1):
            print(f"{i}. {character.name}")
            
        while True:
            choice = int(input("Your choice: ")) - 1
            if 0 <= choice < len(party):
                
                ty_skill = random.choice(tingyun_skill)
                ty_skill.play()
                if ty_skill == tingyun_skill1:
                    lmao("\"Evils Begone~\"", color = "magenta")
                elif ty_skill == tingyun_skill2:
                    lmao("\"All the best~\"", color = "magenta")
                    
                target = party[choice]
                
                if 'Benediction' in target.buffs:
                    print(f"{target.name} already has Benediction. Refreshing its duration!")
                    target.buffs['Benediction'] = 3
                else:   
                    for char in party:
                        if 'Benediction' in char.buffs:
                            del char.buffs['Benediction']
                            char.atk -= self.previous_target_atk_bonus
                            print(f"{char.name}'s Benediction has been removed.")

                    atk_increase = target.original_atk * 0.5
                    if atk_increase > self.original_atk * 0.25:
                        atk_increase = self.original_atk * 0.25
                    sound_effectfxs.play()
                    self.benediction_target = target
                    self.benediction = True
                    target.atk += atk_increase
                    target.buffs['Benediction'] = 3
                    self.previous_target_atk_bonus = atk_increase
                    print(f"{target.name}'s ATK increased to {target.atk} and Benediction applied!")

                self.energize(30)
                time.sleep(1)
                break
            else:
                lmao("\"Who?\"", color = "light_magenta")
                time.sleep(1)
            
    def ultimate(self, party):   
        if self.energy == 130:
            tingyun_ultimate1.play()
            lmao("\"A thousand wonders, to raise your spirits~\"", color = "light_magenta")
                    
            print("Choose a member by number: ")
            for i, character in enumerate(party, start=1):
                print(f"{i}. {character.name}")
                
            while True:
                choice = int(input("Your choice: ")) - 1           
                if 0 <= choice < len(party):
                    
                    tingyun_ultimate2.play()
                    lmao("\"Good omens.... fight as one!\"", color = "light_magenta")
                    
                    target = party[choice]
                    target.energize(50)
                    target.buffs['Damage Bonus (Tingyun)'] = 2
                    target.dmg_bonus += 50
                    sound_effectfxs.play()
                    print(f"{target.name}'s energy increased by 50, Damage Bonus + 50%")
                    self.energy = 0
                    self.energize(5)
                    time.sleep(1)
                    break
                    
                else:
                    lmao("\"Who?\"", color = "light_magenta")
                    time.sleep(1)
        else:
            n("Not enough energy!", color = "red")   
            time.sleep(1)
            
    def talent(self, target):
        if self.benediction == True:
            extra_damage = self.benediction_target.atk * 0.66
            target.hp -= extra_damage
            n(f"Tingyun dealt extra {extra_damage} damage to {target.name}.")
            time.sleep(1)
    
class Natasha(Character):
    def __init__(self):
        super().__init__("Natasha", 6000, 1000, 1000, 10, 60, 50, "Physical")
        
    def energize(self, energy):
        self.energy += energy
        if self.energy > 90:
            self.energy = 90
        
    def basic_attack(self, target):
        clear()
        
        nat_basicatk = random.choice(natasha_basicatk)
        if nat_basicatk == natasha_basicatk1:
            natasha_basicatk1.play()
            lmao("\"You're in bad shape.\"", color = "grey")
        elif nat_basicatk == natasha_basicatk2:
            natasha_basicatk2.play()
            lmao("\"Savor the figure of life.\"", color = "grey")
        elif nat_basicatk == natasha_basicatk3:
            natasha_basicatk3.play()
            lmao("\"Naptime.\"", color = "grey")
            
        sound_effectqqb.play()
        
        damage = self.atk
    
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
            
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
        
        crit_roll = random.randint(0, 100)
        if crit_roll < self.crit_rate:
            damage += damage * (self.crit_dmg/100)
            
        target.hp -= damage
        print(f"{self.name} dealt {damage:.0f} damage to {target.name}!")
        target.toughness -= 10
        time.sleep(1)
        self.energize(20)
        check_others(game.natasha, target)
        
    def skill(self, party):
        print("Choose a member by number: ")
        for i, character in enumerate(party, start=1):
            print(f"{i}. {character.name}")
            
        while True:
            choice = int(input("Your choice: ")) - 1
            if 0 <= choice < len(party):
                
                nat_skill = random.choice(natasha_skill)
                nat_skill.play()
                if nat_skill == natasha_skill1:
                    lmao("\"Here comes the medicine.\"", color = "grey")
                elif nat_skill == natasha_skill2:
                    lmao("\"All better now?\"", color = "grey") 
                sound_effectfxs.play()
                    
                target = party[choice]
                hp_healed = self.max_hp * 0.105 + 280
                hp_healed += hp_healed * 0.1
                hp_healed = self.talent(hp_healed, target)
                target.hp += hp_healed
                
                if target.hp > target.max_hp:
                    target.hp = target.max_hp
                    
                if 'Natasha Skill Healing' in target.buffs:
                    print(f"Refreshing {target.name}'s turn healing duration!")

                target.buffs['Natasha Skill Healing'] = 3
                print(f"Healed {target.name} by {hp_healed} HP!")

                self.energize(30)
                time.sleep(1)
                break
            else:
                lmao("\"Who?\"", color = "light_magenta")
                time.sleep(1)
            
    def ultimate(self, party):   
        if self.energy == 90:
            natasha_ultimate1.play()
            lmao("\"..Just in time...\"", color = "grey")
            natasha_ultimate2.play()
            lmao("\"Just a little something.... Mhm~.. Think nothing of it.\"", color = "grey")
            sound_effectfxs.play()
            
            hp_healed = self.max_hp * 0.138 + 368
            hp_healed += hp_healed * 0.1
            for target in party: 
                hp_healed = self.talent(hp_healed, target)
                target.hp += hp_healed
                if target.hp > target.max_hp:
                    target.hp = target.max_hp
                print(f"{target.name}'s recovered {hp_healed:.2f} HP.")
                
            self.energy -= 90
            time.sleep(1)
            self.energize(5)
            
        else:
            n("Not enough energy!", color = "red")   
            time.sleep(1)
            
    def talent(self, hp_healed, target):
        if target.hp <= target.max_hp * 0.3:
            hp_healed += hp_healed * 0.5
        return hp_healed
   
class March7th(Character):
    def __init__(self):
        super().__init__("March 7th", 3000, 1000, 4000, 10, 50, 50, "Ice")
        self.shield_value = 0
        self.talent_counter = 0
        
    def energize(self, energy):
        self.energy += energy
        if self.energy > 120:
            self.energy = 120
        
    def basic_attack(self, target):
        clear()
        
        march7th_basicatk.play()
        lmao("\"Watch this!\"", color = "cyan")
            
        sound_effectqqb.play()
        
        damage = self.atk
    
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
            
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
        
        crit_roll = random.randint(0, 100)
        if crit_roll < self.crit_rate:
            damage += damage * (self.crit_dmg/100)
            
        target.hp -= damage
        print(f"{self.name} dealt {damage:.0f} damage to {target.name}!")
        target.toughness -= 10
        time.sleep(1)
        self.energize(20)
        check_others(game.march_7th, target)
        
    def skill(self, party):
        print("Choose a member by number: ")
        for i, character in enumerate(party, start=1):
            print(f"{i}. {character.name}")
            
        while True:
            choice = int(input("Your choice: ")) - 1
            if 0 <= choice < len(party):
                
                march_skill = random.choice(march7th_skill)
                march_skill.play()
                if march_skill == march7th_skill1:
                    lmao("\"With me out here, how can we lose~\"", color = "cyan")
                elif march_skill == march7th_skill2:
                    lmao("\"Stay right there while I give you a present~\"", color = "cyan") 
                    
                sound_effectfxs.play()
                    
                target = party[choice]
                shield_give = self.defense * 0.57 + 760
                self.shield_value = shield_give
                if 'Shield (March 7th)' in target.buffs:
                    print(f"Refreshing {target.name}'s shield (March 7th) duration!")
                    target.shield -= self.shield_value
                    
                target.shield += shield_give
                target.buffs['Shield (March 7th)'] = 4
                print(f"Shielded {target.name} with {shield_give} HP!")

                self.energize(30)
                time.sleep(1)
                break
            else:
                lmao("\"Who?\"", color = "cyan")
                time.sleep(1)
            
    def ultimate(self, target):   
        if self.energy == 120:
            march7th_ultimate1.play()
            lmao("\"Gotta try hard sometimes.\"", color = "cyan")
            march7th_ultimate2.play()
            lmao("\"Check out this awesome move~\"", color = "cyan")
            march7th_ultimate2.stop()
            
            damage = self.atk * 1.5
        
            if self.dmg_bonus > 0:
                damage += damage * self.dmg_bonus/100
                
            damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
            
            hit_multipliers = [0.25, 0.25, 0.25, 0.25]
            
            for multiplier in hit_multipliers:
                hit_damage = damage * multiplier
                crit_roll = random.randint(0, 100)
                if crit_roll < self.crit_rate:
                    hit_damage += hit_damage * (self.crit_dmg/100)
                target.hp -= hit_damage
                n(f"{self.name} dealt {hit_damage:.0f} damage to {target.name}!")
                sound_effectqqb.play()
                time.sleep(0.3)
                
            target.toughness -= 20
            freeze_chance = random.randint(1, 100)
            if freeze_chance <= 65:
                target.buffs['Freeze (March 7th)'] = 1
                n(f"{target.name} frozen for 1 turn!")
                target.frozen = True
                
            self.energy -= 120
            time.sleep(1)
            self.energize(5)
            
        else:
            n("Not enough energy!", color = "red")   
            time.sleep(1)
            
    def talent(self, target):
        if self.talent_counter > 0:
            damage = self.atk
            
            if self.dmg_bonus > 0:
                damage += damage * self.dmg_bonus/100
                
            damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
            
            crit_roll = random.randint(0, 100)
            if crit_roll < self.crit_rate:
                damage += damage * (self.crit_dmg/100)
                
            target.hp -= damage
            print(f"{self.name} dealt {damage:.0f} counter damage to {target.name}!")
            self.talent_counter -= 1
            self.energize(10)
            check_others(game.march_7th, target)      

class DanHeng(Character):
    def __init__(self):
        super().__init__("Dan Heng", 3000, 3000, 1000, 70, 150, 50, "Wind")
        self.talent_counter = 0
        
    def energize(self, energy):
        self.energy += energy
        if self.energy > 100:
            self.energy = 100
        
    def basic_attack(self, target):
        clear()
        
        dan_heng_basicatk.play()
        lmao("\"The time is now.\"", color = "green")
        
        damage = self.atk
    
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
            
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
        
        hit_multipliers = [0.45, 0.55]
            
        for multiplier in hit_multipliers:
            hit_damage = damage * multiplier
            crit_roll = random.randint(0, 100)
            if crit_roll < self.crit_rate:
                hit_damage += hit_damage * (self.crit_dmg/100)
                n("CRIT!", "yellow")
            target.hp -= hit_damage
            n(f"{self.name} dealt {hit_damage:.0f} damage to {target.name}!")
            sound_effectqqb.play()
            time.sleep(0.5)
                   
        target.toughness -= 10
        time.sleep(1)
        self.energize(20)
        check_others(game.dan_heng, target)
        
    def skill(self, target):
        clear()
        
        dan_heng_skill.play()
        lmao("\"Hmph.\"", color = "green")
            
        sound_effectqqb.play()
        
        damage = self.atk * 2.60
    
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
            
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
        
        hit_multipliers = [0.30, 0.15, 0.15, 0.40]
            
        for multiplier in hit_multipliers:
            hit_damage = damage * multiplier
            crit_roll = random.randint(0, 100)
            if crit_roll < self.crit_rate:
                hit_damage += hit_damage * (self.crit_dmg/100)
                n("CRIT!", "yellow")
            target.hp -= hit_damage
            n(f"{self.name} dealt {hit_damage:.0f} damage to {target.name}!")
            sound_effectqqb.play()
            time.sleep(0.3)
                   
        target.toughness -= 10
        time.sleep(1)
        self.energize(30)
        check_others(game.dan_heng, target)
            
    def ultimate(self, target):   
        if self.energy == 100:
            dan_heng_ultimate1.play()
            lmao("\"The truth of life and death, revealed in an instant.\"", color = "green")
            dan_heng_ultimate2.play()
            lmao("\"This sanctuary... is but a vision... Tch.. Break!\"", color = "green")
            dan_heng_ultimate2.stop()
            
            damage = self.atk * 4
        
            if self.dmg_bonus > 0:
                damage += damage * self.dmg_bonus/100
                
            damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
    
            crit_roll = random.randint(0, 100)
            if crit_roll < self.crit_rate:
                damage += damage * (self.crit_dmg/100)
                n("CRIT!", "yellow")
            target.hp -= damage
            n(f"{self.name} dealt {damage:.0f} damage to {target.name}!")
            sound_effectqqb.play()
            time.sleep(0.3)
                
            target.toughness -= 30
            self.energy -= 100
            time.sleep(1)
            self.energize(5)
            
        else:
            n("Not enough energy!", color = "red")   
            time.sleep(1)
            
    def talent(self, target):
        if self.talent_counter > 0:
            damage = self.atk
            
            if self.dmg_bonus > 0:
                damage += damage * self.dmg_bonus/100
                
            damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
            
            crit_roll = random.randint(0, 100)
            if crit_roll < self.crit_rate:
                damage += damage * (self.crit_dmg/100)
                
            target.hp -= damage
            print(f"{self.name} dealt {damage:.0f} counter damage to {target.name}!")
            self.talent_counter -= 1
            self.energize(10)
            check_others(game.march_7th, target)      

class Enemy(Character):
    def __init__(self):
        super().__init__("Enemy", 10000, 1000, 1000, 0 ,0, 0, None)
        self.toughness = 100
                
    def basic_attack(self):
        clear()
        damage = self.atk
        target = random.choice(game.class_list)
        
        if 'Matrix of Prescience' in target.buffs:
            damage -= damage * 0.18
            if target != game.fu_xuan:
                distributed_damage = damage * 0.65
                damage -= distributed_damage
                game.fu_xuan.hp -= distributed_damage
                n(f"{distributed_damage} damage redistributed to Fu Xuan")
            
        if target.shield > 0:
            target.shield -= damage
            if target.shield <= 0:
                target.hp += target.shield
                target.shield = 0
        else:
            target.hp -= damage 
        
        n(f"{self.name} dealt {damage:.0f} damage to {target.name}!") 
        
        if 'Shield (March 7th)' in target.buffs:
            game.march_7th.talent(self)
              
        game.fu_xuan.talent()
        
        time.sleep(1)

def check_buffs_before_turns(char):
    if 'Natasha Skill Healing' in char.buffs:
        hp_healed = game.natasha.max_hp * 0.072 + 192
        hp_healed = game.natasha.talent(hp_healed, char)
        char.hp += hp_healed
        if char.hp > char.max_hp:
           char.hp = char.max_hp
        char.buffs['Natasha Skill Healing'] -= 1
        print(f"{char.name} restored {hp_healed} HP from Natasha's skill healing.")
        if char.buffs['Natasha Skill Healing'] == 0:
            del char.buffs['Natasha Skill Healing']
            print(f"{char.name}'s skill healing from Natasha has expired.")
            time.sleep(1)
    
    if char.name == "Tingyun":
        char.energize(5)
        
    if char.name == "March 7th":
        char.talent_counter = 2
        
    if char.name == "Enemy":
        if 'Freeze (March 7th)' in char.buffs:
            ice_dot_damage = game.march_7th.atk * 0.6
            n(f"{char.name} took {ice_dot_damage:.0f} frozen damage.")
            char.buffs['Freeze (March 7th)'] -= 1
            if char.buffs['Freeze (March 7th)'] == 0:
                del char.buffs['Freeze (March 7th)']
            time.sleep(1)
        

def check_buffs_after_turns(char):
    if 'Benediction' in char.buffs:
        char.buffs['Benediction'] -= 1
        if char.buffs['Benediction'] == 0:
            char.atk -= game.tingyun.previous_target_atk_bonus
            if char.atk < char.original_atk:
                char.atk = char.original_atk
            del char.buffs['Benediction']
            print(f"{char.name}'s Benediction buff has expired.")
            time.sleep(1)
            
    if 'Damage Bonus (Tingyun)' in char.buffs:
        char.buffs['Damage Bonus (Tingyun)'] -= 1
        if char.buffs['Damage Bonus (Tingyun)'] == 0:
            char.dmg_bonus -= 50
            del char.buffs['Damage Bonus (Tingyun)']
            print(f"{char.name}'s damage bonus by Tingyun has expired.")
            time.sleep(1)     
            
    if 'Shield (March 7th)' in char.buffs:
        char.buffs['Shield (March 7th)'] -= 1
        if char.buffs['Shield (March 7th)'] == 0:
            char.shield -= game.march_7th.shield_value
            if char.shield <= 0:
                char.shield = 0
            del char.buffs['Shield (March 7th)']
            print(f"{char.name}'s shield by March 7th has expired.")
            time.sleep(1)   

def check_others(char, target):
    if 'Benediction' in char.buffs:
        extra_damage = char.atk * 0.4
        target.hp -= extra_damage
        n(f"{char.name} dealt extra {extra_damage} damage to {target.name} with benediction.")
        time.sleep(1)
    
    if target.toughness <= 0:
        if char.element == "Lightning":
            print("Break damage later added.")
            
class Game:
    def __init__(self):
        self.fu_xuan = FuXuan()
        self.tingyun = Tingyun()
        self.natasha = Natasha()
        self.march_7th = March7th()
        self.dan_heng = DanHeng()
        self.enemy = Enemy()
        self.class_list = []
        self.queue = []

    def party_selection(self):
        while True:
            clear()
            n("""=============================================
Choose your party!
Members Available: Fu Xuan, Tingyun, Natasha,
March 7th, Dan Heng
Type '0' to start battle. 
Type '1' to empty team.
=============================================""", color="yellow")
            if len(self.queue) >= 4:
                print("Your party is full!")
                time.sleep(0.5)
            if self.queue:
                for i, member in enumerate(self.queue, start = 1):
                    n(f"{i}. {member}")
                    
            party_member = input("Type their name: ").lower()
            if party_member == "fu xuan" and "Fu Xuan" not in self.queue:
                self.queue.append("Fu Xuan")
                self.class_list.append(self.fu_xuan)
            elif party_member == "tingyun" and "Tingyun" not in self.queue:
                self.queue.append("Tingyun")
                self.class_list.append(self.tingyun)
            elif party_member == "natasha" and "Natasha" not in self.queue:
                self.queue.append("Natasha")
                self.class_list.append(self.natasha)
            elif party_member == "march 7th" and "March 7th" not in self.queue:
                self.queue.append("March 7th")
                self.class_list.append(self.march_7th)
            elif party_member == "dan heng" and "Dan Heng" not in self.queue:
                self.queue.append("Dan Heng")
                self.class_list.append(self.dan_heng)
            elif party_member == "0":
                if len(self.queue) > 0:  # Ensure at least one member is selected
                    game.fight(self.queue)
                else:
                    print("You must select at least one party member!")
                    time.sleep(0.5)
            elif party_member == "1":
                self.queue = []
            elif party_member.capitalize() in self.queue:
                print("Character already in the party!")
                time.sleep(0.5)
            else:
                print("Invalid input. Try again.")
                time.sleep(0.5)
 
    def skill_point_show(skill_point):
        n("SP : ", color = "blue", end = "")
        for i in range(skill_point):
            n("✧ ", color = "blue", end = "")
        
    def fight(self, queue):
        skill_point = 3
        queue = self.queue
        queue.append("Enemy")
        while True:
            clear()
            who = queue[0]
            current_char = getattr(self, who.lower().replace(" ", "_"))
            check_buffs_before_turns(current_char)
            while True:
                print(queue)
                if who == "Fu Xuan":
                    n("""==========================
What should Fu Xuan do?
==========================
""", color = "magenta", end = "")
                    Game.skill_point_show(skill_point)
                    n(f"\nHP = {self.fu_xuan.hp}, Enemy HP = {self.enemy.hp}\nEnergy = {self.fu_xuan.energy}, Talent Counter = {self.fu_xuan.talent_counter}")
                    if self.fu_xuan.shield > 0:
                        n(f"\nShield = {self.fu_xuan.shield}")
                    n("""
1. Basic Attack
2. Skill
3. Ultimate
4. Check Stats
            """)
                    action = input("Choose an action: ")
                    if action == "1":
                        self.fu_xuan.basic_attack(self.enemy)
                        if skill_point < 5:
                            skill_point += 1
                            check_buffs_after_turns(self.fu_xuan)
                        self.fu_xuan.skill_turn_check()
                        break
                        
                    elif action == "2":
                        if skill_point < 1:
                            print("Not enough skill points!")
                            time.sleep(1)
                            continue
                        
                        else:
                            self.fu_xuan.skill(self.class_list)
                            skill_point -= 1
                            check_buffs_after_turns(self.fu_xuan)
                            self.fu_xuan.skill_turn_check()
                            break

                    elif action == "3":
                        self.fu_xuan.ultimate(self.class_list, self.enemy)
                        continue
                    
                    elif action == "4":
                        self.fu_xuan.check_stats()
                        continue
                    
                    else:
                        print("Invalid action!")
                        time.sleep(1)
                        continue
                
                elif who == "Tingyun":
                    n("""==========================
What should Tingyun do?
==========================
""", color = "light_magenta", end = "")
                    Game.skill_point_show(skill_point)
                    n(f"\nHP = {self.tingyun.hp}, Enemy HP = {self.enemy.hp}\nEnergy = {self.tingyun.energy}")
                    if self.tingyun.shield > 0:
                        n(f"\nShield = {self.tingyun.shield}")
                    n("""
1. Basic Attack
2. Skill
3. Ultimate
4. Check Stats
                """)
                    action = input("Choose an action: ")
                    if action == "1":
                        self.tingyun.basic_attack(self.enemy)
                        if skill_point < 5:
                            skill_point += 1
                        check_buffs_after_turns(self.tingyun)
                        break
                        
                    elif action == "2":
                        if skill_point < 1:
                            print("Not enough skill points!")
                            time.sleep(1)
                            continue
                        else:
                            self.tingyun.skill(self.class_list)
                            skill_point -= 1
                            check_buffs_after_turns(self.tingyun)
                            break

                    elif action == "3":
                        self.tingyun.ultimate(self.class_list)
                        continue
                    
                    elif action == "4":
                        self.tingyun.check_stats()
                        continue
                    
                    else:
                        print("Invalid action!")
                        time.sleep(1)
                        continue
            
                elif who == "Natasha":
                    n("""==========================
What should Natasha do?
==========================
""", color = "grey", end = "")
                    Game.skill_point_show(skill_point)
                    n(f"\nHP = {self.natasha.hp}, Enemy HP = {self.enemy.hp}\nEnergy = {self.natasha.energy}")
                    if self.natasha.shield > 0:
                        n(f"\nShield = {self.natasha.shield}")
                    n("""
1. Basic Attack
2. Skill
3. Ultimate
4. Check Stats
                """)
                    action = input("Choose an action: ")
                    if action == "1":
                        self.natasha.basic_attack(self.enemy)
                        if skill_point < 5:
                            skill_point += 1
                        check_buffs_after_turns(self.natasha)
                        break
                        
                    elif action == "2":
                        if skill_point < 1:
                            print("Not enough skill points!")
                            time.sleep(1)
                            continue
                        else:
                            self.natasha.skill(self.class_list)
                            skill_point -= 1
                            check_buffs_after_turns(self.natasha)
                            break

                    elif action == "3":
                        self.natasha.ultimate(self.class_list)
                        continue
                    
                    elif action == "4":
                        self.natasha.check_stats()
                        continue
                    
                    else:
                        print("Invalid action!")
                        time.sleep(1)
                        continue

                elif who == "March 7th":
                    n("""==========================
What should March 7th do?
==========================
""", color = "cyan", end = "")
                    Game.skill_point_show(skill_point)
                    n(f"\nHP = {self.march_7th.hp}, Enemy HP = {self.enemy.hp}\nEnergy = {self.march_7th.energy} Talent Counter = {self.march_7th.talent_counter}")
                    if self.march_7th.shield > 0:
                        n(f"\nShield = {self.march_7th.shield}")
                    n("""
1. Basic Attack
2. Skill
3. Ultimate
4. Check Stats
                """)
                    action = input("Choose an action: ")
                    if action == "1":
                        self.march_7th.basic_attack(self.enemy)
                        if skill_point < 5:
                            skill_point += 1
                        check_buffs_after_turns(self.march_7th)
                        break
                        
                    elif action == "2":
                        if skill_point < 1:
                            print("Not enough skill points!")
                            time.sleep(1)
                            continue
                        else:
                            self.march_7th.skill(self.class_list)
                            skill_point -= 1
                            check_buffs_after_turns(self.march_7th)
                            break

                    elif action == "3":
                        self.march_7th.ultimate(self.enemy)
                        continue
                    
                    elif action == "4":
                        self.march_7th.check_stats()
                        continue
                    
                    else:
                        print("Invalid action!")
                        time.sleep(1)
                        continue

                elif who == "Dan Heng":
                    n("""==========================
What should Dan Heng do?
==========================
""", color = "green", end = "")
                    Game.skill_point_show(skill_point)
                    n(f"\nHP = {self.dan_heng.hp}, Enemy HP = {self.enemy.hp}\nEnergy = {self.dan_heng.energy} Talent Counter = {self.dan_heng.talent_counter}")
                    if self.dan_heng.shield > 0:
                        n(f"\nShield = {self.dan_heng.shield}")
                    n("""
1. Basic Attack
2. Skill
3. Ultimate
4. Check Stats
                """)
                    action = input("Choose an action: ")
                    if action == "1":
                        self.dan_heng.basic_attack(self.enemy)
                        if skill_point < 5:
                            skill_point += 1
                        check_buffs_after_turns(self.dan_heng)
                        break
                        
                    elif action == "2":
                        if skill_point < 1:
                            print("Not enough skill points!")
                            time.sleep(1)
                            continue
                        else:
                            self.dan_heng.skill(self.enemy)
                            skill_point -= 1
                            check_buffs_after_turns(self.dan_heng)
                            break

                    elif action == "3":
                        self.dan_heng.ultimate(self.enemy)
                        continue
                    
                    elif action == "4":
                        self.dan_heng.check_stats()
                        continue
                    
                    else:
                        print("Invalid action!")
                        time.sleep(1)
                        continue

                elif who == "Enemy":
                    if self.enemy.frozen == True:
                        n(f"{self.enemy.name} is frozen and cannot act!", color="cyan")
                        self.enemy.frozen = False
                        time.sleep(1)
                        
                    else:
                        self.enemy.basic_attack()
                    
                    break

            queue.append(queue.pop(0))
                
if __name__ == "__main__":
    game = Game()
    game.party_selection()
