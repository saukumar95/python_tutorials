# from gtts import gTTS
# import os
import vlc
# mytext = 'Welcome Saurabh Kumar'
#
# # Language in which you want to convert
# language = 'en'
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome1.mp3")

# Playing the converted file
player = vlc.MediaPlayer("/home/banti/PycharmProjects/python_tutorials/welcome1.mp3")
player.play()

