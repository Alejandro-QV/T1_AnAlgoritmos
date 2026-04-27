# ---------------- CLASE ----------------
class PuestoTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo


# ---------------- LISTA GLOBAL ----------------
puestos = []


# ---------------- VALIDACIONEs ----------------
def validar_texto(txt):
    return isinstance(txt, str) and len(txt.strip()) >= 3

def validar_num(n):
    return n > 0


# ---------------- ORDENAMIENTOS ----------------

def burbuja_codigo_desc(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].codigo < lista[j + 1].codigo:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def insercion_sueldo_desc(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i - 1
        while j >= 0 and lista[j].sueldo < aux.sueldo:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = aux


def seleccion_total_desc(lista):
    n = len(lista)
    for i in range(n):
        maximo = i
        for j in range(i + 1, n):
            if (lista[j].plazasRequeridas * lista[j].sueldo) > (lista[maximo].plazasRequeridas * lista[maximo].sueldo):
                maximo = j
        lista[i], lista[maximo] = lista[maximo], lista[i]


# ---------------- FUNCIONES MENU ----------------

def AgregarPuesto():
    try:
        codigo = int(input("codigo: "))
        descripcion = input("descripcion: ")
        area = input("area solicitante: ")
        plazas = int(input("plazas: "))
        sueldo = float(input("sueldo: "))

        if not validar_texto(descripcion) or not validar_texto(area):
            print("texto invalido")
            return

        if not validar_num(plazas) or not validar_num(sueldo):
            print("numeros invalidos")
            return

        for p in puestos:
            if p.codigo == codigo or p.descripcion == descripcion or p.areaSolicitante == area:
                print("ya existe el puesto")
                return

        puestos.append(PuestoTrabajo(codigo, descripcion, area, plazas, sueldo))
        print("puesto agregado")

    except:
        print("error en datos")


def MostrarTodo():
    if len(puestos) == 0:
        print("lista vacia")
        return

    for p in puestos:
        print(p.codigo, "-", p.descripcion, "-", p.areaSolicitante, "-", p.plazasRequeridas, "-", p.sueldo)


def BorraPuesto():
    try:
        cod = int(input("codigo a borrar: "))

        burbuja_codigo_desc(puestos)

        i = 0
        while i < len(puestos):
            if puestos[i].codigo == cod:
                del puestos[i]
                print("eliminado")
                return
            i += 1

        print("no encontrado")

    except:
        print("error")


def busqueda_binaria_sueldo(lista, valor):
    izq = 0
    der = len(lista) - 1
    res = []

    while izq <= der:
        mid = (izq + der) // 2

        if lista[mid].sueldo == valor:

            i = mid
            while i >= 0 and lista[i].sueldo == valor:
                res.append(lista[i])
                i -= 1

            i = mid + 1
            while i < len(lista) and lista[i].sueldo == valor:
                res.append(lista[i])
                i += 1

            return res

        elif lista[mid].sueldo < valor:
            der = mid - 1
        else:
            izq = mid + 1

    return res


def BuscarSueldo():
    try:
        valor = float(input("sueldo a buscar: "))

        insercion_sueldo_desc(puestos)

        res = busqueda_binaria_sueldo(puestos, valor)

        if len(res) == 0:
            print("no hay resultados")
            return

        for p in res:
            print(p.codigo, p.descripcion, p.sueldo)

    except:
        print("error")


def PuestosAContratar():
    try:
        dinero = float(input("presupuesto total: "))

        seleccion_total_desc(puestos)

        acum = 0

        for p in puestos:
            total = p.plazasRequeridas * p.sueldo

            if acum + total <= dinero:
                acum += total
                print("contratado:", p.descripcion, total)
            else:
                break

    except:
        print("error")


# ---------------- MENU ----------------

while True:
    print("\nmenu")
    print("1 agregar puesto")
    print("2 mostrar todo")
    print("3 borrar puesto")
    print("4 buscar sueldo")
    print("5 puestos a contratar")
    print("6 salir")

    op = input("opcion: ")

    if op == "1":
        AgregarPuesto()
    elif op == "2":
        MostrarTodo()
    elif op == "3":
        BorraPuesto()
    elif op == "4":
        BuscarSueldo()
    elif op == "5":
        PuestosAContratar()
    elif op == "6":
        break
    else:
        print("opcion invalida")