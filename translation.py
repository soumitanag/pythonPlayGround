import googletrans
from googletrans import Translator
# print(googletrans.LANGUAGES)
translator = Translator()
result = translator.translate("how are you?", dest="fr")
print(result.src)
print(result.dest)
# print(result.origin)
print(result.text)
print(result.pronunciation)
