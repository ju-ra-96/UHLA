import random
random.seed()
directions = ["LEFT", "RIGHT", "BOTH"]
def generate_data():
    return directions[random.randint(0,2)]