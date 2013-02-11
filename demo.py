import json
import pyttsx
from jinja2 import Environment, PackageLoader
from poetry.one import One
from poetry.util.chooser import ExhaustiveChooser

# Configure Jinja2
env = Environment(loader=PackageLoader('poetry', 'templates'))
template = env.get_template('plain.jinja2')

# Configure pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 175)

# Configure One
configs = [
    ("resources/pastoral.json", "com.apple.speech.synthesis.voice.Alex"),
    ("resources/mechanical.json", "com.apple.speech.synthesis.voice.Vicki"),
    ("resources/interstellar.json", "com.apple.speech.synthesis.voice.Victoria")
]

for config in configs:
    poem = One(ExhaustiveChooser(), json.loads(open(config[0]).read()))
    stanzas = list(poem.generate_stanzas())
    engine.setProperty('voice', config[1])
    print(template.render({'poem': stanzas, 'title': None}))
    print("Wordhoard: " + config[0])
    print("Read by: " + config[1])
    engine.say(reduce(lambda x,y: x + "\n\n" + "\n".join(y), stanzas, ""))
    engine.runAndWait()
