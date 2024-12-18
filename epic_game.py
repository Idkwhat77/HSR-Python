from termcolor import colored
from colorama import init # this is just so color appears when py file open bruh bruh bruh bruh/'
import time
import os
import pygame 
import random

# BEWARE LONG LINES! THIS IS FOR THE HSR BATTLE SYSTEM!
# voicelines and battle music
script_dir = os.path.dirname(__file__)
battle = os.path.join(script_dir, "battle/battle.mp3") # persona music

# fu xuan voiceline loading
fxb1 = os.path.join(script_dir, "battle/fu_xuan_basicatk1.ogg")  
fxb2 = os.path.join(script_dir, "battle/fu_xuan_basicatk2.ogg")
fxs1 = os.path.join(script_dir, "battle/fu_xuan_skill1.ogg")  
fxs2 = os.path.join(script_dir, "battle/fu_xuan_skill2.ogg")
fxu1 = os.path.join(script_dir, "battle/fu_xuan_ultimate1.ogg")  
fxu2 = os.path.join(script_dir, "battle/fu_xuan_ultimate2.ogg")

# qingque voiceline loading
qqb = os.path.join(script_dir, "battle/qingque_basicatk.ogg")
qqeb = os.path.join(script_dir, "battle/qingque_enbasicatk.ogg")
qqs1 = os.path.join(script_dir, "battle/qingque_skill1.ogg")
qqs2 = os.path.join(script_dir, "battle/qingque_skill2.ogg")
qqs3 = os.path.join(script_dir, "battle/qingque_skill3.ogg")
qqs4 = os.path.join(script_dir, "battle/qingque_skill4.ogg")
qqs5 = os.path.join(script_dir, "battle/qingque_skill5.ogg")
qqu1 = os.path.join(script_dir, "battle/qingque_ultimate1.ogg")
qqu2 = os.path.join(script_dir, "battle/qingque_ultimate2.ogg")

# dan heng voiceline loading
dhb = os.path.join(script_dir, "battle/danheng_basicatk.ogg")
dhs = os.path.join(script_dir, "battle/danheng_skill.ogg")
dhu1 = os.path.join(script_dir, "battle/danheng_ultimate1.ogg")
dhu2 = os.path.join(script_dir, "battle/danheng_ultimate2.ogg")

# tingyun voiceline loading
tyb = os.path.join(script_dir, "battle/tingyun_basicatk.ogg")
tys1 = os.path.join(script_dir, "battle/tingyun_skill1.ogg")
tys2 = os.path.join(script_dir, "battle/tingyun_skill2.ogg")
tyu1 = os.path.join(script_dir, "battle/tingyun_ultimate1.ogg")
tyu2 = os.path.join(script_dir, "battle/tingyun_ultimate2.ogg")

# natasha voiceline loading
nsb1 = os.path.join(script_dir, "battle/natasha_basicatk1.ogg")
nsb2 = os.path.join(script_dir, "battle/natasha_basicatk2.ogg")
nsb3 = os.path.join(script_dir, "battle/natasha_basicatk3.ogg")
nss1 = os.path.join(script_dir, "battle/natasha_skill1.ogg")
nss2 = os.path.join(script_dir, "battle/natasha_skill2.ogg")
nsu1 = os.path.join(script_dir, "battle/natasha_ultimate1.ogg")
nsu2 = os.path.join(script_dir, "battle/natasha_ultimate2.ogg")

# march 7th (preservation) voiceline loading
m7b = os.path.join(script_dir, "battle/march7th_basicatk.ogg")
m7s1 = os.path.join(script_dir, "battle/march7th_skill1.ogg")
m7s2 = os.path.join(script_dir, "battle/march7th_skill2.ogg")
m7u1 = os.path.join(script_dir, "battle/march7th_ultimate1.ogg")
m7u2 = os.path.join(script_dir, "battle/march7th_ultimate2.ogg")

# sound effects when attacking
# fu xuan sound effect, might get reused later but too lazy to change the name
fxbasic = os.path.join(script_dir, "battle/holy.mp3")
fxbasic2 = os.path.join(script_dir, "battle/Attack2.mp3")
fxskill = os.path.join(script_dir, "battle/Absorption.mp3")
fxsultimate = os.path.join(script_dir, "battle/Thunder6.mp3")
fxsultimate2 = os.path.join(script_dir, "battle/Blow4.mp3")

# qingque sound effect
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

dan_heng_basicatk = pygame.mixer.Sound(dhb)
dan_heng_skill = pygame.mixer.Sound(dhs)
dan_heng_ultimate1 = pygame.mixer.Sound(dhu1)
dan_heng_ultimate2 = pygame.mixer.Sound(dhu2)

tingyun_basicatk = pygame.mixer.Sound(tyb)
tingyun_skill1 = pygame.mixer.Sound(tys1)
tingyun_skill2 = pygame.mixer.Sound(tys2)
tingyun_ultimate1 = pygame.mixer.Sound(tyu1)
tingyun_ultimate2 = pygame.mixer.Sound(tyu2)

