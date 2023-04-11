import speech_recognition as sr
import platform
import pyttsx3
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.toast import toast

### NLU function(default setting: Google Speech Recognition)###
speech = sr.Recognizer()


def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input


# ----------------------------------------------------------------------------------------------------------------#

corn = {
    '1': "Step one:Choose the Right Seeds. Before you start planting, it's important to choose the right seeds. Look for seeds that are suited to your climate and soil conditions, and that have a high germination rate. You may also want to consider whether you want to plant hybrid or non-hybrid seeds, depending on your preferences and goals.",
    '2': "Step two:Prepare the Soil. Next, you'll need to prepare the soil for planting. This involves tilling the soil to loosen it up and remove any debris, and adding any necessary fertilizers or soil amendments. Make sure the soil is moist but not too wet, as this can affect germination.",
    '3': "Step three:Create Rows. Using a hoe or planting tool, create rows in the soil where you'll be planting the seeds. The rows should be spaced at least 30 inches apart to allow for proper growth.",
    '4': "Step four:Plant the Seeds. Once you've created your rows, it's time to plant the seeds. Place the seeds about 1-2 inches deep in the soil, spacing them about 6 inches apart. Cover the seeds with soil and pat it down lightly to ensure good contact.",
    '5': "Step five: Water and Fertilize.Finally, water the seeds thoroughly to help them germinate, and add any necessary fertilizers or nutrients to the soil. You'll also want to monitor the plants regularly for signs of pests or disease, and take appropriate action if necessary."}

###Dialogue Manager###


class mainApp(MDApp):
    def btn(self):
        return Button(text="Click me!")
    
    def build(self):                                             # Build The GUI
        self.theme_cls.primary_palette="Red"
        box=BoxLayout(orientation="vertical",padding=20,spacing=20,size_hint=(1,.9))
        btn=btn(text="Click me!")
        box.add_widget(btn)
        box.add_widget(Label(text="Hey there"))
        return box
engine = pyttsx3.init()

while True:
    engine.say("welcome to this application")
    engine.say("speak 'plant' for planting seeds instructions,speak 'stop' to quit")
    engine.runAndWait()
    print("speak 'plant' for planting seeds instructions, speak 'stop' to quit")
    inp = voice_to_text()
    print(inp)

    if 'plant' in inp and 'stop' not in inp:
        engine.say("Choose one specific type of seeds, the supported types include corn, tomato")
        engine.runAndWait()
        print('speank one tyue of seeds')
        inp1 = voice_to_text()
        print(inp1)
        if 'corn' in inp1:
            engine.say(
                "Welcome to the latest episode of The Modern Farm Business, where we provide practical advice and instruction for farmers looking to improve their crop production and management. In today's episode, we're going to focus on how to plant corn seeds.")
            
            engine.say(corn['1'])
            engine.runAndWait()
            count = 1
            steps = len(corn)
            while True:
                engine.say(
                    f'To hear the next step, say continue. To hear this step again, say repeat, to hear the previous step, say return. To finish listening corn instructions, say finish')
                engine.runAndWait()
                print("continue,repeat,return,or finish")
                inp2 = voice_to_text()
                if 'continue' in inp2:
                    count += 1
                    if count > step:
                        engine.say("This is the last step, you cannot continue. ")
                        count -=1
                        continue
                    engine.say(corn[str(count)])
                    engine.runAndWait()
                    continue
                elif 'repeat' in inp2:
                    engine.say(corn[str(count)])
                    engine.runAndWait()
                    continue
                elif 'return' in inp2:
                    if count == 1:
                        engine.say('this is the first step, you cannot return anymore')
                        engine.runAndWait()
                        continue
                    else:
                        count -= 1
                        engine.say(corn[str(count)])
                        engine.runAndWait()
                        continue

                elif 'finish' in inp2:
                    break

    elif 'stop' in inp and 'plant' not in inp:
        print(f'You just said stop, goodbye!')

        engine.say(f'You just said stop, goodbye!')
        engine.runAndWait()

        break

    elif 'stop' in inp and 'plant' in inp:
        engine.say('You gave mutiple instructions, please say one insturction at one time')
        engine.runAndWait()
        continue
    # potential elif loop could be added there based on the desired functions
