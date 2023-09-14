from googletrans import Translator
trans=Translator()
print("here are the language codes:\n'af: afrikaans'\n'sq: albanian'\n'am: amharic'\n'ar: arabic'\n'hy: armenian'\n'az: azerbaijani'\n'eu: basque'")
print("'be: belarusian'\n'bn: bengali'\n'bs: bosnian'\n'bg: bulgarian'\n'ca: catalan'\n'ceb: cebuano'\n'ny: chichewa'\n'zh-cn: chinese (simplified)'")
print("'zh-tw: chinese (traditional)'\n'co: corsican'\n'hr: croatian'\n'cs: czech'\n'da: danish'\n'nl: dutch'\n'en: english'\n'eo: esperanto'")
print("'et: estonian'\n'tl: filipino'\n'fi: finnish'\n'fr: french'\n'fy: frisian'\n'gl: galician'\n'ka: georgian'\n'de: german'\n'el: greek'\n'gu: gujarati'")
print("'ht: haitian creole'\n'ha: hausa'\n'haw: hawaiian'\n'iw: hebrew'\n'he: hebrew'\n'hi: hindi'\n'hmn: hnmong'\n'hu: hungarian'\n'is: icelandic'")
print("'ig: igbo'\n'id: indonesian'\n'ga: irish'\n'it: italian'\n'ja: japanese'\n'jw: javanese'\n'kn: kannada'\n'kk: kazakh'\n'km: khmer'\n'ko: korean'")
print("'ku: kurdish (kurmanji)'\n'ky: kyrgyz'\n'lo: lao'\n'la: latin'\n'lv: latvian'\n'lt: lithuanian'\n'lb: luxembourgish'\n'mk: macedonian'\n'mg: malagasy'")
print("'ms: malay'\n'ml: malayalam'\n'mt: maltese'\n'mi: maori'\n'mr: marathi'\n'mn: mongolian'\n'my: myanmar (burmese)'\n'ne: nepali'\n'no: norwegian'")
print("'or: odia'\n'ps: pashto'\n'fa: persian'\n'pl: polish'\n'pt: portuguese'\n'pa: punjabi'\n'ro: romanian'\n'ru: russian'\n'sm: samoan'\n'gd: scots gaelic'")
print("'sr: serbian'\n'st: sesotho'\n'sn: shona'\n'sd: sindhi'\n'si: sinhala'\n'sk: slovak'\n'sl: slovenian'\n'so: somali'\n'es: spanish'\n'su: sundanese'")
print("'sw: swahili'\n'sv: swedish'\n'tg: tajik'\n'ta: tamil'\n'te: telugu'\n'th: thai'\n'tr: turkish'\n'uk: ukrainian'\n'ur: urdu'\n'ug: uyghur'\n'uz: uzbek'")
print("'vi: vietnamese'\n'cy: welsh'\n'xh: xhosa'\n'yi: yiddish'\n'yo: yoruba'\n'zu: zulu'")
b=input("please input the language code in which you want your word or sentence to be translated in:-")
d=input("press v for voice to text and any other letter for text to text translation: ")
if(d=='v'):
    print("if you want to translate something by speaking you can only speak in english and translate it into another language")
    import speech_recognition as sr
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("speak anything in english")
        audio = r.listen(source)
    try:
        tex = r.recognize_google(audio)
        a=tex
        print("you said {}".format(tex))
        c = trans.translate(a,dest=b)
        print(c.text)
    except:
        print("sorry we didn't get what you are saying please try again.")   
else:
  a=input("please input the word or sentence you want to translate:-")
  c = trans.translate(a,dest=b) 
  print(c.text)
  