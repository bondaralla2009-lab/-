import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Начать' была нажата!")
        window = arcade.get_window()
        window.show_text = True
        window.current_text_index = 1  # Начинаем с первого текста
        arcade.set_background_color(arcade.color.BLACK)


class PhotoGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Клик для смены фото")

        # Создаем UI менеджер
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Флаги для отображения текста
        self.show_text = False
        self.current_text_index = 0  # 0 - нет текста, 1-5 - тексты
        self.text_finished = False   # Новый флаг -  тексты завершены

        try:
            # Загружаем все фото
            self.photo1 = arcade.load_texture("data/кабинет с телом1.jpg")
            self.photo2 = arcade.load_texture("data/Комната с ноутом2.png")
            self.photo3 = arcade.load_texture("data/рабочий стол_arcade3.jpg")
            self.photo4 = arcade.load_texture("data/+Белый+шка_измен4.jpeg")
            self.photo5 = arcade.load_texture("data/Group 1 (1)5.png")

        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            arcade.exit()

        # Начинаем с пятого фото (стартового экрана)
        self.current_photo = self.photo5
        self.current_state = "start_screen"

        # Создаем кнопку "Начать" для стартового экрана - В ЦЕНТРЕ
        self.button = MyFlatButton(
            text="Начать",
            center_x=SCREEN_WIDTH // 2,
            center_y=SCREEN_HEIGHT // 2,
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

        # координаты для области кликанья Обратно из photo3 в photo2
        self.click_x_min3_back = 700
        self.click_x_max3_back = 800
        self.click_y_min3_back = 0
        self.click_y_max3_back = 100

        # координаты для области кликанья Шкаф первая комната
        self.click_x_min1_v = 10
        self.click_x_max1_v = 70
        self.click_y_min1_v = 270
        self.click_y_max1_v = 430

        # координаты для возврата с фото4 на фото1 (правый верхний угол)
        self.click_x_min4_back = 700
        self.click_x_max4_back = 800
        self.click_y_min4_back = 0
        self.click_y_max4_back = 600

        # определяем тексты
        self.texts = {
            1: "Ммм да, мама была права, нужно было идти в универ,\n"
               "щас бы работал в офисе... бумажки разгребал",
            2: "Лааадно, Том, соберись, люди нуждаются в тебе,\n"
               "кто если не ты будет копаться в телах людей.\n"
               "Господь, я и правду занимаюсь чем-то не тем.",
            3: "Хотя уже не важно, я слишком долго искал эту работу,\n"
               "она мне и правда нужна.",
            4: "Только таак хочется спать...",
            5: "Почему вообще первый рабочей день и сразу ночная смена??"
        }

    def on_draw(self) -> None:
        self.clear()

        # если показываем текстовые экраны и тексты еще не завершены
        if self.show_text and not self.text_finished and self.current_text_index > 0:
            text = self.texts.get(self.current_text_index, "")

            #текущий текст
            arcade.draw_text(
                text,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                arcade.color.WHITE,
                20,
                anchor_x="center",
                anchor_y="center",
                align="center",
                width=SCREEN_WIDTH - 100,
                multiline=True
            )
        else:
            # рисуем текущую фотографию
            arcade.draw_texture_rect(
                self.current_photo,
                arcade.XYWH(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )

            # Рисуем юи элементы (кнопку) только на стартовом экране
            if self.current_state == "start_screen":
                self.manager.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        # обработка кликов на текстовых экранах (только если тексты еще не завершены)
        if self.show_text and not self.text_finished and self.current_text_index > 0:
            if self.current_text_index < 5:
                # Переходим к следующему тексту
                self.current_text_index += 1
            else:
                # После последнего текста переходим на photo2 и отмечаем, что тексты завершены
                self.show_text = False
                self.text_finished = True #     ага
                self.current_text_index = 0
                self.current_photo = self.photo2
                self.current_state = "photo2"
                arcade.set_background_color(arcade.color.DEFAULT)  # Возвращаем фон по умолчанию
                print("Тексты завершены, переходим на photo2")
            return  # Выходим, так как обработали клик на текстовом экране

        # Обработка кликов по фотографиям (только если не показываем текст)
        if self.current_state == "start_screen":
            # UI менеджер сам обработает клик по кнопке
            pass
        elif self.current_state == "photo1":
            if (self.click_x_min1 <= x <= self.click_x_max1 and
                    self.click_y_min1 <= y <= self.click_y_max1):
                self.current_photo = self.photo2
                self.current_state = "photo2"
                print("Перешли на фото 2 (комната с ноутом)")

            elif (self.click_x_min1_v <= x <= self.click_x_max1_v and
                  self.click_y_min1_v <= y <= self.click_y_max1_v):
                self.current_photo = self.photo4
                self.current_state = "photo4"
                print("Перешли на фото 4 (шкаф)")

        elif self.current_state == "photo2":
            # Если клик в области для возврата на photo1
            if (self.click_x_min2 <= x <= self.click_x_max2 and
                    self.click_y_min2 <= y <= self.click_y_max2):
                self.current_photo = self.photo1
                self.current_state = "photo1"
                print("Вернулись на фото 1")

            # Если клик в области для перехода к компьютеру (photo3)
            elif (self.click_x_min2_comp <= x <= self.click_x_max2_comp and
                  self.click_y_min2_comp <= y <= self.click_y_max2_comp):
                self.current_photo = self.photo3
                self.current_state = "photo3"
                print("Перешли на фото 3 (рабочий стол)")

        elif self.current_state == "photo3":
            if (self.click_x_min3_back <= x <= self.click_x_max3_back and
                    self.click_y_min3_back <= y <= self.click_y_max3_back):
                self.current_photo = self.photo2
                self.current_state = "photo2"
                print("Вернулись на фото 2")

        elif self.current_state == "photo4":
            if (self.click_x_min4_back <= x <= self.click_x_max4_back and
                    self.click_y_min4_back <= y <= self.click_y_max4_back):
                self.current_photo = self.photo1
                self.current_state = "photo1"
                print("Вернулись на фото 1")


if __name__ == "__main__":
    game = PhotoGame()
    arcade.run()