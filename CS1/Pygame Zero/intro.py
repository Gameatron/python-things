import time
from random import randint
import pgzrun

alien1 = Actor('alien')
alien2 = Actor('alien')
alien3 = Actor('alien')
alien4 = Actor('alien')
alien5 = Actor('alien')
alien6 = Actor('alien')
alien7 = Actor('alien')
alien8 = Actor('alien')
alien9 = Actor('alien')
alien10 = Actor('alien')
alien11 = Actor('alien')
alien12 = Actor('alien')
aliens = [alien1, alien2, alien3, alien4, alien5, alien6,
          alien7, alien8, alien9, alien10, alien11, alien12]
b = 0
a = 0
for alien in aliens:
    alien.topright = a, b
    print(b)
    if b < 550:
        b += 110
    if a < 600:
        a += 100

WIDTH = 600
HEIGHT = 6*(alien1.height + 20)


def draw():
    screen.clear()
    for alien in aliens:
        alien.draw()


def update():
    for alien in aliens:
        alien.left += randint(1, 10)
        if alien.left > WIDTH:
            alien.right = 0


def on_mouse_down(pos):
    for alien in aliens:
        if alien.collidepoint(pos):
            set_alien_hurt(alien)
            aliens.remove(alien)


def set_alien_hurt(alien):
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, .5)


def set_alien_normal():
    for alien in aliens:
        alien.image = 'alien'


pgzrun.go()
