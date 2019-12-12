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


from cleverwrap import CleverWrap
chatBot = CleverWrap("CC6zkRgO9TPlPcz6AO_zLCunNBg")
import subprocess
import sys
#hihi
shell = True
#chatBot.reset()

def speak(this):
    print('- '+str(this))
    subprocess.run(['say', str(this)])

speak('I\'m listening')
var = input('> ')

chatting = True
while chatting == True:
        if(var == 'I\'m leaving'):
            chatting = False
            break
        reply = chatBot.say(str(var))
        speak(reply)
        var = input('> ')

speak("Fine, leave. See if I care.")
