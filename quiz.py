import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from random import randint

from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '650')
Config.write()

global questions
global answer_given_yet
global right

def get_x(n):
    if n != 6: return randint(0, n/6 - 1) * 6
    else: return 0

class Quiz(App):
    def build(self):
        return Front()

class Front(Widget):

    question_label = ObjectProperty(None)
    a_answer_label = ObjectProperty(None)
    b_answer_label = ObjectProperty(None)
    c_answer_label = ObjectProperty(None)
    d_answer_label = ObjectProperty(None)
    answer_tip_label = ObjectProperty(None)
    btn_a = ObjectProperty(None)
    btn_b = ObjectProperty(None)
    btn_c = ObjectProperty(None)
    btn_d = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Front, self).__init__(**kwargs)
        
        global answer_given_yet
        global questions
        global right

        answer_given_yet = False

        questions = open("questions.txt").readlines()

        x = get_x(len(questions))

        self.question_label.text = questions[x].replace("\n","")
        self.a_answer_label.text = "a)" + questions[x+1].replace("\n","")
        self.b_answer_label.text = "b)" + questions[x+2].replace("\n","")
        self.c_answer_label.text = "c)" + questions[x+3].replace("\n","")
        self.d_answer_label.text = "d)" + questions[x+4].replace("\n","")
        self.answer_tip_label.text = ""
        right = questions[x+5].replace("\n","")

    def btn_a_pressed(self):
        global answer_given_yet
        global questions

        if not answer_given_yet:
            answer_given_yet = True
            if right == 'a': 
                self.btn_a.background_color = 0,1,0,1
                self.answer_tip_label.text = "Right!"
                self.answer_tip_label.color = 0,1,0,1
            else: 
                self.btn_a.background_color = 0,0.2,0.8,1
                self.answer_tip_label.text = "Wrong!"
                self.answer_tip_label.color = 1,0,0,1

    def btn_b_pressed(self):
        global answer_given_yet
        global questions

        if not answer_given_yet:
            answer_given_yet = True
            if right == 'b': 
                self.btn_b.background_color = 0,1,0,1
                self.answer_tip_label.text = "Right!"
                self.answer_tip_label.color = 0,1,0,1
            else: 
                self.btn_b.background_color = 0,0.2,0.8,1
                self.answer_tip_label.text = "Wrong!"
                self.answer_tip_label.color = 1,0,0,1

    def btn_c_pressed(self):
        global answer_given_yet
        global questions

        if not answer_given_yet:
            answer_given_yet = True
            if right == 'c': 
                self.btn_c.background_color = 0,1,0,1
                self.answer_tip_label.text = "Right!"
                self.answer_tip_label.color = 0,1,0,1
            else: 
                self.btn_c.background_color = 0,0.2,0.8,1
                self.answer_tip_label.text = "Wrong!"
                self.answer_tip_label.color = 1,0,0,1

    def btn_d_pressed(self):
        global answer_given_yet
        global questions

        if not answer_given_yet:
            answer_given_yet = True
            if right == 'd': 
                self.btn_d.background_color = 0,1,0,1
                self.answer_tip_label.text = "Right!"
                self.answer_tip_label.color = 0,1,0,1
            else: 
                self.btn_d.background_color = 0,0.2,0.8,1
                self.answer_tip_label.text = "Wrong!"
                self.answer_tip_label.color = 1,0,0,1

    def btn_next_pressed(self):
        global answer_given_yet
        global questions
        global right

        questions = open("questions.txt").readlines()

        x = get_x(len(questions))

        self.question_label.text = questions[x].replace("\n","")
        self.a_answer_label.text = "a)" + questions[x+1].replace("\n","")
        self.b_answer_label.text = "b)" + questions[x+2].replace("\n","")
        self.c_answer_label.text = "c)" + questions[x+3].replace("\n","")
        self.d_answer_label.text = "d)" + questions[x+4].replace("\n","")
        self.answer_tip_label.text = ""
        right = questions[x+5].replace("\n","")

        answer_given_yet = False

        self.btn_a.background_color = 1,0,0.2,1
        self.btn_b.background_color = 1,0,0.2,1
        self.btn_c.background_color = 1,0,0.2,1
        self.btn_d.background_color = 1,0,0.2,1

if __name__ == "__main__":
    Quiz().run()