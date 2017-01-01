#imports
import curses
from curses import wrapper
import random
from random import randrange
import time

window = curses.initscr()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLACK)
curses.init_pair(4,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
curses.init_pair(5,curses.COLOR_CYAN,curses.COLOR_BLACK)
curses.init_pair(6,curses.COLOR_WHITE,curses.COLOR_BLACK)
curses.init_pair(7,curses.COLOR_RED,curses.COLOR_BLACK)

#Relative grid postions for ball
rad1 = [[0,0]]
rad2 = [[1,0],[0,1],[-1,0],[0,-1]]
rad3 = [[2,-1],[2,0],[2,1],[1,2],[0,2],[-1,2],[-2,1],[-2,0],[-2,-1],[-1,-2],[0,-2],[1,-2]]

#Grid positions for star
l0 = [[5,5]]
l1 = [[4,6],[5,6],[6,6],[5,4],[5,6],[4,4],[4,5],[4,6]]
l2 = [[3,7],[5,7],[7,7],[3,5],[7,5],[3,3],[5,3],[7,3]]
l3 = [[2,8],[5,8],[8,8],[2,5],[8,5],[2,2],[5,2],[8,2]]
l4 = [[1,9],[5,9],[9,9],[1,5],[9,5],[1,1],[5,1],[9,2]]
l5 = [[5,19],[5,0],[0,5],[10,5]]

#Grid positions for happy
happy0 = [[0,0],[0,1],[0,2],[0,3],[0,4]]
happy1 = [[1,2]]
happy2 = [[2,0],[2,1],[2,2],[2,3],[2,4]]
#3
happy4 = [[4,0],[4,1],[4,2],[4,3]]
happy5 = [[5,2],[5,4]]
happy6 = [[6,0],[6,1],[6,2],[6,3]]
#7
happy8 = [[8,0],[8,1],[8,2],[8,3],[8,4]]
happy9 = [[9,2],[9,4]]
happy10 = [[10,2],[10,3],[10,4]]
#11
happy12 = [[12,0],[12,1],[12,2],[12,3],[12,4]]
happy13 = [[13,2],[13,4]]
happy14 = [[14,2],[14,3],[14,4]]
#15
happy16 = [[16,3],[16,4]]
happy17 = [[17,0],[17,1],[17,2]]
happy18 = [[18,3],[18,4]]

#Grid positions for new
new0 = [[0,0],[0,1],[0,2],[0,3],[0,4]]
new1 = [[1,3]]
new2 = [[2,2]]
new3 = [[3,0],[3,1],[3,2],[3,3],[3,4]]
#4
new5 = [[5,0],[5,1],[5,2],[5,3],[5,4]]
new6 = [[6,4],[6,2],[6,0]]
new7 = [[7,4],[7,2],[7,0]]
#8
new9 = [[9,1],[9,2],[9,3],[9,4]]
new10 = [[10,0]]
new11 = [[11,1],[11,2]]
new12 = [[12,0]]
new13 = [[13,1],[13,2],[13,3],[13,4]]

#Grid positions for year
year0 = [[0,3],[0,4]]
year1 = [[1,0],[1,1],[1,2]]
year2 = [[2,3],[2,4]]
#3
year4 = [[4,0],[4,1],[4,2],[4,3],[4,4]]
year5 = [[5,4],[5,2],[5,0]]
year6 = [[6,4],[6,2],[6,0]]
#7
year8 = [[8,0],[8,1],[8,2],[8,3]]
year9 = [[9,2],[9,4]]
year10 = [[10,0],[10,1],[10,2],[10,3]]
#11
year12 = [[12,0],[12,1],[12,2],[12,3],[12,4]]
year13 = [[13,2],[13,4]]
year14 = [[14,1],[14,2],[14,3],[14,4]]
year15 = [[15,0],[15,1]]

#Grid positions for three
three0 = [[0,0],[0,1],[0,2]]
three1 = [[1,3]]
three2 = [[2,3]]
three3 = [[3,1],[3,2]]
three4 = [[4,3]]
three5 = [[5,3]]
three6 = [[6,0],[6,1],[6,2]]

#Grid positions for two
two0 = [[0,0],[0,1],[0,2]]
two1 = [[1,3]]
two2 = [[2,1],[2,2]]
two3 = [[3,1]]
two4 = [[4,0],[4,1],[4,2],[4,3]]

#Grid positions for one
one0 = [[0,0]]
one1 = [[1,0]]
one2 = [[2,0]]

def fireworkLaunch(launchX, height):
    lx = launchX
    ly = height
    for x in range(20,height,-1):
        window.addstr(x, launchX, "*", curses.color_pair(2))
        window.refresh()
        time.sleep(0.01)


def fireworkFlicker(ly, lx, char):
    x = 0 
    window.addstr((lx+l0[x][0]-5), (ly+l0[x][1]-5), char, curses.color_pair(x))
    x = randrange(0,7,1)
    window.addstr((lx+l1[x][0]-5), (ly+l1[x][1]-5), char, curses.color_pair(x))
    x = randrange(0,7,1)
    window.addstr((lx+l2[x][0]-5), (ly+l2[x][1]-5), char, curses.color_pair(x))
    x = randrange(0,7,1)
    window.addstr((lx+l3[x][0]-5), (ly+l3[x][1]-5), char, curses.color_pair(x))
    x = randrange(0,7,1)
    window.addstr((lx+l4[x][0]-5), (ly+l4[x][1]-5), char, curses.color_pair(x))
    x = randrange(0,3,1)
    window.addstr((lx+l5[x][0]-5), (ly+l5[x][1]-5), char, curses.color_pair(x))

def fireworkExplode(ly, lx, radius, char):
    y = randrange(0,7,1)

    for x in range(0,1,1):
            window.addstr((lx+l0[x][0]-5), (ly+l0[x][1]-5), char, curses.color_pair(y))
    window.refresh()
    time.sleep(0.05)
    window.clear()
    window.refresh()
    for x in range(0,8,1):
            window.addstr((lx+l1[x][0]-5), (ly+l1[x][1]-5), char, curses.color_pair(y))
    window.refresh()
    time.sleep(0.06)
    window.clear()
    window.refresh()
    for x in range(0,8,1):
            window.addstr((lx+l2[x][0]-5), (ly+l2[x][1]-5), char, curses.color_pair(y))
    window.refresh()
    time.sleep(0.08)
    window.clear()
    window.refresh()
    for x in range(0,8,1):
            window.addstr((lx+l3[x][0]-5), (ly+l3[x][1]-5), char, curses.color_pair(y))
    window.refresh()
    time.sleep(0.09)
    window.refresh()
    for x in range(0,8,1):
            window.addstr((lx+l4[x][0]-5), (ly+l4[x][1]-5), char, curses.color_pair(y))
    window.refresh()
    time.sleep(0.09)
    window.refresh()
    for x in range(0,4,1):
            window.addstr((lx+l5[x][0]-5), (ly+l5[x][1]-5), char, curses.color_pair(y))
    window.refresh()
    time.sleep(0.09)
    window.refresh()
    if radius==1:
        for x in range(0, 1, 1):
            window.addstr((lx), (ly), char, curses.color_pair(randrange(0,7,1)))
    elif radius==2:
        for x in range(0, 4, 1):
            window.addstr((lx+rad2[x][0]), (ly+rad2[x][1]), char, curses.color_pair(randrange(0,7,1)))
    elif radius==3:
        for x in range(0, 12, 1):
            window.addstr((lx+rad3[x][0]), (ly+rad3[x][1]), char, curses.color_pair(randrange(0,7,1)))
    window.refresh()

def happy(lx,ly,y,char):
    for x in range(0,5,1):
        window.addstr((lx+happy0[x][0]), (ly+happy0[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+happy1[x][0]), (ly+happy1[x][1]), char, curses.color_pair(y))
    for x in range(0,5,1):
        window.addstr((lx+happy2[x][0]), (ly+happy2[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+happy4[x][0]), (ly+happy4[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+happy5[x][0]), (ly+happy5[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+happy6[x][0]), (ly+happy6[x][1]), char, curses.color_pair(y))
    for x in range(0,5,1):
        window.addstr((lx+happy8[x][0]), (ly+happy8[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+happy9[x][0]), (ly+happy9[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+happy10[x][0]), (ly+happy10[x][1]), char, curses.color_pair(y))
    for x in range(0,5,1):
        window.addstr((lx+happy12[x][0]), (ly+happy12[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+happy13[x][0]), (ly+happy13[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+happy14[x][0]), (ly+happy14[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+happy16[x][0]), (ly+happy16[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+happy17[x][0]), (ly+happy17[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+happy18[x][0]), (ly+happy18[x][1]), char, curses.color_pair(y))
 

def new(lx,ly,y,char):
    for x in range(0,5,1):
        window.addstr((lx+new0[x][0]), (ly+new0[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+new1[x][0]), (ly+new1[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+new2[x][0]), (ly+new2[x][1]), char, curses.color_pair(y))
    for x in range(0,5,1):
        window.addstr((lx+new3[x][0]), (ly+new3[x][1]), char, curses.color_pair(y))
    for x in range(0,5,1):
        window.addstr((lx+new5[x][0]), (ly+new5[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+new6[x][0]), (ly+new6[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+new7[x][0]), (ly+new7[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+new9[x][0]), (ly+new9[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+new10[x][0]), (ly+new10[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+new11[x][0]), (ly+new11[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+new12[x][0]), (ly+new12[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+new13[x][0]), (ly+new13[x][1]), char, curses.color_pair(y))
    
def year(lx,ly,y,char):
    for x in range(0,2,1):
        window.addstr((lx+year0[x][0]), (ly+year0[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+year1[x][0]), (ly+year1[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+year2[x][0]), (ly+year2[x][1]), char, curses.color_pair(y))
    for x in range(0,5,1):
        window.addstr((lx+year4[x][0]), (ly+year4[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+year5[x][0]), (ly+year5[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+year6[x][0]), (ly+year6[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+year8[x][0]), (ly+year8[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+year9[x][0]), (ly+year9[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+year10[x][0]), (ly+year10[x][1]), char, curses.color_pair(y))
    for x in range(0,5,1):
        window.addstr((lx+year12[x][0]), (ly+year12[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+year13[x][0]), (ly+year13[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+year14[x][0]), (ly+year14[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+year15[x][0]), (ly+year15[x][1]), char, curses.color_pair(y))

def three(lx,ly,y,char):
    for x in range(0,3,1):
        window.addstr((lx+three0[x][0]), (ly+three0[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+three1[x][0]), (ly+three1[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+three2[x][0]), (ly+three2[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+three3[x][0]), (ly+three3[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+three4[x][0]), (ly+three4[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+three5[x][0]), (ly+three5[x][1]), char, curses.color_pair(y))
    for x in range(0,3,1):
        window.addstr((lx+three6[x][0]), (ly+three6[x][1]), char, curses.color_pair(y))

def two(lx,ly,y,char):
    for x in range(0,3,1):
        window.addstr((lx+two0[x][0]), (ly+two0[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+two1[x][0]), (ly+two1[x][1]), char, curses.color_pair(y))
    for x in range(0,2,1):
        window.addstr((lx+two2[x][0]), (ly+two2[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+two3[x][0]), (ly+two3[x][1]), char, curses.color_pair(y))
    for x in range(0,4,1):
        window.addstr((lx+two4[x][0]), (ly+two4[x][1]), char, curses.color_pair(y))

def one(lx,ly,y,char):
    for x in range(0,1,1):
        window.addstr((lx+one0[x][0]), (ly+one0[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+one1[x][0]), (ly+one1[x][1]), char, curses.color_pair(y))
    for x in range(0,1,1):
        window.addstr((lx+one2[x][0]), (ly+one2[x][1]), char, curses.color_pair(y))
    
def firework(x,y):
    fireworkLaunch(x, y)
    fireworkExplode(x, y, 1, "#")
    for j in range(0,30,1):
        fireworkFlicker(x, y, "#")
        window.refresh()
        window.clear()
        time.sleep(0.05)

try:

    while True:
        color = 1
        for k in range (12, 65, 2):
            window.clear()
            if (k%4)==0:
                color = randrange(0,7,1)
            happy(2,k,color,"■")
            window.refresh()
            time.sleep(0.1)
        window.clear()
        three(5,37,7,"■")
        window.refresh()
        time.sleep(0.7)
        for k in range (12,65,2):
            window.clear()
            if (k%4)==0:
                color = randrange(0,7,1)
            new(2,k,color,"■")
            window.refresh()
            time.sleep(0.1)
        window.clear()
        two(5,37,7,"■")
        window.refresh()
        time.sleep(0.7)
 
        for k in range (12,65,2):
            window.clear()
            if (k%4)==0:
                color = randrange(0,7,1)
            year(2,k,color,"■")
            window.refresh()
            time.sleep(0.1)
        window.clear()
        one(5,37,7,"■")
        window.refresh()
        time.sleep(0.7)
        window.refresh()
        time.sleep(0.1)
        for k in range (0,10,1):
            x = randrange(15, 65, 1)
            y = 10
            firework(x,y)

except KeyboardInterrupt:
    pass
finally:
    curses.endwin()
