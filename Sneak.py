import turtle
import time
import random

posponer= 0.1
Estado_cabeza=0
Estado_manzana=0
Estado_escenario=0
#marcador
score=0
high_score=0



#Interfaz/ventana
vn=turtle.Screen()

vn.title("Sneak")
vn.bgcolor("black")
vn.setup(width=1020, height =620)
vn.screensize(1010,610)
vn.tracer(0)
#Score
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.goto(0,260)
texto.hideturtle()
texto.write ("Score=0            High Score= 0", align ="center", font= ("Helvetica",24,"normal"))

#Paredes #terminar

Pared_columnas=turtle.Turtle()
Pared_columnas.pensize(0)
Pared_columnas.fillcolor("red")
Pared_columnas.begin_fill()
Pared_columnas.penup()
Pared_columnas.goto(-510,310)
Pared_columnas.pendown()
Pared_columnas.goto(510,310)
Pared_columnas.goto(510,-310)
Pared_columnas.goto(-510,-310)
Pared_columnas.goto(-510,310)
Pared_columnas.end_fill()
Pared_columnas.hideturtle()

Pared_fondo=turtle.Turtle()
Pared_fondo.pensize(0)
Pared_fondo.fillcolor("black")
Pared_fondo.begin_fill()
Pared_fondo.penup()
Pared_fondo.goto(-490,290)
Pared_fondo.pendown()
Pared_fondo.goto(490,290)
Pared_fondo.goto(490,-290)
Pared_fondo.goto(-490,-290)
Pared_fondo.goto(-490,290)
Pared_fondo.end_fill()
Pared_fondo.hideturtle()



#Firma
firma=turtle.Turtle()
firma.speed(0)
firma.color("white")
firma.penup()
firma.goto(420,-290)
firma.hideturtle()
firma.write ("By Carrizo")

#Cabeza de serpiente
cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
cabeza.showturtle()

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.direction="stop"

#cuerpos de serpiente
cuerpos=[]
def nuevo_cuerpos():
    nueva_parte= turtle.Turtle()
    nueva_parte.speed(9)
    nueva_parte.shape("square")
    nueva_parte.color("grey")
    nueva_parte.penup()
    cuerpos.append(nueva_parte)
    return cuerpos
    
#Funciones del programa
def arriba():
    if cabeza.direction == "down":
        pass
    else:
        cabeza.direction="up"
def abajo():
    if cabeza.direction == "up":
        pass
    else:
        cabeza.direction="down"
def derecha():
    if cabeza.direction == "left":
        pass
    else:
        cabeza.direction="right"
def izquierda():
    if cabeza.direction=="right":
        pass
    else:
        cabeza.direction="left"
    
def movimiento (): 
    if cabeza.direction=="up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction=="down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction=="left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction=="right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def comprobar_pos(x,y):
    match [x,y]:
        #Comprueba si la posción de cabeza/comida esta en la pared L, superior izquierda o inferior derecha
        case x,y if (((x >= -410 and x <= -330) and (y >= 190 and y <= 210)) or ((x >= -410 and x <= -390) and (y <= 180 and y >= 130))) or (((x <= 410 and x >= 330) and (y <= -190 and y >= -210)) or ((x <= 410 and x >= 390) and (y >= -180 and y <= -130))):
            Pos=1
            return Pos
        #Comprueba si la posción de cabeza/comida esta en la pared L, inferior izquierda o superior derecha
        case x,y if (((x >= -410 and x <= -330) and (y <= -190 and y >= -210)) or ((x >= -410 and x <= -390) and (y >= -190 and y <= -130))) or (((x <= 410 and x >= 330) and (y >= 190 and y <= 210)) or ((x <= 410 and x >= 390) and (y <= 180 and y >= 130))):
            Pos=2
            return Pos
        #Comprueba si la poscion de caebeza/comida esta en la pared I, superior o inferior
        case x,y if (( x <= 70 and x >= -70) and ( y >= -90 and y <= -70)) or (( x <= 70 and x >= -70) and ( y <= 90 and y >= 70)):
            Pos=3
            return Pos
        #Comprueba si la poscion de cabeza/comida esta en la pared I, derecha o izquierda
        case x,y if (( x <= 190 and x >= 170) and (y <= 70 and y >= -70)) or (( x <= -170 and x >= -190) and ( y <= 70 and y >= -70)):
            Pos=4
            return Pos
        #Comprueba si la poscion de cabeza/comida no se salio de los limites
        case x,y if (x > 480 or x < -480 or y > 290 or y <-290):
            Pos=5
            return Pos
        #En caso de no estar en ninguna
        case _:
            Pos=0
            return Pos