natasha_basicatk1 = pygame.mixer.Sound(nsb1)
natasha_basicatk2 = pygame.mixer.Sound(nsb2)
natasha_basicatk3 = pygame.mixer.Sound(nsb3)
natasha_skill1 = pygame.mixer.Sound(nss1)
natasha_skill2 = pygame.mixer.Sound(nss2)
natasha_ultimate1 = pygame.mixer.Sound(nsu1)
natasha_ultimate2 = pygame.mixer.Sound(nsu2)

march7th_basicatk = pygame.mixer.Sound(m7b)
march7th_skill1 = pygame.mixer.Sound(m7s1)
march7th_skill2 = pygame.mixer.Sound(m7s2)
march7th_ultimate1 = pygame.mixer.Sound(m7u1)
march7th_ultimate2 = pygame.mixer.Sound(m7u2)

# pick from random sound
fu_xuan_basicatk = [fu_xuan_basicatk1, fu_xuan_basicatk2]
fu_xuan_skill = [fu_xuan_skill1, fu_xuan_skill2]
qingque_skill = [qingque_skill1, qingque_skill2, qingque_skill3, qingque_skill4, qingque_skill5]
tingyun_skill = [tingyun_skill1, tingyun_skill2]
natasha_basicatk = [natasha_basicatk1, natasha_basicatk2, natasha_basicatk3]
natasha_skill = [natasha_skill1, natasha_skill2]
march7th_skill = [march7th_skill1, march7th_skill2]

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

def lmao(text, color="white", end='\n'): #halo text visual novel mwehehehee
    for char in text:
        if char in i_want_sleep:
            print(colored(char, color), end='', flush=True)
            time.sleep(0.3)
        else:
            print(colored(char, color), end='', flush=True)
            time.sleep(0.05)
    print(end=end, flush=True)

def n(text, color = "white", end = '\n'): #normal print no visual novel style
    print(colored(text, color), end = '')
    print(end=end, flush=True)

i_want_sleep = ['.', ',', '-','!','?', '~']

class Fu_Xuan:
    def __init__(self):
        self.name = "Fu Xuan"
        self.energy = 0
        self.ORIGINAL_HP = 10000
        self.HP = 10000          
        self.Max_HP = 10000     
        self.ATK = 1400       
        self.DEF = 1200   
        self.CRIT_RATE = 20.0  
        self.CRIT_DMG = 0.6     
        self.shield = 0
        self.matrix = False      
        self.skill_counter = 0
        self.talent_counter = 1    
        self.alive = True 
        self.dmg_bonus = 0
        self.buffs = {}
    
    def stats(self):
        print(f"""
Fu Xuan:
HP = {self.HP:,}/{self.Max_HP:,}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
Buffs = {self.buffs}
""")
        time.sleep(0.5)
        
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
        check_character_buffs()
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
            
            if not self.matrix:
                self.matrix = True
                self.skill_counter = 3
                for target in class_list: 
                    target.Max_HP += target.ORIGINAL_HP * 0.06
                    target.HP += target.ORIGINAL_HP * 0.06
                    target.CRIT_RATE += 12
                    print(f"{target.name}'s Max HP increased to {target.Max_HP:,} and Crit Rate increased to {target.CRIT_RATE}%")
                skill_point -= 1
            else:
                if self.skill_counter < 3:
                    self.skill_counter = 3
                    print("Matrix of Prescience turn refreshed.")
                    
            if self.matrix == True:
                self.energize(50)
            else:
                self.energize(30)
                
            skill_point -= 1
            time.sleep(0.5)

    def ultimate(self):
        if self.energy == 135:
            fu_xuan_ultimate1.play()
            lmao("\"All things in this world have their laws.\"", color = "magenta")
            fu_xuan_ultimate2.play()
            lmao("\"Yet stratagems... constellations.. are human.. creations! Hmph!\"", color = "magenta")
            
            damage = self.HP
            crit = random.randint(0, 100)
            is_critical = crit < self.CRIT_RATE
            sound_effectfxu.play()
            sound_effectfxu2.play()
            if is_critical:
                damage += damage * self.CRIT_DMG
                n("CRIT!", color = "yellow")
                
            print(f"Fu Xuan dealt {damage:.2f} damage with her ultimate!")
            enemy.HP -= damage
            check_character_buffs()
            time.sleep(0.5)
            sound_effectfxs.play()
            
            exclude = fu_xuan
            recover = fu_xuan.Max_HP * 0.05 + 133
            for target in class_list:
                if target != exclude : 
                    target.HP += recover
                    if target.HP > target.Max_HP:
                        target.HP = target.Max_HP
                        print(f"{target.name} restored {target.Max_HP - target.HP} HP!")
                    else:
                        print(f"{target.name} restored {recover} HP!")
            
            if self.talent_counter < 2:
                self.talent_counter += 1
            self.energy -= 135
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
                for target in class_list:
                    target.Max_HP = target.ORIGINAL_HP
                    if target.HP > target.Max_HP:
                        target.HP = target.Max_HP
                    target.CRIT_RATE -= 12
                print("Matrix Of Prescience turn has run off.")
                time.sleep(0.5)
            
