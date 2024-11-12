import tkinter as tk
import tkinter.messagebox as MessageBox

class Vista(tk.Frame):
    def __init__(self, root):
        super().__init__(root) 
        self.root = root
        self.root.geometry("500x300")
        self.root.title("CRUD con MySQL")
        self.root.configure(bg="#f2f3f4") 
        

        self.id = tk.Label(self.root, text="Ingrese ID:", font=("verdana", 15), bg="#f2f3f4", fg="#131921")
        self.id.place(x=50, y=30)
        self.id_entry = tk.Entry(self.root, font=("verdana", 15), bg="#ffffff", fg="#333333")
        self.id_entry.place(x=170, y=30)
        self.id_entry.focus_set()

        self.name = tk.Label(self.root, text="Nombre:", font=("verdana", 15), bg="#f2f3f4", fg="#131921")
        self.name.place(x=50, y=80)
        self.name_entry = tk.Entry(self.root, font=("verdana", 15), bg="#ffffff", fg="#333333")
        self.name_entry.place(x=150, y=80)

       
        vcmd = (self.register(self.on_validate), '%P', '11')
        self.phone = tk.Label(self.root, text="Teléfono:", font=("verdana", 15), bg="#f2f3f4", fg="#131921")
        self.phone.place(x=50, y=130)
        self.phone_entry = tk.Entry(self.root, validate='key', validatecommand=vcmd, font=("verdana", 15), bg="#ffffff", fg="#333333")
        self.phone_entry.place(x=150, y=130)
        self.phone_entry.bind('<KeyRelease>', lambda e: self.verificar())

        # Botones estilo Amazon
        self.btnInsert = tk.Button(self.root, text="Insertar", command=lambda:self.click_insertar(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get()), font=("verdana", 15), bg="#FF9900", fg="#ffffff", activebackground="#FFB84D", activeforeground="#ffffff")
        self.btnInsert.place(x=100, y=190)

        self.btnDelete = tk.Button(self.root, text="Eliminar", command=lambda:self.click_eliminar(self.id_entry.get()), font=("verdana", 15), bg="#232f3e", fg="#ffffff", activebackground="#4a5d73", activeforeground="#ffffff")
        self.btnDelete.place(x=210, y=190)

        self.btnUpdate = tk.Button(self.root, text="Actualizar", command=lambda:self.click_actualizar(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get()), font=("verdana", 15), bg="#232f3e", fg="#ffffff", activebackground="#4a5d73", activeforeground="#ffffff")
        self.btnUpdate.place(x=320, y=190)

        self.btnSelect = tk.Button(self.root, text="Consultar", command=lambda:self.click_consultar(self.id_entry.get()), font=("verdana", 15), bg="#FF9900", fg="#ffffff", activebackground="#FFB84D", activeforeground="#ffffff")
        self.btnSelect.place(x=200, y=240)

       
        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador

   
    def click_insertar(self, id, name, phone):
        if id == "" or name == "" or phone == "":
            MessageBox.showerror("ERROR", "Debe ingresar todos los campos")
        else:
            result = self.controlador.insertar(id, name, phone)
            if not(isinstance(result, int)):
                MessageBox.showerror("Error", result)
            else:
                if result > 0:
                    MessageBox.showinfo("Status", "Insertado exitosamente")

    def click_eliminar(self, id):
        if(id == ""):
            MessageBox.showerror("ERROR", "Ingrese el ID para eliminar el registro")
        else:
            if MessageBox.askokcancel("Consulta", "¿Está seguro de eliminar el registro?"):
                result = self.controlador.eliminar(id)
                if result > 0:
                    MessageBox.showinfo("Status", "Eliminado exitosamente")
                    self.id_entry.delete(0, tk.END)
                    self.name_entry.delete(0, tk.END)
                    self.phone_entry.delete(0, tk.END)

    def click_consultar(self, id):
        if id == "":
            MessageBox.showerror("ERROR","Se requiere el ID para ubicar el registro")
        else:
            info = self.controlador.consultar(id)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            if info:
                self.name_entry.insert(0, info[1])
                self.phone_entry.insert(0, info[2])
            else:
                self.name_entry.insert(0, "No encontrado")

    def click_actualizar(self, id, name, phone):
        if name == "" or phone == "":
            MessageBox.showerror("ERROR", "Se requieren los campos a actualizar")
        else:
            result = self.controlador.actualizar(id, name, phone)
            if not(isinstance(result, int)):
                MessageBox.showerror("Error", result)
            else:
                if result > 0:
                    MessageBox.showinfo("Status", "Modificado exitosamente")
                else:
                    MessageBox.showinfo("Status", "Nada que modificar")

  
    def verificar(self):
        codigo = self.phone_entry.get()
        for i in codigo:
            if i not in '0123456789':
                self.phone_entry.delete(codigo.index(i), codigo.index(i)+1)

    def on_validate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True