class Bird(object):
    have_feather = True
    way_of_reproduction = "egg"
    def move(self,dx,dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
        
class Chicken(Bird):
    way_of_reproduction = 'walk'
    possible_in_kfc = True

class Oriole(Bird):
    way_of_reproduction = 'fly'
    possible_in_kfc = False

qike = Chicken()
print(qike.possible_in_kfc)
print(qike.move(10,3))