class Qingque:
    def __init__(self):
        self.name = "Qingque"
        self.alive = True
        self.ORIGINAL_HP = 3000
        self.HP = 3000          
        self.Max_HP = 3000     
        self.ATK = 3000        
        self.DEF = 1200  
        self.CRIT_RATE = 70     
        self.CRIT_DMG = 2  
        self.shield = 0   
        self.energy = 0
        self.dmg_bonus_stack = 0
        self.dmg_bonus = 0
        self.hidden_hand = False
        self.card = []
        self.buffs = {}

    def stats(self):
        print(f"""
Qingque:
HP = {self.HP}/{self.Max_HP}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
Buffs = {self.buffs}
""")
        time.sleep(0.5)
        
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
        check_character_buffs()
        self.dmg_bonus = 0
        self.dmg_bonus_stack = 0
        if skill_point < 5:
            skill_point += 1

        time.sleep(0.5)
        
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
        check_character_buffs()
        self.dmg_bonus = 0
        self.dmg_bonus_stack = 0
        skill_point += 1
        qingque.hidden_hand = False
        qingque.card = []
        time.sleep(0.5)
        
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
                lmao("\"Gotcha!\"", color = "green")
            elif qq_skill == qingque_skill2:
                lmao("\"Stay calm!\"", color = "green")
            elif qq_skill == qingque_skill3:
                lmao("\"Come on!\"", color = "green")
            elif qq_skill == qingque_skill4:
                lmao("\"Ooh!\"", color = "green")
            elif qq_skill == qingque_skill5:
                lmao("\"Wow!\"", color = "green")
                
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
            check_character_buffs()
            self.energy -= 140
            self.energize(5)
        else:
            print("Not enough energy...")

        time.sleep(0.5)

