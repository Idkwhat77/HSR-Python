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
        
    def basic_attack(self, target, party):
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
    
    def skill(self, target, party):
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
        
    def basic_attack(self, target, party):
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
    
    def skill(self, target, party):
        print("Choose a member by number: ")
        for i, character in enumerate(party, start=1):
            print(f"{i}. {character.name}")
            
        while True:
            choice = int(input("Your choice: ")) - 1
            if 0 <= choice < len(party):
                
                ty_skill = random.choice(tingyun_skill)
                ty_skill.play()
                if ty_skill == tingyun_skill1:
                    lmao("\"Evils Begone~\"", color = "light_magenta")
                elif ty_skill == tingyun_skill2:
                    lmao("\"All the best~\"", color = "light_magenta")
                    
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
            
    def ultimate(self, target, party):   
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
        
    def basic_attack(self, target, party):
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
        
    def skill(self, target, party):
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
                lmao("\"Who?\"", color = "grey")
                time.sleep(1)
            
    def ultimate(self, target, party):   
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
        
    def basic_attack(self, target, party):
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
        
    def skill(self, target, party):
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
            
    def ultimate(self, target, party):   
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
        
    def basic_attack(self, target, party):
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
        
    def skill(self, target, party):
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
            
    def ultimate(self, target, party):   
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
        print("wip")    

