from termcolor import colored
from colorama import init # this is just so color appears when py file open bruh bruh bruh bruh/'
import time
import os
import pygame 
import random


# BEWARE LONG LINES! THIS IS FOR THE HSR BATTLE SYSTEM!
# voicelines and battle music
script_dir = os.path.dirname(__file__)
battle = os.path.join(script_dir, "battle/battle.mp3")
fxb1 = os.path.join(script_dir, "battle/fu_xuan_basicatk1.ogg")  
fxb2 = os.path.join(script_dir, "battle/fu_xuan_basicatk2.ogg")
fxs1 = os.path.join(script_dir, "battle/fu_xuan_skill1.ogg")  
fxs2 = os.path.join(script_dir, "battle/fu_xuan_skill2.ogg")
fxu1 = os.path.join(script_dir, "battle/fu_xuan_ultimate1.ogg")  
fxu2 = os.path.join(script_dir, "battle/fu_xuan_ultimate2.ogg")
qqb = os.path.join(script_dir, "battle/qingque_basicatk.ogg")
qqeb = os.path.join(script_dir, "battle/qingque_enbasicatk.ogg")
qqs1 = os.path.join(script_dir, "battle/qingque_skill1.ogg")
qqs2 = os.path.join(script_dir, "battle/qingque_skill2.ogg")
qqs3 = os.path.join(script_dir, "battle/qingque_skill3.ogg")
qqs4 = os.path.join(script_dir, "battle/qingque_skill4.ogg")
qqs5 = os.path.join(script_dir, "battle/qingque_skill5.ogg")
qqu1 = os.path.join(script_dir, "battle/qingque_ultimate1.ogg")
qqu2 = os.path.join(script_dir, "battle/qingque_ultimate2.ogg")

# sound effects atatkcking idk
fxbasic = os.path.join(script_dir, "battle/holy.mp3")
fxbasic2 = os.path.join(script_dir, "battle/Attack2.mp3")
fxskill = os.path.join(script_dir, "battle/Absorption.mp3")
fxsultimate = os.path.join(script_dir, "battle/Thunder6.mp3")
fxsultimate2 = os.path.join(script_dir, "battle/Blow4.mp3")
qqbasic = os.path.join(script_dir, "battle/Blow3.mp3")
qqebasic = os.path.join(script_dir, "battle/Explosion2.mp3")
qqskill = os.path.join(script_dir, "battle/Item1.mp3")
qqultimate = os.path.join(script_dir, "battle/Blow7.mp3")
enemyatk = os.path.join(script_dir, "battle/Damage2.mp3")

# loading stuff
pygame.mixer.init()
sound_effectfxb = pygame.mixer.Sound(fxbasic)
sound_effectfxb2 = pygame.mixer.Sound(fxbasic2)
sound_effectfxs = pygame.mixer.Sound(fxskill)
sound_effectfxu = pygame.mixer.Sound(fxsultimate)
sound_effectfxu2 = pygame.mixer.Sound(fxsultimate2)
sound_effectqqb = pygame.mixer.Sound(qqbasic)
sound_effectqqeb = pygame.mixer.Sound(qqebasic)
sound_effectqqs = pygame.mixer.Sound(qqskill)
sound_effectqqu = pygame.mixer.Sound(qqultimate)
sound_effectea = pygame.mixer.Sound(enemyatk)

fu_xuan_basicatk1 = pygame.mixer.Sound(fxb1)
fu_xuan_basicatk2 = pygame.mixer.Sound(fxb2)
fu_xuan_skill1 = pygame.mixer.Sound(fxs1)
fu_xuan_skill2 = pygame.mixer.Sound(fxs2)
fu_xuan_ultimate1 = pygame.mixer.Sound(fxu1)
fu_xuan_ultimate2 = pygame.mixer.Sound(fxu2)
qingque_basicatk = pygame.mixer.Sound(qqb)
qingque_enbasicatk = pygame.mixer.Sound(qqeb)
qingque_skill1 = pygame.mixer.Sound(qqs1)
qingque_skill2 = pygame.mixer.Sound(qqs2)
qingque_skill3 = pygame.mixer.Sound(qqs3)
qingque_skill4 = pygame.mixer.Sound(qqs4)
qingque_skill5 = pygame.mixer.Sound(qqs5)
qingque_ultimate1 = pygame.mixer.Sound(qqu1)
qingque_ultimate2 = pygame.mixer.Sound(qqu2)

