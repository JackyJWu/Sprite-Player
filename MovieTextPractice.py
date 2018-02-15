import time
import curses
#sprite parts
spr = {}
#sprite assembly
sprite = {}
#end command
SENTINEL = 'end'
#line count (note that it does not include blanks)
linenum = 0
#list which is used to assemble dictionary.
L= []
#space
space= False
spc = []
w=curses.initscr()

#framedelay
framedelay = 0
#framecmd
framecmd= ['copy','start','end']
#draw command, used for drawing the animation.
def draw( y , x ):
    for i in range(0,len(sprite[words[1]])):

        w.addstr(int(words[3])+i, int(words[4]), spr[sprite[words[1]][i]])
#checkarg (cmd ,lw= list of words  ,mn = minumum arg, mx max arg)
def checkarg(cmd):
    if cmd == 'framedelay':
        mn=1
        mx=1
        if len(words)-1 != mn:
            e= 'only allows 1 argument!, argument(s) present:'
            error(e ,linenum, len(words)-1 )

    if cmd == 'line':
        mn=2
        mx=2
        if len(words)-1 != mn:
            e= 'only uses 2 arguments!, argument(s) present:'
            error(e ,linenum,len(words)-1 )


    if cmd == 'end':
        if len(words) != 1:
            if len(words) >1:
                e = 'has no arguments, argument(s) present:'
                error(e ,linenum, len(words)-1 )
    if cmd == 'sprite':
        mn=2
        mx=20000000
        if len(words)-1 < mn:
            e= ' allows 2 or more arguments!, argument(s) present:'
            error(e ,linenum, len(words)-1 )

    if cmd == 'frame':
        mn=1
        mx=1
        if len(words)-1 != mn:
            e= 'only allows 1 argument!, argument(s) present:'
            error(e ,linenum,len(words)-1 )
    if cmd == 'draw':
        mn = 4
        mx = 4
        if len(words)-1 != mn:
            e= 'only allows 4 arguments!, argument(s) present:'
            error(e ,linenum,len(words)-1)
    if cmd == 'space':
        mn = 1
        if len(words)-1 != mn:
            e= 'only allows 1 argument!, argument(s) present:'
            error(e ,linenum,len(words)-1 )


#checks errors
def checkerror(n):
#error framedelay
    if n == 'framedelay':

        if len(words)-1 == 1:
            if words[1].isdigit() == False:
                if '-' in words[1]:
                    e= 'cannot take negative integers/floats'
                    error(e,linenum,words[1])

                if '-' not in words[1]:
                    if words[1].count('.') != 1:
                        e= 'cannot take nonintegers/nonfloats'
                        error(e, linenum,words[1])
                    if words[1].count('.') == 1:
                        if words[1].replace('.','').isdigit() == False:
                            e= 'cannot take nonintegers/nonfloats'
                            error(e, linenum,words[1])
#error draw
    if n == 'draw':
        if 'at' not in words:
            e='draw is missing keyword "at"'
            error(e, linenum, words[2])
        if '-' in words[3]:
            e='cannot use negative row coordinate'
            error(e, linenum,words[3])
        if '-' in words[4]:
            e='cannot use negative column coordinate'
            error(e, linenum, words[4])
        if words[1] not in sprite:
            e='cannot use the undefined sprite'
            error(e, linenum, words[1])
        if words[3].isdigit() ==False:
            e='coordinates are not integers!'
            error(e, linenum, words[3])
        if words[4].isdigit() ==False:
            e='coordinates are not integers!'
            error(e, linenum, words[4])

#error sprite
    if n == 'sprite':
        if len(words) < 3:
            e = 'not enough arguments! (name of sprite and one or more data lines)'
            error(e, linenum)
        for i in range(2,len(words)):
            if words[i] not in spr:
                e = 'there is no data associated with'
                error(e, linenum, words[i])
#error frame
    if n == 'frame':
        if words[1] not in framecmd:
            e = 'command undefined'
            error(e,linenum, words[1])
    if n == 'space':
        if len(words[1])!= 1:
            e = 'uses a single character'
            error(e,linenum, words[1])








#error (e = wrong, l= linenum)
def error(e,l,j):
    w=curses.endwin()
    print('ERROR: line number:',linenum+1,'the command','"',words[0],'"',e, 'error =','"',j,'"')


    quit()











#line reading command
while True:

    line = input()
    words = line.split(' ')
    if line == input():
#end command
        if line == '':
            line = linenum +1
            continue
        elif line != '':
            checkarg(words[0])
            checkerror(words[0])

            if words[0] == SENTINEL:

                linenum = linenum + 1
                checkerror(words[0])
                if w == curses.initscr():
                    w = curses.endwin()
                if w == curses.endwin():
                    continue
                break




    #line command (removes all the periods )
            elif words[0] == 'framedelay':


                linenum = linenum + 1
                if '.' in words[1]:
                    framedelay = float(words[1])
                elif '.' not in words[1]:
                    framedelay = int(words[1])




            elif words[0] == 'line':
                linenum = linenum + 1

    #space command (+ line)
                if space == False:
                    words[2].replace('.', ' ')

                    spr[words[1]] = words[2].replace('.', ' ')

                elif space == True:
                    words[2].replace(spc[0], ' ')
                    spr[words[1]] = words[2].replace(spc[0], ' ')


    #space

            elif words[0] == 'space':
                if space != True:
                    spc = []
                    space = True
                    spc.append(words[1])
                if space == True:
                    spc = []
                    spc.append(words[1])


    #assembles the sprite
            elif words[0] == 'sprite':
                linenum = linenum + 1
                for i in range(2,len(words)):

                    L.append(words[i])

                    sprite[words[1]] = L
                L = []
    #draws the sprite in window
            elif words[0] == 'draw':
                linenum = linenum + 1

                draw(int(words[3]),int(words[4]))

    #checks for hash symbols
            elif '#' in words[0]:
                linenum = linenum + 1
                continue
            elif words[0] == 'frame':
                linenum = linenum + 1


                if words[1] == 'start':

                    w.clear()
                if words[1] == 'copy':
                    w.refresh()

                if words[1] == 'end':
                    w.move( 0 , 0)
                    w.refresh()
                    time.sleep(framedelay)
    #command not defined
            else:
                print(words[0], 'is not a proper command!')
        elif line == False:
            w.endwin()
            print('hi')
            quit()
