import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Начать' была нажата!")
        window = arcade.get_window()
        window.show_text = True
        window.current_text_index = 1
        arcade.set_background_color(arcade.color.BLACK)


class RulesButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Правила' была нажата!")
        window = arcade.get_window()
        window.show_rules = True
        arcade.set_background_color(arcade.color.BLACK)


class ClickAreas:
    """Координаты кликабельных областей"""
    def __init__(self):
        # Дверь первая комната
        self.door_photo1 = {
            "x_min": 150, "x_max": 300,
            "y_min": 200, "y_max": 400
        }
        # Обратно в первую комнату
        self.back_to_photo1 = {
            "x_min": 10, "x_max": 50,
            "y_min": 0, "y_max": 1000
        }
        # На рабочий стол (из photo2 в photo3)
        self.to_computer = {
            "x_min": 80, "x_max": 290,
            "y_min": 210, "y_max": 380
        }
        # Обратно из photo3 в photo2
        self.back_from_computer = {
            "x_min": 700, "x_max": 800,
            "y_min": 0, "y_max": 100
        }
        # Шкаф первая комната
        self.cabinet_photo1 = {
            "x_min": 10, "x_max": 70,
            "y_min": 270, "y_max": 430
        }
        # Возврат с фото4 на фото1
        self.back_from_cabinet = {
            "x_min": 700, "x_max": 800,
            "y_min": 0, "y_max": 600
        }
        # Осмотр тела на photo1
        self.examination_area = {
            "x_min": 300, "x_max": 500,
            "y_min": 200, "y_max": 400
        }
        # Отчет на photo3
        self.report_area = {
            "x_min": 160, "x_max": 200,
            "y_min": 50, "y_max": 100
        }

    def is_in_area(self, x, y, area_name):
        """Проверка, находится ли точка в указанной области"""
        area = getattr(self, area_name, None)
        if area:
            return (area["x_min"] <= x <= area["x_max"] and
                    area["y_min"] <= y <= area["y_max"])
        return False


class PhotoManager:
    """Менеджер загрузки и хранения фотографий"""
    def __init__(self):
        self.photos = {}
        self.load_photos()

    def load_photos(self):
        """Загрузка всех фотографий"""
        photo_files = {
            "photo1": "data/кабинет с телом1.jpg",
            "photo2": "data/Комната с ноутом2.png",
            "photo3": "data/рабочий стол_arcade3.jpg",
            "photo4": "data/+Белый+шка_измен4.jpeg",
            "photo5": "data/Group 1 (1)5.png",
            "photo6": "data/Отчет6.png"
        }

        for key, filepath in photo_files.items():
            try:
                self.photos[key] = arcade.load_texture(filepath)
            except Exception as e:
                print(f"Ошибка загрузки изображения {filepath}: {e}")
                arcade.exit()


class GameTexts:
    """Хранение всех текстов игры"""
    def __init__(self):
        self.texts = {
            1: "Ммм да, мама была права, нужно было идти в универ,\n"
               "щас бы работал в офисе... бумажки разгребал",
            2: "Лааадно, Том, соберись, люди нуждаются в тебе,\n"
               "кто если не ты будет копаться в телах людей.\n"
               "Господь, я и правду занимаюсь чем-то не тем.",
            3: "Хотя уже не важно, я слишком долго искал эту работу,\n"
               "она мне и правда нужна.",
            4: "Только таак хочется спать...",
            5: "Почему вообще первый рабочий день и сразу ночная смена??"
        }
        self.photo2_texts = [
            "М-м-м, как миленько здесь..",
            "Мне обещали, что скоро придёт помощник.",
            "Думаю с ним будет не так мрачно находится тут.",
            "Хотя мне всегда было лучше одному.",
            "Хах стационарный, серьезно??"
        ]
        self.phone_call_texts = [
            "Ало? Кто это?",
            "Здравствуй, Том, это Билл, твой начальник. Звоню, чтобы проинформировать о первом рабочем дне",
            "Рядом с тобой (компьютер), там в папках всё, что тебе нужно: инфа про пациентов, препараты, документация, "
            "отчеты, что тебу будет писать после каждой смены.",
            "В папку (пароли) тебе лезть нечего..",
            "Твой кабинет слева от тебя за белой дверью. С прошлой смены осталось одно не законченное тело, начни с него.",
            "Нужно провести общий осмотр, да и в целом ты сам разберешься.",
            "А-а, ладно, понял.",
            "А что на счет помощника? Он опаздывает?",
            "Что какой еще помощник? На эту смену (ты один).",
            "Э-э ладно, мне пора.",
            "Давай, работай."
        ]
        self.examination_texts = [
            "Так ладно начнем...",
            "Черт по привычке пульс мерею.",
            "Чувствуя эту усталось, я бы не увидился такому",
            "Ну вроде всё. Нужно записать это в отчет.",
            "Чем раньше начну, тем раньше свалю уже отсюда."
        ]
        self.report_texts = [
            "поздние трупные пятна в районе плеч.",
            "Наблюдается общее вздутие.",
            "Общих патологий не выявлено",
            "Общий осмотр проведён."
        ]
        self.rules_text = (
            "Хз допишу потом )) "

        )
        self.after_call_text = "Ну просто сказка.."


class PhotoGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Клик для смены фото")
        # Инициализация менеджеров
        self.photo_manager = PhotoManager()
        self.click_areas = ClickAreas()
        self.texts = GameTexts()

        # Инициализация UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Инициализация состояния игры
        self.show_text = False
        self.current_text_index = 0
        self.text_finished = False
        self.show_rules = False

        # Флаги для текстов на photo2
        self.show_photo2_text = False
        self.photo2_text_index = 0
        self.photo2_texts_finished = False
        self.photo2_texts_shown = False

        # Флаги для цели и телефонного звонка
        self.show_goal = False
        self.goal_text = ""
        self.phone_call_available = False
        self.show_phone_call = False
        self.phone_call_index = 0

        # Флаг для текста после звонка
        self.show_after_call_text = False

        self.show_examination = False
        self.examination_index = 0
        self.examination_finished = False
        self.examination_available = False

        self.report_available = False
        self.report_finished = False
        self.current_report_texts = []

        self.current_photo = self.photo_manager.photos["photo5"]
        self.current_state = "start_screen"

        self.setup_ui()

    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        # кнопка "Начать"
        start_button = MyFlatButton(
            text="Начать",
            width=200,
            height=40
        )

        # кнопка "Правила"
        rules_button = RulesButton(
            text="Правила",
            width=200,
            height=40
        )

        anchor_layout = arcade.gui.UIAnchorLayout()
        # Добавляем кнопку "Начать" правее центра
        anchor_layout.add(
            child=start_button,
            anchor_x="center_x",
            anchor_y="center_y",
            align_x=170,
            align_y=20
        )
        # Добавляем кнопку "Правила" ПОД кнопкой "Начать"
        anchor_layout.add(
            child=rules_button,
            anchor_x="center_x",
            anchor_y="center_y",
            align_x=170,
            align_y=-30
        )

        self.manager.add(anchor_layout)

    def on_draw(self) -> None:
        self.clear()
        if self.show_rules:
            self.draw_rules_screen()
        elif self.show_text and not self.text_finished and self.current_text_index > 0:
            self.draw_main_text()
        elif self.show_phone_call and self.phone_call_index < len(self.texts.phone_call_texts):
            self.draw_phone_call()
        elif self.show_after_call_text:
            self.draw_after_call()
        elif self.show_examination and self.examination_index < len(self.texts.examination_texts):
            self.draw_examination()
        elif self.current_state == "report" or self.current_state == "photo6":
            self.draw_report()
        elif (self.current_state == "photo2" and
              not self.photo2_texts_shown and
              self.show_photo2_text and
              not self.photo2_texts_finished and
              self.photo2_text_index < len(self.texts.photo2_texts)):
            self.draw_photo2_texts()
        else:
            self.draw_current_photo()
            if self.current_state == "start_screen":
                self.manager.draw()
        # Рисуем цель
        self.draw_goal()

    def draw_rules_screen(self):
        """Отрисовка экрана с правилами"""
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text(
            self.texts.rules_text,
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            arcade.color.WHITE,
            18,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=SCREEN_WIDTH - 50,
            multiline=True
        )
        arcade.draw_text(
            "Нажмите для возврата...",
            SCREEN_WIDTH // 2,
            50,
            arcade.color.LIGHT_GRAY,
            14,
            anchor_x="center"
        )

    def draw_main_text(self):
        """Отрисовка основного текста"""
        text = self.texts.texts.get(self.current_text_index, "")
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

    def draw_phone_call(self):
        """Отрисовка телефонного звонка"""
        arcade.draw_texture_rect(
            self.current_photo,
            arcade.XYWH(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT
            )
        )
        call_text = self.texts.phone_call_texts[self.phone_call_index]
        arcade.draw_text(
            call_text,
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            arcade.color.WHITE,
            20,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=SCREEN_WIDTH - 150,
            multiline=True
        )

    def draw_after_call(self):
        """Отрисовка текста после звонка"""
        arcade.draw_texture_rect(
            self.current_photo,
            arcade.XYWH(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT
            )
        )
        arcade.draw_text(
            self.texts.after_call_text,
            SCREEN_WIDTH // 2,
            100,
            arcade.color.WHITE,
            20,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=SCREEN_WIDTH - 100,
            multiline=True
        )

    def draw_examination(self):
        """Отрисовка осмотра"""
        arcade.draw_texture_rect(
            self.current_photo,
            arcade.XYWH(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT
            )
        )
        exam_text = self.texts.examination_texts[self.examination_index]
        arcade.draw_text(
            exam_text,
            SCREEN_WIDTH // 2,
            100,
            arcade.color.WHITE,
            20,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=SCREEN_WIDTH - 100,
            multiline=True
        )

    def draw_report(self):
        """Отрисовка отчета"""
        arcade.draw_texture_rect(
            self.photo_manager.photos["photo6"],
            arcade.XYWH(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT
            )
        )
        if self.current_report_texts:
            start_y = SCREEN_HEIGHT - 150
            for i, text in enumerate(self.current_report_texts):
                arcade.draw_text(
                    text,
                    100,
                    start_y - (i * 30),
                    arcade.color.BLACK,
                    14,
                    width=SCREEN_WIDTH - 200,
                    multiline=True
                )

    def draw_photo2_texts(self):
        """Отрисовка текстов на photo2"""
        arcade.draw_texture_rect(
            self.current_photo,
            arcade.XYWH(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT
            )
        )
        current_text = self.texts.photo2_texts[self.photo2_text_index]
        arcade.draw_text(
            current_text,
            SCREEN_WIDTH // 2,
            100,
            arcade.color.WHITE,
            20,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=SCREEN_WIDTH - 100,
            multiline=True
        )

    def draw_current_photo(self):
        """Отрисовка текущей фотографии"""
        arcade.draw_texture_rect(
            self.current_photo,
            arcade.XYWH(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT
            )
        )

    def draw_goal(self):
        """Отрисовка цели"""
        if self.show_goal and self.current_state not in ["photo3", "report", "photo6"]:
            arcade.draw_text(
                "Цель:",
                30,
                SCREEN_HEIGHT - 50,
                arcade.color.WHITE,
                21,
                bold=True
            )
            arcade.draw_text(
                self.goal_text,
                110,
                SCREEN_HEIGHT - 50,
                arcade.color.WHITE,
                18
            )

    def on_mouse_press(self, x, y, button, modifiers):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        # Обработка кликов по экранам
        if self.show_rules:
            self.handle_rules_click()
        elif self.show_text and not self.text_finished and self.current_text_index > 0:
            self.handle_main_text_click()
        elif self.show_phone_call:
            self.handle_phone_call_click()
        elif self.show_after_call_text:
            self.handle_after_call_click()
        elif self.show_examination:
            self.handle_examination_click()
        elif self.current_state in ["report", "photo6"]:
            self.handle_report_click()
        elif (self.current_state == "photo2" and
              not self.photo2_texts_shown and
              self.show_photo2_text and
              not self.photo2_texts_finished):
            self.handle_photo2_text_click()
        else:
            self.handle_game_click(x, y)

    def handle_rules_click(self):
        """Обработка клика на правилах"""
        self.show_rules = False
        arcade.set_background_color(arcade.color.DEFAULT)

    def handle_main_text_click(self):
        """Обработка клика на основном тексте"""
        if self.current_text_index < 5:
            self.current_text_index += 1
        else:
            self.show_text = False
            self.text_finished = True
            self.current_text_index = 0
            self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"

            if not self.photo2_texts_shown:
                self.show_photo2_text = True
                self.photo2_text_index = 0
                self.photo2_texts_finished = False

            self.show_goal = True
            self.goal_text = ""
            arcade.set_background_color(arcade.color.DEFAULT)

    def handle_phone_call_click(self):
        """Обработка клика во время звонка"""
        if self.phone_call_index < len(self.texts.phone_call_texts) - 1:
            self.phone_call_index += 1
        else:
            self.show_phone_call = False
            self.show_after_call_text = True
            self.goal_text = "провести осмотр"

    def handle_after_call_click(self):
        """Обработка клика после звонка"""
        self.show_after_call_text = False

    def handle_examination_click(self):
        """Обработка клика во время осмотра"""
        if self.examination_index < len(self.texts.examination_texts) - 1:
            self.examination_index += 1
            print(f"Перешли к тексту осмотра: {self.examination_index + 1}")
            if self.examination_index == 2:
                self.show_goal = False
                self.goal_text = ""
            if self.examination_index == len(self.texts.examination_texts) - 1:
                self.goal_text = "написать отчет об состоянии"
                self.show_goal = True
                self.report_available = True

        else:
            self.show_examination = False
            self.examination_finished = True

    def handle_report_click(self):
        """Обработка клика на отчете"""
        if len(self.current_report_texts) < len(self.texts.report_texts):
            next_text = self.texts.report_texts[len(self.current_report_texts)]
            self.current_report_texts.append(next_text)
            if len(self.current_report_texts) == len(self.texts.report_texts):
                self.report_finished = True

    def handle_photo2_text_click(self):
        """Обработка клика на текстах photo2"""
        if self.photo2_text_index < len(self.texts.photo2_texts) - 1:
            self.photo2_text_index += 1
        else:
            self.show_photo2_text = False
            self.photo2_texts_finished = True
            self.photo2_texts_shown = True
            self.goal_text = "ответить на звонок"
            self.phone_call_available = True

    def handle_game_click(self, x, y):
        """Обработка кликов по игровым областям"""
        if self.current_state == "start_screen":
            pass
        elif self.current_state == "photo1":
            self.handle_photo1_click(x, y)
        elif self.current_state == "photo2":
            self.handle_photo2_click(x, y)
        elif self.current_state == "photo3":
            self.handle_photo3_click(x, y)
        elif self.current_state == "photo4":
            self.handle_photo4_click(x, y)

    def handle_photo1_click(self, x, y):
        """Обработка кликов на photo1"""
        if (self.examination_available and
                self.click_areas.is_in_area(x, y, "examination_area")):
            self.show_examination = True
            self.examination_index = 0
            self.examination_available = False
        elif self.click_areas.is_in_area(x, y, "door_photo1"):
            self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"

            if not self.photo2_texts_shown:
                self.show_photo2_text = True
                self.photo2_text_index = 0
                self.photo2_texts_finished = False

            self.show_goal = True
        elif self.click_areas.is_in_area(x, y, "cabinet_photo1"):
            self.current_photo = self.photo_manager.photos["photo4"]
            self.current_state = "photo4"

    def handle_photo2_click(self, x, y):
        """Обработка кликов на photo2"""
        if self.click_areas.is_in_area(x, y, "back_to_photo1"):
            if self.show_photo2_text and not self.photo2_texts_shown:
                self.show_photo2_text = False
                self.photo2_texts_finished = True
            else:
                self.current_photo = self.photo_manager.photos["photo1"]
                self.current_state = "photo1"

                if self.goal_text == "провести осмотр":
                    self.examination_available = True
        elif self.click_areas.is_in_area(x, y, "to_computer"):
            if self.show_photo2_text and not self.photo2_texts_shown:
                self.show_photo2_text = False
                self.photo2_texts_finished = True
            else:
                self.current_photo = self.photo_manager.photos["photo3"]
                self.current_state = "photo3"
                self.show_goal = False
        elif self.phone_call_available:
            self.show_phone_call = True
            self.phone_call_index = 0
            self.phone_call_available = False

    def handle_photo3_click(self, x, y):
        """Обработка кликов на photo3"""
        if (self.report_available and
                self.click_areas.is_in_area(x, y, "report_area")):
            self.current_photo = self.photo_manager.photos["photo6"]
            self.current_state = "report"
            self.show_goal = False
            self.current_report_texts = []
        elif self.click_areas.is_in_area(x, y, "back_from_computer"):
            self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"
            if self.goal_text:
                self.show_goal = True

    def handle_photo4_click(self, x, y):
        """Обработка кликов на photo4"""
        if self.click_areas.is_in_area(x, y, "back_from_cabinet"):
            self.current_photo = self.photo_manager.photos["photo1"]
            self.current_state = "photo1"


if __name__ == "__main__":
    game = PhotoGame()
    arcade.run()