from modelo.actividad import (
    AmpliacionPastizales, ConstruccionRural, ExpansionAgricola,
    ExtraccionIlegal, TalaIndiscriminada,
)
from modelo.autoridad import Autoridad
from modelo.efecto import EfectoAmbiental, TIPOS_EFECTO
from modelo.reporte import ReporteActividad
from modelo.zona import Zona

ACTIVIDADES = {
    "1": ("Tala indiscriminada", TalaIndiscriminada),
    "2": ("Expansión agrícola", ExpansionAgricola),
    "3": ("Ampliación de pastizales", AmpliacionPastizales),
    "4": ("Construcción rural", ConstruccionRural),
    "5": ("Extracción ilegal", ExtraccionIlegal),
}


def crear_datos_demo():
    fusa = Zona("Fusagasugá", 20000)
    norte = Zona("Vereda Norte (ejemplo)", 3000)
    sur = Zona("Vereda Sur (ejemplo)", 2500)
    alto = Zona("Sector Alto (ejemplo)", 800)
    fusa.agregar_subzona(norte)
    fusa.agregar_subzona(sur)
    norte.agregar_subzona(alto)
    norte.registrar_perdida(12.5, "Tala indiscriminada")
    alto.registrar_perdida(3.0, "Expansión agrícola")
    norte.actividades.append(TalaIndiscriminada(12.5))
    alto.actividades.append(ExpansionAgricola(3.0))
    norte.efectos.append(EfectoAmbiental("riesgo de deslizamiento", 4))
    return fusa


def pedir_numero(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        print("Valor numérico no válido.")
        return None


def pedir_zona(raiz):
    nombre = input("Nombre de la zona: ")
    zona = raiz.buscar(nombre)
    if zona is None:
        print("Zona no encontrada.")
    return zona


def mostrar_menu():
    print("\n=== Pérdida de cobertura vegetal en Fusagasugá ===")
    print("1. Registrar reporte          6. Deshacer último registro")
    print("2. Atender reporte            7. Hectáreas perdidas (recursivo)")
    print("3. Ver siguiente reporte      8. Contar actividades (recursivo)")
    print("4. Registrar pérdida          9. Resumen de zonas")
    print("5. Ver último registro        10. Registrar actividad / efecto")
    print("0. Salir")


def main():
    raiz = crear_datos_demo()
    autoridad = Autoridad("Autoridad ambiental")
    autoridad.vigilar(raiz)
    contador = 0

    while True:
        mostrar_menu()
        op = input("Opción: ").strip()

        if op == "1":
            contador += 1
            try:
                autoridad.recibir_reporte(ReporteActividad(contador, input("Descripción: ")))
                print(f"Reporte registrado. Pendientes: {autoridad.pendientes()}")
            except ValueError as e:
                contador -= 1
                print(f"Error: {e}")
        elif op == "2":
            r = autoridad.atender_reporte()
            print(f"Atendido: {r}" if r else "No hay reportes pendientes.")
        elif op == "3":
            r = autoridad.siguiente_reporte()
            print(f"Siguiente: {r} (pendientes: {autoridad.pendientes()})" if r
                  else "No hay reportes pendientes.")
        elif op == "4":
            zona = pedir_zona(raiz)
            ha = pedir_numero("Hectáreas perdidas: ") if zona else None
            if ha is not None:
                try:
                    zona.registrar_perdida(ha, input("Motivo: "))
                    print("Pérdida registrada.")
                except ValueError as e:
                    print(f"Error: {e}")
        elif op == "5":
            zona = pedir_zona(raiz)
            if zona:
                ultimo = zona.historial.ultimo()
                print(f"Último registro: {ultimo}" if ultimo else "No hay registros.")
        elif op == "6":
            zona = pedir_zona(raiz)
            if zona:
                eliminado = zona.historial.deshacer()
                print(f"Eliminado: {eliminado}" if eliminado else "No hay registros para deshacer.")
        elif op == "7":
            zona = pedir_zona(raiz)
            if zona:
                print(f"{zona.nombre}: {zona.hectareas_perdidas_total()} ha perdidas en total")
        elif op == "8":
            zona = pedir_zona(raiz)
            if zona:
                print(f"Actividades: {zona.contar_actividades()} "
                      f"(ilegales: {zona.contar_actividades(solo_ilegales=True)})")
        elif op == "9":
            print(raiz.resumen())
        elif op == "10":
            zona = pedir_zona(raiz)
            if zona:
                print("Actividades:", ", ".join(f"{k}={v[0]}" for k, v in ACTIVIDADES.items()))
                tipo = input("Tipo (1-5) o Enter para registrar un efecto: ").strip()
                try:
                    if tipo in ACTIVIDADES:
                        ha = pedir_numero("Intensidad (ha): ")
                        if ha is not None:
                            zona.actividades.append(ACTIVIDADES[tipo][1](ha))
                            print("Actividad registrada.")
                    else:
                        for i, t in enumerate(TIPOS_EFECTO, 1):
                            print(f"{i}. {t}")
                        idx = int(input("Efecto (número): ")) - 1
                        grav = int(input("Gravedad (1-5): "))
                        zona.efectos.append(EfectoAmbiental(TIPOS_EFECTO[idx], grav))
                        print("Efecto registrado.")
                except (ValueError, IndexError) as e:
                    print(f"Error: {e}")
        elif op == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
