# cpt-michael-jun-an-shea
cpt-michael-jun-an-shea created by GitHub Classroom

import arcade
WIDTH = 719
HEIGHT = 982
button1 = [314, 327, 50, 30]
button2 = [290, 431, 20, 20]
dictionary = {
    "con_table": [387, 488, 106, 655],
    "precook_table": [387, 326, 111, 489],
    "cup_tray": [508, 260, 33, 294],
    "long_table": [172, 237, 336, 324],
    "table_sticking_out_of_long_table": [175, 223, 123, 237],
    "sink": [123, 295, 42, 321],
    "ice_cream_machine": [29, 255, 91, 324],
    "ice_despenser": [55, 235, 39, 255],
    "ice_condiments": [0, 211, 23, 256],
    "bottom_left_wall": [0, 0, 212, 838],
    "cashier_table": [212, 21, 506, 108],
    "box1": [18, 365, 53, 448],
    "box2": [77, 370, 54, 448],
    "box3": [135, 359, 83, 448],
    "box4": [225, 368, 89, 451],
    "box5": [258, 457, 89, 540],
    "long_wall": [0, 326, 385, 354],
    "long_wall2": [355, 357, 30, 885],
    "wall_pole": [354, 886, 33, 918],
    "egg_machine": [612, 643, 106, 706],
    "grill": [600, 342, 118, 460],
    "deep_fryer": [620, 346, 98, 521],
    "papa_frita": [616, 252, 102, 345],
    "papas _fritas_crudas": [613, 174, 105, 251],
}
current_screen = "menu"
#player_location = player_x and player_y
ball_x = 0
player_x = 67
player_y = 495
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
    elif current_screen == "Mcdonaldsecretrecipe":
        draw_Mcdonaldsecretrecipe()



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
    if current_screen == "menu":
        if x > button1[0] and x < button1[1] + button1[2] and y > button1[1] and y < button1[1] + button1[3]:
            print("clicked")
    if current_screen == "instructions":
        if x > button2[0] and x < button2[1] + button2[2] and y > button2[1] and y < button2[1] + button2[3]:
            print("clicked2")


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
    collision()

def draw_Mcdonaldsecretrecipe():
    pass

def collision():
    for obst in dictionary:
        if player_x <= 0 or player_x >= 719 or player_y <= 0 or player_y >= 982:
            print("wall")
        elif player_x >= 387 and player_x <= 493 and player_y >= 488 and player_y <= 655:
            print("con_table")
        elif player_x >= 387 and player_x <= 498 and player_y >= 326 and player_y <= 489:
            print("precook_table")
        elif player_x >= 508 and player_x <= 541 and player_y >= 260 and player_y <= 294:
            print("cup_tray")
        elif player_x >= 172 and player_x <= 508 and player_y >= 237 and player_y <= 324:
            print("long_table")
        elif player_x >= 175 and player_x <= 298 and player_y >= 223 and player_y <= 237:
            print("table_sticking_out_of_long_table")
if __name__ == '__main__':
    setup()


