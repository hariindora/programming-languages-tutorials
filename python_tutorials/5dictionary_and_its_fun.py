d1 = {}
print(type(d1))

d2 = {"hari":"human", "vibhor":"kala kutta", "aaditya":"kutte ka baccha", "bhagwan jetwani":"snake"}
print(d2["hari"])

d2["kapil"] = "jukfood"
d2["rohan"] = "kebabs"
d2.update({"keshav":"murga"})
print(d2)
print(d2.keys())
print(d2.items())

d3 = d2

del d3["kapil"]
print(d2)

d4 = d2.copy()
del d4["hari"]
print(d4)
print(d2)

d3 = {"hari": {"breakfast":"burger", "lunch":"roti", "dinner":"rice"}, "vibhor": {"breakfast":"tos", "lunch":"calcium bone", "dinner":"none"}}
print(d3["hari"])