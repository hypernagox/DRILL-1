import turtle
t = turtle
def move_right():
    t.setheading(0)
def move_up():
    t.setheading(90)
def move_left():
    t.setheading(180)
def move_down():
    t.setheading(270)
t.shape('turtle')
key_commands = {'d':[move_right,False],'w':[move_up,False],'a':[move_left,False],'s':[move_down,False]}
def UpdateState(key,b):
    def handler():
        key_commands[key][1] = b
    return handler
def Update():
    t.onkey(lambda : t.reset(),'Escape')
    t.stamp()
    for key in key_commands.keys():
        t.onkeypress(UpdateState(key,True),key)
        t.onkeyrelease(UpdateState(key,False),key)
    for func,b in key_commands.values():
        if b:
            func()
            t.forward(50)
    t.ontimer(Update,16)
t.listen()
Update()
t.mainloop()