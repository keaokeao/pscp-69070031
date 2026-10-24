"""AMOGUS"""
import json
alive = {}
dead = {}
is_voting = False
while True:
    line = input().strip()
    if line == "Start":
        is_voting = True
        continue
    if line == "End":
        break
    if not is_voting:
        player_data = json.loads(line)
        alive.update(player_data)
    else:
        name = line
        if name in alive:
            dead[name] = alive.pop(name)
impostor_remains = list(alive.values()).count("Impostor")
print(f"{impostor_remains} Impostor Remains")
print("***Alive***")
for name in sorted(alive.keys()):
    print(f"{name} : {alive[name]}")
print("***Dead***")
for name in sorted(dead.keys()):
    print(f"{name} : {dead[name]}")
