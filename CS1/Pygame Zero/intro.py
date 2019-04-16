import time

alien1 = Actor('alien')
alien2 = Actor('alien')
alien3 = Actor('alien')
alien4 = Actor('alien')
alien5 = Actor('alien')
alien6 = Actor('alien')
aliens = [alien1, alien2, alien3, alien4, alien5, alien6]
i = 0
for alien in aliens:
    alien.topright = 0, i
    i += 100
WIDTH = 300
HEIGHT = 6*(alien1.height + 20)


def draw():
    screen.clear()
    for alien in aliens:
        alien.draw()


def update():
    for alien in aliens:
        alien.left += 2
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
