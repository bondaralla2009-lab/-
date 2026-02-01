import arcade
import arcade.gui

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 650


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Начать' была нажата!")
        window: PhotoGame = arcade.get_window()
        window._show_text = True
        window._current_text_index = 1
        arcade.set_background_color(arcade.color.BLACK)
        window.start_music()
        window._manager.disable()
        window._manager.clear()


class RulesButton(arcade.gui.UIFlatButton):
    def on_click(self, event):
        print("Кнопка 'Правила' была нажата!")
        window: PhotoGame = arcade.get_window()
        window._show_rules = True
        arcade.set_background_color(arcade.color.BLACK)


class ClickAreas:
    def __init__(self) -> None:
        self._areas: dict = {
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

    def is_in_area(self, x: float, y: float, area_name: str) -> bool:
        a = self._areas.get(area_name)
        return a and a["x_min"] <= x <= a["x_max"] and a["y_min"] <= y <= a["y_max"]


class PhotoManager:
    def __init__(self) -> None:
        self._photos: dict = {}
        self._photos_replaced: bool = False
        self._original_photo1 = None
        self._original_photo2 = None
        self.load_photos()

    def load_photos(self) -> None:
        photo_files: dict = {
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
                self._photos[key] = arcade.load_texture(filepath)
            except Exception as e:
                print(f"Ошибка загрузки {filepath}: {e}")
                self._photos[key] = arcade.Texture.create_empty(key, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def replace_photos_after_black_screen(self) -> None:
        if not self._photos_replaced:
            self._original_photo1 = self._photos["photo1"]
            self._original_photo2 = self._photos["photo2"]
            self._photos["photo1"] = self._photos["photo12_1"]
            self._photos_replaced = True

    def show_photo2_1(self) -> None:
        if "photo2_1" in self._photos:
            self._photos["photo2"] = self._photos["photo2_1"]


class GameTexts:
    def __init__(self) -> None:
        self.texts: dict = {
            1: "Ммм, да, мама была права, нужно было идти в универ,\nсейчас бы работал в офисе... бумажки разгребал.",
            2: "Лааадно, Том, соберись, люди нуждаются в тебе,\nкто, если не ты, будет копаться в телах людей.\nГосподь, я и правда занимаюсь чем-то не тем.",
            3: "Хотя уже не важно, я слишком долго искал эту работу,\nона мне и правда нужна.",
            4: "Только таак хочется спать...",
            5: "Почему вообще первый рабочий день и сразу ночная смена??"
        }
        self.photo2_texts: list = ["М-м-м, как миленько здесь...", "Мне обещали, что скоро придёт помощник.",
                                   "Думаю, с ним будет не так мрачно находиться тут.", "Хотя мне всегда было лучше одному.",
                                   "...", "Хах, стационарный, серьёзно??"]
        self.phone_call_texts: list = ["- Алло? Кто это?",
                                       "- Здравствуй, Том, это Билл, твой начальник. Звоню, чтобы проинформировать о первом рабочем дне.",
                                       "Рядом с тобой компьютер, там в папках всё, что тебе нужно: инфа про пациентов, препараты, документация, отчёты, что тебе будет писать после каждой смены.",
                                       "В папку 'пароли' тебе лезть нечего...",
                                       "Твой кабинет слева от тебя. С прошлой смены осталось одно незаконченное тело, начни с него.",
                                       "Нужно провести общий осмотр, да и в целом ты сам разберёшься.",
                                       "- А-а, ладно, понял.",
                                       "А что насчёт помощника? Он опаздывает?",
                                       "- Какой ещё помощник? На эту смену... ты один.", "Э-э, ладно, мне пора.",
                                       "Давай, работай."]
        self.examination_texts: list = ["Так, ладно, начнём...", "Чёрт, по привычке пульс мерю.",
                                        "Чувствуя эту усталость, я бы не удивился такому.",
                                        "Ну, вроде всё. Нужно записать это в отчёт.",
                                        "Чем раньше начну, тем раньше свалю уже отсюда."]
        self.report_texts: list = ["Поздние трупные пятна в районе плеч.", "Общее вздутие не наблюдается.",
                                   "Общих патологий не выявлено.", "Общий осмотр проведён."]
        self.monologue_after_black: list = ["Что это было??", "Смерти не боюсь, а темноты - да?",
                                            "Мне кажется, я видел щиток на улице.", "Нужно его проверить..."]
        self.door_locked_texts: list = ["Хаха, смешная шутка. Не думал, что дверь автоматическая.", "И к чему её ставить?",
                                        "Чтоб пациенты не сбежали?",
                                        "Может быть, в папках есть инфа об этом?"]
        self.door_info_texts: list = ["...", "А вот, дверь закрыта на время смены для общей безопасности сотрудников.",
                                      "Чёрт, ну и что это за правило?",
                                      "Бред какой-то...", "Ладно, такое бывает.", "Я и в похуже местах работал.",
                                      "Как только вспомню о том дне в мясокомбинате...",
                                      "Какой чёрт дёрнул меня это сделать.", "Так, нужно посмотреть, что вводить.",
                                      "Иначе я эту работу никогда не закончу."]
        self.photo7_repeat_texts: list = ["Это уже было"]
        self.photo8_texts: list = ["Хахах", "Предложить чай??", "Не слишком оригинально для такого места.", "Ммм...",
                                   "Так, нуу, вроде понял, что брать."]
        self.photo8_repeat_texts: list = ["Том, что с памятью. Ты уже же все понял."]
        self.photo4_texts: list = ["Жесть, от усталости в глазах плывёт.", "Так, ну, вроде бы это.", "Сейф??",
                                   "И для чего ты здесь?..", "Ну ладно, буду знать."]
        self.photo1_after_black_texts: list = ["...", "М?", "Мне показалось или мгновение назад на столе никого не было.",
                                               "Чёрт, Том, нужно высыпаться. А может даже согласиться с предложением Сьюзан, пойти к психотерапевту. Возможно, хоть он поможет с галлюцинациями.",
                                               "А может, и исчезновение тела тоже было галлюцинацией??.. Как же я надеюсь на это."]
        self.rules_text: str = "Добро пожаловать на смену. Работа патологоанатома — это покой и стабильность,\nпока ваш внутренний голос не начинает требовать антракта.\nГлавное правило: не спорьте с тем, кто держит скальпель, когда вы спите,\nиначе следующая запись в журнале вскрытия может оказаться вашей собственной.\nИ помните: правила лишь в вашей голове."
        self.after_call_text: str = "Ну просто сказка..."
        self.body_after_seq_texts: list = ["Никаких трупных пятен, необычно, ведь срок уже подошёл.",
                                           "Лицо, правда, у тебя знакомое.",
                                           "К-х", "Как же сильно болит голова...", "..."]
        self.black_screen_texts: list = ["Где я??", "Ты там, где должен быть.", "Что ты, бл**ь, такое?!",
                                         "Хаха, не догадываешься??", "Ты правда не помнишь меня?",
                                         "Я даже как-то огорчён, что ты каждый раз забываешь меня. Ведь я единственный, кто всегда был рядом с тобой.",
                                         "Да, что ты такое?", "Я", "И есть", "Ты", "Тебе было одиноко, и ты выдумал меня.",
                                         "Хах, кажется, я всё-таки чего-то надышался.",
                                         "Слушай, ты, ну то есть я.", "Я тебя создал, я тебя и убью.",
                                         "Хах, смешной, ты говорил уже это однажды.",
                                         "Но я по-прежнему здесь.", "Ц-ц, это глупый кошмар.",
                                         "А ты фальшивый, как и этот сон.", "Нуу, это ведь только сон.?",
                                         "...", "Так?", "Кх, идиот, мы ещё вернёмся к этому разговору."]
        self.final_texts: list = ["Хаха, что это было...", "Обещаю, что сегодня же пойду к психотерапевту и уволюсь.",
                                  "Но сначала нужно выбраться отсюда.",
                                  "Помню, Билл говорил про папку 'пароли', вроде бы, что делать мне там нечего...",
                                  "Но я считаю иначе."]
        self.photo10_text: str = "Ага, вот и ты.\nУдивлён, что не '1234'?"
        self.door_closed_final_texts: list = ["Дверь закрыта", "Что?", "Как она вообще может быть закрыта?",
                                              "Нужно найти другой способ выйти.",
                                              "Это глупо, ноо...", "Может быть, попробовать через главный вход?",
                                              "Полагаю, исчезновение тела было галлюцинацией, в этом случае мой выход за белой дверью."]
        self.door_open_texts: list = ["Хахаах", "Свобода!", "Лишь бы это сейчас было реальным.", "Прошу..."]
        self.photo14_texts: list = ["...", "Фух", "Это был слишком реалистичный сон.", "Я ведь успел поверить...",
                                    "Ни за что больше не вернусь туда...", "Я не могу потерять это чувство свободы снова.",
                                    "А ты в этом уверен?))"]
        self.photo13_1_texts: list = ["Сергей Борисович, мы ввели пациенту №116 двойную дозу а********и.",
                                      "Но должных улучшений не наблюдается.",
                                      "Всё хорошо, Людочка.", "Вводите тройную дозу.",
                                      "Мы достанем из него это грязное и лживое 'я'.", "Поняла, Сергей Борисович."]
        self.photo13_2_texts: list = ["Ц-ц-ц", "Не бойся", "Это всего лишь сон.", "Но он повторится."]
        self.red_texts: list = ["Ты там, где должен быть.", "Хаха, не догадываешься??", "Ты правда не помнишь меня?",
                                "Я даже как-то огорчён, что ты каждый раз забываешь меня. Ведь я единственный, кто всегда был рядом с тобой.",
                                "Я", "И есть", "Ты", "Тебе было одиноко, и ты выдумал меня.",
                                "Хах, смешной, ты говорил уже это однажды.",
                                "Но я по-прежнему здесь.", "Кх, идиот, мы ещё вернёмся к этому разговору.",
                                "А ты в этом уверен?))", "Но он повторится."]
        self.hurry_text: str = "Том, не тяни время, пора валить."
        self.final_end_text: str = "Увы, сны снятся не только ночью."


class RulesScreenRenderer:
    def __init__(self, texts: GameTexts) -> None:
        self._texts: GameTexts = texts

    def draw(self) -> None:
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text(
            self._texts.rules_text,
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
    def __init__(self, game_state) -> None:
        self._game_state = game_state

    def should_draw_goal(self) -> bool:
        if not self._game_state._show_goal:
            return False
        if any([
            self._game_state._show_rules,
            self._game_state._show_photo10_text,
            self._game_state._final_sequence_active,
            self._game_state._show_black_screen_dialogue,
            self._game_state._show_body_after_seq_text,
            self._game_state._show_text,
            self._game_state._show_phone_call,
            self._game_state._show_after_call_text,
            self._game_state._show_examination,
            self._game_state._current_state in ["report", "photo6"],
            self._game_state._show_monologue_on_photo2,
            self._game_state._show_door_closed_title,
            self._game_state._show_door_locked,
            self._game_state._show_photo7,
            self._game_state._show_photo8,
            self._game_state._show_photo9,
            self._game_state._photo4_text_active,
            self._game_state._after_photo4_sequence_step > 0,
            self._game_state._photo1_after_seq_active,
            self._game_state._photo12_step > 0,
            self._game_state._show_black_screen,
            self._game_state._door_closed_final_active,
            self._game_state._show_door_open,
            self._game_state._door_open_sequence_active,
            self._game_state._show_photo14,
            self._game_state._after_door_open_black,
            self._game_state._after_photo14_black,
            self._game_state._show_photo13_1,
            self._game_state._show_photo13_2,
            self._game_state._show_hurry_text,
            self._game_state._show_final_black_screen
        ]):
            return False
        return True

    def draw(self) -> None:
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
                self._game_state._goal_text,
                110,
                SCREEN_HEIGHT - 50,
                arcade.color.WHITE,
                18
            )


class PhotoGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Me")
        self.photo_manager: PhotoManager = PhotoManager()
        self.click_areas: ClickAreas = ClickAreas()
        self.texts: GameTexts = GameTexts()
        self._manager: arcade.gui.UIManager = arcade.gui.UIManager()
        self._manager.enable()
        self.music_player_1: arcade.Sound = arcade.Sound("data/mel_1.mp3")
        self.music_player_2: arcade.Sound = arcade.Sound("data/mel_2.mp3")
        self._music_player = None
        self._current_music_playing = None

        self._show_text: bool = False
        self._current_text_index: int = 0
        self._text_finished: bool = False
        self._show_rules: bool = False
        self._show_photo2_text: bool = False
        self._photo2_text_index: int = 0
        self._photo2_texts_finished: bool = False
        self._photo2_texts_shown: bool = False
        self._show_goal: bool = False
        self._goal_text: str = ""
        self._phone_call_available: bool = False
        self._show_phone_call: bool = False
        self._phone_call_index: int = 0
        self._show_after_call_text: bool = False
        self._show_examination: bool = False
        self._examination_index: int = 0
        self._examination_finished: bool = False
        self._examination_available: bool = False
        self._report_available: bool = False
        self._report_finished: bool = False
        self._current_report_texts: list = []
        self._show_black_screen: bool = False
        self._show_monologue_on_photo2: bool = False
        self._monologue_index: int = 0
        self._monologue_finished: bool = False
        self._came_from_photo6: bool = False
        self._black_screen_shown: bool = False
        self._show_door_locked: bool = False
        self._door_locked_index: int = 0
        self._door_locked_finished: bool = False
        self._door_checked: bool = False
        self._show_photo9: bool = False
        self._show_photo7: bool = False
        self._photo7_text_index: int = 0
        self._photo7_texts_finished: bool = False
        self._photo7_visited: bool = False
        self._show_photo8: bool = False
        self._photo8_text_index: int = 0
        self._photo8_texts_finished: bool = False
        self._door_info_found: bool = False
        self._meds_info_found: bool = False
        self._photo4_text_index: int = 0
        self._photo4_text_active: bool = False
        self._safe_checked: bool = False
        self._after_photo4_sequence_step: int = 0
        self._photo1_after_seq_text_index: int = 0
        self._photo1_after_seq_active: bool = False
        self._show_body_after_seq_text: bool = False
        self._body_after_seq_text_index: int = 0
        self._body_after_seq_text_shown: bool = False
        self._show_photo12_sequence: bool = False
        self._photo12_step: int = 0
        self._show_black_screen_dialogue: bool = False
        self._black_screen_dialogue_index: int = 0
        self._show_final_sequence: bool = False
        self._final_text_index: int = 0
        self._final_sequence_active: bool = False
        self._final_texts_completed: bool = False
        self._photo10_sequence_active: bool = False
        self._show_photo10_text: bool = False
        self._photo10_text_shown: bool = False
        self._show_door_closed_final: bool = False
        self._door_closed_final_index: int = 0
        self._door_closed_final_active: bool = False
        self._show_door_open: bool = False
        self._door_open_sequence_active: bool = False
        self._door_open_text_index: int = 0
        self._show_photo14: bool = False
        self._photo14_text_index: int = 0
        self._show_photo13_1: bool = False
        self._photo13_1_text_index: int = 0
        self._show_photo13_2: bool = False
        self._photo13_2_text_index: int = 0
        self._after_door_open_black: bool = False
        self._after_photo14_black: bool = False
        self._black_screen_dialogue_completed: bool = False
        self._photo2_1_shown: bool = False
        self._show_hurry_text: bool = False
        self._door_closed_final_completed: bool = False
        self._show_door_closed_title: bool = False
        self._show_final_black_screen: bool = False
        self._photo8_visited: bool = False
        self._photo6_visited: bool = False
        self._door_closed_final_texts_completed: bool = False

        self.current_photo = self.photo_manager._photos["photo5"]
        self._current_state: str = "start_screen"

        self._rules_renderer: RulesScreenRenderer = RulesScreenRenderer(self.texts)
        self._goal_renderer: GoalRenderer = GoalRenderer(self)

        self.setup_ui()

    def disable_menu_ui(self) -> None:
        self._manager.disable()
        self._manager.clear()

    def setup_ui(self) -> None:
        start_button: MyFlatButton = MyFlatButton(text="Начать", width=200, height=40)
        rules_button: RulesButton = RulesButton(text="Правила", width=200, height=40)
        anchor_layout: arcade.gui.UIAnchorLayout = arcade.gui.UIAnchorLayout()
        anchor_layout.add(child=start_button, anchor_x="center_x", anchor_y="center_y", align_x=170, align_y=20)
        anchor_layout.add(child=rules_button, anchor_x="center_x", anchor_y="center_y", align_x=170, align_y=-30)
        self._manager.add(anchor_layout)

    def start_music(self) -> None:
        if self._music_player:
            self.stop_music()
        self._music_player = arcade.play_sound(self.music_player_1, volume=0.5)
        self._current_music_playing = "music_1"

    def switch_to_music_2(self) -> None:
        if self._music_player:
            self.stop_music()
        self._music_player = arcade.play_sound(self.music_player_2, volume=0.5)
        self._current_music_playing = "music_2"

    def stop_music(self) -> None:
        if self._music_player:
            arcade.stop_sound(self._music_player)
            self._music_player = None
            self._current_music_playing = None

    def on_draw(self) -> None:
        self.clear()
        if self._show_final_black_screen:
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
        elif self._show_photo13_2:
            self.draw_photo13_2()
        elif self._show_photo13_1:
            self.draw_photo13_1()
        elif self._after_photo14_black:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self._show_photo14:
            self.draw_photo14()
        elif self._after_door_open_black:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self._show_door_open:
            self.draw_door_open_message()
        elif self._door_open_sequence_active:
            self.draw_door_open_sequence()
        elif self._show_rules:
            self._rules_renderer.draw()
        elif self._show_photo10_text:
            self.draw_photo10_with_text()
        elif self._final_sequence_active and self._final_text_index < len(self.texts.final_texts):
            self.draw_final_text()
        elif self._show_black_screen_dialogue:
            self.draw_black_screen_dialogue()
        elif self._photo12_step == 1 and not self._black_screen_dialogue_completed:
            self.draw_photo12_1()
        elif self._photo12_step == 2 and not self._black_screen_dialogue_completed:
            self.draw_photo12_2()
        elif self._show_body_after_seq_text and self._body_after_seq_text_index < len(self.texts.body_after_seq_texts):
            self.draw_body_after_seq_text()
        elif self._show_text and not self._text_finished and self._current_text_index > 0:
            self.draw_main_text()
        elif self._show_phone_call and self._phone_call_index < len(self.texts.phone_call_texts):
            self.draw_phone_call_with_colors()
        elif self._show_after_call_text:
            self.draw_after_call()
        elif self._show_examination and self._examination_index < len(self.texts.examination_texts):
            self.draw_examination()
        elif self._current_state in ["report", "photo6"]:
            self.draw_report()
        elif (self._current_state == "photo2" and
              not self._photo2_texts_shown and
              self._show_photo2_text and
              not self._photo2_texts_finished and
              self._photo2_text_index < len(self.texts.photo2_texts)):
            self.draw_photo2_texts()
        elif self._show_monologue_on_photo2 and self._monologue_index < len(self.texts.monologue_after_black):
            self.draw_photo2_with_monologue()
        elif self._show_door_closed_title:
            self.draw_door_closed_title()
        elif self._show_door_locked and self._door_locked_index < len(self.texts.door_locked_texts):
            self.draw_door_locked()
        elif self._show_photo7 and self._photo7_text_index < len(self.texts.door_info_texts):
            self.draw_photo7()
        elif self._show_photo8:
            self.draw_photo8()
        elif self._show_photo9:
            self.draw_photo9()
        elif self._photo4_text_active and self._photo4_text_index < len(self.texts.photo4_texts):
            self.draw_photo4_with_text()
        elif self._after_photo4_sequence_step == 1:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self._after_photo4_sequence_step == 2:
            arcade.draw_texture_rect(self.photo_manager._photos["photo11"],
                                     arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        elif self._after_photo4_sequence_step == 3:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self._photo1_after_seq_active and self._photo1_after_seq_text_index < len(
                self.texts.photo1_after_black_texts):
            self.draw_photo1_with_text()
        elif self._show_black_screen:
            arcade.set_background_color(arcade.color.BLACK)
            self.clear()
        elif self._door_closed_final_active and self._door_closed_final_index < len(self.texts.door_closed_final_texts):
            self.draw_door_closed_final()
        elif self._current_state == "photo4" and not self._photo4_text_active:
            arcade.draw_texture_rect(self.photo_manager._photos["photo4"],
                                     arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            self.draw_current_photo()
            if self._current_state == "start_screen":
                self._manager.draw()
        if self._show_hurry_text:
            self.draw_hurry_text()

        self._goal_renderer.draw()

    def draw_photo8(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo8"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

        if self._photo8_visited:
            if self._photo8_text_index < len(self.texts.photo8_repeat_texts):
                photo8_text: str = self.texts.photo8_repeat_texts[self._photo8_text_index]
                arcade.draw_text(photo8_text, SCREEN_WIDTH // 2, 50, arcade.color.BLACK, 20, anchor_x="center",
                                 anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)
        else:
            if self._photo8_text_index < len(self.texts.photo8_texts):
                photo8_text: str = self.texts.photo8_texts[self._photo8_text_index]
                arcade.draw_text(photo8_text, SCREEN_WIDTH // 2, 50, arcade.color.BLACK, 20, anchor_x="center",
                                 anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_report(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo6"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

        if self._photo6_visited:
            start_y: int = SCREEN_HEIGHT - 400
            for i, text in enumerate(self.texts.report_texts):
                arcade.draw_text(text, 200, start_y - (i * 45), arcade.color.BLACK, 18, width=SCREEN_WIDTH - 200,
                                 multiline=True)
        else:
            if self._current_report_texts:
                start_y: int = SCREEN_HEIGHT - 400
                for i, text in enumerate(self._current_report_texts):
                    arcade.draw_text(text, 200, start_y - (i * 45), arcade.color.BLACK, 18, width=SCREEN_WIDTH - 200,
                                     multiline=True)

    def draw_door_closed_title(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_text("Дверь закрыта", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 40,
                         anchor_x="center", anchor_y="center", align="center", bold=True)

    def draw_photo14(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo14"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self._photo14_text_index < len(self.texts.photo14_texts):
            current_text: str = self.texts.photo14_texts[self._photo14_text_index]
            text_color = arcade.color.RED if current_text in self.texts.red_texts else arcade.color.WHITE
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, text_color, 24, anchor_x="center", anchor_y="center",
                             align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo13_1(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo13_1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self._photo13_1_text_index < len(self.texts.photo13_1_texts):
            current_text: str = self.texts.photo13_1_texts[self._photo13_1_text_index]
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo13_2(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo13_2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self._photo13_2_text_index < len(self.texts.photo13_2_texts):
            current_text: str = self.texts.photo13_2_texts[self._photo13_2_text_index]
            if current_text:
                text_color = arcade.color.RED if current_text in self.texts.red_texts else arcade.color.WHITE
                arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, text_color, 24, anchor_x="center",
                                 anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_door_open_message(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_text("Дверь открыта", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.GREEN, 40,
                         anchor_x="center", anchor_y="center", align="center", bold=True)

    def draw_door_open_sequence(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self._door_open_text_index < len(self.texts.door_open_texts):
            current_text: str = self.texts.door_open_texts[self._door_open_text_index]
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 24, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_door_closed_final(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text: str = self.texts.door_closed_final_texts[self._door_closed_final_index]
        if self._door_closed_final_index == 0:
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 30,
                             anchor_x="center", anchor_y="center", align="center", bold=True)
        else:
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo12_1(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo12_1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_photo12_2(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo12_2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_black_screen_dialogue(self) -> None:
        arcade.set_background_color(arcade.color.BLACK)
        self.clear()
        if self._black_screen_dialogue_index < len(self.texts.black_screen_texts):
            current_text: str = self.texts.black_screen_texts[self._black_screen_dialogue_index]
            text_color = arcade.color.RED if current_text in self.texts.red_texts else arcade.color.WHITE
            arcade.draw_text(current_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, text_color, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_final_text(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text: str = self.texts.final_texts[self._final_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo10_with_text(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo10"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        text_to_display: str = self.texts.photo10_text
        if self._photo10_text_shown:
            text_to_display += "\n\nНаконец-то я выберусь из этого кошмара."
        arcade.draw_text(text_to_display, SCREEN_WIDTH // 2, 150, arcade.color.BLACK, 24, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_body_after_seq_text(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text: str = self.texts.body_after_seq_texts[self._body_after_seq_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo4_with_text(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo4"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text: str = self.texts.photo4_texts[self._photo4_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, 22, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo1_with_text(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo1"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text: str = self.texts.photo1_after_black_texts[self._photo1_after_seq_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_phone_call_with_colors(self) -> None:
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        call_text: str = self.texts.phone_call_texts[self._phone_call_index]
        text_x: int = SCREEN_WIDTH // 2
        text_y: int = SCREEN_HEIGHT // 2
        arcade.draw_text(call_text, text_x, text_y, arcade.color.WHITE, 20,
                         anchor_x="center", anchor_y="center",
                         align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_main_text(self) -> None:
        text: str = self.texts.texts.get(self._current_text_index, "")
        arcade.draw_text(text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_after_call(self) -> None:
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_text(self.texts.after_call_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_examination(self) -> None:
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        exam_text: str = self.texts.examination_texts[self._examination_index]
        arcade.draw_text(exam_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo2_texts(self) -> None:
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        current_text: str = self.texts.photo2_texts[self._photo2_text_index]
        arcade.draw_text(current_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo2_with_monologue(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        monologue_text: str = self.texts.monologue_after_black[self._monologue_index]
        arcade.draw_text(monologue_text, SCREEN_WIDTH // 2, 50, arcade.color.WHITE, 20, anchor_x="center",
                         anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_door_locked(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo2"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self._door_locked_index < len(self.texts.door_locked_texts):
            door_text: str = self.texts.door_locked_texts[self._door_locked_index]
            arcade.draw_text(door_text, SCREEN_WIDTH // 2, 100, arcade.color.WHITE, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo7(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo7"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self._photo7_visited:
            text_list: list = self.texts.photo7_repeat_texts
        else:
            text_list: list = self.texts.door_info_texts
        if self._photo7_text_index < len(text_list):
            photo7_text: str = text_list[self._photo7_text_index]
            arcade.draw_text(photo7_text, SCREEN_WIDTH // 2, 50, arcade.color.BLACK, 20, anchor_x="center",
                             anchor_y="center", align="center", width=SCREEN_WIDTH - 100, multiline=True)

    def draw_photo9(self) -> None:
        arcade.draw_texture_rect(self.photo_manager._photos["photo9"],
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_current_photo(self) -> None:
        arcade.draw_texture_rect(self.current_photo,
                                 arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_hurry_text(self) -> None:
        arcade.draw_text(self.texts.hurry_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 30,
                         anchor_x="center", anchor_y="center", align="center", bold=True)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if not self._active:
            return
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        if self._show_final_black_screen:
            arcade.close_window()
            return

        if self._show_photo13_2:
            if self._photo13_2_text_index < len(self.texts.photo13_2_texts) - 1:
                self._photo13_2_text_index += 1
            else:
                self._show_photo13_2 = False
                self.stop_music()
                self._show_final_black_screen = True
                arcade.set_background_color(arcade.color.BLACK)
            return

        if self._show_photo13_1:
            if self._photo13_1_text_index < len(self.texts.photo13_1_texts) - 1:
                self._photo13_1_text_index += 1
            else:
                self._show_photo13_1 = False
                self._show_photo13_2 = True
                self._photo13_2_text_index = 0
            return
        if self._after_photo14_black:
            self._after_photo14_black = False
            self._show_photo13_1 = True
            self._photo13_1_text_index = 0
            return
        if self._show_photo14:
            if self._photo14_text_index < len(self.texts.photo14_texts) - 1:
                self._photo14_text_index += 1
            else:
                self._show_photo14 = False
                self._after_photo14_black = True
                arcade.set_background_color(arcade.color.BLACK)
            return
        if self._after_door_open_black:
            self._after_door_open_black = False
            self._show_photo14 = True
            self._photo14_text_index = 0
            return
        if self._show_hurry_text:
            self._show_hurry_text = False
            if self._photo2_1_shown:
                self.current_photo = self.photo_manager._photos["photo2"]
            self._current_state = "photo2"
            self._show_goal = True
            self._goal_text = "Беги"
            return
        if self._show_door_closed_title:
            self._show_door_closed_title = False
            self._show_door_locked = True
            self._door_locked_index = 0
            return
        if self._show_door_open:
            self._show_door_open = False
            self._door_open_sequence_active = True
            self._door_open_text_index = 0
            self._show_goal = False
            return
        if self._door_open_sequence_active:
            if self._door_open_text_index < len(self.texts.door_open_texts) - 1:
                self._door_open_text_index += 1
            else:
                self._door_open_sequence_active = False
                self._after_door_open_black = True
                arcade.set_background_color(arcade.color.BLACK)
            return
        if self._show_photo10_text:
            if not self._photo10_text_shown:
                self._photo10_text_shown = True
            else:
                self._show_photo10_text = False
                self.current_photo = self.photo_manager._photos["photo2"]
                self._current_state = "photo2"
                self._show_goal = True
                self._goal_text = "Беги"
            return
        if (self._current_state == "photo3" and
                self._final_texts_completed and
                self._goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "center_photo3")):
            self.current_photo = self.photo_manager._photos["photo10"]
            self._current_state = "photo10"
            self._show_photo10_text = True
            self._photo10_text_shown = False
            self._show_goal = False
            return
        if self._final_sequence_active:
            if self._final_text_index < len(self.texts.final_texts) - 1:
                self._final_text_index += 1
            else:
                self._final_sequence_active = False
                self._final_texts_completed = True
                self._show_goal = True
                self._goal_text = "Беги"
                self._current_state = "photo1"
            return
        if self._show_black_screen_dialogue:
            if self._black_screen_dialogue_index < len(self.texts.black_screen_texts) - 1:
                self._black_screen_dialogue_index += 1
            else:
                if not self._black_screen_dialogue_completed:
                    self.photo_manager.replace_photos_after_black_screen()
                    self._black_screen_dialogue_completed = True
                self._show_black_screen_dialogue = False
                self.current_photo = self.photo_manager._photos["photo1"]
                self._current_state = "photo1"
                self._final_sequence_active = True
                self._final_text_index = 0
                self._show_goal = False
            return
        if self._photo12_step == 1 and not self._black_screen_dialogue_completed:
            self._photo12_step = 2
            return
        elif self._photo12_step == 2 and not self._black_screen_dialogue_completed:
            self._photo12_step = 0
            self._show_black_screen_dialogue = True
            self._black_screen_dialogue_index = 0
            arcade.set_background_color(arcade.color.BLACK)
            return
        if self._show_body_after_seq_text:
            if self._body_after_seq_text_index < len(self.texts.body_after_seq_texts) - 1:
                self._body_after_seq_text_index += 1
            else:
                if self._current_music_playing != "music_2":
                    self.switch_to_music_2()
                self._show_body_after_seq_text = False
                self._body_after_seq_text_shown = True
                if not self._black_screen_dialogue_completed:
                    self._photo12_step = 1
                    self._show_goal = False
                    self._current_state = "photo12_sequence"
                else:
                    self._current_state = "photo1"
                    self._final_sequence_active = True
                    self._final_text_index = 0
                    self._show_goal = False
            return
        if self._after_photo4_sequence_step == 1:
            self._after_photo4_sequence_step = 2
            return
        elif self._after_photo4_sequence_step == 2:
            self._after_photo4_sequence_step = 3
            return
        elif self._after_photo4_sequence_step == 3:
            self._after_photo4_sequence_step = 0
            self._photo1_after_seq_active = True
            self._photo1_after_seq_text_index = 0
            self._current_state = "photo1"
            self.current_photo = self.photo_manager._photos["photo1"]
            return
        if self._show_black_screen:
            self.handle_black_screen_click()
            return
        if self._photo1_after_seq_active:
            if self._photo1_after_seq_text_index < len(self.texts.photo1_after_black_texts) - 1:
                self._photo1_after_seq_text_index += 1
            else:
                if self._current_music_playing == "music_1":
                    self.switch_to_music_2()
                self._photo1_after_seq_active = False
                self._current_state = "photo1"
                self._show_goal = True
                self._goal_text = "Взять препарат и ввести в тело"
            return
        if self._door_closed_final_active:
            if self._door_closed_final_index < len(self.texts.door_closed_final_texts) - 1:
                self._door_closed_final_index += 1
            else:
                self._door_closed_final_active = False
                self._door_closed_final_index = 0
                self._door_closed_final_completed = True
                self._door_closed_final_texts_completed = True
                self._show_goal = True
                self._goal_text = "Беги"
            return
        if self._show_door_locked:
            if self._door_locked_index < len(self.texts.door_locked_texts) - 1:
                self._door_locked_index += 1
            else:
                self._show_door_locked = False
                self._door_locked_finished = True
                self._door_checked = True
                self._goal_text = "Найти инфу про дверь"
                self._show_goal = True
            return
        if self._show_rules and self._current_state == "start_screen":
            self._show_rules = False
            arcade.set_background_color(arcade.color.DEFAULT)
        elif self._show_text and not self._text_finished and self._current_text_index > 0:
            self.handle_main_text_click()
        elif self._show_phone_call:
            self.handle_phone_call_click()
        elif self._show_after_call_text:
            self.handle_after_call_click()
        elif self._show_examination:
            self.handle_examination_click()
        elif self._current_state in ["report", "photo6"]:
            self.handle_report_click(x, y)
        elif (self._current_state == "photo2" and
              not self._photo2_texts_shown and
              self._show_photo2_text and
              not self._photo2_texts_finished):
            self.handle_photo2_text_click()
        elif self._show_monologue_on_photo2:
            self.handle_monologue_click()
        elif self._show_photo7:
            self.handle_photo7_click(x, y)
        elif self._show_photo8:
            self.handle_photo8_click(x, y)
        elif self._show_photo9:
            self.handle_photo9_click(x, y)
        elif self._photo4_text_active:
            self.handle_photo4_text_click(x, y)
        else:
            self.handle_game_click(x, y)

    def handle_game_click(self, x: float, y: float) -> None:
        if self._current_state == "start_screen":
            pass
        elif self._current_state == "photo1":
            self.handle_photo1_click(x, y)
        elif self._current_state == "photo2":
            self.handle_photo2_click(x, y)
        elif self._current_state == "photo3":
            self.handle_photo3_click(x, y)
        elif self._current_state == "photo4":
            self.handle_photo4_click(x, y)

    def handle_photo2_click(self, x: float, y: float) -> None:
        if (self._current_state == "photo2" and
                self._door_closed_final_completed and
                self.click_areas.is_in_area(x, y, "back_to_photo1")):
            self._show_hurry_text = True
            self._show_goal = False
            return
        if (self._current_state == "photo2" and
                self._final_texts_completed and
                self._goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "door_photo2")):
            if self._door_closed_final_texts_completed:
                self._show_door_open = True
                self._show_goal = False
            return
        if self._show_monologue_on_photo2:
            return
        if (self._final_texts_completed and
                self._goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "to_computer")):
            self.current_photo = self.photo_manager._photos["photo3"]
            self._current_state = "photo3"
            self._show_goal = True
            self._goal_text = "Беги"
            return
        if (self._final_texts_completed and
                self._goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "back_to_photo1")):
            if not self._door_closed_final_texts_completed:
                self._door_closed_final_active = True
                self._door_closed_final_index = 0
                self._show_goal = False
            return
        if self.click_areas.is_in_area(x, y, "back_to_photo1"):
            if self._show_photo2_text and not self._photo2_texts_shown:
                self._show_photo2_text = False
                self._photo2_texts_finished = True
            else:
                self.current_photo = self.photo_manager._photos["photo1"]
                self._current_state = "photo1"
                if self._goal_text == "провести осмотр":
                    self._examination_available = True
        elif self.click_areas.is_in_area(x, y, "to_computer"):
            if self._show_photo2_text and not self._photo2_texts_shown:
                self._show_photo2_text = False
                self._photo2_texts_finished = True
            else:
                self.current_photo = self.photo_manager._photos["photo3"]
                self._current_state = "photo3"
                self._show_goal = False
        elif self.click_areas.is_in_area(x, y, "door_photo2"):
            if self._goal_text == "Проверить щиток" and not self._door_checked:
                self._show_door_closed_title = True
                self._show_goal = False
                return
        elif self.click_areas.is_in_area(x, y, "phone_call_button"):
            if self._phone_call_available:
                self._show_phone_call = True
                self._phone_call_index = 0
                self._phone_call_available = False

    def handle_photo1_click(self, x: float, y: float) -> None:
        if (self._black_screen_dialogue_completed and
                self.click_areas.is_in_area(x, y, "door_photo1")):
            if not self._photo2_1_shown:
                self.photo_manager.show_photo2_1()
                self._photo2_1_shown = True
            self.current_photo = self.photo_manager._photos["photo2"]
            self._current_state = "photo2"
            if self._final_texts_completed:
                self._show_goal = True
                self._goal_text = "Беги"
            else:
                self._show_goal = True
                self._goal_text = "Продолжить осмотр"
            return
        if (self._photo1_after_seq_active == False and
                self._photo1_after_seq_text_index == len(self.texts.photo1_after_black_texts) - 1 and
                self._goal_text == "Взять препарат и ввести в тело" and
                self.click_areas.is_in_area(x, y, "examination_area") and
                not self._body_after_seq_text_shown):
            self._show_body_after_seq_text = True
            self._body_after_seq_text_index = 0
            return
        if (self._final_texts_completed and
                self._goal_text == "Беги" and
                self.click_areas.is_in_area(x, y, "door_photo1")):
            self.current_photo = self.photo_manager._photos["photo2"]
            self._current_state = "photo2"
            self._show_goal = True
            self._goal_text = "Беги"
            return
        if (self._examination_available and
                self.click_areas.is_in_area(x, y, "examination_area")):
            self._show_examination = True
            self._examination_index = 0
            self._examination_available = False
        elif self.click_areas.is_in_area(x, y, "door_photo1"):
            self.current_photo = self.photo_manager._photos["photo2"]
            self._current_state = "photo2"
            if not self._photo2_texts_shown:
                self._show_photo2_text = True
                self._photo2_text_index = 0
                self._photo2_texts_finished = False
            if self._door_info_found:
                self._goal_text = "найти инфу про препараты"
            self._show_goal = True
        elif self.click_areas.is_in_area(x, y, "cabinet_photo1"):
            self.current_photo = self.photo_manager._photos["photo4"]
            self._current_state = "photo4"

    def handle_photo4_text_click(self, x: float, y: float) -> None:
        if self._photo4_text_index < len(self.texts.photo4_texts) - 1:
            self._photo4_text_index += 1
        else:
            self._photo4_text_active = False
            self._after_photo4_sequence_step = 1

    def handle_photo4_click(self, x: float, y: float) -> None:
        if self.click_areas.is_in_area(x, y, "back_from_cabinet"):
            self.current_photo = self.photo_manager._photos["photo1"]
            self._current_state = "photo1"
            if self._goal_text == "провести осмотр":
                self._examination_available = True
        elif (self.click_areas.is_in_area(x, y, "safe_area_photo4") and
              self._goal_text == "Взять препарат и ввести в тело"):
            if not self._safe_checked:
                self._photo4_text_active = True
                self._photo4_text_index = 0
                self._safe_checked = True

    def handle_main_text_click(self) -> None:
        if self._current_text_index < 5:
            self._current_text_index += 1
        else:
            self._show_text = False
            self._text_finished = True
            self._current_text_index = 0
            self.current_photo = self.photo_manager._photos["photo2"]
            self._current_state = "photo2"
            if not self._photo2_texts_shown:
                self._show_photo2_text = True
                self._photo2_text_index = 0
                self._photo2_texts_finished = False
            self._show_goal = True
            self._goal_text = ""
            arcade.set_background_color(arcade.color.DEFAULT)

    def handle_phone_call_click(self) -> None:
        if self._phone_call_index < len(self.texts.phone_call_texts) - 1:
            self._phone_call_index += 1
        else:
            self._show_phone_call = False
            self._show_after_call_text = True
            self._goal_text = "провести осмотр"

    def handle_after_call_click(self) -> None:
        self._show_after_call_text = False

    def handle_examination_click(self) -> None:
        if self._examination_index < len(self.texts.examination_texts) - 1:
            self._examination_index += 1
            if self._examination_index == 2:
                self._show_goal = False
                self._goal_text = ""
            if self._examination_index == len(self.texts.examination_texts) - 1:
                self._goal_text = "написать отчет об состоянии"
                self._show_goal = True
                self._report_available = True
        else:
            self._show_examination = False
            self._examination_finished = True

    def handle_report_click(self, x: float, y: float) -> None:
        if self.click_areas.is_in_area(x, y, "back_from_photo6"):
            self.current_photo = self.photo_manager._photos["photo3"]
            self._current_state = "photo3"

            if not self._photo6_visited:
                self._photo6_visited = True

            self._current_report_texts = []
            self._report_finished = False
            self._came_from_photo6 = True
            return

        if self._photo6_visited:
            self.current_photo = self.photo_manager._photos["photo3"]
            self._current_state = "photo3"
            self._came_from_photo6 = True
            return

        if len(self._current_report_texts) < len(self.texts.report_texts):
            next_text: str = self.texts.report_texts[len(self._current_report_texts)]
            self._current_report_texts.append(next_text)
            if len(self._current_report_texts) == len(self.texts.report_texts):
                self._report_finished = True
                self._photo6_visited = True

    def handle_photo2_text_click(self) -> None:
        if self._photo2_text_index < len(self.texts.photo2_texts) - 1:
            self._photo2_text_index += 1
        else:
            self._show_photo2_text = False
            self._photo2_texts_finished = True
            self._photo2_texts_shown = True
            self._goal_text = "ответить на звонок"
            self._phone_call_available = True

    def handle_black_screen_click(self) -> None:
        self._show_black_screen = False
        self._black_screen_shown = True
        self.current_photo = self.photo_manager._photos["photo2"]
        self._current_state = "photo2"
        self._show_monologue_on_photo2 = True
        self._monologue_index = 0
        self._monologue_finished = False
        arcade.set_background_color(arcade.color.DEFAULT)

    def handle_monologue_click(self) -> None:
        if self._monologue_index < len(self.texts.monologue_after_black) - 1:
            self._monologue_index += 1
        else:
            self._show_monologue_on_photo2 = False
            self._monologue_finished = True
            self._goal_text = "Проверить щиток"
            self._show_goal = True

    def handle_door_locked_click(self) -> None:
        if self._door_locked_index < len(self.texts.door_locked_texts) - 1:
            self._door_locked_index += 1
        else:
            self._show_door_locked = False
            self._door_locked_finished = True
            self._door_checked = True
            self._goal_text = "Найти инфу про дверь"
            self._show_goal = True

    def handle_photo7_click(self, x: float, y: float) -> None:
        if self.click_areas.is_in_area(x, y, "back_from_photo7"):
            self._show_photo7 = False
            self._photo7_visited = True
            if self._photo7_text_index == len(self.texts.door_info_texts) - 1:
                self._door_info_found = True
                self._goal_text = "найти инфу про препараты"
            self.current_photo = self.photo_manager._photos["photo9"]
            self._current_state = "photo9"
            self._show_photo9 = True
            return
        if self._photo7_visited:
            text_list: list = self.texts.photo7_repeat_texts
        else:
            text_list: list = self.texts.door_info_texts
        if self._photo7_text_index < len(text_list) - 1:
            self._photo7_text_index += 1

    def handle_photo8_click(self, x: float, y: float) -> None:
        if self.click_areas.is_in_area(x, y, "back_from_photo8"):
            self._show_photo8 = False
            self.current_photo = self.photo_manager._photos["photo9"]
            self._current_state = "photo9"
            self._show_photo9 = True
            return
        if self.click_areas.is_in_area(x, y, "photo8_to_photo1"):
            self._show_photo8 = False
            self.current_photo = self.photo_manager._photos["photo1"]
            self._current_state = "photo1"
            self._show_goal = False
            return

        if self._photo8_visited:
            if self._photo8_text_index < len(self.texts.photo8_repeat_texts) - 1:
                self._photo8_text_index += 1
            else:
                self._show_photo8 = False
                self.current_photo = self.photo_manager._photos["photo2"]
                self._current_state = "photo2"
        else:
            if self._photo8_text_index < len(self.texts.photo8_texts) - 1:
                self._photo8_text_index += 1
            else:
                self._photo8_visited = True
                self._meds_info_found = True
                self._goal_text = "Взять препарат и ввести в тело"
                self._show_goal = True
                self._show_photo8 = False
                self.current_photo = self.photo_manager._photos["photo2"]
                self._current_state = "photo2"

    def handle_photo9_click(self, x: float, y: float) -> None:
        if (self._goal_text == "Найти инфу про дверь" and
                self.click_areas.is_in_area(x, y, "photo9_to_photo8")):
            return

        if self.click_areas.is_in_area(x, y, "photo9_to_photo7"):
            self._show_photo9 = False
            self.current_photo = self.photo_manager._photos["photo7"]
            self._current_state = "photo7"
            self._show_photo7 = True
            self._photo7_text_index = 0
            return
        if self.click_areas.is_in_area(x, y, "photo9_to_photo8"):
            self._show_photo9 = False
            self.current_photo = self.photo_manager._photos["photo8"]
            self._current_state = "photo8"
            self._show_photo8 = True
            self._photo8_text_index = 0
            self._show_goal = False
            return
        if self.click_areas.is_in_area(x, y, "back_from_photo9"):
            self._show_photo9 = False
            self.current_photo = self.photo_manager._photos["photo3"]
            self._current_state = "photo3"
            if self._door_info_found:
                self._goal_text = "найти инфу про препараты"
            self._show_goal = True
            return

    def handle_photo3_click(self, x: float, y: float) -> None:
        if (self._goal_text == "Найти инфу про дверь" or
                self._goal_text == "найти инфу про препараты"):
            if self.click_areas.is_in_area(x, y, "door_info_folder"):
                self.current_photo = self.photo_manager._photos["photo9"]
                self._current_state = "photo9"
                self._show_photo9 = True
                self._show_goal = False
                return
        if (self._report_available and
                self.click_areas.is_in_area(x, y, "report_area")):
            self.current_photo = self.photo_manager._photos["photo6"]
            self._current_state = "report"
            self._show_goal = False
            self._current_report_texts = []
        elif self.click_areas.is_in_area(x, y, "back_from_computer"):
            self.current_photo = self.photo_manager._photos["photo2"]
            self._current_state = "photo2"
            if self._came_from_photo6 and not self._black_screen_shown:
                self._show_black_screen = True
                arcade.set_background_color(arcade.color.BLACK)
                self._show_goal = False
                self._came_from_photo6 = False
            else:
                if self._goal_text:
                    self._show_goal = True


if __name__ == "__main__":
    game: PhotoGame = PhotoGame()
    arcade.run()