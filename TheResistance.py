
from __future__ import division
import pygame
import pickle
import random
from os import path
from pygame.locals import *

##carpeta de assets y sonidos
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sounds')

###############################

WIDTH = 500
HEIGHT = 720
FPS = 60
POWERUP_TIME = 5000

# Define Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

###############################

###############################

## inicializa pygame y se crea la ventana
pygame.init()

## para el sonido
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

## se sincronizan los FPS
clock = pygame.time.Clock()
###############################

##tipo de fuente
font_name = pygame.font.match_font('Starhol')


## definicion del menu
def main_menu():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "gameSong.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "Presiona [ENTER]", 50, WIDTH/2, HEIGHT/3)
            draw_text(screen, "para Continuar", 50, WIDTH/2, (HEIGHT/3)+60)
            draw_text(screen, "o [Q] para Salir", 50, WIDTH/2, (HEIGHT/3)+200)
            pygame.display.update()



    screen.fill((0,0,0))

    draw_text(screen, "Empecemos!", 60, WIDTH/2, HEIGHT/3)
    pygame.display.update()

    ## se detiene la música
    pygame.mixer.music.stop()

## definicion del menu de fin
def end_menu():
    global screen

    end_menu_song = pygame.mixer.music.load(path.join(sound_folder, "gameSong.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "endmain.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "SU PUNTUACION FUE DE:", 50, WIDTH/2, (HEIGHT/4))
            draw_text(screen, str(score), 60, WIDTH/2, (HEIGHT/4)+100)
            draw_text(screen, "Presione [Q] para Salir", 50, WIDTH/2, (HEIGHT/3)+200)
            pygame.display.update()



    screen.fill((0,0,0))

    ## se detiene la música
    pygame.mixer.music.stop()

def draw_text(surf, text, size, x, y):

    ## seleccion de fuente para la puntuacion
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 15
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


 ##barra de vida
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


##cracion de asteroides
def newmob():
    mob_element = Mob()
    all_sprites.add(mob_element)
    mobs.add(mob_element)

##explosion de los elementos
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Player(pygame.sprite.Sprite):             ## configuracion de la nave y las vidas
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        ## tamaño de la nave en el juego
        self.image = pygame.transform.scale(player_img, (70, 60))  ##50,38
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 350
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()

    def update(self):

        ## tiempo fuera para retomar la vida
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        ## unhide
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 30

        ## posiciona al juegador estatico en la pantalla del juego
        self.speedx = 0


        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5

        #disparar manteniendo apretada la barra espaciadora
        if keystate[pygame.K_SPACE]:
            self.shoot()

        ## checkea los bordes
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx

    def shoot(self):

        ## los disparos de la nave por cada poder que agarra
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shooting_sound.play()
            if self.power == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()

            ## poder maximo
            """ MOAR POWAH """
            if self.power >= 3:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)

                ## disparo de misiles desde el centro de la nave
                missile1 = Missile(self.rect.centerx, self.rect.top)

                ##---------
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(missile1)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(missile1)
                shooting_sound.play()
                missile_sound.play()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)


# define los asteroides
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)

        ## hace random la velocidad
        self.speedy = random.randrange(8, 25)

        ## random de los movimientos mas pequeños
        self.speedx = random.randrange(-3, 3)

        ## agrega rotacion a los asteroides
        self.rotation = 0

        ## velocidad de rotacion
        self.rotation_speed = random.randrange(-6, 12)

        ## tiempo de rotacion
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_update > 50: # en milisegundos
            self.last_update = time_now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        ## los elementos que salen de la pantalla

        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

            ## hace random la velocidad de los asteroides
            self.speedy = random.randrange(1, 8)


## define los poderes que se toman

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        ## posiciona los disparos de acuerdo a la posicion de la nave
        self.rect.center = center
        self.speedy = 2

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy

        ## elimina los sprite luego de que salen de la pantalla
        if self.rect.top > HEIGHT:
            self.kill()



## Define los sprite para los disparos
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        ## posiciona los disparos de acuerdo a la posicion del jugador
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy

        ## elimina los sprites cuando salen de la pantalla
        if self.rect.bottom < 0:
            self.kill()

        ## ahora se definen los disparos
        ## el funcionamiento de la barra espaciadora
        ## se añade el loop a juego

## disparo de misiles
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


###################################################
## cargamos todas las imagenes

background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
background_rect = background.get_rect()


player_img = pygame.image.load(path.join(img_dir, 'playerShip1_blue.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 25))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, 'laserBlue16.png')).convert()
missile_img = pygame.image.load(path.join(img_dir, 'spaceMissiles.png')).convert_alpha()
# meteor_img = pygame.image.load(path.join(img_dir, 'meteorBrown_med1.png')).convert()

## lista de meteoritos en el juego

meteor_images = []
meteor_list = [
    'meteorGrey_big3.png',
    'meteorGrey_big4.png',
    'meteorGrey_med1.png',
    'meteorBrown_big1.png',
    'meteorGrey_med2.png',
    'meteorGrey_small1.png',
    'meteorGrey_small2.png',
    'meteorBrown_big2.png',
    'meteorGrey_tiny2.png',
    'meteorGrey_med1.png',
    'meteorGrey_med2.png',
    'meteorBrown_big3.png',
]

for image in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, image)).convert())

