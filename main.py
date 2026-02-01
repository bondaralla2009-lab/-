import arcade
import arcade.gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Начать' была нажата!")
        window = arcade.get_window()
        window.show_text = True
        window.current_text_index = 1
        arcade.set_background_color(arcade.color.BLACK)
        window.start_music()
        window.manager.disable()
        window.manager.clear()


class RulesButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Правила' была нажата!")
        window = arcade.get_window()
        window.show_rules = True
        arcade.set_background_color(arcade.color.BLACK)


class ClickAreas:
    def __init__(self):
        self.areas = {
            "door_photo1": {"x_min": 150, "x_max": 300, "y_min": 200, "y_max": 400},
            "back_to_photo1": {"x_min": 10, "x_max": 50, "y_min": 0, "y_max": 1000},
            "to_computer": {"x_min": 80, "x_max": 290, "y_min": 210, "y_max": 380},
            "back_from_computer": {"x_min": 700, "x_max": 800, "y_min": 0, "y_max": 100},
            "cabinet_photo1": {"x_min": 10, "x_max": 70, "y_min": 270, "y_max": 430},
            "back_from_cabinet": {"x_min": 700, "x_max": 800, "y_min": 0, "y_max": 600},
            "examination_area": {"x_min": 300, "x_max": 500, "y_min": 200, "y_max": 400},
            "report_area": {"x_min": 150, "x_max": 220, "y_min": 45, "y_max": 100},
            "back_from_photo6": {"x_min": 700, "x_max": 800, "y_min": 0, "y_max": 100},
            "door_photo2": {"x_min": 450, "x_max": 1000, "y_min": 0, "y_max": 700},
            "door_info_folder": {"x_min": 20, "x_max": 80, "y_min": 50, "y_max": 100},
            "photo9_to_photo7": {"x_min": 250, "x_max": 295, "y_min": 450, "y_max": 550},
            "photo9_to_photo8": {"x_min": 300, "x_max": 350, "y_min": 450, "y_max": 550},
            "photo8_to_photo1": {"x_min": 400, "x_max": 600, "y_min": 200, "y_max": 400},
            "back_from_photo7": {"x_min": 700, "x_max": 800, "y_min": 0, "y_max": 100},
            "back_from_photo8": {"x_min": 700, "x_max": 800, "y_min": 0, "y_max": 100},
            "back_from_photo9": {"x_min": 700, "x_max": 800, "y_min": 0, "y_max": 100},
            "phone_call_button": {"x_min": 400, "x_max": 600, "y_min": 300, "y_max": 375},
            "safe_area_photo4": {"x_min": 300, "x_max": 500, "y_min": 200, "y_max": 400},
            "center_photo3": {"x_min": 350, "x_max": 450, "y_min": 250, "y_max": 350},
            "center_photo10": {"x_min": 350, "x_max": 450, "y_min": 250, "y_max": 350}
        }

    def is_in_area(self, x, y, area_name):
        a = self.areas.get(area_name)
        return a and a["x_min"] <= x <= a["x_max"] and a["y_min"] <= y <= a["y_max"]


