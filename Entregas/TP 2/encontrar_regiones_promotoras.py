import re

def cargar_secuencia_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        lineas = f.readlines()
    # Ignoro encabezado tipo FASTA (>) y une líneas
    secuencia = ''.join([linea.strip() for linea in lineas if not linea.startswith('>')])
    return secuencia.upper()

def encontrar_regiones_promotoras(secuencia, motivo='TATAAA'):
    regiones = []
    posiciones = [m.start() for m in re.finditer(f'(?={motivo})', secuencia)]
    
    for i in range(len(posiciones) - 1):
        inicio = posiciones[i]
        fin = posiciones[i + 1] + len(motivo)
        region = secuencia[inicio:fin]
        regiones.append({
            'inicio': inicio,
            'fin': fin,
            'secuencia': region
        })
    
    return regiones

def main():
    archivo = 'secuencia_adn.txt'
    secuencia = cargar_secuencia_desde_archivo(archivo)
    
    regiones = encontrar_regiones_promotoras(secuencia)
    if not regiones:
        print("No se encontraron regiones promotoras.")
    else:
        for idx, r in enumerate(regiones, 1):
            print(f"Región promotora #{idx}")
            print(f"Posición: {r['inicio']} - {r['fin']}")
            print(f"Secuencia: {r['secuencia']}\n")

if __name__ == "__main__":
    main()
