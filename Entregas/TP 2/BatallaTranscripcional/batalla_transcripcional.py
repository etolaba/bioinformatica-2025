
import random

# Estados iniciales de los jugadores
jugadores = {
    "A": {
        "gen": "ATGGCTAACGTTAGATGGCTA",
        "arn": "",
        "prot": [],
        "errores": [],
        "energia": 5,
        "turnos_bloqueado": 0
    },
    "B": {
        "gen": "ATGGCTAACGTTAGATGGCTA",
        "arn": "",
        "prot": [],
        "errores": [],
        "energia": 5,
        "turnos_bloqueado": 0
    }
}

# Codigo genetico simplificado
codones = {
    # Fenilalanina
    'UUU': 'F', 'UUC': 'F',
    # Leucina
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucina
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    # Metionina (Inicio)
    'AUG': 'M',
    # Valina
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serina
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    # Prolina
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Treonina
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanina
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tirosina
    'UAU': 'Y', 'UAC': 'Y',
    # Histidina
    'CAU': 'H', 'CAC': 'H',
    # Glutamina
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagina
    'AAU': 'N', 'AAC': 'N',
    # Lisina
    'AAA': 'K', 'AAG': 'K',
    # Ácido aspártico
    'GAU': 'D', 'GAC': 'D',
    # Ácido glutámico
    'GAA': 'E', 'GAG': 'E',
    # Cisteína
    'UGU': 'C', 'UGC': 'C',
    # Triptófano
    'UGG': 'W',
    # Arginina
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glicina
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    # STOP codones
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
}


def transcribir_adn_fragmento(adn, avance):
    fragmento = adn[:avance].replace('T', 'U')
    return fragmento, adn[avance:]

def traducir_codon(arn):
    if len(arn) < 3:
        return None, arn
    codon = arn[:3]
    aa = codones.get(codon, '?')
    if aa == 'STOP':
        return None, arn[3:]
    return aa, arn[3:]

acciones = ["tr", "td", "mt", "rp", "rf", "br"]

def mostrar_estado():
    print("\n========================================")
    print("ESTADO DEL JUEGO")
    for j in jugadores:
        prot_visual = '-'.join(jugadores[j]['prot'] + ['_'] * (7 - len(jugadores[j]['prot'])))
        print(f"Jugador {j}")
        print(f"  ARN parcial: {jugadores[j]['arn']}")
        print(f"  Proteina   : [{prot_visual}] ({len(jugadores[j]['prot'])}/7 aminoacidos)")
        print(f"  Energia    : {jugadores[j]['energia']}")
        print(f"  Errores    : {jugadores[j]['errores']}")
        print(f"  Bloqueado  : {jugadores[j]['turnos_bloqueado']} turno(s)")
        print("----------------------------------------")

turno = 0
avance_transcripcion = 9

while True:
    mostrar_estado()
    jugador = "A" if turno % 2 == 0 else "B"
    rival = "B" if jugador == "A" else "A"

    if jugadores[jugador]['turnos_bloqueado'] > 0:
        print(f"\n--- Turno de Jugador {jugador}: BLOQUEADO ---\n")
        jugadores[jugador]['turnos_bloqueado'] -= 1
        turno += 1
        continue

    if len(jugadores[jugador]['arn']) < 3 and not jugadores[jugador]['gen']:
        print("\n========================================")
        print(f"El Jugador {jugador} no puede completar su proteina (sin ADN ni suficiente ARN).")
        print(f"El Jugador {rival} gana la partida!")
        print("========================================\n")
        break

    print(f"\n=== Turno de Jugador {jugador} ===")
    print("Acciones disponibles: tr (Transcribir), td (Traducir), mt (Mutar), rp (Reparar), rf (Reforzar promotor), br (Bloquear)")

    accion = ""
    while accion not in acciones:
        accion = input("> ").strip().lower()
        if accion not in acciones:
            print("Accion no valida. Por favor ingresa una accion correcta.")


    if accion == "tr":
        if jugadores[jugador]['gen']:
            fragmento, restante = transcribir_adn_fragmento(jugadores[jugador]['gen'], avance_transcripcion)
            jugadores[jugador]['arn'] += fragmento
            jugadores[jugador]['gen'] = restante
            print("Fragmento de ADN transcripto a ARN.")
        else:
            print("No queda ADN para transcribir.")

    elif accion == "td":
        if jugadores[jugador]['errores']:
            print("No podes traducir: tu ADN esta dañado. Debes reparar las mutaciones primero.")
        elif len(jugadores[jugador]['arn']) >= 3:
            aa, restante_arn = traducir_codon(jugadores[jugador]['arn'])
            jugadores[jugador]['arn'] = restante_arn
            if aa:
                jugadores[jugador]['prot'].append(aa)
                print(f"Se tradujo un aminoacido: {aa}")
            else:
                print("Codon de STOP encontrado o codon invalido.")
        else:
            print("No hay ARN suficiente para traducir (se necesitan al menos 3 bases).")


    elif accion == "mt":
        if jugadores[jugador]['energia'] >= 2:
            if jugadores[rival]['gen']:
                pos = random.randint(0, len(jugadores[rival]['gen']) - 1)
                jugadores[rival]['errores'].append(pos)
                jugadores[jugador]['energia'] -= 2
                print(f"Mutacion insertada en el gen del jugador {rival} en la posicion {pos}.")
            else:
                print("El rival ya termino de transcribir todo su ADN.")
        else:
            print("No tenes suficiente energia.")

    elif accion == "rp":
        if jugadores[jugador]['energia'] >= 2 and jugadores[jugador]['errores']:
            pos = jugadores[jugador]['errores'].pop()
            jugadores[jugador]['energia'] -= 2
            print(f"Reparaste una mutacion en la posicion {pos}.")
        else:
            print("No hay mutaciones para reparar o no tenes energia.")

    elif accion == "rf":
        jugadores[jugador]['energia'] += 1
        print("Ganaste 1 punto de energia adicional.")

    elif accion == "br":
        if jugadores[jugador]['energia'] >= 3:
            jugadores[rival]['turnos_bloqueado'] = 1
            jugadores[jugador]['energia'] -= 3
            print(f"Bloqueaste la traduccion del jugador {rival} por 1 turno.")
        else:
            print("No tenes suficiente energia.")

    else:
        print("Accion no valida.")
        continue

    if len(jugadores[jugador]['prot']) >= 7:
        print("\n========================================")
        print(f"FELICITACIONES: El Jugador {jugador} completo una proteina funcional y gana el juego!")
        print("========================================\n")
        break

    turno += 1
