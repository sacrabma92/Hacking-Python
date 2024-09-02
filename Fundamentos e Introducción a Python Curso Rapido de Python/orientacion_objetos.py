

class Coche:
  
  # Metodo constructor de la clase
  def __init__(self, vel_max):
    self.max_vel = vel_max

  def velocidad_maxim(self):
    print("Velocidad maxima: ", self.max_vel)



coche1 = Coche(150)

coche1.velocidad_maxim()

# print(type(coche))