import colorgram

colors = colorgram.extract("image.jpg", 30)

colors_list = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    colors_list.append((r,g,b))

print(colors_list)
