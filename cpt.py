import arcade
WIDTH = 719
HEIGHT = 982
button1 = [314, 327, 50, 30]
button2 = [280, 431, 9, 20]
#dictionary is used to set cordinates for obst
dictionary = {
    "con_table": [387, 488, 106, 167],
    "precook_table": [387, 326, 111, 163],
    "cup_tray": [508, 260, 33, 34],
    "long_table": [172, 237, 336, 87],
    "table_sticking_out_of_long_table": [175, 223, 123, 14],
    "sink": [123, 295, 42, 26],
    "ice_cream_machine": [29, 255, 91, 69],
    "ice_despenser": [55, 235, 39, 20],
    "ice_condiments": [0, 211, 23, 45],
    "bottom_left_wall": [0, 0, 212, 212],
    "cashier_table": [212, 21, 506, 87],
    "box1": [18, 365, 53, 83],
    "box2": [77, 370, 54, 78],
    "box3": [135, 359, 83, 89],
    "box4": [225, 368, 89, 83],
    "box5": [258, 457, 89, 83],
    "long_wall": [0, 326, 385, 28],
    "long_wall2": [355, 357, 30, 528],
    "wall_pole": [354, 886, 33, 32],
    "egg_machine": [612, 643, 106, 63],
    "grill": [600, 342, 118, 118],
    "deep_fryer": [620, 346, 98, 175],
    "papa_frita": [616, 252, 102, 93],
    "papa_fritas_crudas": [613, 174, 105, 77],
}
current_screen = "menu"
ball_x = 0
player_x = 67
player_y = 495
up_pressed = False
down_pressed = False
right_pressed = False
left_pressed = False

previous_x_input = False
previous_y_input = False


def update(delta_time):
    global player_y, player_x, previous_x_input, previous_y_input
    #player movements
    if up_pressed:
        player_y += 3
        previous_y_input = 2.45

    elif down_pressed:
        player_y -= 3
        previous_y_input = -3

    if right_pressed:
        player_x += 3
        previous_x_input = 3
    elif left_pressed:
        player_x -= 3
        previous_x_input = -3

    if collision():
        player_x -= previous_x_input
        player_y -= previous_y_input


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
    elif current_screen == "burger_making":
        draw_burger_making()



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
    elif current_screen == "burger_making":
        if key == arcade.key.ESCAPE:
            current_screen = "play"

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
    global current_screen
    #these are for the functionable buttons you can press on in certain screens
    if current_screen == "menu":
        if x > button1[0] and x < button1[1] + button1[2] and y > button1[1] and y < button1[1] + button1[3]:
            current_screen  = "play"
    if current_screen == "instructions":
        if x > button2[0] and x < button2[1] + button2[2] and y > button2[1] and y < button2[1] + button2[3]:
            current_screen = "menu"
    if current_screen == "play":
        if x > 387 and x < 488 + 106 and y > 488 and y < 488 + 167:
            current_screen = "burger_making"

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
    image = arcade.load_texture("michaeljunan/images/computersciencelogo.png")
    arcade.draw_texture_rectangle(WIDTH//2,HEIGHT//2, WIDTH, HEIGHT, image)
    arcade.draw_text("Play", WIDTH/2-45, HEIGHT/3,
                  arcade.color.WHITE_SMOKE, font_size=35)
    arcade.draw_text("Setting", WIDTH/2-35, HEIGHT/3.50,
                  arcade.color.WHITE_SMOKE, font_size=15)


def draw_instructions():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2, arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("click to go back", WIDTH/2, HEIGHT/2-60, arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_play():
    image = arcade.load_texture("michaeljunan/images/computerscience2.png")
    arcade.draw_texture_rectangle(WIDTH//2,HEIGHT//2, WIDTH, HEIGHT, image)
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)
    collision()

def draw_Mcdonaldsecretrecipe():
    pass

def draw_burger_making():
    #click on the con_table located on the oppisite side of the grill. the grill is located on the left of the deep fryer
    image = arcade.load_texture("michaeljunan/images/con_table.png")
    arcade.draw_texture_rectangle(WIDTH//2,HEIGHT//2, WIDTH, HEIGHT, image)

def collision():
    for obst in dictionary:
        if player_x >= dictionary[obst][0] and player_x <= dictionary[obst][0] + dictionary[obst][2] and player_y >= dictionary[obst][1] and player_y <= dictionary[obst][3] + dictionary[obst][1]:
            return True

if __name__ == '__main__':
    setup()