fu_xuan_basicatk = [fu_xuan_basicatk1, fu_xuan_basicatk2]
fu_xuan_skill = [fu_xuan_skill1, fu_xuan_skill2]
qingque_skill = [qingque_skill1, qingque_skill2, qingque_skill3, qingque_skill4, qingque_skill5]

def lmao(text, color="white", end='\n'): #halo text visual novel mwehehehee
    for char in text:
        if char in i_want_sleep:
            print(colored(char, color), end='', flush=True)
            time.sleep(0.3)
        else:
            print(colored(char, color), end='', flush=True)
            time.sleep(0.05)
    print(end=end, flush=True)
    
class Fu_Xuan:
    def __init__(self):
        self.energy = 0
        self.ORIGINAL_HP = 10000
        self.HP = 10000          
        self.Max_HP = 10000     
        self.ATK = 1400          
        self.CRIT_RATE = 20.0  
        self.CRIT_DMG = 0.6     
        self.matrix = False      
        self.skill_counter = 0
        self.talent_counter = 1    
        self.alive = True 
    
    def stats(self):
        print(f"""
Fu Xuan:
HP = {self.HP:,}/{self.Max_HP:,}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
""")
        time.sleep(1)
        
    def energize(self, amount):
        self.energy += amount
        if self.energy > 135:
            self.energy = 135

    def basic_atk(self):
        global skill_point
        damage = self.HP * 0.5  
        crit = random.randint(0, 100)
        is_critical = crit < self.CRIT_RATE
        fuxuan_basicatk = random.choice(fu_xuan_basicatk)
        if fuxuan_basicatk == fu_xuan_basicatk1:
            fu_xuan_basicatk1.play()
            lmao("\"With all my power.. Scry the future!\"", color = "magenta")
        elif fuxuan_basicatk == fu_xuan_basicatk2:
            fu_xuan_basicatk2.play()
            lmao("\"In formation, in accordance!\"", color = "magenta")
        sound_effectfxb.play()
        sound_effectfxb2.play()
        if is_critical:
            damage += damage * self.CRIT_DMG
            n("CRIT!", color = "yellow")

        self.energize(20)
        if skill_point < 5:
            skill_point += 1

        print(f"Fu Xuan dealt {damage:.2f} damage.")
        enemy.HP -= damage
        time.sleep(0.5)

    def skill(self):
        global skill_point
        if skill_point == 0:
            print("Not enough SP!")
            pass
        else:    
            fuxuan_skill = random.choice(fu_xuan_skill)
            if fuxuan_skill == fu_xuan_skill1:
                fu_xuan_skill1.play()
                lmao("\"Converge... and awaken!\"", color = "magenta")
            elif fuxuan_skill == fu_xuan_skill2:
                fu_xuan_skill2.play()
                lmao("\"Together... as one!\"", color = "magenta")
            sound_effectfxs.play()
            
            if self.matrix == True:
                self.energize(50)
            else:
                self.energize(30)
                
            if not self.matrix:
                self.matrix = True
                self.skill_counter = 3
                self.Max_HP += self.ORIGINAL_HP * 0.06
                self.HP += self.ORIGINAL_HP * 0.06
                self.CRIT_RATE += 12
                print(f"Fu Xuan's Max HP increased to {self.Max_HP:,} and Crit Rate increased to {self.CRIT_RATE}%")
                if qingque.alive == True:
                    qingque.Max_HP += self.ORIGINAL_HP * 0.06
                    qingque.HP += self.ORIGINAL_HP * 0.06
                    qingque.CRIT_RATE += 12
                    print(f"Qingque's Max HP increased to {qingque.Max_HP:,} and Crit Rate increased to {qingque.CRIT_RATE}%")
                skill_point -= 1
            else:
                if self.skill_counter < 3:
                    self.skill_counter = 3
                if self.matrix == True:
                    self.energize(50)
                else:
                    self.energize(30)
                skill_point -= 1
                print("Matrix of Prescience turn refreshed.")
            time.sleep(0.5)

    def ultimate(self):
        
        if self.energy == 135:
            fu_xuan_ultimate1.play()
            lmao("\"All things in this world have their laws.\"", color = "magenta")
            damage = self.HP
            crit = random.randint(0, 100)
            is_critical = crit < self.CRIT_RATE
            fu_xuan_ultimate2.play()
            lmao("\"Yet stratagems... constellations.. are human.. creations! Hmph!\"", color = "magenta")
            sound_effectfxu.play()
            sound_effectfxu2.play()
            if is_critical:
                damage += damage * self.CRIT_DMG
                n("CRIT!", color = "yellow")
                
            print(f"Fu Xuan dealt {damage:.2f} damage with her ultimate!")
            enemy.HP -= damage
            time.sleep(1)
            if qingque.HP > 0:
                recover = fu_xuan.Max_HP * 0.05 + 133
                qingque.HP += recover
                if qingque.HP > qingque.Max_HP:
                    qingque.HP = qingque.Max_HP
                    print(f"Qingque restored {qingque.Max_HP - qingque.HP} HP!")
                else:
                    print(f"Qingque restored {recover} HP!")
                
            if self.talent_counter < 2:
                self.talent_counter += 1
            self.energy = 0
            self.energize(5)
        else:
            print("Not enough energy...")

        time.sleep(0.5)

    def talent(self):
        if self.HP < self.Max_HP * 0.5 and self.talent_counter > 0: 
            missing_hp = self.Max_HP - self.HP
            restore_amount = missing_hp * 0.9 
            self.HP += restore_amount
            self.HP = min(self.HP, self.Max_HP)
            self.talent_counter -= 1
            print(f"Fu Xuan restored {restore_amount:.2f} HP. Current HP: {self.HP:.2f}")
        time.sleep(0.5)

    def matrix_of_prescience(self):
        if self.skill_counter > 0:
            self.skill_counter -= 1
            if self.skill_counter == 0:
                self.matrix = False
                self.Max_HP = self.ORIGINAL_HP
                if self.HP > self.Max_HP:
                    self.HP = self.Max_HP
                self.CRIT_RATE -= 12
                
                qingque.Max_HP = qingque.ORIGINAL_HP
                if qingque.HP > qingque.Max_HP:
                    qingque.HP = qingque.Max_HP
                qingque.CRIT_RATE -= 12
                print("Matrix Of Prescience turn has run off.")
                time.sleep(1)
            
