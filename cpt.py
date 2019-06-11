import arcade
WIDTH = 719
HEIGHT = 982
button1 = [314, 327, 50, 30]
button2 = [290, 431, 20, 20]
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
#player_location = player_x and player_y
ball_x = 0
player_x = 67
player_y = 495
up_pressed = False
down_pressed = False
right_pressed = False
left_pressed = False

def update(delta_time):
    previous_x_input = None
    previous_y_input = None

    global player_y, player_x
    if up_pressed:
        player_y += 2.45
        previous_y_input = 2.45

    elif down_pressed:
        player_y -= 2.45
        previous_y_input = -2.45

    if right_pressed:
        player_x += 2.45
        previous_x_input = 2.45
    elif left_pressed:
        player_x -= 2.45
        previous_x_input = -2.45

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
    image = arcade.load_texture("/home/robuntu/shea/classwork/computersciencelogo.png")
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
    image = arcade.load_texture("/home/robuntu/shea/classwork/computerscience (2).png")
    arcade.draw_texture_rectangle(WIDTH//2,HEIGHT//2, WIDTH, HEIGHT, image)
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)
    collision()

def draw_Mcdonaldsecretrecipe():
    pass

def collision():
    for obst in dictionary:
        if player_x >= dictionary["con_table"][0] and player_x <= dictionary["con_table"][0] + dictionary["con_table"][2] and player_y >= dictionary["con_table"][1] and player_y <= dictionary["con_table"][3] + dictionary["con_table"][1]:
            print("con_table")
        if player_x >= dictionary["cup_tray"][0] and player_x <= dictionary["cup_tray"][0] + dictionary["cup_tray"][2] and player_y >= dictionary["cup_tray"][1] and player_y <= dictionary["cup_tray"][3] + dictionary["cup_tray"][1]:
            print("cup_tray")
        if player_x >= dictionary["precook_table"][0] and player_x <= dictionary["precook_table"][0] + dictionary["precook_table"][2] and player_y >= dictionary["precook_table"][1] and player_y <= 489:
            print("precook_table")
        if player_x >= dictionary["long_table"][0] and player_x <= dictionary["long_table"][0] + dictionary["long_table"][2] and player_y >= dictionary["long_table"][1] and player_y <= dictionary["long_table"][3] + dictionary["long_table"][1]:
            print("long_table")
        if player_x >= dictionary["table_sticking_out_of_long_table"][0] and player_x <= dictionary["table_sticking_out_of_long_table"][0] + dictionary["table_sticking_out_of_long_table"][2] and player_y >= dictionary["table_sticking_out_of_long_table"][1] and player_y <= dictionary["table_sticking_out_of_long_table"][3] + dictionary["table_sticking_out_of_long_table"][1]:
            print("table_stick_out_of_long_table")
        if player_x >= dictionary["sink"][0] and player_x <= dictionary["sink"][0] + dictionary["sink"][2] and player_y >= dictionary["sink"][1] and player_y <= dictionary["sink"][3] + dictionary["sink"][1]:
            print("sink")
        if player_x >= dictionary["ice_cream_machine"][0] and player_x <= dictionary["ice_cream_machine"][0] + dictionary["ice_cream_machine"][2] and player_y >= dictionary["ice_cream_machine"][1] and player_y <= dictionary["ice_cream_machine"][3] + dictionary["ice_cream_machine"][1]:
            print("ice_cream_machine")
        if player_x >= dictionary["ice_despenser"][0] and player_x <= dictionary["ice_despenser"][0] + dictionary["ice_despenser"][2] and player_y >= dictionary["ice_despenser"][1] and player_y <= dictionary["ice_despenser"][3] + dictionary["ice_despenser"][1]:
            print("ice_despenser")
        if player_x >= dictionary["ice_condiments"][0] and player_x <= dictionary["ice_condiments"][0] + dictionary["ice_condiments"][2] and player_y >= dictionary["ice_condiments"][1] and player_y <= dictionary["ice_condiments"][3] + dictionary["ice_condiments"][1]:
            print("ice_condiments")
        if player_x >= dictionary["bottom_left_wall"][0] and player_x <= dictionary["bottom_left_wall"][0] + dictionary["bottom_left_wall"][2] and player_y >= dictionary["bottom_left_wall"][1] and player_y <= dictionary["bottom_left_wall"][3] + dictionary["bottom_left_wall"][1]:
            print("bottom_left_wall")
        if player_x >= dictionary["cashier_table"][0] and player_x <= dictionary["cashier_table"][0] + dictionary["cashier_table"][2] and player_y >= dictionary["cashier_table"][1] and player_y <= dictionary["cashier_table"][3] + dictionary["cashier_table"][1]:
            print("cashier_table")
        if player_x >= dictionary["box1"][0] and player_x <= dictionary["box1"][0] + dictionary["box1"][2] and player_y >= dictionary["box1"][1] and player_y <= dictionary["box1"][3] + dictionary["box1"][1]:
            print("box1")
        if player_x >= dictionary["box2"][0] and player_x <= dictionary["box2"][0] + dictionary["box2"][2] and player_y >= dictionary["box2"][1] and player_y <= dictionary["box2"][3] + dictionary["box2"][1]:
            print("box2")
        if player_x >= dictionary["box3"][0] and player_x <= dictionary["box3"][0] + dictionary["box3"][2] and player_y >= dictionary["box3"][1] and player_y <= dictionary["box3"][3] + dictionary["box3"][1]:
            print("box3")
        if player_x >= dictionary["box4"][0] and player_x <= dictionary["box4"][0] + dictionary["box4"][2] and player_y >= dictionary["box4"][1] and player_y <= dictionary["box4"][3] + dictionary["box4"][1]:
            print("box4")
        if player_x >= dictionary["box5"][0] and player_x <= dictionary["box5"][0] + dictionary["box5"][2] and player_y >= dictionary["box5"][1] and player_y <= dictionary["box5"][3] + dictionary["box5"][1]:
            print("box5")
        if player_x >= dictionary["long_wall"][0] and player_x <= dictionary["long_wall"][0] + dictionary["long_wall"][2] and player_y >= dictionary["long_wall"][1] and player_y <= dictionary["long_wall"][3] + dictionary["long_wall"][1]:
            print("long_wall")
        if player_x >= dictionary["long_wall2"][0] and player_x <= dictionary["long_wall2"][0] + dictionary["long_wall2"][2] and player_y >= dictionary["long_wall2"][1] and player_y <= dictionary["long_wall2"][3] + dictionary["long_wall2"][1]:
            print("long_wall2")
        if player_x >= dictionary["wall_pole"][0] and player_x <= dictionary["wall_pole"][0] + dictionary["wall_pole"][2] and player_y >= dictionary["wall_pole"][1] and player_y <= dictionary["wall_pole"][3] + dictionary["wall_pole"][1]:
            print("wall_pole")
        if player_x >= dictionary["egg_machine"][0] and player_x <= dictionary["egg_machine"][0] + dictionary["egg_machine"][2] and player_y >= dictionary["egg_machine"][1] and player_y <= dictionary["egg_machine"][3] + dictionary["egg_machine"][1]:
            print("egg_machine")
        if player_x >= dictionary["grill"][0] and player_x <= dictionary["grill"][0] + dictionary["grill"][2] and player_y >= dictionary["grill"][1] and player_y <= dictionary["grill"][3] + dictionary["grill"][1]:
            print("grill")
        if player_x >= dictionary["deep_fryer"][0] and player_x <= dictionary["deep_fryer"][0] + dictionary["deep_fryer"][2] and player_y >= dictionary["deep_fryer"][1] and player_y <= dictionary["deep_fryer"][3] + dictionary["deep_fryer"][1]:
            print("deep_fryer")
        if player_x >= dictionary["papa_frita"][0] and player_x <= dictionary["papa_frita"][0] + dictionary["papa_frita"][2] and player_y >= dictionary["papa_frita"][1] and player_y <= dictionary["papa_frita"][3] + dictionary["papa_frita"][1]:
            print("papa_frita")
        if player_x >= dictionary["papa_fritas_crudas"][0] and player_x <= dictionary["papa_fritas_crudas"][0] + dictionary["papa_fritas_crudas"][2] and player_y >= dictionary["papa_fritas_crudas"][1] and player_y <= dictionary["papa_fritas_crudas"][3] + dictionary["papa_fritas_crudas"][1]:
            print("papa_fritas_crudas")

if __name__ == '__main__':
    setup()
