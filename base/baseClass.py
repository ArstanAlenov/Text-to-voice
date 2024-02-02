import gtts
from googletrans import Translator
from tika import parser

pdf = parser.from_file('s.docx')
print(pdf['content'])

tts = gtts.gTTS(pdf['content'], lang = 'ru')
tts.save('audio.mp3')