class Qingque:
    def __init__(self):
        self.alive = True
        self.ORIGINAL_HP = 3000
        self.HP = 3000          
        self.Max_HP = 3000     
        self.ATK = 3000         
        self.CRIT_RATE = 70     
        self.CRIT_DMG = 2     
        self.energy = 0
        self.dmg_bonus_stack = 0
        self.dmg_bonus = 0
        self.hidden_hand = False
        self.card = []

    def stats(self):
        print(f"""
Qingque:
HP = {self.HP}/{self.Max_HP}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
""")
        time.sleep(1)
        
    def energize(self, amount):
        self.energy += amount
        if self.energy > 140:
            self.energy = 140

    def basic_atk(self):
        global skill_point
        damage = self.ATK * 1.1
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus
            
        crit = random.randint(0, 100)
        is_critical = crit < self.CRIT_RATE
        qingque_basicatk.play()
        lmao("\"Don't need this tile~\"", color = "green")
        sound_effectqqb.play()
        if is_critical:
            damage += damage * self.CRIT_DMG
            n("CRIT!", color = "yellow")

        self.energize(20)
        enemy.HP -= damage
        print(f"Qingque dealt {damage:.2f} damage using her basic attack.")
        self.dmg_bonus = 0
        self.dmg_bonus_stack = 0
        if skill_point < 5:
            skill_point += 1

        time.sleep(1)
        
    def enhanced_basic_atk(self):
        global skill_point
        qingque_enbasicatk.play()
        lmao("\"Time for the payout...!\"", color = "green")
        damage = self.ATK * 2.64  
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus
        crit = random.randint(0, 100)
        is_critical = crit < self.CRIT_RATE

        sound_effectqqeb.play()
        if is_critical:
            damage += damage * self.CRIT_DMG
            n("CRIT!", color = "yellow")

        self.energize(20)
        enemy.HP -= damage
        print(f"Qingque dealt {damage:.2f} damage using her enhanced basic attack.")
        self.dmg_bonus = 0
        self.dmg_bonus_stack = 0
        skill_point += 1
        qingque.hidden_hand = False
        qingque.card = []
        time.sleep(1)
        
    def skill(self):
        global skill_point
        if skill_point == 0:
            print("Not enough SP!")
            pass
        else: 
            idk = [1,2,3]   
            for i in range(3):
                self.card.append(random.choice(idk))
            if self.dmg_bonus_stack < 4:
                self.dmg_bonus_stack += 1
                self.dmg_bonus += 0.3
                
            qq_skill = random.choice(qingque_skill)
            qq_skill.play()
            if qq_skill == qingque_skill1:
                lmao("Gotcha!", color = "green")
            elif qq_skill == qingque_skill2:
                lmao("Stay calm!", color = "green")
            elif qq_skill == qingque_skill3:
                lmao("Come on!", color = "green")
            elif qq_skill == qingque_skill4:
                lmao("Ooh!", color = "green")
            elif qq_skill == qingque_skill5:
                lmao("Wow!", color = "green")
                
            sound_effectqqs.play()
            print(f"Qingque's cards = ({self.card}), Damage boost = {self.dmg_bonus * 100}%")
            if self.card[0] == self.card[1] == self.card[2]:
                self.hidden_hand = True
            else:
                self.card = []
                skill_point -= 1
                
            self.energize(5)
            
    def ultimate(self):
        if self.energy == 140:
            qingque_ultimate1.play()
            lmao("\"Luck of the draw!\"", color = "green")
            damage = self.ATK * 2.16
            crit = random.randint(0, 100)
            is_critical = crit < self.CRIT_RATE
            qingque_ultimate2.play()
            lmao("\"Please please please please please.. ah...! Looks like, victory!\"", color = "green")
            
            sound_effectqqu.play()
            if is_critical:
                damage += damage * self.CRIT_DMG
                n("CRIT!", color = "yellow")
                
            enemy.HP -= damage
            qingque.hidden_hand = True
            print(f"Qingque dealt {damage:.2f} damage with her ultimate!")
            self.energy = 0
            self.energize(5)
        else:
            print("Not enough energy...")

        time.sleep(0.5)

