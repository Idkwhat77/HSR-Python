import os
import pygame

script_dir = os.path.dirname(__file__)
battle = os.path.join(script_dir, "battle/battle.mp3") # persona music

# Fu Xuan voiceline loading
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

# Dan Heng voiceline loading
dhb = os.path.join(script_dir, "battle/danheng_basicatk.ogg")
dhs = os.path.join(script_dir, "battle/danheng_skill.ogg")
dhu1 = os.path.join(script_dir, "battle/danheng_ultimate1.ogg")
dhu2 = os.path.join(script_dir, "battle/danheng_ultimate2.ogg")

# jingliu voiceline loading
jlb = os.path.join(script_dir, "battle/jingliu_basicatk.ogg")
jls = os.path.join(script_dir, "battle/jingliu_skill.ogg")
jlu1 = os.path.join(script_dir, "battle/jingliu_ultimate1.ogg")
jlu2 = os.path.join(script_dir, "battle/jingliu_ultimate2.ogg")

# tingyun voiceline loading
tyb = os.path.join(script_dir, "battle/tingyun_basicatk.ogg")
tys1 = os.path.join(script_dir, "battle/tingyun_skill1.ogg")
tys2 = os.path.join(script_dir, "battle/tingyun_skill2.ogg")
tyu1 = os.path.join(script_dir, "battle/tingyun_ultimate1.ogg")
tyu2 = os.path.join(script_dir, "battle/tingyun_ultimate2.ogg")

# tingyun voiceline loading
byb = os.path.join(script_dir, "battle/bronya_basicatk.ogg")
bys1 = os.path.join(script_dir, "battle/bronya_skill1.ogg")
bys2 = os.path.join(script_dir, "battle/bronya_skill2.ogg")
byu1 = os.path.join(script_dir, "battle/bronya_ultimate1.ogg")
byu2 = os.path.join(script_dir, "battle/bronya_ultimate2.ogg")

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
# Fu Xuan sound effect, might get reused later but too lazy to change the name
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

# jingliu sound effect
jlskill = os.path.join(script_dir, "battle/Kill3.mp3")

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

sound_effectjls = pygame.mixer.Sound(jlskill)

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

jingliu_basicatk = pygame.mixer.Sound(jlb)
jingliu_skill = pygame.mixer.Sound(jls)
jingliu_ultimate1 = pygame.mixer.Sound(jlu1)
jingliu_ultimate2 = pygame.mixer.Sound(jlu2)

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

bronya_basicatk = pygame.mixer.Sound(byb)
bronya_skill1 = pygame.mixer.Sound(bys1)
bronya_skill2 = pygame.mixer.Sound(bys2)
bronya_ultimate1 = pygame.mixer.Sound(byu1)
bronya_ultimate2 = pygame.mixer.Sound(byu2)

# pick from random sound
fu_xuan_basicatk = [fu_xuan_basicatk1, fu_xuan_basicatk2]
fu_xuan_skill = [fu_xuan_skill1, fu_xuan_skill2]
qingque_skill = [qingque_skill1, qingque_skill2, qingque_skill3, qingque_skill4, qingque_skill5]
tingyun_skill = [tingyun_skill1, tingyun_skill2]
natasha_basicatk = [natasha_basicatk1, natasha_basicatk2, natasha_basicatk3]
natasha_skill = [natasha_skill1, natasha_skill2]
march7th_skill = [march7th_skill1, march7th_skill2]

pygame.mixer.init()