## explosiones

## se definen los vectores y las escalas con respecto a la pantalla, de las explosiones
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):

    ##explosion de meteoritos
    filename = 'explosionRed.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)

    ## tamaño de la explosion
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

    ## explosion del jugador
    filename = 'player_explosion4.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

## se cargan los poderes
powerup_images = {}

## aumenta la barra de vida
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()

## aumenta el armamento de la nave
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()


###################################################


###################################################
### se cargan todos los sonidos del juego

## sonidos de disparos (rayitos)
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'laser1.ogg'))

## sonidos de los misiles
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'tone1.ogg'))

## sonidos de las explosiones
expl_sounds = []
for sound in ['explosion_asteroid.wav', 'explosion_enemy.wav']: ##expl 13, 16
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))

## sonido de fondo del juego
pygame.mixer.music.set_volume(5)

## sonido de la muerte del jugador
player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'explosion_player.wav'))

###################################################

## se agrupan todos los sprites para ser actualizados más facilmente
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

## se generan grupos
mobs = pygame.sprite.Group()
for i in range(8):      ## 8 mobs
    # mob_element = Mob()
    # all_sprites.add(mob_element)
    # mobs.add(mob_element)
    newmob()

## grupo para las balas
bullets = pygame.sprite.Group()

##para los poderes
powerups = pygame.sprite.Group()

#### variable de contador de puntaje
score = 0

## hace que la música del juego se repita siempre. si la reproduccion es (loops=-1) no funciona.
# Error :
# Tipo de error: play() takes no keyword arguments
#pygame.mixer.music.play()

#############################

## loop del juego
running = True
menu_display = True
while running:
    if menu_display:
        main_menu()
        pygame.time.wait(3000)

        #se detiene la música del menu
        pygame.mixer.music.stop()

        #empieza la música del juego
        pygame.mixer.music.load(path.join(sound_folder, 'music_background.wav'))

        ## hace que la música termine cuando el jugador pierda
        pygame.mixer.music.play(-1)

        menu_display = False

    #1 procesos de eventos o entradas

    ## hace que el bucle se ejecute a la misma velocidad
    clock.tick(FPS)

    for event in pygame.event.get():
        # mantiene todos los eventos que se han producido hasta el momento y
        ## mantiene una pestaña con ellos

        ## espera a que el boton "X" se presione
        if event.type == pygame.QUIT:
            running = False

        ## el boton ESC hace que el juego se cierre
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # ## evento para disparar las balas
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()      ## we have to define the shoot()  function

    #2 actualizacion
    all_sprites.update()


    ## comprueba si las balas golpearon algo
    ## ahora se tiene un grupo de bullets y un grupo de mobs

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    ## se eliminan los asteroides que chocan con las balas
    ## ya que no habran elementos fuera del juego
    for hit in hits:

        ## se obtienen distintos puntajes por el tamaño de cada meteorito
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        # m = Mob()
        # all_sprites.add(m)
        # mobs.add(m)
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)

        ## se genera un nuevo asteroide
        newmob()


    ## ^^ este loop de arriba crea la cantidad de objetos que fueron destruidos
    #########################

    ## verifica si el jugador colisiona con un meteorito
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)        ## gives back a list, True makes the mob element disappear
    for hit in hits:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            # running = False     ## GAME OVER
            player.hide()
            player.lives -= 1
            player.shield = 100

    ## si el jugador toma un aumento de vida
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            player.powerup()

    ## la ultima muerte del jugador hace que el juego finalice
    if player.lives == 0 and not death_explosion.alive():
        running = False
        menu_display = True
        pygame.display.update()

    #3 dibujar / hacer
    screen.fill(BLACK)

    ## dibuja la imagen de fondo
    screen.blit(background, background_rect)

    all_sprites.draw(screen)

    ## 10px abajo del inicio de la pantalla
    draw_text(screen, str(score), 30, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)

    # dibuja  las vidas
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)

    ## finaliza el dibujado de todo en la pantalla
    pygame.display.flip()


## loop para mostrar la puntuacion
running = True
end_menu_display = True
while running:
    if end_menu_display:
        end_menu()
        pygame.time.wait(3000)

        #se detiene la música del menu
        pygame.mixer.music.stop()

        #empieza la música del juego
        pygame.mixer.music.load(path.join(sound_folder, 'music_background.wav'))

        ## hace que la música termine cuando el jugador pierda
        pygame.mixer.music.play(-1)

        end_menu_display = False


##TODO: finaliza el juego
pygame.quit()