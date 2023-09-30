games={"call of duty":9700,"free fire":10200,"asphalt9":8000,"anger of stick":15000}
# print(games)
print(games["free fire"])
asphalt9=games.get("asphalt9")
# print(asphalt9)
games["anger of stick"]=200
# print(games)
# games.pop("anger of stick")
del games ["asphalt9"]
# print(games)
# getting keys and values
# for key in games:
#     print(key,games[key])

games_key=games.keys()
print(games_key)

games_value=games.values()
print(games_value)