# cpt-michael-jun-an-shea
cpt-michael-jun-an-shea created by GitHub Classroom

import arcade
WIDTH = 719
HEIGHT = 982
button1 = [314, 327, 50, 30]

current_screen = "menu"
#player_location = player_x and player_y
ball_x = 0
player_x = 100
player_y = 100
up_pressed = False
down_pressed = False
right_pressed = False
left_pressed = False

def update(delta_time):
    global player_y, player_x
    if up_pressed:
     player_y += 2.45
    elif down_pressed:
     player_y -= 2.45

    if right_pressed:
     player_x += 2.45
    elif left_pressed:
     player_x -= 2.45


def on_draw():
    arcade.start_render()
    if current_screen == "menu":
     draw_menu()
    elif current_screen == "instructions":
     draw_instructions()
    elif current_screen == "play":
     draw_play()

def on_key_press(key, modifiers):
    global current_screen

    if current_screen == "menu":
     if key == arcade.key.I:
         current_screen = "instructions"
     elif key == arcade.key.P:
         current_screen = "play"
     elif key == arcade.key.ESCAPE:
         exit()
    elif current_screen == "instructions":
     if key == arcade.key.ESCAPE:
         current_screen = "menu"
    elif current_screen == "play":
     if key == arcade.key.ESCAPE:
         current_screen = "menu"

    global up_pressed, down_pressed
    if current_screen == "play":
     if key == arcade.key.UP:
         up_pressed = True
     elif key == arcade.key.DOWN:
         down_pressed = True
     global right_pressed, left_pressed
     if key == arcade.key.RIGHT:
         right_pressed = True
     elif key == arcade.key.LEFT:
         left_pressed = True

def on_key_release(key, modifiers):
    global up_pressed, down_pressed
    if current_screen == "play":
     if key == arcade.key.UP:
         up_pressed = False
     elif key == arcade.key.DOWN:
         down_pressed = False
     global right_pressed, left_pressed
     if key == arcade.key.RIGHT:
         right_pressed = False
     elif key == arcade.key.LEFT:
         left_pressed = False


def on_mouse_press(x, y, button, modifiers):
    if x > button1[0] and x < button1[1] + button1[2] and y > button1[1] and y < button1[1] + button1[3]:
        #i am trying to make it go into the function draw_play
        #draw_play()
        print("clicked")


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def draw_menu():
    image = arcade.load_texture("C:/Users/micha/Downloads/computersciencelogo.png")
    arcade.draw_texture_rectangle(WIDTH//2,HEIGHT//2, WIDTH, HEIGHT, image)
    arcade.draw_text("Play", WIDTH/2-45, HEIGHT/3,
                  arcade.color.WHITE_SMOKE, font_size=35)
    arcade.draw_text("Setting", WIDTH/2-35, HEIGHT/3.50,
                  arcade.color.WHITE_SMOKE, font_size=15)


def draw_instructions():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2, arcade.color.WHITE, font_size=30, anchor_x="center")
    arcade.draw_text("ESC to go back", WIDTH/2, HEIGHT/2-60, arcade.color.WHITE, font_size=20, anchor_x="center")


def draw_play():
    image = arcade.load_texture("C:/Users/micha/Downloads/computerscience2.png")
    arcade.draw_texture_rectangle(WIDTH//2,HEIGHT//2, WIDTH, HEIGHT, image)
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)


if __name__ == '__main__':
    setup()


