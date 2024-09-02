class Coche():
  """ Esta clase representa un coche."""
  def __init__(self, modelo, potencia, consumo):
    """ Inicializa los atributos de instancia
    Argumentos posicionales:
    modelo -- String que representa el modelo del coche
    potencia -- int que representa la potencia en cv
    consumo -- int que representa el consumo en litros/100km
    """

    self.modelo = modelo
    self.potencia = potencia
    self.consumo = consumo
    self.km_actuales = 0

  def especificaciones(self):
    """Muestra las espicificaciones del coche."""
    print("Modelo:", self.modelo,
          f"\nPotencia: {self.potencia} cv",
          f"\nConsumo: {self.consumo} l/100km",
          "\nKilometros actuales:",self.km_actuales)
    
  def __str__(self):
    print("Esto es un coche.")
    
  def actualizar_kilometros(self, kilometros):
    """Actualizar los km actuales del coche"""
    if kilometros > self.km_actuales:
      self.km_actuales = kilometros
    else:
      print("ERROR: No se puede establecer un numero de km inferior al actual")

class CocheElectrico(Coche):
  """Esta clase representa un coche electrico"""
  def __init__(self, modelo, potencia, consumo):
    super().__init__(modelo, potencia, consumo)

    def especificaciones(self):
      """Muestra las especificaciones del coche."""
      print("Modelo:", self.modelo,
            f"\nPotencia: {self.potencia} cv",
            f"\nConsumo: {self.consumo} kWh/100km",
            "\nKilometros actuales:",self.km_actuales)


# coche_mercedes = Coche('merceder', 150, 10)
# coche_mercedes.actualizar_kilometros(40000)
# coche_mercedes.especificaciones()

# Muestra los metodos implementados en la clase COche
# print(dir(coche_mercedes))
# print(coche_mercedes.__dict__)

# str(coche_mercedes)

print("######")
coche_tesla = CocheElectrico("tesla", "200", "12")
coche_tesla.especificaciones()