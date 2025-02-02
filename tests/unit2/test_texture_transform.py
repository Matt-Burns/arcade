# """
# Unit tests
# Sprites with texture transformations
# """

# import arcade
# from arcade import Matrix3x3

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SHIP_SPEED = 5
# ASPECT = SCREEN_HEIGHT / SCREEN_WIDTH
# SCREEN_TITLE = "Texture transformations"


# def test_tranform(window):
#     ship = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
#     ship.center_x = SCREEN_WIDTH / 2
#     ship.center_y = SCREEN_HEIGHT / 2
#     ship.angle = 270
#     xy_square = arcade.load_texture(":resources:images/test_textures/xy_square.png")
#     t = 0

#     # Set the background color
#     arcade.set_background_color(arcade.color.BLACK)

#     # This command has to happen before we start drawing
#     self.clear()

#     tests = [
#         ['identity', Matrix3x3(), (14, 14, 0)],
#         ['rotate(30)', Matrix3x3().rotate(30), (231, 86, 0)],
#         ['scale(0.8, 0.5)', Matrix3x3().scale(0.8, 0.5), (245, 159, 0)],
#         ['translate(0.3, 0.1)', Matrix3x3().translate(0.3, 0.1), (195, 247, 0)],
#         ['rotate(10).\nscale(0.33, 0.33)', Matrix3x3().rotate(10).scale(0.7, 0.7), (253, 255, 247)],
#         ['scale(-1, 1)', Matrix3x3().scale(-1, 1), (241, 14, 0)],
#         ['shear(0.3, 0.1)', Matrix3x3().shear(0.3, 0.1), (48, 25, 0)],
#         [f'rotate({int(t) % 360})', Matrix3x3().rotate(t), (14, 14, 0)],
#         ]

#     for i, test_data in enumerate(tests):
#         x = 80 + 180 * (i % 4)
#         y = 420 - (i // 4) * 320
#         text, texture, desired_color = test_data
#         arcade.draw_text(text, x, y - 20 - text.count('\n') * 10, arcade.color.WHITE, 10)
#         xy_square.draw_transformed(x, y, 100, 100, 0, 255, texture)

#         test_x = x + 5
#         test_y = y + 5
#         actual_color = arcade.get_pixel(test_x, test_y)

#         # Mac, with its retina scaling, doesn't match other platforms.
#         import sys
#         if sys.platform != "darwin":
#             #
#             print(actual_color, desired_color)
#             assert actual_color[0] == desired_color[0]
#             assert actual_color[1] == desired_color[1]
#             assert actual_color[2] == desired_color[2]
