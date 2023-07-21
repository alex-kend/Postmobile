import math
from datetime import *
from kivy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class Menu(Screen):
    def goal(self):

        P_max_pad_1 = int(self.ids.min.text)
        P_max_pad = math.ceil(P_max_pad_1 / 3)

        P_k_vih = (P_max_pad_1 - P_max_pad)

        Delt_t = math.floor(P_max_pad * 6.8 / 45)

        hour = int(self.ids.hour.text)
        minut = int(self.ids.minut.text)
        timeobj = timedelta(hours=int(hour), minutes=int(minut))
        timeobj_2 = timedelta(hours=int(0), minutes=int(Delt_t))
        timeobj_3 = timeobj + timeobj_2
        time_vkl = timedelta(hours=int(hour), minutes=int(minut))

        t_ob = math.floor(P_max_pad_1 * 6.8 / 45)

        t_ob_m = timedelta(hours=int(0), minutes=int(t_ob))
        t_ras = timeobj + t_ob_m

        self.ids.goals1.text = f"Максимально допустимое падение давления в СИЗОД с момента включения " \
                              f"до момента окончания работ (P max. pad): {P_max_pad}"
        self.ids.goals2.text = f"Контрольное давление, при котором звену необходимо возвращаться " \
                               f"из НДС (Pк. вых): {P_k_vih}"
        self.ids.goals3.text = f"Промежуток времени с момента включения в СИЗОД до команды на возвращение," \
                               f" мин (дельта Т): {Delt_t}"
        self.ids.goals4.text = f"Время подачи команды постовым на ПБ ГДЗС на возвращение звена " \
                               f"ГДЗС, час. мин (Т вых.): {timeobj_3}"
        self.ids.goals5.text = f"Общее примерное время работы (Т общ.): {t_ob}"
        self.ids.goals6.text = f"Расчетное время возвращения звена ГДЗС из НДС (Т возвр.): {t_ras}"


class Test1(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('vid.kv')


class FirstApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    FirstApp().run()