vn.listen()
vn.onkeypress(arriba,"Up")
vn.onkeypress(abajo,"Down")
vn.onkeypress(derecha,"Right")
vn.onkeypress(izquierda,"Left")
while True:
    vn.update()
    texto.clear()
    time.sleep(posponer)
    texto.write ("Score={}            High Score= {}".format(score,high_score), align ="center", font= ("Helvetica",24,"normal"))
    #Colision con paredes
    if (comprobar_pos(cabeza.xcor(),cabeza.ycor())== 5) or (comprobar_pos(cabeza.xcor(),cabeza.ycor()) == 1 and (Pared_L1.fillcolor() == "red" and Pared_L3.fillcolor() == "red")) or (comprobar_pos(cabeza.xcor(),cabeza.ycor()) == 2 and (Pared_L2.fillcolor() == "red" and Pared_L4.fillcolor() == "red")) or (comprobar_pos(cabeza.xcor(),cabeza.ycor()) == 3 and (Pared_I2.fillcolor() == "red" and Pared_I4.fillcolor() == "red")) or (comprobar_pos(cabeza.xcor(),cabeza.ycor()) == 4 and (Pared_I1.fillcolor() == "red" and Pared_I3.fillcolor() == "red")):
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction= "stop"
        comida.clear()
        comida.goto(0,100)
        for cuerpo in cuerpos:
            cuerpo.goto(1000,1000)
        cuerpos.clear()
        score=0
        posponer= 0.1
        Estado_escenario=0
        texto.clear()
        texto.write ("Score={}            High Score= {}".format(score,high_score), align ="center", font= ("Helvetica",24,"normal"))
        

    #comprobar que la manzana no spawnee en el cuerpo de la serpiente
    if cabeza.distance(comida) < 20:
        x= random.randrange(-480,480,20)
        y= random.randrange(-290,290,20)
        comida.goto(x,y)
        for cuerpo in cuerpos:
            if comida.distance(cuerpo) < 20 and comida.distance(cuerpo) < 20:
                comida.clear()
                x= random.randrange(-280,280,20)
                y= random.randrange(-280,280,20)
        comida.goto(x,y)
    #Adicion de nuevo cuerpos
        nuevo_cuerpos()
    #Score
        score += 10
        if score > high_score:
            high_score = score
            texto.clear()
            texto.write ("Score={}            High Score= {}".format(score,high_score), align ="center", font= ("Helvetica",24,"normal"))
    #comprobar que la manzana no spawnee en las paredes
    if (comprobar_pos(comida.xcor(),comida.ycor())== 5) or (comprobar_pos(comida.xcor(),comida.ycor()) == 1 and (Pared_L1.fillcolor() == "red" and Pared_L3.fillcolor() == "red")) or (comprobar_pos(comida.xcor(),comida.ycor()) == 2 and (Pared_L2.fillcolor() == "red" and Pared_L4.fillcolor() == "red")) or (comprobar_pos(comida.xcor(),comida.ycor()) == 3 and (Pared_I2.fillcolor() == "red" and Pared_I4.fillcolor() == "red")) or (comprobar_pos(comida.xcor(),comida.ycor()) == 4 and (Pared_I1.fillcolor() == "red" and Pared_I3.fillcolor() == "red")):
        x= random.randrange(-480,480,20)
        y= random.randrange(-290,290,20)
        comida.goto(x,y)
            
    total_partes=len(cuerpos)
    #Adicion de nuevo cuerpos
    for index in range (total_partes -1,0,-1):
        x=cuerpos[index-1].xcor()
        y=cuerpos[index-1].ycor()
        cuerpos[index].goto(x,y)
    if total_partes > 0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        cuerpos[0].goto(x,y)
    #colicion con cuerpo
    movimiento()
    for cuerpo in cuerpos:
            if cuerpo.distance(cabeza) < 14:
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction= "stop"
                for cuerpo in cuerpos:
                    cuerpo.goto(1000,1000)
                cuerpos.clear()
                comida.clear()
                comida.goto(0,100)
                score=0
                Estado_escenario=0
                posponer= 0.1
                texto.clear()
                texto.write ("Score={}            High Score= {}".format(score,high_score), align ="center", font= ("Helvetica",24,"normal"))

    #Dificultad
                
    if score == 0 and Estado_escenario == 0:
        Pared_L1=turtle.Turtle()
        Pared_L1.pensize(0)
        Pared_L1.fillcolor("black")
        Pared_L1.begin_fill()
        Pared_L1.penup()
        Pared_L1.goto(-410,130)
        Pared_L1.pendown()
        Pared_L1.goto(-410,210)
        Pared_L1.goto(-330,210)
        Pared_L1.goto(-330,190)
        Pared_L1.goto(-390,190)
        Pared_L1.goto(-390,130)
        Pared_L1.goto(-410,130)
        Pared_L1.end_fill()
        Pared_L1.hideturtle()

        Pared_L2=turtle.Turtle()
        Pared_L2.pensize(0)
        Pared_L2.fillcolor("black")
        Pared_L2.begin_fill()
        Pared_L2.penup()
        Pared_L2.goto(-410,-130)
        Pared_L2.pendown()
        Pared_L2.goto(-410,-210)
        Pared_L2.goto(-330,-210)
        Pared_L2.goto(-330,-190)
        Pared_L2.goto(-390,-190)
        Pared_L2.goto(-390,-130)
        Pared_L2.goto(-410,-130)
        Pared_L2.end_fill()
        Pared_L2.hideturtle()

        Pared_L3=turtle.Turtle()
        Pared_L3.pensize(0)
        Pared_L3.fillcolor("black")
        Pared_L3.begin_fill()
        Pared_L3.penup()
        Pared_L3.goto(410,-130)
        Pared_L3.pendown()
        Pared_L3.goto(410,-210)
        Pared_L3.goto(330,-210)
        Pared_L3.goto(330,-190)
        Pared_L3.goto(390,-190)
        Pared_L3.goto(390,-130)
        Pared_L3.goto(410,-130)
        Pared_L3.end_fill()
        Pared_L3.hideturtle()

        Pared_L4=turtle.Turtle()
        Pared_L4.pensize(0)
        Pared_L4.fillcolor("black")
        Pared_L4.begin_fill()
        Pared_L4.penup()
        Pared_L4.goto(410,130)
        Pared_L4.pendown()
        Pared_L4.goto(410,210)
        Pared_L4.goto(330,210)
        Pared_L4.goto(330,190)
        Pared_L4.goto(390,190)
        Pared_L4.goto(390,130)
        Pared_L4.goto(410,130)
        Pared_L4.end_fill()
        Pared_L4.hideturtle()

        Pared_I1=turtle.Turtle()
        Pared_I1.pensize(0)
        Pared_I1.fillcolor("black")
        Pared_I1.begin_fill()
        Pared_I1.penup()
        Pared_I1.goto(-70,-90)
        Pared_I1.pendown()
        Pared_I1.goto(-70,-70)
        Pared_I1.goto(70,-70)
        Pared_I1.goto(70,-90)
        Pared_I1.goto(-70,-90)
        Pared_I1.end_fill()
        Pared_I1.hideturtle()

        Pared_I2=turtle.Turtle()
        Pared_I2.pensize(0)
        Pared_I2.fillcolor("black")
        Pared_I2.begin_fill()
        Pared_I2.penup()
        Pared_I2.goto(-70,90)
        Pared_I2.pendown()
        Pared_I2.goto(-70,70)
        Pared_I2.goto(70,70)
        Pared_I2.goto(70,90)
        Pared_I2.goto(-70,90)
        Pared_I2.end_fill()
        Pared_I2.hideturtle()

        Pared_I3=turtle.Turtle()
        Pared_I3.pensize(0)
        Pared_I3.fillcolor("black")
        Pared_I3.begin_fill()
        Pared_I3.penup()
        Pared_I3.goto(190,-70)
        Pared_I3.pendown()
        Pared_I3.goto(170,-70)
        Pared_I3.goto(170,70)
        Pared_I3.goto(190,70)
        Pared_I3.goto(190,-70)
        Pared_I3.end_fill()
        Pared_I3.hideturtle()

        Pared_I4=turtle.Turtle()
        Pared_I4.pensize(0)
        Pared_I4.fillcolor("black")
        Pared_I4.begin_fill()
        Pared_I4.penup()
        Pared_I4.goto(-190,-70)
        Pared_I4.pendown()
        Pared_I4.goto(-170,-70)
        Pared_I4.goto(-170,70)
        Pared_I4.goto(-190,70)
        Pared_I4.goto(-190,-70)
        Pared_I4.end_fill()
        Pared_I4.hideturtle()
        posponer= 0.1
        Opcion=3
        Estado_escenario=1
    if score == 10 and Estado_escenario == 1:
        #Comprobar que el jugador no este en la poscion del nuevo muro
        Estado_cabeza1= cabeza.pos()
        Estado_cabeza= comprobar_pos(Estado_cabeza1[0],Estado_cabeza1[1])
        match Estado_cabeza:
            case Estado_cabeza if score !=0 and Estado_cabeza == 1:
                #Izquierda inferior
                Pared_L2=turtle.Turtle()
                Pared_L2.pensize(0)
                Pared_L2.fillcolor("red")
                Pared_L2.begin_fill()
                Pared_L2.penup()
                Pared_L2.goto(-410,130)
                Pared_L2.pendown()
                Pared_L2.goto(-410,210)
                Pared_L2.goto(-330,210)
                Pared_L2.goto(-330,190)
                Pared_L2.goto(-390,190)
                Pared_L2.goto(-390,130)
                Pared_L2.goto(-410,130)
                Pared_L2.end_fill()
                Pared_L2.hideturtle()
                
                #Derecha superior
                Pared_L4=turtle.Turtle()
                Pared_L4.pensize(0)
                Pared_L4.fillcolor("red")
                Pared_L4.begin_fill()
                Pared_L4.penup()
                Pared_L4.goto(410,130)
                Pared_L4.pendown()
                Pared_L4.goto(410,210)
                Pared_L4.goto(330,210)
                Pared_L4.goto(330,190)
                Pared_L4.goto(390,190)
                Pared_L4.goto(390,130)
                Pared_L4.goto(410,130)
                Pared_L4.end_fill()
                Pared_L4.hideturtle()

                
                Opcion=1
                posponer=0.080
                Estado_escenario=2
            case _:
                #Derecha superior
                Pared_L1=turtle.Turtle()
                Pared_L1.pensize(0)
                Pared_L1.fillcolor("red")
                Pared_L1.begin_fill()
                Pared_L1.penup()
                Pared_L1.goto(-410,130)
                Pared_L1.pendown()
                Pared_L1.goto(-410,210)
                Pared_L1.goto(-330,210)
                Pared_L1.goto(-330,190)
                Pared_L1.goto(-390,190)
                Pared_L1.goto(-390,130)
                Pared_L1.goto(-410,130)
                Pared_L1.end_fill()
                Pared_L1.hideturtle()
                
                #Izquierda inferior
                Pared_L3=turtle.Turtle()
                Pared_L3.pensize(0)
                Pared_L3.fillcolor("red")
                Pared_L3.begin_fill()
                Pared_L3.penup()
                Pared_L3.goto(410,-130)
                Pared_L3.pendown()
                Pared_L3.goto(410,-210)
                Pared_L3.goto(330,-210)
                Pared_L3.goto(330,-190)
                Pared_L3.goto(390,-190)
                Pared_L3.goto(390,-130)
                Pared_L3.goto(410,-130)
                Pared_L3.end_fill()
                Pared_L3.hideturtle()
                
                Opcion=2
                posponer=0.080
                Estado_escenario=2
                    

        
    if score == 30 and Estado_escenario==2:
        #Comprobar que el jugador no este en la poscion del nuevo muro
            Estado_cabeza1= cabeza.pos()
            Estado_cabeza= comprobar_pos(Estado_cabeza1[0],Estado_cabeza1[1])
            match Estado_cabeza:
                case Estado_cabeza if score !=0 and Estado_cabeza != 2 and Opcion == 2:
                    #Izquierda inferior
                    Pared_L2=turtle.Turtle()
                    Pared_L2.pensize(0)
                    Pared_L2.fillcolor("red")
                    Pared_L2.begin_fill()
                    Pared_L2.penup()
                    Pared_L2.goto(-410,-130)
                    Pared_L2.pendown()
                    Pared_L2.goto(-410,-210)
                    Pared_L2.goto(-330,-210)
                    Pared_L2.goto(-330,-190)
                    Pared_L2.goto(-390,-190)
                    Pared_L2.goto(-390,-130)
                    Pared_L2.goto(-410,-130)
                    Pared_L2.end_fill()
                    Pared_L2.hideturtle()

                    #Derecha superior
                    Pared_L4=turtle.Turtle()
                    Pared_L4.pensize(0)
                    Pared_L4.fillcolor("red")
                    Pared_L4.begin_fill()
                    Pared_L4.penup()
                    Pared_L4.goto(410,130)
                    Pared_L4.pendown()
                    Pared_L4.goto(410,210)
                    Pared_L4.goto(330,210)
                    Pared_L4.goto(330,190)
                    Pared_L4.goto(390,190)
                    Pared_L4.goto(390,130)
                    Pared_L4.goto(410,130)
                    Pared_L4.end_fill()
                    Pared_L4.hideturtle()

                    Opcion="A"
                    posponer= 0.060
                    Estado_escenario=3
                case _:
                    #pared Izquierda
                    Pared_I1=turtle.Turtle()
                    Pared_I1.pensize(0)
                    Pared_I1.fillcolor("red")
                    Pared_I1.begin_fill()
                    Pared_I1.penup()
                    Pared_I1.goto(-70,-90)
                    Pared_I1.pendown()
                    Pared_I1.goto(-70,-70)
                    Pared_I1.goto(70,-70)
                    Pared_I1.goto(70,-90)
                    Pared_I1.goto(-70,-90)
                    Pared_I1.end_fill()
                    Pared_I1.hideturtle()


                    #Pared Derecha
                    Pared_I3=turtle.Turtle()
                    Pared_I3.pensize(0)
                    Pared_I3.fillcolor("red")
                    Pared_I3.begin_fill()
                    Pared_I3.penup()
                    Pared_I3.goto(190,-70)
                    Pared_I3.pendown()
                    Pared_I3.goto(170,-70)
                    Pared_I3.goto(170,70)
                    Pared_I3.goto(190,70)
                    Pared_I3.goto(190,-70)
                    Pared_I3.end_fill()
                    Pared_I3.hideturtle()

                    Opcion=3
                    Estado_escenario=3
                    posponer= 0.060
    if score == 60 and Estado_escenario==3:
            #Comprobar que el jugador no este en la poscion del nuevo muro
            Estado_cabeza1= cabeza.pos()
            Estado_cabeza= comprobar_pos(Estado_cabeza1[0],Estado_cabeza1[1])
            match Estado_cabeza:
                case Estado_cabeza if score !=0 and Estado_cabeza != 4 and Opcion == "A":
                    #Pared Derecha
                    Pared_I3=turtle.Turtle()
                    Pared_I3.pensize(0)
                    Pared_I3.fillcolor("red")
                    Pared_I3.begin_fill()
                    Pared_I3.penup()
                    Pared_I3.goto(190,-70)
                    Pared_I3.pendown()
                    Pared_I3.goto(170,-70)
                    Pared_I3.goto(170,70)
                    Pared_I3.goto(190,70)
                    Pared_I3.goto(190,-70)
                    Pared_I3.end_fill()
                    Pared_I3.hideturtle()

                    #Pared Izquierda
                    Pared_I4=turtle.Turtle()
                    Pared_I4.pensize(0)
                    Pared_I4.fillcolor("red")
                    Pared_I4.begin_fill()
                    Pared_I4.penup()
                    Pared_I4.goto(-190,-70)
                    Pared_I4.pendown()
                    Pared_I4.goto(-170,-70)
                    Pared_I4.goto(-170,70)
                    Pared_I4.goto(-190,70)
                    Pared_I4.goto(-190,-70)
                    Pared_I4.end_fill()
                    Pared_I4.hideturtle()

                    Opcion="B"
                    posponer= 0.040
                    Estado_escenario=4
                case _:
                    Pared_L2=turtle.Turtle()
                    Pared_L2.pensize(0)
                    Pared_L2.fillcolor("red")
                    Pared_L2.begin_fill()
                    Pared_L2.penup()
                    Pared_L2.goto(-410,-130)
                    Pared_L2.pendown()
                    Pared_L2.goto(-410,-210)
                    Pared_L2.goto(-330,-210)
                    Pared_L2.goto(-330,-190)
                    Pared_L2.goto(-390,-190)
                    Pared_L2.goto(-390,-130)
                    Pared_L2.goto(-410,-130)
                    Pared_L2.end_fill()
                    Pared_L2.hideturtle()


                    Pared_L4=turtle.Turtle()
                    Pared_L4.pensize(0)
                    Pared_L4.fillcolor("red")
                    Pared_L4.begin_fill()
                    Pared_L4.penup()
                    Pared_L4.goto(410,130)
                    Pared_L4.pendown()
                    Pared_L4.goto(410,210)
                    Pared_L4.goto(330,210)
                    Pared_L4.goto(330,190)
                    Pared_L4.goto(390,190)
                    Pared_L4.goto(390,130)
                    Pared_L4.goto(410,130)
                    Pared_L4.end_fill()
                    Pared_L4.hideturtle()

                    Opcion="B"

                    Estado_escenario=4
                    posponer= 0.040
    if score ==  90 and Estado_escenario==4:
        #Comprobar que el jugador no este en la poscion del nuevo muro
        Estado_cabeza1= cabeza.pos()
        Estado_cabeza= comprobar_pos(Estado_cabeza1[0],Estado_cabeza1[1])
        match Estado_cabeza:
            case Estado_cabeza if score !=0 and Estado_cabeza != 3 and Opcion == "B":
                #pared Arriba
                Pared_I1=turtle.Turtle()
                Pared_I1.pensize(0)
                Pared_I1.fillcolor("red")
                Pared_I1.begin_fill()
                Pared_I1.penup()
                Pared_I1.goto(-70,-90)
                Pared_I1.pendown()
                Pared_I1.goto(-70,-70)
                Pared_I1.goto(70,-70)
                Pared_I1.goto(70,-90)
                Pared_I1.goto(-70,-90)
                Pared_I1.end_fill()
                Pared_I1.hideturtle()

                #Pared abajo
                Pared_I2=turtle.Turtle()
                Pared_I2.pensize(0)
                Pared_I2.fillcolor("red")
                Pared_I2.begin_fill()
                Pared_I2.penup()
                Pared_I2.goto(-70,90)
                Pared_I2.pendown()
                Pared_I2.goto(-70,70)
                Pared_I2.goto(70,70)
                Pared_I2.goto(70,90)
                Pared_I2.goto(-70,90)
                Pared_I2.end_fill()
                Pared_I2.hideturtle()

                Opcion="B"
                Estado_escenario=5
                posponer= 0.030
    if score ==  120 and Estado_escenario==5:
        posponer=0.020
        Estado_cabeza1= cabeza.pos()
        Estado_cabeza= comprobar_pos(Estado_cabeza1[0],Estado_cabeza1[1])
        
    if score ==  200 and Estado_escenario==5:
        #final
        final=turtle.Turtle()
        final.speed(0)
        final.color("white")
        
        final.penup()
        final.goto(-130,120)
        final.hideturtle()
        final.write ("Felicidades, haz ganado!", font=("Palatino Linotype",20,"normal"))
        cabeza.goto(0,0)
        cabeza.direction= "stop"
        for cuerpo in cuerpos:
            cuerpo.goto(1000,1000)
        cuerpos.clear()
        comida.clear()
        comida.goto(1000,1000)
        cabeza.direction= "stop"
        
        time.sleep(posponer)  
