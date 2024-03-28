
class Building:

    total = 0

    def __init__(self):
        self.total += 1

buildings = []
while len(buildings) < 40:
    new_building = Building()
    buildings.append(new_building)
print(buildings)