class Jingliu(Character):
    def __init__(self):
        super().__init__("Jingliu", 3000, 3000, 1000, 40, 170, 50, "Ice")
        self.talent_counter = 0
        self.special_state = False
        
    def energize(self, energy):
        self.energy += energy
        if self.energy > 140:
            self.energy = 100
        
    def basic_attack(self, target, party):
        clear()
        
        jingliu_basicatk.play()
        lmao("\"Swordward!\"", color = "cyan")
        
        damage = self.atk
    
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
            
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
        
        hit_multipliers = [0.30, 0.70]
            
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
        check_others(game.jingliu, target)
            
    def skill(self, target, party):
        clear()
        
        jingliu_skill.play()
        lmao("\"Fleeting light, roaring flood!\"", color = "cyan")
            
        sound_effectqqb.play()
        
        damage = self.atk * 2
    
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
                    
        target.toughness -= 20
        self.talent()
        time.sleep(1)
        self.energize(20)
        check_others(game.jingliu, target)
            
    def enhanced_skill(self, target, party):
        clear()
        
        jingliu_skill.play()
        lmao("\"Fleeting light, roaring flood!\"", color = "cyan")
            
        if self.special_state == True :
            accumulated_hp = 0
            for char in party:
                if char.name != "Jingliu" :
                    accumulated_hp += char.max_hp * 0.04
                    char.hp -= char.max_hp * 0.04
                    if char.hp < 0 :
                        char.hp = 1
            original_atk = self.atk
            self.atk += accumulated_hp * 5.4
            if self.atk > original_atk * 1.8 :
                self.atk = original_atk * 1.8
                    
        damage = self.atk * 2.5
    
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus/100
            
        damage = damage * (1 - (target.defense / (target.defense + 200 + (10 * 90))))
        
        hit_multipliers = [0.10, 0.10, 0.10, 0.20, 0.50]
            
        for multiplier in hit_multipliers:
            hit_damage = damage * multiplier
            crit_roll = random.randint(0, 100)
            if crit_roll < self.crit_rate:
                hit_damage += hit_damage * (self.crit_dmg/100)
                n("CRIT!", "yellow")
            target.hp -= hit_damage
            n(f"{self.name} dealt {hit_damage:.0f} damage to {target.name}!")
            sound_effectqqb.play()
            time.sleep(0.2)
                   
        target.toughness -= 20
        self.atk = original_atk
        self.talent()
        time.sleep(1)
        self.energize(30)
        check_others(game.jingliu, target)
        
    def ultimate(self, target, party):   
        if self.energy == 140:
            jingliu_ultimate1.play()
            lmao("\"All will be revealed.\"", color = "cyan")
            jingliu_ultimate2.play()
            lmao("\".. In lunar flame!\"", color = "cyan")
            
            if self.special_state == True :
                accumulated_hp = 0
                for char in party:
                    if char.name != "Jingliu" :
                        accumulated_hp += char.max_hp * 0.04
                        char.hp -= char.max_hp * 0.04
                        if char.hp < 0 :
                            char.hp = 1
                original_atk = self.atk
                self.atk += accumulated_hp * 5.4
                if self.atk > original_atk * 1.8 :
                    self.atk = original_atk * 1.8
                
            damage = self.atk * 3
        
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
                
            target.toughness -= 20
            self.energy -= 140
            self.talent()
            time.sleep(1)
            self.energize(5)
            
        else:
            n("Not enough energy!", color = "red")   
            time.sleep(1)
            
    def talent(self):
        if self.talent_counter < 3 and self.special_state == False:
            n("Jingliu gained 1 stack of Syzygy.")
            self.talent_counter += 1
            if self.talent_counter == 2 :
                n("Jingliu has entered the Special Transmigration state!")
                self.special_state = True
                self.crit_rate += 50
                return
            
        if self.talent_counter > 0 and self.special_state == True:
            self.talent_counter -= 1
            if self.talent_counter == 0 :
                n("Jingliu has exited the Special Transmigration state!")
                self.special_state -= 1 
                self.crit_rate -= 50

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
            
    if char.name == "Fu Xuan" :
        char.skill_turn_check()

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
        self.jingliu = Jingliu()
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
            
            if self.queue:
                for i, member in enumerate(self.queue, start = 1):
                    n(f"{i}. {member}")
                    
            party_member = input("Type their name: ").lower()
            
            if len(self.queue) >= 4:
                print("Your party is full!")
                time.sleep(0.5)
            elif party_member == "fu xuan" and "Fu Xuan" not in self.queue:
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
            elif party_member == "jingliu" and "Jingliu" not in self.queue:
                self.queue.append("Jingliu")
                self.class_list.append(self.jingliu)
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

    def _increase_skill_point(self, skill_point):
        if skill_point < 5 :
            skill_point += 1
            return skill_point

    def _use_skill(self, char, skill_point):
        if skill_point < 1:
            print("Not enough skill points!")
            time.sleep(1)
            return skill_point
        else:
            char.skill(self.class_list)
            return skill_point - 1

    def check_color(self, char) :
        
        char_element_color = {
            "Ice": "cyan",
            "Wind" : "green",
            "Lightning" : "light_magenta",
            "Physical" : "grey",
            "Quantum" : "magenta",
            "Fire" : "red",
            "Imaginary" : "yellow"
        }
        
        return char_element_color.get(char.element, "white")  
        
    def fight(self, queue):
        epic_color = "none"
        skill_point = 3
        queue.append("Enemy")

        while True:
            clear()
            who = queue[0]
            current_char = getattr(self, who.lower().replace(" ", "_"))
            check_buffs_before_turns(current_char)

            if current_char.name != "Enemy" :
                action_map = {
                    "1": current_char.basic_attack,
                    "2": current_char.skill,
                    "3": current_char.ultimate,
                    "4": current_char.check_stats,
                }

            while True:
                epic_color = self.check_color(current_char)
                print(queue)
                
                if current_char.name == "Enemy" :
                    current_char.basic_attack()
                    break
                    
                else :
                    n(f"==========================\nWhat should {who} do?\n==========================\n", color = epic_color, end="")
                    Game.skill_point_show(skill_point)
                    n(f"\nHP = {current_char.hp}, Enemy HP = {self.enemy.hp}\nEnergy = {current_char.energy}")

                    if current_char.shield > 0:
                        n(f"\nShield = {current_char.shield}")

                    n("\n1. Basic Attack\n2. Skill\n3. Ultimate\n4. Check Stats")
                    action = input("Choose an action: ")

                    if action in action_map:
                        if action == "1" :
                            if current_char.name == "Jingliu" and current_char.special_state == True:
                                clear()
                                n("Basic attack not available.", color = "red")  
                            else :
                                action_map[action](self.enemy, self.class_list)
                                break
                        
                        elif action == "2" : 
                            if current_char.name == "Jingliu" and current_char.special_state == True:
                                current_char.enhanced_skill(self.enemy, self.class_list)
                            else :
                                action_map[action](self.enemy, self.class_list)
                            break
                            
                        elif action == "3" :
                            action_map[action](self.enemy, self.class_list)
                            
                        elif action == "4" :
                            action_map[action]()
                            pass
                        
                    else:
                        print("Invalid action!")
                        time.sleep(1)
            check_buffs_after_turns(current_char)
            queue.append(queue.pop(0))

                
if __name__ == "__main__":
    game = Game()
    game.party_selection()
