from kandinsky import *
from ion import *
from time import *
from random import *
big_font=[(20,20,8,50,(255,)*3)
]
time=0
def menu():
  global time
 
  fill_rect(0,0,322,222,(0,20,100))
  while not keydown(KEY_EXE):
   
    for i in big_font:
      fill_rect(*i)
   
    time+=1    
    if time>0 and time<500:
      draw_string("PRESS [EXE] key to start",40,160,(0,255,255),(0,20,100))
     
    if time>500 and time<800:
        draw_string("                         ",40,160,(0,20,100),(0,20,100))
     
    if time>800:
      time=0
 
     
  if keydown(KEY_EXE):
    menu=0
menu()
paused=False
score=0
clock=0
star_size=1
star_colors=["white",
"yellow",
"orange",
"red",
"blue"
]
C=(randint(0,255),randint(0,255),randint(0,255))
R=(randint(0,255),randint(0,255),randint(0,255))
c=randint(0,322)
d=randint(0,222)
R=randint(0,70)
G=randint(0,70)
B=randint(0,70)
rr=40
gg=25
bb=100
r=randint(0,80)
g=randint(10,50)
b=randint(15,25)
r2=randint(5,55)
g2=randint(5,55)
b2=randint(5,55)
energy=50
energy_x=randint(5,250)
energy_y=randint(10,200)
energy_width=9
energy_height=15
energy_timer=0
background_color=(rr,gg,bb)
RC=(randint(0,230),randint(0,230),randint(0,230))
move=True
game_end=False
p_timer=0
p_dir_LEFT=1
p_dir_RIGHT=2
p_dir_UP=3
p_dir_DOWN=4
p_x=10
p_y=100
sleep_slow=1/10**4
p_speed_fast=1/10**9
p_pace=1
p_speed_range=2
p_width=10
p_height=4
p_color="white"
SCREEN_width=321
SCREEN_height=222
bar_width=randint(15,40)
bar_height=randint(170,210)
bar_x=randint(170,265-bar_width)
bar_y=randint(10,200)
bar_color=(r,g,b)
bar_width2=randint(15,40)
bar_height2=randint(170,210)
bar_x2=randint(170,265-bar_width)
bar_y2=randint(10,200)
bar_color2=(r,g,b)
bar_dir_LEFT=False
bar_dir_RIGHT=False
bar_dir_UP=False
bar_dir_DOWN=False
bar_UP=False
timer_bar=0
fill_rect(0,0,322,222,background_color)
fill_rect(265,0,2,222,(225,)*3)
while not game_end and not paused:
  score+=randint(0,1)
  clock+=1
  if clock>0 and clock<30:
    c=randint(0,322)
    d=randint(0,90)
    C=star_colors[randint(0,4)]
 
  fill_rect(c,d,star_size,star_size,C)
  draw_string("S:"+str(score),260,6,(169,169,169),background_color)
  draw_string("+",energy_x,energy_y,(255,)*3,(255,0,0))  
  draw_string("E:"+str(energy),260,24,(169,)*3,background_color)
  energy+=0.002
  bar_x-=1
  bar_x2-=1
  energy_timer+=1
  fill_rect(0,0,265,5,(40,0,0))
  fill_rect(0,217,265,4,(40,0,0))
 
 
  if bar_x < -bar_width-1:
    bar_x=randint(170,265-bar_width)
    bar_y=randint(-50,150)
    bar_width=randint(15,40)
    bar_height=randint(120,200)
    r=randint(5,255)
    g=randint(5,255)
    b=randint(5,255)
    bar_color=(r,g,b)
    clock=0
    c=randint(0,322)
    d=randint(0,90)
    C=star_colors[randint(0,4)]
    fill_rect(c,d,star_size,star_size,C)
 
   
  if bar_x2 < -bar_width2-1:
    bar_x2=randint(150,200-bar_width)
    bar_y2=randint(-30,0)
    bar_width2=randint(20,50)
    bar_height2=randint(80,150)
    r2=randint(5,55)
    g2=randint(5,55)
    b2=randint(5,55)
    bar_color2=(r2,g2,b2)
       
   
  fill_rect(bar_x,bar_y,bar_width,bar_height,bar_color)
  fill_rect(bar_x+bar_width+1,bar_y,1,bar_height,background_color)
 
  fill_rect(bar_x2,bar_y2,bar_width2,bar_height2,bar_color2)
  fill_rect(bar_x2+bar_width2+1,bar_y2,1,bar_height2,background_color)
  fill_rect(p_x,p_y,p_width,p_height,p_color)
  fill_rect(p_x,p_y,p_width,p_height,p_color)
         
  if p_x+10 > bar_x and p_x<=bar_x+bar_width and p_y+4 >= bar_y and p_y <= bar_y+bar_height or p_x+10 > bar_x2 and p_x<=bar_x2+bar_width2 and p_y+4 >= bar_y2 and p_y <= bar_y2+bar_height2:
    energy-=0.5
  if energy<1:
    game_end=True
  if p_x+10>265:
    p_x=265-10
    move=False
  else:
    move=True
  #could just use 0
 
  if p_x+p_width >= energy_x and p_y+p_height >= energy_y and p_y <= energy_y+energy_height or p_x <= bar_x+bar_width and p_y+p_height >= bar_y and p_y <= energy_y+energy_height:
    energy+=2
    draw_string(".",energy_x,energy_y,background_color,background_color)      
    energy_x=randint(-20,250)
    energy_y=randint(-20,300)
    energy_timer=0
    score+=randint(5,20)
 
  if energy_timer>randint(400,600):
    draw_string(" ",energy_x,energy_y,background_color,background_color)      
    energy_x=randint(5,250)
    energy_y=randint(5,210)
    energy_timer=0
   
  if p_x<(SCREEN_width-SCREEN_width):
    move=False
    p_x=SCREEN_width-SCREEN_width
  else:
    move=True
  if p_y<5:
    move=False
    p_y=5
  else:
    move=True
  if p_y>SCREEN_height-10:
    move=False
    p_y=SCREEN_height-10
  else:
    move=True
  if move:
    if keydown(KEY_RIGHT):
      move=True
      energy-=0.002
      sleep(sleep_slow)
      p_x+=p_pace
      fill_rect(p_x-1,p_y,1,4,background_color)
     
      if keydown(KEY_OK):
        move=True
        for i in range(p_speed_range):
          p_x+=1
          fill_rect(p_x-1,p_y,1,10,background_color)
    if keydown(KEY_LEFT):
      move=True
      energy-=0.002
      sleep(sleep_slow)
      p_x-=p_pace
      fill_rect(p_x+10,p_y,1,10,background_color)
     
      if keydown(KEY_OK):
        move=True
        energy-=0.005
        for i in range(p_speed_range):
          p_x-=1
          fill_rect(p_x+10,p_y,1,10,background_color)
    if keydown(KEY_UP):
      move=True
      energy-=0.002
      sleep(sleep_slow)
      p_y-=1
      fill_rect(p_x,p_y+4,10,1,background_color)
     
      if keydown(KEY_OK):
        move=True
        energy-=0.005
        for i in range(p_speed_range):
          p_y-=1
          fill_rect(p_x,p_y+4,10,1,background_color)
     
    if keydown(KEY_DOWN):
      move=True
      energy-=0.002
      sleep(sleep_slow)
      p_y+=1
      fill_rect(p_x,p_y-1,10,1,background_color)
      if keydown(KEY_OK):
        move=True
        energy-=0.005
        for i in range(p_speed_range):
          p_y+=1
          fill_rect(p_x,p_y-1,10,1,background_color)
     
    if keydown(KEY_BACKSPACE):
      draw_string("(PAUSED)",100,10,"white",background_color)
      draw_string("OK Key = Fast Speed",70,50,"white",background_color)
      while keydown(KEY_BACKSPACE):
        pass
      while not keydown(KEY_BACKSPACE):
        pass
      while keydown(KEY_BACKSPACE):
        draw_string("        ",100,10,background_color,background_color)
        draw_string("                    ",70,50,background_color,background_color)
        pass
    if keydown(KEY_SHIFT):
      draw_string("(PAUSED)",100,10,"white",background_color)
      draw_string("OK Key = Fast Speed",70,50,"white",background_color)
      while keydown(KEY_SHIFT):
        pass
      while not keydown(KEY_SHIFT):
        pass
      while keydown(KEY_SHIFT):
        draw_string("        ",100,10,background_color,background_color)
        draw_string("                    ",70,50,background_color,background_color)
        pass
     
for i in range(320):
    for j in range(220):
     
      fill_rect(i,j,5,5,"black")
 
draw_string("GAME OVER",100,70,(255,)*3,(0,)*3)      
draw_string("Score: "+str(score),100,120,(0,255,0),(0,)*3)
fill_rect(0,0,322,40,(269,)*3)
fill_rect(0,182,322,40,(269,)*3)
