# This is a voice-output interface for CleverBot, a chatbot.
# Needs python3, cleverwrap and flite chattyto run
# python should be present in a unix terminal
#
# pip install cleverwrap
# sudo apt-get install flite
#
# Usage:
# python chatBot.py
# then just type after the > prompt
# to leave, type > I'm leaving
# add some CHT support and make two bot chat each other. 
# 2019 NTHU classroom example in Taiwan. merry xMas~

from cleverwrap import CleverWrap
from googletrans import Translator
translator = Translator()
chatBot1 = CleverWrap("CC6zkRgO9TPlPcz6AO_zLCunNBg")
chatBot2 = CleverWrap("CC6zkRgO9TPlPcz6AO_zLCunNBg")
import subprocess
import sys

shell = True
#chatBot.reset()

def speak(this):
    print('- '+str(this))
    subprocess.run(['say', str(this)])

speak('I\'m listening')
var1_CH = input('> ')
var1_EN=translator.translate(var1_CH,dest='en', src='auto')
print (var1_CH,' = ',var1_EN.text) 
chatting = True
while chatting == True:
        if(var1_EN == 'I\'m leaving'):
            chatting = False
            break
        reply1_EN = chatBot1.say(str(var1_EN))
        reply1_CH=translator.translate(reply1_EN,dest='zh-tw', src='en')
        # reply1_CH=reply1_CH.split("=", 1)
        print (reply1_CH.text,' = ',reply1_EN) 
        subprocess.run(['say', str(reply1_CH.text)])
        # speak(reply1_CH)
        reply2_EN = chatBot2.say(str(reply1_EN))
        reply2_CH=translator.translate(reply2_EN,dest='zh-tw', src='en')
        # reply2_CH=reply2_CH.split("=", 1)
        print (reply2_CH.text,' = ',reply2_EN) 
        subprocess.run(['say', str(reply2_CH.text)])
        # speak(reply2_CH)

        var1_EN = reply2_EN

speak("Fine, leave. See if I care.")
