# Tire Height Calculator
def tire_height(width, height, rim):
    th = (((width/25.4) * height * 2) + rim)
    print(th)

tire_height(265, .40, 22)