class PhotoManager:
    def __init__(self):
        self.photos = {}
        self.photos_replaced = False
        self.load_photos()

    def load_photos(self):
        photo_files = {
            "photo1": "data/кабинет с телом1.jpg", "photo2": "data/Комната с компом2.png",
            "photo3": "data/рабочий стол_arcade3.jpg", "photo4": "data/+Белый+шка_измен4.jpeg",
            "photo5": "data/Group 1 (1)5.png", "photo6": "data/Отчет6.png", "photo7": "data/Правила7.png",
            "photo8": "data/Препараты8.png", "photo9": "data/Важное9.png", "photo10": "data/пароль10.jpg",
            "photo11": "data/первая комната БЕЗ ТЕЛА11.png", "photo12_1": "data/Галлюн1.png",
            "photo12_2": "data/Галлюн12-2.png", "photo13_1": "data/псих13-1.png", "photo13_2": "data/псих13-2.png",
            "photo14": "data/лес14.png", "photo2_1": "data/комп красный2_1.png"
        }
        for key, filepath in photo_files.items():
            try:
                self.photos[key] = arcade.load_texture(filepath)
            except Exception as e:
                print(f"Ошибка загрузки {filepath}: {e}")
                self.photos[key] = arcade.Texture.create_empty(key, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def replace_photos_after_black_screen(self):
        if not self.photos_replaced:
            self.original_photo1 = self.photos["photo1"]
            self.original_photo2 = self.photos["photo2"]
            self.photos["photo1"] = self.photos["photo12_1"]
            self.photos_replaced = True

    def show_photo2_1(self):
        if "photo2_1" in self.photos:
            self.photos["photo2"] = self.photos["photo2_1"]


class GameTexts:
    def __init__(self):
        self.texts = {
            1: "Ммм, да, мама была права, нужно было идти в универ,\nсейчас бы работал в офисе... бумажки разгребал.",
            2: "Лааадно, Том, соберись, люди нуждаются в тебе,\nкто, если не ты, будет копаться в телах людей.\nГосподь, я и правда занимаюсь чем-то не тем.",
            3: "Хотя уже не важно, я слишком долго искал эту работу,\nона мне и правда нужна.",
            4: "Только таак хочется спать...",
            5: "Почему вообще первый рабочий день и сразу ночная смена??"
        }
        self.photo2_texts = ["М-м-м, как миленько здесь...", "Мне обещали, что скоро придёт помощник.",
                             "Думаю, с ним будет не так мрачно находиться тут.", "Хотя мне всегда было лучше одному.",
                             "...", "Хах, стационарный, серьёзно??"]
        self.phone_call_texts = ["- Алло? Кто это?",
                                 "- Здравствуй, Том, это Билл, твой начальник. Звоню, чтобы проинформировать о первом рабочем дне.",
                                 "Рядом с тобой компьютер, там в папках всё, что тебе нужно: инфа про пациентов, препараты, документация, отчёты, что тебе будет писать после каждой смены.",
                                 "В папку 'пароли' тебе лезть нечего...",
                                 "Твой кабинет слева от тебя. С прошлой смены осталось одно незаконченное тело, начни с него.",
                                 "Нужно провести общий осмотр, да и в целом ты сам разберёшься.",
                                 "- А-а, ладно, понял.",
                                 "А что насчёт помощника? Он опаздывает?",
                                 "- Какой ещё помощник? На эту смену... ты один.", "Э-э, ладно, мне пора.",
                                 "Давай, работай."]
        self.examination_texts = ["Так, ладно, начнём...", "Чёрт, по привычке пульс мерю.",
                                  "Чувствуя эту усталость, я бы не удивился такому.",
                                  "Ну, вроде всё. Нужно записать это в отчёт.",
                                  "Чем раньше начну, тем раньше свалю уже отсюда."]
        self.report_texts = ["Поздние трупные пятна в районе плеч.", "Общее вздутие не наблюдается.",
                             "Общих патологий не выявлено.", "Общий осмотр проведён."]
        self.monologue_after_black = ["Что это было??", "Смерти не боюсь, а темноты - да?",
                                      "Мне кажется, я видел щиток на улице.", "Нужно его проверить..."]
        self.door_locked_texts = ["Хаха, смешная шутка. Не думал, что дверь автоматическая.", "И к чему её ставить?",
                                  "Чтоб пациенты не сбежали?",
                                  "Может быть, в папках есть инфа об этом?"]
        self.door_info_texts = ["...", "А вот, дверь закрыта на время смены для общей безопасности сотрудников.",
                                "Чёрт, ну и что это за правило?",
                                "Бред какой-то...", "Ладно, такое бывает.", "Я и в похуже местах работал.",
                                "Как только вспомню о том дне в мясокомбинате...",
                                "Какой чёрт дёрнул меня это сделать.", "Так, нужно посмотреть, что вводить.",
                                "Иначе я эту работу никогда не закончу."]
        self.photo7_repeat_texts = ["Это уже было"]
        self.photo8_texts = ["Хахах", "Предложить чай??", "Не слишком оригинально для такого места.", "Ммм...",
                             "Так, нуу, вроде понял, что брать."]
        self.photo4_texts = ["Жесть, от усталости в глазах плывёт.", "Так, ну, вроде бы это.", "Сейф??",
                             "И для чего ты здесь?..", "Ну ладно, буду знать."]
        self.photo1_after_black_texts = ["...", "М?", "Мне показалось или мгновение назад на столе никого не было.",
                                         "Чёрт, Том, нужно высыпаться. А может даже согласиться с предложением Сьюзан, пойти к психотерапевту. Возможно, хоть он поможет с галлюцинациями.",
                                         "А может, и исчезновение тела тоже было галлюцинацией??.. Как же я надеюсь на это."]
        self.rules_text = "Добро пожаловать на смену. Работа патологоанатома — это покой и стабильность,\nпока ваш внутренний голос не начинает требовать антракта.\nГлавное правило: не спорьте с тем, кто держит скальпель, когда вы спите,\nиначе следующая запись в журнале вскрытия может оказаться вашей собственной.\nИ помните: правила лишь в вашей голове."
        self.after_call_text = "Ну просто сказка..."
        self.body_after_seq_texts = ["Никаких трупных пятен, необычно, ведь срок уже подошёл.",
                                     "Лицо, правда, у тебя знакомое.",
                                     "К-х", "Как же сильно болит голова...", "..."]
        self.black_screen_texts = ["Где я??", "Ты там, где должен быть.", "Что ты, бл**ь, такое?!",
                                   "Хаха, не догадываешься??", "Ты правда не помнишь меня?",
                                   "Я даже как-то огорчён, что ты каждый раз забываешь меня. Ведь я единственный, кто всегда был рядом с тобой.",
                                   "Да, что ты такое?", "Я", "И есть", "Ты", "Тебе было одиноко, и ты выдумал меня.",
                                   "Хах, кажется, я всё-таки чего-то надышался.",
                                   "Слушай, ты, ну то есть я.", "Я тебя создал, я тебя и убью.",
                                   "Хах, смешной, ты говорил уже это однажды.",
                                   "Но я по-прежнему здесь.", "Ц-ц, это глупый кошмар.",
                                   "А ты фальшивый, как и этот сон.", "Нуу, это ведь только сон.?",
                                   "...", "Так?", "Кх, идиот, мы ещё вернёмся к этому разговору."]
        self.final_texts = ["Хаха, что это было...", "Обещаю, что сегодня же пойду к психотерапевту и уволюсь.",
                            "Но сначала нужно выбраться отсюда.",
                            "Помню, Билл говорил про папку 'пароли', вроде бы, что делать мне там нечего...",
                            "Но я считаю иначе."]
        self.photo10_text = "Ага, вот и ты.\nУдивлён, что не '1234'?"
        self.door_closed_final_texts = ["Дверь закрыта", "Что?", "Как она вообще может быть закрыта?",
                                        "Нужно найти другой способ выйти.",
                                        "Это глупо, ноо...", "Может быть, попробовать через главный вход?",
                                        "Полагаю, исчезновение тела было галлюцинацией, в этом случае мой выход за белой дверью."]
        self.door_open_texts = ["Хахаах", "Свобода!", "Лишь бы это сейчас было реальным.", "Прошу..."]
        self.photo14_texts = ["...", "Фух", "Это был слишком реалистичный сон.", "Я ведь успел поверить...",
                              "Ни за что больше не вернусь туда...", "Я не могу потерять это чувство свободы снова.",
                              "А ты в этом уверен?))"]
        self.photo13_1_texts = ["Сергей Борисович, мы ввели пациенту №116 двойную дозу а********и.",
                                "Но должных улучшений не наблюдается.",
                                "Всё хорошо, Людочка.", "Вводите тройную дозу.",
                                "Мы достанем из него это грязное и лживое 'я'.", "Поняла, Сергей Борисович."]
        self.photo13_2_texts = ["Ц-ц-ц", "Не бойся", "Это всего лишь сон.", "Но он повторится."]
        self.red_texts = ["Ты там, где должен быть.", "Хаха, не догадываешься??", "Ты правда не помнишь меня?",
                          "Я даже как-то огорчён, что ты каждый раз забываешь меня. Ведь я единственный, кто всегда был рядом с тобой.",
                          "Я", "И есть", "Ты", "Тебе было одиноко, и ты выдумал меня.",
                          "Хах, смешной, ты говорил уже это однажды.",
                          "Но я по-прежнему здесь.", "Кх, идиот, мы ещё вернёмся к этому разговору.",
                          "А ты в этом уверен?))", "Но он повторится."]
        self.hurry_text = "Том, не тяни время, пора валить."
        self.final_end_text = "Увы, сны снятся не только ночью."


class RulesScreenRenderer:
    def __init__(self, texts):
        self.texts = texts

    def draw(self):
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


class GoalRenderer:
    def __init__(self, game_state):
        self.game_state = game_state

    def should_draw_goal(self):
        if not self.game_state.show_goal:
            return False
        if any([
            self.game_state.show_rules,
            self.game_state.show_photo10_text,
            self.game_state.final_sequence_active,
            self.game_state.show_black_screen_dialogue,
            self.game_state.show_body_after_seq_text,
            self.game_state.show_text,
            self.game_state.show_phone_call,
            self.game_state.show_after_call_text,
            self.game_state.show_examination,
            self.game_state.current_state in ["report", "photo6"],
            self.game_state.show_monologue_on_photo2,
            self.game_state.show_door_closed_title,
            self.game_state.show_door_locked,
            self.game_state.show_photo7,
            self.game_state.show_photo8,
            self.game_state.show_photo9,
            self.game_state.photo4_text_active,
            self.game_state.after_photo4_sequence_step > 0,
            self.game_state.photo1_after_seq_active,
            self.game_state.photo12_step > 0,
            self.game_state.show_black_screen,
            self.game_state.door_closed_final_active,
            self.game_state.show_door_open,
            self.game_state.door_open_sequence_active,
            self.game_state.show_photo14,
            self.game_state.after_door_open_black,
            self.game_state.after_photo14_black,
            self.game_state.show_photo13_1,
            self.game_state.show_photo13_2,
            self.game_state.show_hurry_text,
            self.game_state.show_final_black_screen
        ]):
            return False
        return True

    def draw(self):
        if self.should_draw_goal():
            arcade.draw_text(
                "Цель:",
                30,
                SCREEN_HEIGHT - 50,
                arcade.color.WHITE,
                21,
                bold=True
            )
            arcade.draw_text(
                self.game_state.goal_text,
                110,
                SCREEN_HEIGHT - 50,
                arcade.color.WHITE,
                18
            )


class PhotoGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Me")
        self.photo_manager = PhotoManager()
        self.click_areas = ClickAreas()
        self.texts = GameTexts()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.music_player_1 = arcade.Sound("data/mel_1.mp3")
        self.music_player_2 = arcade.Sound("data/mel_2.mp3")
        self.music_player = None
        self.current_music_playing = None  # Текущая играющая музыка
        self.active = True

        self.show_text = False
        self.current_text_index = 0
        self.text_finished = False
        self.show_rules = False
        self.show_photo2_text = False
        self.photo2_text_index = 0
        self.photo2_texts_finished = False
        self.photo2_texts_shown = False
        self.show_goal = False
        self.goal_text = ""
        self.phone_call_available = False
        self.show_phone_call = False
        self.phone_call_index = 0
        self.show_after_call_text = False
        self.show_examination = False
        self.examination_index = 0
        self.examination_finished = False
        self.examination_available = False
        self.report_available = False
        self.report_finished = False
        self.current_report_texts = []
        self.show_black_screen = False
        self.show_monologue_on_photo2 = False
        self.monologue_index = 0
        self.monologue_finished = False
        self.came_from_photo6 = False
        self.black_screen_shown = False
        self.show_door_locked = False
        self.door_locked_index = 0
        self.door_locked_finished = False
        self.door_checked = False
        self.show_photo9 = False
        self.show_photo7 = False
        self.photo7_text_index = 0
        self.photo7_texts_finished = False
        self.photo7_visited = False
        self.show_photo8 = False
        self.photo8_text_index = 0
        self.photo8_texts_finished = False
        self.door_info_found = False
        self.meds_info_found = False
        self.photo4_text_index = 0
        self.photo4_text_active = False
        self.safe_checked = False
        self.after_photo4_sequence_step = 0
        self.photo1_after_seq_text_index = 0
        self.photo1_after_seq_active = False
        self.show_body_after_seq_text = False
        self.body_after_seq_text_index = 0
        self.body_after_seq_text_shown = False
        self.show_photo12_sequence = False
        self.photo12_step = 0
        self.show_black_screen_dialogue = False
        self.black_screen_dialogue_index = 0
        self.show_final_sequence = False
        self.final_text_index = 0
        self.final_sequence_active = False
        self.final_texts_completed = False
        self.photo10_sequence_active = False
        self.show_photo10_text = False
        self.photo10_text_shown = False
        self.show_door_closed_final = False
        self.door_closed_final_index = 0
        self.door_closed_final_active = False
        self.show_door_open = False
        self.door_open_sequence_active = False
        self.door_open_text_index = 0
        self.show_photo14 = False
        self.photo14_text_index = 0
        self.show_photo13_1 = False
        self.photo13_1_text_index = 0
        self.show_photo13_2 = False
        self.photo13_2_text_index = 0
        self.after_door_open_black = False
        self.after_photo14_black = False
        self.black_screen_dialogue_completed = False
        self.photo2_1_shown = False
        self.show_hurry_text = False
        self.door_closed_final_completed = False
        self.show_door_closed_title = False
        # Новый флаг для финального черного экрана
        self.show_final_black_screen = False

        self.current_photo = self.photo_manager.photos["photo5"]
        self.current_state = "start_screen"

        # Создаем рендереры
        self.rules_renderer = RulesScreenRenderer(self.texts)
        self.goal_renderer = GoalRenderer(self)

        self.setup_ui()

    def disable_menu_ui(self):
        self.manager.disable()
        self.manager.clear()

    def setup_ui(self):
        start_button = MyFlatButton(text="Начать", width=200, height=40)
        rules_button = RulesButton(text="Правила", width=200, height=40)
        anchor_layout = arcade.gui.UIAnchorLayout()
        anchor_layout.add(child=start_button, anchor_x="center_x", anchor_y="center_y", align_x=170, align_y=20)
        anchor_layout.add(child=rules_button, anchor_x="center_x", anchor_y="center_y", align_x=170, align_y=-30)
        self.manager.add(anchor_layout)

    def start_music(self):
        if self.music_player:
            self.stop_music()
        self.music_player = arcade.play_sound(self.music_player_1, volume=0.5)
        self.current_music_playing = "music_1"

    def switch_to_music_2(self):
        if self.music_player:
            self.stop_music()
        self.music_player = arcade.play_sound(self.music_player_2, volume=0.5)
        self.current_music_playing = "music_2"

    def stop_music(self):
        if self.music_player:
            arcade.stop_sound(self.music_player)
            self.music_player = None
            self.current_music_playing = None

    def on_draw(self) -> None:
        self.clear()
        if self.show_final_black_screen:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
            arcade.draw_text(self.texts.final_end_text,
                             SCREEN_WIDTH // 2,
                             SCREEN_HEIGHT // 2,
                             arcade.color.RED,
                             20,
                             anchor_x="center",
                             anchor_y="center",
                             align="center")
        elif self.show_photo13_2:
            self.draw_photo13_2()
        elif self.show_photo13_1:
            self.draw_photo13_1()
        elif self.after_photo14_black:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self.show_photo14:
            self.draw_photo14()
        elif self.after_door_open_black:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self.show_door_open:
            self.draw_door_open_message()
        elif self.door_open_sequence_active:
            self.draw_door_open_sequence()
        elif self.show_rules:
            self.rules_renderer.draw()  # Используем класс RulesScreenRenderer
        elif self.show_photo10_text:
            self.draw_photo10_with_text()
        elif self.final_sequence_active and self.final_text_index < len(self.texts.final_texts):
            self.draw_final_text()
        elif self.show_black_screen_dialogue:
            self.draw_black_screen_dialogue()
        elif self.photo12_step == 1 and not self.black_screen_dialogue_completed:
            self.draw_photo12_1()
        elif self.photo12_step == 2 and not self.black_screen_dialogue_completed:
            self.draw_photo12_2()
        elif self.show_body_after_seq_text and self.body_after_seq_text_index < len(self.texts.body_after_seq_texts):
            self.draw_body_after_seq_text()
        elif self.show_text and not self.text_finished and self.current_text_index > 0:
            self.draw_main_text()
        elif self.show_phone_call and self.phone_call_index < len(self.texts.phone_call_texts):
            self.draw_phone_call_with_colors()
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
        elif self.show_monologue_on_photo2 and self.monologue_index < len(self.texts.monologue_after_black):
            self.draw_photo2_with_monologue()
        elif self.show_door_closed_title:
            self.draw_door_closed_title()
        elif self.show_door_locked and self.door_locked_index < len(self.texts.door_locked_texts):
            self.draw_door_locked()
        elif self.show_photo7 and self.photo7_text_index < len(self.texts.door_info_texts):
            self.draw_photo7()
        elif self.show_photo8 and self.photo8_text_index < len(self.texts.photo8_texts):
            self.draw_photo8()
        elif self.show_photo9:
            self.draw_photo9()
        elif self.photo4_text_active and self.photo4_text_index < len(self.texts.photo4_texts):
            self.draw_photo4_with_text()
        elif self.after_photo4_sequence_step == 1:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self.after_photo4_sequence_step == 2:
            arcade.draw_texture_rect(self.photo_manager.photos["photo11"],
                                     arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        elif self.after_photo4_sequence_step == 3:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self.photo1_after_seq_active and self.photo1_after_seq_text_index < len(
                self.texts.photo1_after_black_texts):
            self.draw_photo1_with_text()
        elif self.show_black_screen:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self.door_closed_final_active and self.door_closed_final_index < len(self.texts.door_closed_final_texts):
            self.draw_door_closed_final()
        elif self.current_state == "photo4" and not self.photo4_text_active:
            arcade.draw_texture_rect(self.photo_manager.photos["photo4"],
                                     arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            self.draw_current_photo()
            if self.current_state == "start_screen":
                self.manager.draw()
        if self.show_hurry_text:
            self.draw_hurry_text()

        # Используем класс GoalRenderer для отрисовки цели
        self.goal_renderer.draw()

    def draw_door_closed_title(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_text("Дверь закрыта", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 40,
                         anchor_x="center", anchor_y="center", align="center", bold=True)

    def draw_photo14(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo14"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.photo14_text_index < len(self.texts.photo14_texts):
            current_text = self.texts.photo14_texts[self.photo14_text_index]
            text_color = arcade.color.RED if current_text in self.texts.red_texts else arcade.color.WHITE
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, text_color, 24, anchor_x="center", anchor_y="center",
                             align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo13_1(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo13_1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.photo13_1_text_index < len(self.texts.photo13_1_texts):
            current_text = self.texts.photo13_1_texts[self.photo13_1_text_index]
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo13_2(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo13_2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.photo13_2_text_index < len(self.texts.photo13_2_texts):
            current_text = self.texts.photo13_2_texts[self.photo13_2_text_index]
            if current_text:
                text_color = arcade.color.RED if current_text in self.texts.red_texts else arcade.color.WHITE
                arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, text_color, 24, anchor_x="center",
                                 anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_door_open_message(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_text("Дверь открыта", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.GREEN, 40,
                         anchor_x="center", anchor_y="center", align="center", bold=True)

    def draw_door_open_sequence(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.door_open_text_index < len(self.texts.door_open_texts):
            current_text = self.texts.door_open_texts[self.door_open_text_index]
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 24, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_door_closed_final(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text = self.texts.door_closed_final_texts[self.door_closed_final_index]
        if self.door_closed_final_index == 0:
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 30,
                             anchor_x="center", anchor_y="center", align="center", bold=True)
        else:
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo12_1(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo12_1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_photo12_2(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo12_2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_black_screen_dialogue(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.clear()
        if self.black_screen_dialogue_index < len(self.texts.black_screen_texts):
            current_text = self.texts.black_screen_texts[self.black_screen_dialogue_index]
            text_color = arcade.color.RED if current_text in self.texts.red_texts else arcade.color.WHITE
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, text_color, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_final_text(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text = self.texts.final_texts[self.final_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo10_with_text(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo10"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        text_to_display = self.texts.photo10_text
        if self.photo10_text_shown:
            text_to_display += "\n\nНаконец-то я выберусь из этого кошмара."
        arcade.draw_text(text_to_display, SCREEN_WIDTH // 2, 150, arcade.color.BLACK, 24, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_body_after_seq_text(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text = self.texts.body_after_seq_texts[self.body_after_seq_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo4_with_text(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo4"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text = self.texts.photo4_texts[self.photo4_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, 22, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo1_with_text(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text = self.texts.photo1_after_black_texts[self.photo1_after_seq_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_phone_call_with_colors(self):
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        call_text = self.texts.phone_call_texts[self.phone_call_index]
        text_x = SCREEN_WIDTH // 2
        text_y = SCREEN_HEIGHT // 2
        arcade.draw_text(call_text, text_x, text_y, arcade.color.WHITE, 20,
                         anchor_x="center", anchor_y="center",
                         align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_main_text(self):
        text = self.texts.texts.get(self.current_text_index, "")
        arcade.draw_text(text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_after_call(self):
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_text(self.texts.after_call_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_examination(self):
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        exam_text = self.texts.examination_texts[self.examination_index]
        arcade.draw_text(exam_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_report(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo6"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.current_report_texts:
            start_y = SCREEN_HEIGHT - 400
            for i, text in enumerate(self.current_report_texts):
                arcade.draw_text(text, 200, start_y - (i * 45), arcade.color.BLACK, 18, width=SCREEN_WIDTH - 200,
                                 multiline=True)

    def draw_photo2_texts(self):
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text = self.texts.photo2_texts[self.photo2_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo2_with_monologue(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        monologue_text = self.texts.monologue_after_black[self.monologue_index]
        arcade.draw_text(monologue_text, SCREEN_WIDTH // 2, 50, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_door_locked(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.door_locked_index < len(self.texts.door_locked_texts):
            door_text = self.texts.door_locked_texts[self.door_locked_index]
            arcade.draw_text(door_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo7(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo7"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.photo7_visited:
            text_list = self.texts.photo7_repeat_texts
        else:
            text_list = self.texts.door_info_texts
        if self.photo7_text_index < len(text_list):
            photo7_text = text_list[self.photo7_text_index]
            arcade.draw_text(photo7_text, SCREEN_WIDTH // 2, 50, arcade.color.BLACK, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo8(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo8"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.photo8_text_index < len(self.texts.photo8_texts):
            photo8_text = self.texts.photo8_texts[self.photo8_text_index]
            arcade.draw_text(photo8_text, SCREEN_WIDTH // 2, 50, arcade.color.BLACK, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo9(self):
        arcade.draw_texture_rect(self.photo_manager.photos["photo9"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_current_photo(self):
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_hurry_text(self):
        arcade.draw_text(self.texts.hurry_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 30,
                         anchor_x="center", anchor_y="center", align="center", bold=True)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.active:
            return
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        if self.show_final_black_screen:
            arcade.close_window()
            return

        if self.show_photo13_2:
            if self.photo13_2_text_index < len(self.texts.photo13_2_texts) - 1:
                self.photo13_2_text_index += 1
            else:
                # После завершения текстов photo13_2_texts показываем финальный черный экран
                self.show_photo13_2 = False
                self.stop_music()
                self.show_final_black_screen = True
                arcade.set_background_color(arcade.color.BLACK)
            return

        if self.show_photo13_1:
            if self.photo13_1_text_index < len(self.texts.photo13_1_texts) - 1:
                self.photo13_1_text_index += 1
            else:
                self.show_photo13_1 = False
                self.show_photo13_2 = True
                self.photo13_2_text_index = 0
            return
        if self.after_photo14_black:
            self.after_photo14_black = False
            self.show_photo13_1 = True
            self.photo13_1_text_index = 0
            return
        if self.show_photo14:
            if self.photo14_text_index < len(self.texts.photo14_texts) - 1:
                self.photo14_text_index += 1
            else:
                self.show_photo14 = False
                self.after_photo14_black = True
                arcade.set_background_color(arcade.color.BLACK)
            return
        if self.after_door_open_black:
            self.after_door_open_black = False
            self.show_photo14 = True
            self.photo14_text_index = 0
            return
        if self.show_hurry_text:
            self.show_hurry_text = False
            if self.photo2_1_shown:
                self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"
            self.show_goal = True
            self.goal_text = "Беги"
            return
        if self.show_door_closed_title:
            self.show_door_closed_title = False
            self.show_door_locked = True
            self.door_locked_index = 0
            return
        if self.show_door_open:
            self.show_door_open = False
            self.door_open_sequence_active = True
            self.door_open_text_index = 0
            self.show_goal = False
            return
        if self.door_open_sequence_active:
            if self.door_open_text_index < len(self.texts.door_open_texts) - 1:
                self.door_open_text_index += 1
            else:
                self.door_open_sequence_active = False
                self.after_door_open_black = True
                arcade.set_background_color(arcade.color.BLACK)
            return
        if self.show_photo10_text:
            if not self.photo10_text_shown:
                self.photo10_text_shown = True
            else:
                self.show_photo10_text = False
                self.current_photo = self.photo_manager.photos["photo2"]
                self.current_state = "photo2"
                self.show_goal = True
                self.goal_text = "Беги"
            return
        if (self.current_state == "photo3" and
                self.final_texts_completed and
                self.goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "center_photo3")):
            self.current_photo = self.photo_manager.photos["photo10"]
            self.current_state = "photo10"
            self.show_photo10_text = True
            self.photo10_text_shown = False
            self.show_goal = False
            return
        if self.final_sequence_active:
            if self.final_text_index < len(self.texts.final_texts) - 1:
                self.final_text_index += 1
            else:
                self.final_sequence_active = False
                self.final_texts_completed = True
                self.show_goal = True
                self.goal_text = "Беги"
                self.current_state = "photo1"
            return
        if self.show_black_screen_dialogue:
            if self.black_screen_dialogue_index < len(self.texts.black_screen_texts) - 1:
                self.black_screen_dialogue_index += 1
            else:
                if not self.black_screen_dialogue_completed:
                    self.photo_manager.replace_photos_after_black_screen()
                    self.black_screen_dialogue_completed = True
                self.show_black_screen_dialogue = False
                self.current_photo = self.photo_manager.photos["photo1"]
                self.current_state = "photo1"
                self.final_sequence_active = True
                self.final_text_index = 0
                self.show_goal = False
            return
        if self.photo12_step == 1 and not self.black_screen_dialogue_completed:
            self.photo12_step = 2
            return
        elif self.photo12_step == 2 and not self.black_screen_dialogue_completed:
            self.photo12_step = 0
            self.show_black_screen_dialogue = True
            self.black_screen_dialogue_index = 0
            arcade.set_background_color(arcade.color.BLACK)
            return
        if self.show_body_after_seq_text:
            if self.body_after_seq_text_index < len(self.texts.body_after_seq_texts) - 1:
                self.body_after_seq_text_index += 1
            else:
                # Переключаем музыку на вторую после завершения текстов
                if self.current_music_playing != "music_2":
                    self.switch_to_music_2()
                self.show_body_after_seq_text = False
                self.body_after_seq_text_shown = True
                if not self.black_screen_dialogue_completed:
                    self.photo12_step = 1
                    self.show_goal = False
                    self.current_state = "photo12_sequence"
                else:
                    self.current_state = "photo1"
                    self.final_sequence_active = True
                    self.final_text_index = 0
                    self.show_goal = False
            return
        if self.after_photo4_sequence_step == 1:
            self.after_photo4_sequence_step = 2
            return
        elif self.after_photo4_sequence_step == 2:
            self.after_photo4_sequence_step = 3
            return
        elif self.after_photo4_sequence_step == 3:
            self.after_photo4_sequence_step = 0
            self.photo1_after_seq_active = True
            self.photo1_after_seq_text_index = 0
            self.current_state = "photo1"
            self.current_photo = self.photo_manager.photos["photo1"]
            return
        if self.show_black_screen:
            self.handle_black_screen_click()
            return
        if self.photo1_after_seq_active:
            if self.photo1_after_seq_text_index < len(self.texts.photo1_after_black_texts) - 1:
                self.photo1_after_seq_text_index += 1
            else:
                # ПОСЛЕ ЗАВЕРШЕНИЯ photo1_after_black_texts ПЕРЕКЛЮЧАЕМ МУЗЫКУ
                if self.current_music_playing == "music_1":
                    self.switch_to_music_2()
                self.photo1_after_seq_active = False
                self.current_state = "photo1"
                self.show_goal = True
                self.goal_text = "Взять препарат и ввести в тело"
            return
        if self.door_closed_final_active:
            if self.door_closed_final_index < len(self.texts.door_closed_final_texts) - 1:
                self.door_closed_final_index += 1
            else:
                self.door_closed_final_active = False
                self.door_closed_final_index = 0
                self.door_closed_final_completed = True
                self.show_goal = True
                self.goal_text = "Беги"
            return
        if self.show_door_locked:
            if self.door_locked_index < len(self.texts.door_locked_texts) - 1:
                self.door_locked_index += 1
            else:
                self.show_door_locked = False
                self.door_locked_finished = True
                self.door_checked = True
                self.goal_text = "Найти инфу про дверь"
                self.show_goal = True
            return
        if self.show_rules and self.current_state == "start_screen":
            self.show_rules = False
            arcade.set_background_color(arcade.color.DEFAULT)
        elif self.show_text and not self.text_finished and self.current_text_index > 0:
            self.handle_main_text_click()
        elif self.show_phone_call:
            self.handle_phone_call_click()
        elif self.show_after_call_text:
            self.handle_after_call_click()
        elif self.show_examination:
            self.handle_examination_click()
        elif self.current_state in ["report", "photo6"]:
            self.handle_report_click(x, y)
        elif (self.current_state == "photo2" and
              not self.photo2_texts_shown and
              self.show_photo2_text and
              not self.photo2_texts_finished):
            self.handle_photo2_text_click()
        elif self.show_monologue_on_photo2:
            self.handle_monologue_click()
        elif self.show_photo7:
            self.handle_photo7_click(x, y)
        elif self.show_photo8:
            self.handle_photo8_click(x, y)
        elif self.show_photo9:
            self.handle_photo9_click(x, y)
        elif self.photo4_text_active:
            self.handle_photo4_text_click(x, y)
        else:
            self.handle_game_click(x, y)

    def handle_game_click(self, x, y):
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

    def handle_photo2_click(self, x, y):
        if (self.current_state == "photo2" and
                self.door_closed_final_completed and
                self.click_areas.is_in_area(x, y, "back_to_photo1")):
            self.show_hurry_text = True
            self.show_goal = False
            return
        if (self.current_state == "photo2" and
                self.final_texts_completed and
                self.goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "door_photo2")):
            self.show_door_open = True
            self.show_goal = False
            return
        if self.show_monologue_on_photo2:
            return
        if (self.final_texts_completed and
                self.goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "to_computer")):
            self.current_photo = self.photo_manager.photos["photo3"]
            self.current_state = "photo3"
            self.show_goal = True
            self.goal_text = "Беги"
            return
        if (self.final_texts_completed and
                self.goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "back_to_photo1")):
            self.door_closed_final_active = True
            self.door_closed_final_index = 0
            self.show_goal = False
            return
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
        elif self.click_areas.is_in_area(x, y, "door_photo2"):
            if self.goal_text == "Проверить щиток" and not self.door_checked:
                self.show_door_closed_title = True
                self.show_goal = False
                return
        elif self.click_areas.is_in_area(x, y, "phone_call_button"):
            if self.phone_call_available:
                self.show_phone_call = True
                self.phone_call_index = 0
                self.phone_call_available = False

    def handle_photo1_click(self, x, y):
        if (self.black_screen_dialogue_completed and
                self.click_areas.is_in_area(x, y, "door_photo1")):
            if not self.photo2_1_shown:
                self.photo_manager.show_photo2_1()
                self.photo2_1_shown = True
            self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"
            if self.final_texts_completed:
                self.show_goal = True
                self.goal_text = "Беги"
            else:
                self.show_goal = True
                self.goal_text = "Продолжить осмотр"
            return
        if (self.photo1_after_seq_active == False and
                self.photo1_after_seq_text_index == len(self.texts.photo1_after_black_texts) - 1 and
                self.goal_text == "Взять препарат и ввести в тело" and
                self.click_areas.is_in_area(x, y, "examination_area") and
                not self.body_after_seq_text_shown):
            self.show_body_after_seq_text = True
            self.body_after_seq_text_index = 0
            return
        if (self.final_texts_completed and
                self.goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "door_photo1")):
            self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"
            self.show_goal = True
            self.goal_text = "Беги"
            return
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
            if self.door_info_found:
                self.goal_text = "найти инфу про препараты"
            self.show_goal = True
        elif self.click_areas.is_in_area(x, y, "cabinet_photo1"):
            self.current_photo = self.photo_manager.photos["photo4"]
            self.current_state = "photo4"

    def handle_photo4_text_click(self, x, y):
        if self.photo4_text_index < len(self.texts.photo4_texts) - 1:
            self.photo4_text_index += 1
        else:
            self.photo4_text_active = False
            self.after_photo4_sequence_step = 1

    def handle_photo4_click(self, x, y):
        if self.click_areas.is_in_area(x, y, "back_from_cabinet"):
            self.current_photo = self.photo_manager.photos["photo1"]
            self.current_state = "photo1"
            if self.goal_text == "провести осмотр":
                self.examination_available = True
        # ВОТ ЗДЕСЬ ДОБАВЛЕНА ПРОВЕРКА ЦЕЛИ!
        elif (self.click_areas.is_in_area(x, y, "safe_area_photo4") and
              self.goal_text == "Взять препарат и ввести в тело"):  # Проверяем цель
            if not self.safe_checked:
                self.photo4_text_active = True
                self.photo4_text_index = 0
                self.safe_checked = True
        # Если клик на safe_area_photo4, но цель не соответствует, ничего не происходит

    def handle_main_text_click(self):
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
        if self.phone_call_index < len(self.texts.phone_call_texts) - 1:
            self.phone_call_index += 1
        else:
            self.show_phone_call = False
            self.show_after_call_text = True
            self.goal_text = "провести осмотр"

    def handle_after_call_click(self):
        self.show_after_call_text = False

    def handle_examination_click(self):
        if self.examination_index < len(self.texts.examination_texts) - 1:
            self.examination_index += 1
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

    def handle_report_click(self, x, y):
        if self.click_areas.is_in_area(x, y, "back_from_photo6"):
            self.current_photo = self.photo_manager.photos["photo3"]
            self.current_state = "photo3"
            self.current_report_texts = []
            self.report_finished = False
            self.came_from_photo6 = True
            return
        if len(self.current_report_texts) < len(self.texts.report_texts):
            next_text = self.texts.report_texts[len(self.current_report_texts)]
            self.current_report_texts.append(next_text)
            if len(self.current_report_texts) == len(self.texts.report_texts):
                self.report_finished = True

    def handle_photo2_text_click(self):
        if self.photo2_text_index < len(self.texts.photo2_texts) - 1:
            self.photo2_text_index += 1
        else:
            self.show_photo2_text = False
            self.photo2_texts_finished = True
            self.photo2_texts_shown = True
            self.goal_text = "ответить на звонок"
            self.phone_call_available = True

    def handle_black_screen_click(self):
        self.show_black_screen = False
        self.black_screen_shown = True
        self.current_photo = self.photo_manager.photos["photo2"]
        self.current_state = "photo2"
        self.show_monologue_on_photo2 = True
        self.monologue_index = 0
        self.monologue_finished = False
        arcade.set_background_color(arcade.color.DEFAULT)

    def handle_monologue_click(self):
        if self.monologue_index < len(self.texts.monologue_after_black) - 1:
            self.monologue_index += 1
        else:
            self.show_monologue_on_photo2 = False
            self.monologue_finished = True
            self.goal_text = "Проверить щиток"
            self.show_goal = True

    def handle_door_locked_click(self):
        if self.door_locked_index < len(self.texts.door_locked_texts) - 1:
            self.door_locked_index += 1
        else:
            self.show_door_locked = False
            self.door_locked_finished = True
            self.door_checked = True
            self.goal_text = "Найти инфу про дверь"
            self.show_goal = True

    def handle_photo7_click(self, x, y):
        if self.click_areas.is_in_area(x, y, "back_from_photo7"):
            self.show_photo7 = False
            self.photo7_visited = True
            if self.photo7_text_index == len(self.texts.door_info_texts) - 1:
                self.door_info_found = True
                self.goal_text = "найти инфу про препараты"
            self.current_photo = self.photo_manager.photos["photo9"]
            self.current_state = "photo9"
            self.show_photo9 = True
            return
        if self.photo7_visited:
            text_list = self.texts.photo7_repeat_texts
        else:
            text_list = self.texts.door_info_texts
        if self.photo7_text_index < len(text_list) - 1:
            self.photo7_text_index += 1

    def handle_photo8_click(self, x, y):
        if self.click_areas.is_in_area(x, y, "back_from_photo8"):
            self.show_photo8 = False
            self.current_photo = self.photo_manager.photos["photo9"]
            self.current_state = "photo9"
            self.show_photo9 = True
            return
        if self.click_areas.is_in_area(x, y, "photo8_to_photo1"):
            self.show_photo8 = False
            self.current_photo = self.photo_manager.photos["photo1"]
            self.current_state = "photo1"
            self.show_goal = False
            return
        if self.photo8_text_index < len(self.texts.photo8_texts) - 1:
            self.photo8_text_index += 1
        else:
            self.meds_info_found = True
            self.goal_text = "Взять препарат и ввести в тело"
            self.show_goal = True
            self.show_photo8 = False
            self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"

    def handle_photo9_click(self, x, y):
        if self.click_areas.is_in_area(x, y, "photo9_to_photo7"):
            self.show_photo9 = False
            self.current_photo = self.photo_manager.photos["photo7"]
            self.current_state = "photo7"
            self.show_photo7 = True
            self.photo7_text_index = 0
            return
        if self.click_areas.is_in_area(x, y, "photo9_to_photo8"):
            self.show_photo9 = False
            self.current_photo = self.photo_manager.photos["photo8"]
            self.current_state = "photo8"
            self.show_photo8 = True
            self.photo8_text_index = 0
            self.show_goal = False
            return
        if self.click_areas.is_in_area(x, y, "back_from_photo9"):
            self.show_photo9 = False
            self.current_photo = self.photo_manager.photos["photo3"]
            self.current_state = "photo3"
            if self.door_info_found:
                self.goal_text = "найти инфу про препараты"
            self.show_goal = True
            return

    def handle_photo3_click(self, x, y):
        if (self.goal_text == "Найти инфу про дверь" or
                self.goal_text == "найти инфу про препараты"):
            if self.click_areas.is_in_area(x, y, "door_info_folder"):
                self.current_photo = self.photo_manager.photos["photo9"]
                self.current_state = "photo9"
                self.show_photo9 = True
                self.show_goal = False
                return
        if (self.report_available and
                self.click_areas.is_in_area(x, y, "report_area")):
            self.current_photo = self.photo_manager.photos["photo6"]
            self.current_state = "report"
            self.show_goal = False
            self.current_report_texts = []
        elif self.click_areas.is_in_area(x, y, "back_from_computer"):
            self.current_photo = self.photo_manager.photos["photo2"]
            self.current_state = "photo2"
            if self.came_from_photo6 and not self.black_screen_shown:
                self.show_black_screen = True
                arcade.set_background_color(arcade.color.BLACK)
                self.show_goal = False
                self.came_from_photo6 = False
            else:
                if self.goal_text:
                    self.show_goal = True


if __name__ == "__main__":
    game = PhotoGame()
    arcade.run()