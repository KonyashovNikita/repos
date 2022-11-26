import matplotlib.pyplot as plt
from math import sin, cos, exp, atan
from numpy import arange
t = 20
m = 0.1
k = 0.9
v0 = 50
angel = 1.5
g = 10

# content = document["content"]
# canvas = content.select_one(".myCanvas")
# ctx = canvas.getContext("2d")

# ctx.beginPath()
# ctx.rect(20, 40, 50, 50)
# ctx.fillStyle = "#FF0000"
# ctx.fill()
# ctx.closePath()


# self.x = self.v0 * cos(self.angel) * self.k / self.m * (1 - exp(-self.k * self.t / self.m))
# self.y = self.m / self.k * ((self.v0 * sin(self.angel) + self.m * self.g / self.k) * (1 - exp(-self.k * self.t / self.m)) - self.g * self.t)


# def draw():
#     ctx.clearRect(0, 0, canvas.width, canvas.height)
#     drawBall()
#     t += 1     

from browser import document, window, timer
        from random import randint
        from math import sin, cos, exp, pi, atan, sqrt
        ballRadius = 20
        ballcount = 2

    
        class Balls():

            def __init__(self, ctx):
                self.ctx = ctx
                self.t = [0 for _ in range(ballcount)]
                self.g = 10
                self.v0 = [randint(50, 150) for _ in range(ballcount)]
                self.angle = [randint(1, 10) / 10 for _ in range(ballcount)]
                self.vx = [self.v0[i] * cos(self.angle[i]) for i in range(ballcount)]
                self.v0y = [self.v0[i] * sin(self.angle[i]) for i in range(ballcount)]
                self.vy = [self.v0[i] * sin(self.angle[i]) for i in range(ballcount)]
                self.x0 = [randint(ballRadius, canvas.width - ballRadius) for _ in range(ballcount)]
                self.y0 = [randint(ballRadius, canvas.height - ballRadius) for _ in range(ballcount)]
                self.x = [self.x0[i] + self.vx[i] * self.t[i] for i in range(ballcount)]
                self.y = [self.y0[i] + self.v0y[i] * self.t[i] - self.g * self.t[i] * self.t[i] / 2 for i in range(ballcount)]
                self.e = [self.vx[i] ** 2 + self.vy[i] for i in range(ballcount)]

            def drawBalls(self):
                for i in range(ballcount):
                    ctx = self.ctx 
                    ctx.beginPath()
                    ctx.arc(self.x[i], canvas.height - self.y[i], ballRadius, 0, 2 * pi)
                    ctx.fillStyle = "#0095DD"
                    ctx.fill()
                    ctx.closePath()
                    self.updateBalls()

            def updateBalls(self):
                for i in range(ballcount):
                    if (self.x[i] > canvas.width-ballRadius):
                        self.vx[i] = -self.vx[i] * 0.8
                        self.t[i] = 0
                        self.x0[i] = canvas.width-ballRadius
                        self.y0[i] = self.y[i]
                        self.v0y[i] = self.vy[i]

                    if (self.x[i] < ballRadius):
                        self.vx[i] = -self.vx[i] * 0.8
                        self.t[i] = 0
                        self.x0[i] = ballRadius
                        self.y0[i] = self.y[i]
                        self.v0y[i] = self.vy[i]
    
                    if (self.y[i] > canvas.height - ballRadius):
                        self.vy[i] = -self.vy[i] * 0.8
                        self.t[i] = 0
                        self.x0[i] = self.x[i]
                        self.y0[i] = canvas.height - ballRadius
                        self.v0y[i] = self.vy[i]

                    if (self.y[i] < ballRadius):
                        self.vy[i] = -self.vy[i] * 0.8
                        self.t[i] = 0
                        self.x0[i] = self.x[i]
                        self.y0[i] = ballRadius
                        self.v0y[i] = self.vy[i]

                    for j in range(i+1, ballcount):
                        dx = self.x[i] - self.x[j]
                        dy = self.y[i] - self.y[j]
                        if sqrt(dx ** 2 + dy ** 2) <= 2 * ballRadius:
                            v1x = self.vx[i] * 0.8
                            v1y = self.vy[i] * 0.8
                            v2x = self.vx[j] * 0.8
                            v2y = self.vy[j] * 0.8
                            self.vx[i] = v2x
                            self.v0y[i] = v2y
                            self.vy[i] = v2y
                            self.x0[i] = max(self.x[i] - dx/2 - ballRadius * cos(ang), ballRadius)
                            self.y0[i] = self.y[i] - dy/2 - ballRadius * sin(ang)
                            self.t[i] = 0
                            self.vx[j] = v1x
                            self.v0y[j] = v1y
                            self.vy[j] = v1y
                            self.x0[j] = max(self.x[j] + dx/2 + ballRadius * cos(ang), ballRadius)
                            self.y0[j] = self.y[j] + dy/2 + ballRadius * sin(ang) 
                            self.t[j] = 0

    
                    self.t[i] += 0.1 / ballcount
                    self.vy[i] -= self.g * 0.1 / ballcount
                    self.vy[i] = self.vy[i] * 0.99999
                    self.vx[i] = self.vx[i] * 0.9999 
                    self.x[i] = self.x0[i] + self.vx[i] * self.t[i] 
                    self.y[i] = self.y0[i] + self.v0y[i] * self.t[i] - self.g * self.t[i] * self.t[i] / 2

            def draw(self, *args):
                self.ctx.clearRect(0, 0, canvas.width, canvas.height)
                self.drawBalls()
                window.requestAnimationFrame(self.draw)
            
                    
        canvas = document["myCanvas"]
        ctx = canvas.getContext("2d")
        balls = Balls(ctx)
        balls.draw()
        document <= "test"