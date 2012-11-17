import json
import random
from poetry.pastoral import Pastoral
p = Pastoral(json.loads(open("resources/pastoral.json").read()))
for i in range(random.randint(2, 4)): print(p)