class Dan_Heng: 
    def __init__(self):
        self.name = "Dan Heng"
        self.alive = True
        self.ORIGINAL_HP = 3000
        self.HP = 3000          
        self.Max_HP = 3000     
        self.ATK = 3000         
        self.DEF = 1200 
        self.CRIT_RATE = 70     
        self.CRIT_DMG = 1.5  
        self.shield = 0   
        self.energy = 0
        self.talent_counter = 0
        self.dmg_bonus = 0
        self.buffs = {}

    def stats(self):
        print(f"""
Dan Heng:
HP = {self.HP}/{self.Max_HP}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
Buffs = {self.buffs}
""")
        time.sleep(0.5)
        
    def energize(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100

    def basic_atk(self):
        global skill_point
        damage = self.ATK * 1.1
        if self.dmg_bonus > 0:
            damage += damage * self.dmg_bonus
        hit1 = damage * 0.45
        hit2 = damage * 0.55
        
        dan_heng_basicatk.play()
        lmao("\"The time is now.\"", color = "green")
        
        crit1 = random.randint(0, 100)
        crit2 = random.randint(0, 100)
        is_critical1 = crit1 < self.CRIT_RATE
        is_critical2 = crit2 < self.CRIT_RATE
        sound_effectqqb.play()
        if is_critical1:
            hit1 += hit1 * self.CRIT_DMG
            n("CRIT!", color = "yellow")    
        enemy.HP -= hit1
        print(f"Dan Heng dealt {hit1:.2f} damage using her basic attack.")

        time.sleep(0.5)
        
        sound_effectqqb.play()
        if is_critical2:
            hit2 += hit2 * self.CRIT_DMG
            n("CRIT!", color = "yellow")    
        enemy.HP -= hit2
        print(f"Dan Heng dealt {hit2:.2f} damage using her basic attack.")

        check_character_buffs()
        
        self.energize(20)
        sound_effectfxb
        if skill_point < 5:
            skill_point += 1

        time.sleep(0.5)
         
    def skill(self):
        global skill_point
        if skill_point == 0:
            print("Not enough SP!")
            pass
        else: 
            damage = self.ATK * 2.86
            if self.dmg_bonus > 0:
                damage += damage * self.dmg_bonus
            hit1 = damage * 0.30
            hit2 = damage * 0.15
            hit3 = damage * 0.15
            hit4 = damage * 0.40
            
            dan_heng_skill.play()
            lmao("\"Hmph.\"", color = "green")
            
            crit1 = random.randint(0, 100)
            crit2 = random.randint(0, 100)
            crit3 = random.randint(0, 100)
            crit4 = random.randint(0, 100)
            is_critical1 = crit1 < self.CRIT_RATE
            is_critical2 = crit2 < self.CRIT_RATE
            is_critical3 = crit3 < self.CRIT_RATE
            is_critical4 = crit4 < self.CRIT_RATE
            sound_effectqqb.play()
            if is_critical1:
                hit1 += hit1 * self.CRIT_DMG
                n("CRIT!", color = "yellow")    
            sound_effectqqb.play()
            enemy.HP -= hit1
            print(f"Dan Heng dealt {hit1:.2f} damage using his skill.")

            time.sleep(0.5)

            if is_critical2:
                hit2 += hit2 * self.CRIT_DMG
                n("CRIT!", color = "yellow")    
            sound_effectqqb.play()
            enemy.HP -= hit2
            print(f"Dan Heng dealt {hit2:.2f} damage using his skill.")

            time.sleep(0.2)
            
            if is_critical3:
                hit3 += hit3 * self.CRIT_DMG
                n("CRIT!", color = "yellow")    
            sound_effectqqb.play()
            enemy.HP -= hit3
            print(f"Dan Heng dealt {hit3:.2f} damage using his skill.")

            time.sleep(0.2)

            if is_critical4:
                hit4 += hit4 * self.CRIT_DMG
                n("CRIT!", color = "yellow")    
            sound_effectqqb.play()
            enemy.HP -= hit4
            print(f"Dan Heng dealt {hit4:.2f} damage using his skill.")

            check_character_buffs()
            
            self.energize(30)
            skill_point -= 1

            time.sleep(0.5)
        
    def ultimate(self):
        if self.energy == 100:
            dan_heng_ultimate1.play()
            lmao("\"The truth of life and death, revealed in an instant.\"", color = "green")
            damage = self.ATK * 4.32
            if self.dmg_bonus > 0:
                damage += damage * self.dmg_bonus
            crit = random.randint(0, 100)
            is_critical = crit < self.CRIT_RATE
            dan_heng_ultimate2.play()
            lmao("\"This sanctuary... is but a vision.. Tch... Break!\"", color = "green")
            
            sound_effectqqu.play()
            if is_critical:
                damage += damage * self.CRIT_DMG
                n("CRIT!", color = "yellow")
                
            enemy.HP -= damage
            print(f"Dan Heng dealt {damage:.2f} damage with his ultimate!")
            
            check_character_buffs()
            
            self.energy -= 100
            self.energize(5)
        else:
            print("Not enough energy...")

        time.sleep(0.5)

    def talent(self):
        print("lmao")
        
class Tingyun: 
    def __init__(self):
        self.name = "Tingyun"
        self.alive = True
        self.ORIGINAL_HP = 2500
        self.HP = 2500         
        self.Max_HP = 2500 
        self.ATK = 3000     
        self.DEF = 1200     
        self.CRIT_RATE = 10     
        self.CRIT_DMG = 0.7   
        self.shield = 0  
        self.energy = 0
        self.benediction = False
        self.ultimate_yes = False
        self.skill_counter = 0
        self.ultimate_counter = 0
        self.dmg_bonus = 0
        self.buffs = {}

    def stats(self):
        print(f"""
Tingyun:
HP = {self.HP}/{self.Max_HP}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
Buffs = {self.buffs}
""")
        time.sleep(0.5)
        
    def energize(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100

    def basic_atk(self):
        global skill_point
        damage = self.ATK * 1.1
        
        tingyun_basicatk.play()
        lmao("\"..Chill out!\"", color = "magenta")
        
        crit = random.randint(0, 100)
        is_critical = crit < self.CRIT_RATE
        
        sound_effectqqb.play()
        if is_critical:
            damage += damage * self.CRIT_DMG
            n("CRIT!", color = "yellow")    
            
        enemy.HP -= damage
        print(f"Tingyun dealt {damage:.2f} damage using her basic attack.")
        
        if self.benediction:
            time.sleep(0.5)
            self.talent()
            
        self.energize(20)
        if skill_point < 5:
            skill_point += 1

        time.sleep(0.5)
         
    def skill(self):
        global skill_point, queue
        if skill_point == 0:
            print("Not enough SP!")
            pass
        else: 
            team()
            while True: 
                try: 
                    choice = int(input("Choose a member by number: ")) - 1
                    if 0 <= choice < len(class_list):               
                        ty_skill = random.choice(tingyun_skill)
                        ty_skill.play()
                        if ty_skill == tingyun_skill1:
                            lmao("\"Evils Begone~\"", color = "magenta")
                        elif ty_skill == tingyun_skill2:
                            lmao("\"All the best~\"", color = "magenta")
                            
                        time.sleep(0.5)
                        sound_effectfxs.play()
                        if self.benediction:
                            previous_target = self.skill_target
                            previous_target.ATK -= self.buff_amount
                            previous_target.buffs.pop("Benediction")
                            self.benediction = False

                        target = class_list[choice]
                        self.skill_target = target
                        tingyun_buff = target.ATK * 0.55
                        if tingyun_buff > self.ATK * 0.27:
                            tingyun_buff = self.ATK * 0.27
                            
                        if "Benediction" != target.buffs:
                            target.buffs["Benediction"] = 3
                        
                        target.ATK = target.ATK + tingyun_buff
                        self.buff_amount = tingyun_buff
                        self.benediction = True 
                        
                        print(f"Tingyun buffed {target.name} with Benediction! {target.name}'s ATK increased to {target.ATK:.2f}.")
                        self.energize(30)
                        skill_point -= 1
                        time.sleep(0.5)
                        break
                    else:
                        lmao("\"That person doesn't exist, silly~.\"", color = "magenta")
                except ValueError:
                    lmao("\"What?\"", color = "magenta")
        
    def ultimate(self):
        if self.energy == 100:
            tingyun_ultimate1.play()
            lmao("\"A thousand wonders, to raise your spirits~\"", color = "magenta")
            while True: 
                team()
                try: 
                    choice = int(input("Choose a member (1-4): ")) - 1
                    if 0 <= choice < len(class_list):               
                        tingyun_ultimate2.play()
                        lmao("\"Good omens.... fight as one!\"", color = "magenta")
                        target = class_list[choice] 
                        if self.ultimate_yes and target == self.ultimate_target:
                            self.ultimate_target.dmg_bonus -= self.buff_ultimate
                            self.ultimate_yes = False
                            
                        time.sleep(0.5)
                        sound_effectfxs.play()  
                        self.ultimate_target = target
                        target.buffs["56% Damage Bonus (Tingyun)"] = 2
                        
                        target.energize(50)
                        target.dmg_bonus += 0.56
                        self.ultimate_yes = True
                        self.buff_ultimate = 0.56
                        
                        print(f"Tingyun increased {target.name}'s energy to {target.energy} and buffed damage by 56%")
                        self.energy -= 100
                        self.energize(5)
                        time.sleep(0.5)
                        break
                    else:
                        lmao("\"That person doesn't exist, silly~.\"", color = "magenta")
                except ValueError:
                    lmao("\"What?\"", color = "magenta")
        else:
            print("Not enough energy...")

        time.sleep(0.5)

    def talent(self):
        target = self.skill_target
        damage = target.ATK * 0.66
        crit = random.randint(0, 100)
        is_critical = crit < target.CRIT_RATE
        
        if is_critical:
            damage += damage * target.CRIT_DMG
            n("CRIT!", color = "yellow")    
            
        enemy.HP -= damage
        print(f"Tingyun dealt additional {damage:.2f} damage with her talent.")
        
    def skill_turn(self):
        if self.benediction:
            target = self.skill_target
            if self.benediction and target.buffs["Benediction"] > 0:
                target.buffs["Benediction"] -= 1
                if target.buffs["Benediction"] == 0 and self.benediction:
                        target.ATK -= self.buff_amount
                        print(f"Tingyun's Benediction on {target.name} has expired. {target.name}'s ATK is now {target.ATK:.2f}.")
                        self.benediction = False
                        target.buffs.pop("Benediction")

    def ultimate_turn(self):
        if self.ultimate_yes:
            target = self.ultimate_target
            if self.ultimate_yes and target.buffs["56% Damage Bonus (Tingyun)"] > 0:
                target.buffs["56% Damage Bonus (Tingyun)"] -= 1
                if target.buffs["56% Damage Bonus (Tingyun)"] == 0:
                        target.dmg_bonus -= self.buff_ultimate
                        print(f"Tingyun's ultimate buff on {target.name} has expired.")
                        self.ultimate_yes = False
                        target.buffs.pop("56% Damage Bonus (Tingyun)")

class Natasha:
    def __init__(self):
        self.name = "Natasha"
        self.alive = True
        self.ORIGINAL_HP = 6600
        self.HP = 6600
        self.Max_HP = 6600 
        self.ATK = 1000      
        self.DEF = 1200   
        self.CRIT_RATE = 20     
        self.CRIT_DMG = 0.8     
        self.shield = 0
        self.energy = 0
        self.skill_counter = 0
        self.dmg_bonus = 0
        self.buffs = {}

    def stats(self):
        print(f"""
Natasha:
HP = {self.HP}/{self.Max_HP}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
Buffs = {self.buffs}
""")
        time.sleep(0.5)
        
    def energize(self, amount):
        self.energy += amount
        if self.energy > 90:
            self.energy = 90

    def basic_atk(self):
        global skill_point
        damage = self.ATK * 1.1
        
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
        
        crit = random.randint(0, 100)
        is_critical = crit < self.CRIT_RATE
        
        sound_effectqqb.play()
        if is_critical:
            damage += damage * self.CRIT_DMG
            n("CRIT!", color = "yellow")    
            
        enemy.HP -= damage
        print(f"Natasha dealt {damage:.2f} damage using her basic attack.")
        
        check_character_buffs()
        
        self.energize(20)
        if skill_point < 5:
            skill_point += 1

        time.sleep(0.5)
         
    def skill(self):
        global skill_point, queue
        if skill_point == 0:
            print("Not enough SP!")
        else: 
            team()
            while True: 
                try: 
                    choice = int(input("Choose a member by number: ")) - 1
                    if 0 <= choice < len(class_list):               
                        nat_skill = random.choice(natasha_skill)
                        nat_skill.play()
                        if nat_skill == natasha_skill1:
                            lmao("\"Here comes the medicine.\"", color = "grey")
                        elif nat_skill == natasha_skill2:
                            lmao("\"All better now?\"", color = "grey")
                            
                        sound_effectfxs.play()

                        target = class_list[choice]
                        self.skill_target = target
                        natasha_skill_healing = self.Max_HP * 0.112 + 311.5
                        target.HP += natasha_skill_healing
                        
                        if target.HP > target.Max_HP: 
                            target.HP = target.Max_HP
                        print(f"Natasha healed {target.name} for {natasha_skill_healing:.2f}.")
                        self.energize(30)
                        skill_point -= 1
                        time.sleep(0.5)
                        break
                    else:
                        lmao("\"Who are you choosing?\"", color = "grey")
                except ValueError:
                    lmao("\"What?\"", color = "grey")
        
    def ultimate(self):
        if self.energy == 90:
            natasha_ultimate1.play()
            lmao("\"..Just in time...\"", color = "grey")
            natasha_ultimate_healing = self.Max_HP * 0.1472 + 409.4
            natasha_ultimate2.play()
            lmao("\"Just a little something.... Mhm~.. Think nothing of it.\"", color = "grey")
            sound_effectfxs.play()
            for target in class_list: 
                target.HP += natasha_ultimate_healing
                print(f"{target.name}'s recovered {natasha_ultimate_healing:.2f} HP.")
            self.energy -= 90
            self.energize(5)
        else:
            print("Not enough energy...")

        time.sleep(0.5)

    def talent(self):
        print("lmao")
                    
class March_7th:
    def __init__(self):
        self.name = "March 7th"
        self.alive = True
        self.ORIGINAL_HP = 2900
        self.HP = 2900
        self.Max_HP = 2900 
        self.ATK = 1500     
        self.DEF = 4000
        self.CRIT_RATE = 15
        self.CRIT_DMG = 0.7    
        self.shield = 0 
        self.energy = 0
        self.skill_counter = 0
        self.dmg_bonus = 0
        self.buffs = {}

    def stats(self):
        print(f"""
March 7th:
HP = {self.HP}/{self.Max_HP}
ATK = {self.ATK}
Crit Rate = {self.CRIT_RATE}%
Crit Damage = {self.CRIT_DMG * 100}%
Buffs = {self.buffs}
""")
        time.sleep(0.5)
        
    def energize(self, amount):
        self.energy += amount
        if self.energy > 120:
            self.energy = 120

    def basic_atk(self):
        global skill_point
        damage = self.ATK * 1.1
        
        march7th_basicatk.play()
        lmao("\"Watch this!\"", color = "cyan")
        
        crit = random.randint(0, 100)
        is_critical = crit < self.CRIT_RATE
        
        sound_effectqqb.play()
        if is_critical:
            damage += damage * self.CRIT_DMG
            n("CRIT!", color = "yellow")    
            
        enemy.HP -= damage
        print(f"March 7th dealt {damage:.2f} damage using her basic attack.")
        
        check_character_buffs()
        
        self.energize(20)
        if skill_point < 5:
            skill_point += 1

        time.sleep(0.5)
         
    def skill(self):
        global skill_point, queue
        team()
        while True: 
            try: 
                choice = int(input("Choose a member by number: ")) - 1
                if 0 <= choice < len(class_list):               
                    march_skill = random.choice(march7th_skill)
                    march_skill.play()
                    if march_skill == march7th_skill1:
                        lmao("\"With me out here, how can we lose~\"", color = "cyan")
                    elif march_skill == march7th_skill2:
                        lmao("\"Stay right there while I give you a present~\"", color = "cyan")
                        
                    sound_effectfxs.play()
                    self.march_shield_power = self.Max_HP * 0.608 + 845.5
                    target = class_list[choice]
                    self.skill_target = target
                    
                    if "Shield (March 7th)" in target.buffs:
                        target.shield -= self.march_shield_power
                        if target.shield < 0:
                            target.shield = 0

                    target.shield += self.march_shield_power
                    target.buffs["Shield (March 7th)"] = 4
                        
                    if target.HP > target.Max_HP: 
                        target.HP = target.Max_HP
                    print(f"March 7th gave {target.name} a shield with {self.march_shield_power:.2f} HP.")
                    self.energize(30)
                    skill_point -= 1
                    time.sleep(0.5)
                    break
                else:
                    lmao("\"Who are you choosing?\"", color = "grey")
            except ValueError:
                lmao("\"What?\"", color = "grey")
        
    def ultimate(self):
        if self.energy == 120:
            damage = self.ATK * 0.162
            march7th_ultimate1.play()
            lmao("\"Gotta try hard sometimes.\"", color = "cyan")
            march7th_ultimate2.play()
            lmao("\"Check out this awesome move~\"", color = "cyan")
            march7th_ultimate2.stop()

            crit = random.randint(0,100)
            is_critical = crit < self.CRIT_RATE
        
            sound_effectqqu.play()
            if is_critical:
                damage += damage * self.CRIT_DMG
                n("CRIT!", color = "yellow")
                
            enemy.HP -= damage
            print(f"March 7th dealt {damage:.2f} damage with his ultimate!")
            
            freeze = random.randint(0,100)
            if freeze >= 65:
                enemy.buffs["Freeze (March 7th)"] = 1
                print(f"The enemy got frozen for 1 turn.")
            
            self.energy -= 120
            self.energize(5)
        else:
            print("Not enough energy...")

        time.sleep(0.5)

    def talent(self):
        if march7th.alive == True:
            damage = self.ATK * 1.1
            
            crit = random.randint(0,100)
            is_critical = crit < self.CRIT_RATE
            
            if is_critical:
                damage += damage * self.CRIT_DMG
                n("CRIT!", color = "yellow")
                
            print(f"March 7th launched a counterattack, dealing {damage:.2f} HP.")
                    
    def skill_turn(self):
        target = self.skill_target
        if 'Shield (March 7th)' in target.buffs:
            if target.buffs["Shield (March 7th)"] > 0:
                target.buffs["Shield (March 7th)"] -= 1
                if target.buffs["Shield (March 7th)"] == 0:
                        target.shield -= self.march_shield_power
                        if target.shield <= 0:
                            target.shield = 0
                        print(f"March 7th's shield on {target.name} has expired. {target.name}'s shield is now {target.shield:.2f}.")
                        target.buffs.pop("Shield (March 7th)")
class Enemy:
    def __init__(self):
        self.HP = 300000
        self.ATK = 1800
        self.buffs = {}
        
    def attack(self):
        global queue
        
        if "Freeze (March 7th)" in self.buffs:
            print("Enemy frozen.")
            self.buffs["Freeze (March 7th)"] -= 1
            damage = march7th.ATK * 0.66
            enemy.HP -= march7th.ATK * 0.66
            print(f"Enemy took {damage} frozen damage.")
            if self.buffs["Freeze (March 7th)"] == 0:
                self.buffs.pop("Freeze (March 7th)")
            return
            
        damage = self.ATK * 0.5
        if fu_xuan.matrix == True:
            damage = damage * 0.82
            
        if not class_list:
            print("dED")
            selection()
            
        sound_effectea.play()
        
        target = random.choice(class_list)
        if target.shield > 0:
            target.shield -= damage
            if target.shield < 0:
                target.HP += target.shield
                target.shield = 0
        else:
            target.HP -= damage
        
        print(f"{target.name} got hit! (-{damage})")
        if "Shield (March 7th)" in target.buffs:
            march7th.talent()
            
        if target.HP < 0:
            target.HP = 0
            print(f"{target.name} is down!")
            target.alive = False
            queue.remove(target.name.lower())
            class_list.remove(target)
        else:
            target.energize(10)    
                
def check_character_buffs(): # check for any additional damage like tingyun's benediction
    if tingyun.benediction:
        target = tingyun.skill_target
        if target.name.lower() == queue[0]:
            damage = target.ATK * 0.44
            crit = random.randint(0, 100)
            is_critical = crit < target.CRIT_RATE
            if is_critical:
                damage += damage * target.CRIT_DMG
                n("CRIT!", color = "yellow")    
                
            enemy.HP -= damage
            print(f"{target.name} dealt additional {damage:.2f} damage with Benediction.")
            
fu_xuan = Fu_Xuan()
qingque = Qingque()
danheng = Dan_Heng()
tingyun = Tingyun()
natasha = Natasha()
march7th = March_7th()

enemy = Enemy()
queue = []
class_list = []
skill_point = 3

# here lies the grave of fucntions mwahahahaa
def team():
    print("Team members:")
    for i, member in enumerate(class_list, start=1):
        print(f"{i}. {member.name}")
        
def selection():
    global queue, class_list
    limit = len(class_list)
    n("Choose your team members:", color="yellow")
    
    while True:
        n("Available team members: Fu Xuan, Qingque, Tingyun, Dan Heng, Natasha, March 7th", color = "yellow")
        team()
        character = input("Type their name here (Team limit = 4, type 0 to start battle, type their name again to remove them.): ").lower()
        if limit < 4:
            if character == "tingyun" and "tingyun" not in queue:
                queue.append(character)
                class_list.append(tingyun)  
                print(f"Tingyun added to the team!")
            elif character == "fu xuan" and "fu xuan" not in queue:
                queue.append(character)
                class_list.append(fu_xuan)  
                print(f"Fu Xuan added to the team!")
            elif character == "qingque" and "qingque" not in queue:
                queue.append(character)
                class_list.append(qingque)  
                print(f"Qingque added to the team!")
            elif character == "dan heng" and "dan heng" not in queue:
                queue.append(character)
                class_list.append(danheng) 
                print(f"Dan Heng added to the team!")
            elif character == "natasha" and "natasha" not in queue:
                queue.append(character)
                class_list.append(natasha)  
                print(f"Natasha added to the team!")
            elif character == "march 7th" and "march 7th" not in queue:
                queue.append(character)
                class_list.append(march7th)  
                print(f"Natasha added to the team!")
            elif character == "0":
                queue.append("enemy")
                fight()
            elif character in queue:
                print(f"{character} is already in the team.")
            else:
                print(f"{character} is not a valid character.")
        else:
            print()
    
def fight():
    global queue
    pygame.mixer.music.load(battle)
    pygame.mixer.music.set_volume(0.5)  
    pygame.mixer.music.play(loops=-1)
    while True:
        who = queue[0]
        if who == "fu xuan" and fu_xuan.alive == True:
            fu_xuan.talent()
            choose = input(f"""
What should Fu Xuan do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {fu_xuan.HP:.2f}) (Talent Counter = {fu_xuan.talent_counter}) (Matrix of Prescience = {fu_xuan.skill_counter}) (Energy = {fu_xuan.energy})
1. Basic ATK (Novaburst)
2. Skill (Known by Stars, Shown by Hearts)
3. Ultimate (Woes of Many Morphed to One)
4. Check Stats
Input : """)
            if choose == "1":
                fu_xuan.basic_atk()
                queue.pop(0)
                queue.append("fu xuan")
            elif choose == "2":
                fu_xuan.skill()
                if skill_point == 0:
                    pass
                else:
                    queue.pop(0)
                    queue.append("fu xuan")
            elif choose == "3":
                fu_xuan.ultimate()
            elif choose == "4":
                fu_xuan.stats()
        elif who == "dan heng" and danheng.alive == True:
            fu_xuan.talent()
            choose = input(f"""
What should Dan Heng do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {danheng.HP:.2f}) (Talent Counter = {danheng.talent_counter}) (Energy = {danheng.energy})
1. Basic ATK (Cloudlancer Art: North Wind)
2. Skill (Cloudlancer Art: Torrent)
3. Ultimate (Ethereal Dream)
4. Check Stats
Input : """)
            if choose == "1":
                danheng.basic_atk()
                queue.pop(0)
                queue.append("dan heng")
            elif choose == "2":
                danheng.skill()
                if skill_point == 0:
                    pass
                else:
                    queue.pop(0)
                    queue.append("dan heng")
            elif choose == "3":
                danheng.ultimate()
            elif choose == "4":
                danheng.stats()
        elif who == "natasha" and natasha.alive == True:
            fu_xuan.talent()
            choose = input(f"""
What should Natasha do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {natasha.HP:.2f}) (Energy = {natasha.energy})
1. Basic ATK (Behind The Kindness)
2. Skill (Love, Heal, and Choose)
3. Ultimate (Gift of Rebirth)
4. Check Stats
Input : """)
            if choose == "1":
                natasha.basic_atk()
                queue.pop(0)
                queue.append("natasha")
            elif choose == "2":
                natasha.skill()
                if skill_point == 0:
                    pass
                else:
                    queue.pop(0)
                    queue.append("natasha")
            elif choose == "3":
                natasha.ultimate()
            elif choose == "4":
                natasha.stats()
        elif who == "march 7th" and march7th.alive == True:
            fu_xuan.talent()
            choose = input(f"""
What should March 7th do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {march7th.HP:.2f}) (Energy = {march7th.energy}) (Shield = {march7th.shield:.2f})
1. Basic ATK (Frigid Cold Arrow)
2. Skill (The Power of Cuteness)
3. Ultimate (Glacial Cascade)
4. Check Stats
Input : """)
            if choose == "1":
                march7th.basic_atk()
                queue.pop(0)
                queue.append("march 7th")
            elif choose == "2":
                if skill_point == 0:
                    print("Not enough SP!")
                    pass
                else:
                    march7th.skill()
                    queue.pop(0)
                    queue.append("march 7th")
            elif choose == "3":
                march7th.ultimate()
            elif choose == "4":
                march7th.stats()
        elif who == "tingyun" and tingyun.alive == True:
            fu_xuan.talent
            placeholder_skill = 0
            placeholder_ultimate = 0
            if tingyun.benediction:
                target = tingyun.skill_target
                placeholder_skill = target.buffs["Benediction"]
            if tingyun.ultimate_yes:
                target = tingyun.ultimate_target
                placeholder_ultimate = target.buffs["56% Damage Bonus (Tingyun)"]
            choose = input(f"""
What should Tingyun do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {tingyun.HP:.2f}) (Skill Turn left = {placeholder_skill}) (Ultimate Turn left = {placeholder_ultimate}) (Energy = {tingyun.energy})
1. Basic ATK (Dislodged)
2. Skill (Soothing Melody)
3. Ultimate (Amidst the Rejoicing Clouds)
4. Check Stats
Input : """)
            if choose == "1":
                tingyun.basic_atk()
                queue.pop(0)
                queue.append("tingyun")
            elif choose == "2":
                tingyun.skill()
                if skill_point == 0:
                    pass
                else:
                    queue.pop(0)
                    queue.append("tingyun")
            elif choose == "3":
                tingyun.ultimate()
            elif choose == "4":
                tingyun.stats()
        elif who == "qingque" and qingque.alive == True:
            fu_xuan.talent()
            if qingque.hidden_hand == False:
                choose = input(f"""
What should Qingque do? (Skill Point = {skill_point}) (Enemy HP = {enemy.HP})
(HP = {qingque.HP:.2f}) (Energy = {qingque.energy})
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
            tingyun.skill_turn()
            tingyun.ultimate_turn()
            march7th.skill_turn()
selection()