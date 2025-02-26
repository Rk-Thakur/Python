import colorgram

rgb_colors = []
colors = colorgram.extract("python_images.jpeg",10)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    

print(f"The RGB Colors are: {rgb_colors}")    