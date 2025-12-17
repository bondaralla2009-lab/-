import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ночная смена"
PLAYER_SPEED = 5


class NightShiftGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player = None

    def setup(self): # пока овал
        self.player = arcade.SpriteSolidColor(80, 50, arcade.color.GRAY)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 3

    def on_draw(self):
        self.clear()

        background = arcade.load_texture("морг.png")

        # Отрисовка игрока
        self.player.draw()

        arcade.draw_text(
            "рассудок",
            start_x=20,
            start_y=SCREEN_HEIGHT - 50,
            color=arcade.color.WHITE,
            font_size=16
        )

    def update(self, delta_time):
        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

    def on_key_press(self, key, modifiers):
        if self.player:
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.player.center_x -= PLAYER_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player.center_x += PLAYER_SPEED


def main():
    game = NightShiftGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()