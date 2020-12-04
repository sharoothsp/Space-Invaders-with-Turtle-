
import turtle
import os
import math
import random


wn=turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Space invaders")
wn.bgpic("sbg.gif")

turtle.register_shape("enemy.gif")
turtle.register_shape("player.gif")

border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for i in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()


score=0

scorep=turtle.Turtle()
scorep.speed(0)
scorep.color("white")
scorep.penup()
scorep.setposition(210,250)
scores="Score: %s" %score
scorep.write(scores, False, align="left",font=("Arial"
, 14, "normal"))
scorep.hideturtle()




player=turtle.Turtle()

player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.lt(90)


playerspeed=15


no_of_enemies=5
enemies=[]
for i in range(no_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("green")
	enemy.shape("enemy.gif")
	enemy.penup()
	enemy.speed(0)
	x=random.randint(-200,200)
	y=random.randint(100,250)		
	enemy.setposition(x,y)
enemyspeed=2

bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed=20

bulletstate="ready"








def mleft():
	x=player.xcor()
	if x>-285:
		
		x=x-playerspeed
		player.setx(x)
def mright():
	x=player.xcor()
	if x<285:
		
		x=x+playerspeed
		player.setx(x)
def firebullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate= "fire"

		
		x=player.xcor()
		y=player.ycor()
		bullet.setposition(x,y+10)
		bullet.showturtle()




def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True 
	else:
		return False
	


turtle.listen()
turtle.onkey(mleft,"Left")
turtle.onkey(mright,"Right")
turtle.onkey(firebullet,"space")



while True:
	for enemy in enemies:
		x=enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
		if enemy.xcor() > 280:
			for e in enemies:
			
				y=e.ycor()
				y-=40
				e.sety(y)
			enemyspeed *=-1 
		if enemy.xcor() < -280:
			for e in enemies:
				y=e.ycor()
				y-=40
				e.sety(y)
			enemyspeed *= -1
		if isCollision(bullet,enemy):
			score +=1
			scores="Score: %s" %score
			scorep.clear()
			scorep.write(scores, False, align="left",font=("Arial", 14, "normal"))
			
			bullet.hideturtle()
			bulletstate ="ready"
			x=random.randint(-200,200)
			y=random.randint(100,250)
			enemy.setposition(x,y)
		if isCollision(player,enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("game over")
			break
	if bulletstate == "fire":
		y=bullet.ycor()
		y+=bulletspeed
		bullet.sety(y)
	if bullet.ycor() > 275:
		
		bullet.hideturtle()
		bulletstate="ready"
	
	
	
		

	
	








delay=input("press enter to finish")
