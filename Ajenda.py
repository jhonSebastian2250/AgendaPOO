class Ajenda:
    listaContactos = []

    def guardar(self, contacto, contactoModificado=None):
        """
        Guardar Contacto

        :param contacto: Datos del nuevo contacto
        :param contactoModificado: Contacto con los datos modificados
        """

        if contactoModificado is None:  # Si la accion es guardar el contacto
            self.listaContactos.append(contacto.nombre + '^' + contacto.apellido + '^' +
                                       contacto.telefono + '^' + contacto.correo)  # Agrega el nuevo contacto a la lista

            self.escribirContacto()  # Escribe los contactos en un archivo

        if contactoModificado is not None:  # Si la accion es modificar el contacto
            self.modificar(contacto, contactoModificado)

    def modificar(self, contacto, contactoModificado):
        """
        Modificar Contacto

        :param contacto: Datos del contacto seleccionado para modificar
        :param contactoModificado: Contacto con los datos modificados
        """

        for i in range(len(self.listaContactos)):
            """conExistente es una lista con los datos del contacto, Nombre, Apellido, Correo, Telefono
            el metodo split divide una cadena de caracteres en una lista, teniendo en cuenta el separador, en este caso 
            el simbolo ^"""
            conExistente = self.listaContactos[i].split('^')
            if contacto == conExistente:  # Identifica el indice del contacto que se quiere modificar
                self.listaContactos[i] = contactoModificado[0] + '^' + contactoModificado[1] + '^' + contactoModificado[
                    2] + '^' + contactoModificado[3]
                self.escribirContacto()  # Escribe los contactos en un archivo
                break

    def eliminar(self, contacto):
        """
        Eliminar contacto

        :param contacto: list [] Contacto a eliminar
        """
        for con in self.listaContactos:
            """conExistente es una lista con los datos del contacto, Nombre, Apellido, Correo y Telefono. El metodo 
            split divide una cadena de caracteres en una lista, teniendo en cuenta el separador, en este caso el signo 
            de ^ """
            conExistente = con.split('^')

            if contacto == conExistente:  # Identifica el contacto que se quiere eliminar
                self.listaContactos.remove(con)  # Remueve el contacto

                self.escribirContacto()  # Escribe los contactos en un archivo
                break

    def buscar(self, caracteres):
        """
        Buscar Contacto

        Busca contactos que coincida con los caracteres ingresados

        :param caracteres: caracteres que se comparan con el nombre de cada contacto

        :return: Lista de contactos encontrados
        """
        contactosEncontrados = []  # Almacena los contactos encontrados
        for contacto in self.listaContactos:
            conExistente = contacto.split('^')
            #if caracteres.upper() in conExistente[0] or caracteres.lower() in conExistente[0]:
            if caracteres.capitalize() in conExistente[0]:
                contactosEncontrados.append(conExistente)
        return contactosEncontrados

    def iniciarArchivo(self):
        """
        Inicializar archivo

        crea un archivo contactos.txt donde se almacenaran los contactos
        """
        baseContactos = open("contactos.txt", "a")
        baseContactos.close()  # Cierra el archivo

    def cargar(self):
        """
        Cargar contactos

        Carga todos los contactos que tenga el archivo contactos.txt y los almacena en la lista listaContactos
        """

        baseContactos = open("contactos.txt", "r")  # Abre el archivo contactos.txt en el modo solo lectura
        linea = baseContactos.readline()

        if linea:  # Si el archivo contactos.txt tiene al menos un contacto
            while linea:  # siempre y cuando exista una linea (contractos)
                if linea[-1] == "\n":  # Si es el final de la linea
                    linea = linea[:-1]  # Selecciona todo menos el enter
                    self.listaContactos.append(linea)  # Agrega cada contacto a la listaContactos
                    linea = baseContactos.readline()  # indica a la siguiente linea del archivo contactos.txt
        baseContactos.close()  # Cierra el archivo

    def escribirContacto(self):
        """
        Escribir Contacto

        Escribe cada uno de los contactos que se encuentran en listaContactos en el archivo contactos.txt
        """

        contactos = open("contactos.txt", "w")  # Abre el archivo en modo escritura
        self.listaContactos.sort()  # Ordena los contactos

        for contacto in self.listaContactos:
            contactos.write(contacto + "\n")  # Escribe en el archivo contactos.txt
        contactos.close()  # Cierra el archivo