class Enemy:
    def __init__(self):
        self.HP = 300000
        self.ATK = 1800
        
    def attack(self):
        global queue
        damage = self.ATK * 0.5
        name = ["Fu Xuan", "Qingque"]
        target = random.choice(name)
        if fu_xuan.matrix == True:
            damage = damage * 0.82
            
        if qingque.alive == False:
            target = "Fu Xuan"
        elif fu_xuan.alive == False:
            target = "Qingque"
        
        sound_effectea.play()
        if target == "Fu Xuan":
            fu_xuan.HP -= damage
            print(f"{target} got hit! (-{damage})")
            if fu_xuan.HP < 0:
                print(f"{target} is down!")
                fu_xuan.alive = False
                queue.remove("fu_xuan")
            else:
                fu_xuan.energize(10)    
                    
        elif target == "Qingque":
            qingque.HP -= damage
            print(f"{target} got hit! (-{damage})")                  
            if qingque.HP < 0:
                print(f"{target} is down!")
                qingque.alive = False
                queue.remove("qingque")
            else:
                qingque.energize(10)

fu_xuan = Fu_Xuan()
qingque = Qingque()
enemy = Enemy()
queue = ["fu_xuan", "qingque", "enemy"]
skill_point = 3

# MUSIC STUFFFFFFFFFFFFFFFFFFFFFFFFF Fother than battle
script_dir = os.path.dirname(__file__)
hotel = os.path.join(script_dir, "hotel.mp3")   # i love undertale
menu = os.path.join(script_dir, "menu.mp3")
ruins = os.path.join(script_dir, "ruins.mp3")
persona = os.path.join(script_dir, "persona.mp3")
histheme = os.path.join(script_dir, "histheme.mp3")
chest_open = os.path.join(script_dir, "open.mp3")  
chest_close = os.path.join(script_dir, "close.mp3")
blender = os.path.join(script_dir, "blender.mp3")
pygame.mixer.init()

