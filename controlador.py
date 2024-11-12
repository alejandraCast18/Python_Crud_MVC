from basedatos import Basedatos

class Controlador():
    def __init__(self, basedatos):
        self.basedatos = basedatos

    def insertar(self, id, name, phone):
        result = self.basedatos.Insert(id, name, phone)
        return result

    def eliminar(self, id):
        result = self.basedatos.Delete(id)
        return result

    def actualizar(self, id, name, phone):
        result = self.basedatos.Update(id, name, phone)
        return result

    def consultar(self, id):
        info = self.basedatos.Select(id)
        return info