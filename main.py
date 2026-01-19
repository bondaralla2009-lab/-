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


class RulesButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Правила' была нажата!")
        window = arcade.get_window()
        # Устанавливаем флаг для показа правил ТОЛЬКО если мы на стартовом экране
        if window.current_state == "start_screen":
            window.show_rules = True  # Показываем правила
            arcade.set_background_color(arcade.color.BLACK)
        else:
            print("Кнопка 'Правила' неактивна на этом экране")


class PhotoGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Клик для смены фото")

        # Создаем UI менеджер
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Флаги для отображения текста
        self.show_text = False
        self.current_text_index = 0  # 0 - нет текста, 1-5 - тексты
        self.text_finished = False  # Новый флаг - тексты завершены
        self.show_rules = False  # Флаг для отображения правил

        # Новые флаги для текстов на photo2
        self.show_photo2_text = False  # Показывать ли текст на photo2
        self.photo2_text_index = 0  # Текущий индекс текста на photo2
        self.photo2_texts_finished = False  # Закончились ли тексты на photo2
        self.photo2_texts_shown = False  # Были ли уже показаны тексты на photo2

        # Флаги для цели и телефонного звонка
        self.show_goal = False  # Показывать ли цель
        self.goal_text = ""  # Текст цели
        self.phone_call_available = False  # Доступен ли телефонный звонок
        self.show_phone_call = False  # Показывать ли диалог телефонного звонка
        self.phone_call_index = 0  # Текущий индекс диалога звонка

        # Новый флаг для текста после звонка
        self.show_after_call_text = False  # Показывать текст после звонка
        self.after_call_text = "Ну просто сказка.."  # Текст после звонка

        # Флаги для осмотра тела на photo1
        self.show_examination = False  # Показывать ли осмотр
        self.examination_index = 0  # Текущий индекс текста осмотра
        self.examination_texts = [
            "Так ладно начнем...",
            "Черт по привычке пульс мерею.",
            "Чувствуя эту усталось, я бы не увидился такому",
            "Ну вроде всё. Нужно записать это в отчет.",
            "Чем раньше начну, тем раньше свалю уже отсюда."
        ]
        self.examination_finished = False  # Осмотр завершен
        self.examination_available = False  # Осмотр доступен

        # Флаги для отчета на photo3
        self.report_available = False  # Доступно ли написание отчета
        self.show_report_text = False  # Показывать ли текст отчета
        self.report_texts = [  # Тексты которые появляются постепенно
            "поздние трупные пятна в районе плеч.",
            "Наблюдается общее вздутие.",
            "Общих патологий не выявлено",
            "Общий осмотр проведён."
        ]
        self.current_report_texts = []  # Текущие показанные тексты отчета
        self.report_finished = False  # Отчет завершен

        try:
            # Загружаем все фото
            self.photo1 = arcade.load_texture("data/кабинет с телом1.jpg")
            self.photo2 = arcade.load_texture("data/Комната с ноутом2.png")
            self.photo3 = arcade.load_texture("data/рабочий стол_arcade3.jpg")
            self.photo4 = arcade.load_texture("data/+Белый+шка_измен4.jpeg")
            self.photo5 = arcade.load_texture("data/Group 1 (1)5.png")
            self.photo6 = arcade.load_texture("data/Отчет6.png")  # Фото отчета

        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            arcade.exit()

        # Начинаем с пятого фото (стартового экрана)
        self.current_photo = self.photo5
        self.current_state = "start_screen"

        # Создаем кнопку "Начать"
        start_button = MyFlatButton(
            text="Начать",
            width=200,
            height=40
        )

        # Создаем кнопку "Правила"
        rules_button = RulesButton(
            text="Правила",
            width=200,
            height=40
        )

        # Создаем anchor layout
        anchor_layout = arcade.gui.UIAnchorLayout()

        # Добавляем кнопку "Начать" правее центра
        anchor_layout.add(
            child=start_button,
            anchor_x="center_x",
            anchor_y="center_y",
            align_x=170,  # Сдвигаем на 170 пикселей вправо от центра
            align_y=20
        )

        # Добавляем кнопку "Правила" ПОД кнопкой "Начать"
        anchor_layout.add(
            child=rules_button,
            anchor_x="center_x",
            anchor_y="center_y",
            align_x=170,  # Такое же смещение по X
            align_y=-30  # Отрицательное значение - ниже (под) кнопкой "Начать"
        )

        self.manager.add(anchor_layout)

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

        # координаты для осмотра тела на photo1 (центр фото)
        self.click_examination_x_min = 300
        self.click_examination_x_max = 500
        self.click_examination_y_min = 200
        self.click_examination_y_max = 400

        # КООРДИНАТЫ ДЛЯ ОБЛАСТИ ОТЧЕТА НА PHOTO3 (УКАЖИТЕ САМИ ЗДЕСЬ)
        self.click_report_x_min = 160 # МИНИМАЛЬНЫЙ X - ВСТАВЬТЕ СВОЕ ЗНАЧЕНИЕ
        self.click_report_x_max = 200  # МАКСИМАЛЬНЫЙ X - ВСТАВЬТЕ СВОЕ ЗНАЧЕНИЕ
        self.click_report_y_min = 50  # МИНИМАЛЬНЫЙ Y - ВСТАВЬТЕ СВОЕ ЗНАЧЕНИЕ
        self.click_report_y_max = 100  # МАКСИМАЛЬНЫЙ Y - ВСТАВЬТЕ СВОЕ ЗНАЧЕНИЕ

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
            5: "Почему вообще первый рабочий день и сразу ночная смена??"
        }

        # Тексты для photo2 (снизу по центру)
        self.photo2_texts = [
            "М-м-м, как миленько здесь..",
            "Мне обещали, что скоро придёт помощник.",
            "Думаю с ним будет не так мрачно находится тут.",
            "Хотя мне всегда было лучше одному.",
            "Хах стационарный, серьезно??"
        ]

        # Диалог телефонного звонка
        self.phone_call_texts = [
            "Ало? Кто это?",
            "Здравствуй, Том, это Билл, твой начальник. Звоню, чтобы проинформировать о первом рабочем дне",
            "Рядом с тобой (компьютер), там в папках всё, что тебе нужно: инфа про пациентов, препараты, документация, "
            "отчеты, что тебе нужно будет писать после каждой смены.",
            "В папку (пароли) тебе лезть нечего..",
            "Твой кабинет слева от тебя за белой дверью. С прошлой смены осталось одно не законченное тело, начни с него.",
            "Нужно провести общий осмотр, да и в целом ты сам разберешься.",
            "А-а, ладно, понял.",
            "А что на счет помощника? Он опаздывает?",
            "Что какой еще помощник? На эту смену (ты один).",
            "Э-э ладно, мне пора.",
            "Давай, работай."
        ]

        # Текст правил
        self.rules_text = (
            "Тебе реально интересно? Ну тогда слушай, правил нет. "
            "Любые рамки и запреты лишь в твоей голове. И ты своими "
            "руками себя в них загнал.. Молодец, отличная работа, "
            "хоть что-то ты сделал до конца. А ведь всё могло "
            "закончится по другому. Разве не так?))"
        )

    def on_draw(self) -> None:
        self.clear()

        # если показываем правила
        if self.show_rules:
            # Черный фон
            arcade.set_background_color(arcade.color.BLACK)

            # Рисуем текст правил
            arcade.draw_text(
                self.rules_text,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                arcade.color.WHITE,
                18,  # Размер шрифта немного меньше
                anchor_x="center",
                anchor_y="center",
                align="center",
                width=SCREEN_WIDTH - 50,  # Уже, чтобы текст не растягивался
                multiline=True
            )

            # Инструкция для возврата
            arcade.draw_text(
                "Нажмите для возврата...",
                SCREEN_WIDTH // 2,
                50,
                arcade.color.LIGHT_GRAY,
                14,
                anchor_x="center"
            )

        # если показываем текстовые экраны и тексты еще не завершены
        elif self.show_text and not self.text_finished and self.current_text_index > 0:
            text = self.texts.get(self.current_text_index, "")

            # текущий текст
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

        # если показываем диалог телефонного звонка
        elif self.show_phone_call and self.phone_call_index < len(self.phone_call_texts):
            # Рисуем текущую фотографию (photo2)
            arcade.draw_texture_rect(
                self.current_photo,
                arcade.XYWH(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )

            # Рисуем текст диалога
            call_text = self.phone_call_texts[self.phone_call_index]

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

        # если показываем текст после звонка
        elif self.show_after_call_text:
            # Рисуем текущую фотографию (photo2)
            arcade.draw_texture_rect(
                self.current_photo,
                arcade.XYWH(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )

            # Рисуем текст "Ну просто сказка.." снизу по центру
            arcade.draw_text(
                self.after_call_text,
                SCREEN_WIDTH // 2,
                100,  # Позиция снизу экрана
                arcade.color.WHITE,
                20,
                anchor_x="center",
                anchor_y="center",
                align="center",
                width=SCREEN_WIDTH - 100,
                multiline=True
            )

        # если показываем осмотр тела на photo1
        elif self.show_examination and self.examination_index < len(self.examination_texts):
            # Рисуем текущую фотографию (photo1)
            arcade.draw_texture_rect(
                self.current_photo,
                arcade.XYWH(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )

            # Рисуем текст осмотра снизу по центру
            exam_text = self.examination_texts[self.examination_index]

            arcade.draw_text(
                exam_text,
                SCREEN_WIDTH // 2,
                100,  # Позиция снизу экрана
                arcade.color.WHITE,
                20,
                anchor_x="center",
                anchor_y="center",
                align="center",
                width=SCREEN_WIDTH - 100,
                multiline=True
            )

        # если показываем отчет (photo6) с постепенным текстом
        elif self.current_state == "report" or self.current_state == "photo6":
            # Рисуем фото6 (отчет)
            arcade.draw_texture_rect(
                self.photo6,
                arcade.XYWH(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )

            # Рисуем накопленные тексты отчета (каждый под предыдущим)
            if self.current_report_texts:
                start_y = SCREEN_HEIGHT - 150  # Начинаем сверху
                for i, text in enumerate(self.current_report_texts):
                    arcade.draw_text(
                        text,
                        100,  # Левая позиция
                        start_y - (i * 30),  # Каждый следующий текст на 30 пикселей ниже
                        arcade.color.BLACK,  # Черный текст для читаемости на белом фоне
                        14,  # Мелкий шрифт
                        width=SCREEN_WIDTH - 200,
                        multiline=True
                    )

        # если показываем тексты на photo2 (только при первом посещении)
        elif (self.current_state == "photo2" and
              not self.photo2_texts_shown and
              self.show_photo2_text and
              not self.photo2_texts_finished and
              self.photo2_text_index < len(self.photo2_texts)):

            # Рисуем фото2
            arcade.draw_texture_rect(
                self.current_photo,
                arcade.XYWH(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )

            # Рисуем текущий текст снизу по центру (без фона)
            current_text = self.photo2_texts[self.photo2_text_index]

            # Сам текст белым цветом снизу по центру
            arcade.draw_text(
                current_text,
                SCREEN_WIDTH // 2,
                100,  # Позиция снизу экрана
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

            # Рисуем UI элементы (кнопку) только на стартовом экране
            if self.current_state == "start_screen":
                self.manager.draw()

        # Рисуем цель в левом верхнем углу (без фона) - НЕ показываем на photo3 и photo6
        if self.show_goal and self.current_state not in ["photo3", "report", "photo6"]:
            # Текст "Цель:"
            arcade.draw_text(
                "Цель:",
                30,
                SCREEN_HEIGHT - 50,
                arcade.color.WHITE,
                21,
                bold=True
            )

            # Текст цели
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

        # обработка кликов на экране правил
        if self.show_rules:
            # Возвращаемся к стартовому экрану
            self.show_rules = False
            arcade.set_background_color(arcade.color.DEFAULT)  # Возвращаем стандартный фон
            return

        # обработка кликов на текстовых экранах (только если тексты еще не завершены)
        if self.show_text and not self.text_finished and self.current_text_index > 0:
            if self.current_text_index < 5:
                # Переходим к следующему текста
                self.current_text_index += 1
            else:
                # После последнего текста переходим на photo2 и отмечаем, что тексты завершены
                self.show_text = False
                self.text_finished = True
                self.current_text_index = 0
                self.current_photo = self.photo2
                self.current_state = "photo2"
                # Автоматически показываем первый текст на photo2 (только при первом посещении)
                if not self.photo2_texts_shown:
                    self.show_photo2_text = True
                    self.photo2_text_index = 0
                    self.photo2_texts_finished = False
                # Включаем отображение цели
                self.show_goal = True
                self.goal_text = ""  # Пока цель пустая
                arcade.set_background_color(arcade.color.DEFAULT)  # Возвращаем фон по умолчанию
                print("Тексты завершены, переходим на photo2 и показываем первый текст")
            return  # Выходим, так как обработали клик на текстовом экране

        # обработка кликов на диалоге телефонного звонка
        if self.show_phone_call:
            if self.phone_call_index < len(self.phone_call_texts) - 1:
                # Переходим к следующему диалогу
                self.phone_call_index += 1
                print(f"Перешли к диалогу: {self.phone_call_index + 1}")
            else:
                # Завершаем диалог
                self.show_phone_call = False
                # Показываем текст "Ну просто сказка.."
                self.show_after_call_text = True
                # Обновляем цель на "провести осмотр"
                self.goal_text = "провести осмотр"
                print("Диалог телефонного звонка завершен, новая цель: провести осмотр")
            return

        # обработка кликов на тексте после звонка
        if self.show_after_call_text:
            # Скрываем текст "Ну просто сказка.."
            self.show_after_call_text = False
            # Цель "провести осмотр" остается видимой
            print("Текст после звонка скрыт, цель остается: провести осмотр")
            return

        # обработка кликов на осмотре тела
        if self.show_examination:
            if self.examination_index < len(self.examination_texts) - 1:
                # Переходим к следующему тексту осмотра
                self.examination_index += 1
                print(f"Перешли к тексту осмотра: {self.examination_index + 1}")

                # После третьей фразы убираем цель
                if self.examination_index == 2:  # "Чувствуя эту усталось, я бы не увидился такому"
                    self.show_goal = False
                    self.goal_text = ""
                    print("Цель убрана после осмотра")

                # После последней фразы появляется новая цель
                if self.examination_index == len(self.examination_texts) - 1:
                    self.goal_text = "написать отчет об состоянии"
                    self.show_goal = True
                    self.report_available = True  # Делаем отчет доступным
                    print("Появилась новая цель: написать отчет об состоянии, отчет доступен на photo3")

            else:
                # Завершаем осмотр
                self.show_examination = False
                self.examination_finished = True
                print("Осмотр завершен, цель: написать отчет об состоянии")
            return

        # обработка кликов на отчете (photo6) - добавляем следующий текст
        if self.current_state == "report" or self.current_state == "photo6":
            if len(self.current_report_texts) < len(self.report_texts):
                # Добавляем следующий текст в список показанных
                next_text = self.report_texts[len(self.current_report_texts)]
                self.current_report_texts.append(next_text)
                print(f"Добавлен текст отчета: {next_text}")

                # Если добавили последний текст, завершаем
                if len(self.current_report_texts) == len(self.report_texts):
                    self.report_finished = True
                    print("Отчет полностью завершен")
            return

        # обработка кликов на текстах photo2 (только при первом показе)
        if (self.current_state == "photo2" and
                not self.photo2_texts_shown and
                self.show_photo2_text and
                not self.photo2_texts_finished):

            if self.photo2_text_index < len(self.photo2_texts) - 1:
                # Переходим к следующему тексту
                self.photo2_text_index += 1
                print(f"Перешли к тексту photo2: {self.photo2_text_index + 1}")
            else:
                # После последнего текста скрываем тексты
                self.show_photo2_text = False
                self.photo2_texts_finished = True
                self.photo2_texts_shown = True  # Помечаем, что тексты уже были показаны
                # После завершения монолога появляется цель "ответить на звонок"
                self.goal_text = "ответить на звонок"
                # Делаем телефонный звонок доступным
                self.phone_call_available = True
                print("Тексты на photo2 завершены, цель: ответить на звонок")
            return  # Выходим, так как обработали клик на текстовом экране photo2

        # Обработка кликов по фотографиям (только если не показываем текст)
        if self.current_state == "start_screen":
            # UI менеджер сам обработает клик по кнопке
            # Кнопка "Правила" теперь проверяет current_state в своем on_click
            pass
        elif self.current_state == "photo1":
            # Если осмотр доступен и клик в области тела
            if (self.examination_available and
                    self.click_examination_x_min <= x <= self.click_examination_x_max and
                    self.click_examination_y_min <= y <= self.click_examination_y_max):
                # Начинаем осмотр
                self.show_examination = True
                self.examination_index = 0
                self.examination_available = False
                print("Начался осмотр тела")

            # Если клик в области для возврата на photo2
            elif (self.click_x_min1 <= x <= self.click_x_max1 and
                  self.click_y_min1 <= y <= self.click_y_max1):
                self.current_photo = self.photo2
                self.current_state = "photo2"
                # При переходе на photo2 показываем тексты (только при первом посещении)
                if not self.photo2_texts_shown:
                    self.show_photo2_text = True
                    self.photo2_text_index = 0
                    self.photo2_texts_finished = False
                # Включаем отображение цели
                self.show_goal = True
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
                # Если показываются тексты (при первом посещении), сначала скрываем их
                if self.show_photo2_text and not self.photo2_texts_shown:
                    self.show_photo2_text = False
                    self.photo2_texts_finished = True
                else:
                    # Иначе переходим на photo1
                    self.current_photo = self.photo1
                    self.current_state = "photo1"
                    # При переходе на photo1 после появления цели "провести осмотр"
                    # делаем осмотр доступным
                    if self.goal_text == "провести осмотр":
                        self.examination_available = True
                        print("Осмотр теперь доступен на photo1")
                    print("Вернулись на фото 1")

            # Если клик в области для перехода к компьютеру (photo3)
            elif (self.click_x_min2_comp <= x <= self.click_x_max2_comp and
                  self.click_y_min2_comp <= y <= self.click_y_max2_comp):
                # Если показываются тексты (при первом посещении), сначала скрываем их
                if self.show_photo2_text and not self.photo2_texts_shown:
                    self.show_photo2_text = False
                    self.photo2_texts_finished = True
                else:
                    # Иначе переходим на photo3
                    self.current_photo = self.photo3
                    self.current_state = "photo3"
                    # На photo3 скрываем цель
                    self.show_goal = False
                    print("Перешли на фото 3 (рабочий стол), цель скрыта")

            # Если телефонный звонок доступен и мы на photo2 - ЛЮБОЙ клик начинает диалог
            elif self.phone_call_available:
                # Запускаем диалог телефонного звонка
                self.show_phone_call = True
                self.phone_call_index = 0
                # Отключаем возможность повторного ответа на звонок
                self.phone_call_available = False
                print("Начался телефонный звонок (клик в любом месте на photo2)")

        elif self.current_state == "photo3":
            # Если отчет доступен и клик в области отчета
            if (self.report_available and
                    self.click_report_x_min <= x <= self.click_report_x_max and
                    self.click_report_y_min <= y <= self.click_report_y_max):
                # Переходим на фото отчета (photo6)
                self.current_photo = self.photo6
                self.current_state = "report"
                # Скрываем цель
                self.show_goal = False
                # Начинаем отчет с пустого списка текстов
                self.current_report_texts = []
                print("Начали отчет, перешли на photo6")

            # Если клик в области для возврата на photo2
            elif (self.click_x_min3_back <= x <= self.click_x_max3_back and
                  self.click_y_min3_back <= y <= self.click_y_max3_back):
                self.current_photo = self.photo2
                self.current_state = "photo2"
                # При возврате на photo2 НЕ показываем тексты снова
                # Восстанавливаем цель, если она была
                if self.goal_text:
                    self.show_goal = True
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