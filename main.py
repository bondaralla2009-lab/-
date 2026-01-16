import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Начать' была нажата!")
        # Получаем доступ к окну через функцию arcade.get_window()
        window = arcade.get_window()
        window.current_photo = window.photo1
        window.current_state = "photo1"


class PhotoGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Клик для смены фото")

        # Создаем UI менеджер
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        try:
            # Загружаем все фото
            self.photo1 = arcade.load_texture(r"C:\Users\Алла\Downloads\кабинет с телом.jpg")
            self.photo2 = arcade.load_texture(r"C:\Users\Алла\Downloads\кабинет с ноутом.jpg")
            self.photo3 = arcade.load_texture(r"C:\Users\Алла\Downloads\рабочий стол_arcade.jpg")
            self.photo4 = arcade.load_texture(r"C:\Users\Алла\Downloads\+Белый+шка_измен.jpeg")
            self.photo5 = arcade.load_texture(r"C:\Users\Алла\Downloads\Group 1 (1).png")

        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            arcade.exit()

        # Начинаем с пятого фото (стартового экрана)
        self.current_photo = self.photo5
        self.current_state = "start_screen"

        # Создаем кнопку "Начать" для стартового экрана - В ЦЕНТРЕ
        self.button = MyFlatButton(
            text="Начать",
            center_x=SCREEN_WIDTH // 2,  # Центр по горизонтали
            center_y=SCREEN_HEIGHT // 2,  # Центр по вертикали
            width=200,
            height=40
        )
        self.manager.add(self.button)

        # Координаты для области кликанья Двери первая комната
        self.click_x_min1 = 150
        self.click_x_max1 = 300
        self.click_y_min1 = 200
        self.click_y_max1 = 400

        # Координаты для области кликанья Обратно в первую комнату
        self.click_x_min2 = 10
        self.click_x_max2 = 50
        self.click_y_min2 = 0
        self.click_y_max2 = 1000

        # Координаты для области кликанья На рабочий стол (из photo2 в photo3)
        self.click_x_min2_comp = 80
        self.click_x_max2_comp = 290
        self.click_y_min2_comp = 210
        self.click_y_max2_comp = 380

        # Координаты для области кликанья Обратно из photo3 в photo2
        self.click_x_min3_back = 700
        self.click_x_max3_back = 800
        self.click_y_min3_back = 0
        self.click_y_max3_back = 100

        # Координаты для области кликанья Шкаф первая комната
        self.click_x_min1_v = 10
        self.click_x_max1_v = 70
        self.click_y_min1_v = 270
        self.click_y_max1_v = 430

        # Координаты для возврата с фото4 на фото1 (правый верхний угол)
        self.click_x_min4_back = 700
        self.click_x_max4_back = 800
        self.click_y_min4_back = 0
        self.click_y_max4_back = 600

    def on_draw(self) -> None:
        self.clear()

        # Рисуем текущую фотографию
        arcade.draw_texture_rect(
            self.current_photo,
            arcade.XYWH(
                SCREEN_WIDTH // 2,  # x
                SCREEN_HEIGHT // 2,  # y
                SCREEN_WIDTH,  # ширина
                SCREEN_HEIGHT  # высота
            )
        )

        # Рисуем UI элементы (кнопку) только на стартовом экране
        if self.current_state == "start_screen":
            self.manager.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        # Если мы на стартовом экране, обрабатываем только через UI менеджер
        if self.current_state == "start_screen":
            # UI менеджер сам обработает клик по кнопке
            pass
        elif self.current_state == "photo1":
            # Если на первой фото - дверь
            if (self.click_x_min1 <= x <= self.click_x_max1 and
                    self.click_y_min1 <= y <= self.click_y_max1):
                self.current_photo = self.photo2
                self.current_state = "photo2"
                print("Перешли на фото 2 (комната с ноутом)")

            # Если на первой фото - шкаф
            elif (self.click_x_min1_v <= x <= self.click_x_max1_v and
                  self.click_y_min1_v <= y <= self.click_y_max1_v):
                self.current_photo = self.photo4
                self.current_state = "photo4"
                print("Перешли на фото 4 (шкаф)")

        elif self.current_state == "photo2":
            # Если на второй фото
            # Проверяем зону для возврата в первую комнату
            if (self.click_x_min2 <= x <= self.click_x_max2 and
                    self.click_y_min2 <= y <= self.click_y_max2):
                self.current_photo = self.photo1
                self.current_state = "photo1"
                print("Вернулись на фото 1")

            # Проверяем зону для перехода к компьютеру (photo3)
            elif (self.click_x_min2_comp <= x <= self.click_x_max2_comp and
                  self.click_y_min2_comp <= y <= self.click_y_max2_comp):
                self.current_photo = self.photo3
                self.current_state = "photo3"
                print("Перешли на фото 3 (рабочий стол)")

        elif self.current_state == "photo3":
            # Если на третьей фото, выход из компа
            if (self.click_x_min3_back <= x <= self.click_x_max3_back and
                    self.click_y_min3_back <= y <= self.click_y_max3_back):
                self.current_photo = self.photo2
                self.current_state = "photo2"
                print("Вернулись на фото 2")

        elif self.current_state == "photo4":
            # Если на четвертой фото - возврат на первую
            if (self.click_x_min4_back <= x <= self.click_x_max4_back and
                    self.click_y_min4_back <= y <= self.click_y_max4_back):
                self.current_photo = self.photo1
                self.current_state = "photo1"
                print("Вернулись на фото 1")


if __name__ == "__main__":
    game = PhotoGame()
    arcade.run()