sound_effect1 = pygame.mixer.Sound(chest_open)
sound_effect2 = pygame.mixer.Sound(chest_close)
sound_effect3 = pygame.mixer.Sound(blender)

# here lies the grave of fucntions mwahahahaa
def fight():
    global queue
    pygame.mixer.music.load(battle)
    pygame.mixer.music.set_volume(0.5)  
    pygame.mixer.music.play(loops=-1)
    while True:
        if fu_xuan.alive == False and qingque.alive == False:
            c("You both died.")
            go_back()
        if enemy.HP <= 0:
            after_fight()
        who = queue[0]
        if who == "fu_xuan" and fu_xuan.alive == True:
            fu_xuan.talent()
            choose = input(f"""
What should Fu Xuan do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {fu_xuan.HP}) (Talent Counter = {fu_xuan.talent_counter}) (Matrix of Prescience = {fu_xuan.skill_counter}) (Energy = {fu_xuan.energy})
1. Basic ATK (Novaburst)
2. Skill (Known by Stars, Shown by Hearts)
3. Ultimate (Woes of Many Morphed to One)
4. Check Stats
Input : """)
            if choose == "1":
                fu_xuan.basic_atk()
                queue.pop(0)
                queue.append("fu_xuan")
            elif choose == "2":
                fu_xuan.skill()
                queue.pop(0)
                queue.append("fu_xuan")
            elif choose == "3":
                fu_xuan.ultimate()
            elif choose == "4":
                fu_xuan.stats()
        elif who == "qingque" and qingque.alive == True:
            fu_xuan.talent()
            if qingque.hidden_hand == False:
                choose = input(f"""
What should Qingque do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {qingque.HP}) (Energy = {qingque.energy})
1. Basic ATK (Flower Pick)
2. Skill (A Scoof of Moon)
3. Ultimate (A Quartet? Woo-hoo!)
4. Check Stats
Input : """)
            else:
                choose = input(f"""
What should Qingque do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {qingque.HP}) (Energy = {qingque.energy})
1. Enhanced Basic ATK (Cherry on Top)
2. Skill (A Scoof of Moon)
3. Ultimate (A Quartet? Woo-hoo!)
4. Check Stats
Input : """) 
            if choose == "1" and qingque.hidden_hand == False:
                qingque.basic_atk()
                queue.pop(0)
                queue.append("qingque")
            elif choose == "1" and qingque.hidden_hand == True:
                qingque.enhanced_basic_atk()
                queue.pop(0)
                queue.append("qingque")
            elif choose == "2" and qingque.hidden_hand == False:
                qingque.skill()
            elif choose == "3":
                qingque.ultimate()
            elif choose == "4":
                qingque.stats()
        elif who == "enemy":
            enemy.attack()
            fu_xuan.talent()
            queue.pop(0)
            queue.append("enemy")
            qingque.dmg_bonus == 0
            fu_xuan.matrix_of_prescience()

fight()
