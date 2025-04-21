import random

# Estados iniciales de los jugadores
jugadores = {
    "A": {
        "gen": "ATGGCTAACGTTAG",  # Simulación de gen con codón STOP al final
        "arn": "",
        "prot": "",
        "errores": [],
        "energia": 5,
        "turnos_bloqueado": 0
    },
    "B": {
        "gen": "ATGGCTAACGTTAG",
        "arn": "",
        "prot": "",
        "errores": [],
        "energia": 5,
        "turnos_bloqueado": 0
    }
}

# Código genético simplificado
codones = {
    'AUG': 'M', 'GCU': 'A', 'AAU': 'N', 'GAA': 'E', 'UGA': 'STOP',
    'GCC': 'A', 'UAC': 'Y', 'CGU': 'R', 'UAA': 'STOP', 'UAG': 'STOP'
}

# Transcripción ADN a ARN (simplificada)
def transcribir_adn(adn):
    return adn.replace('T', 'U')

# Traducción simple (3 bases → codón)
def traducir_arn(arn):
    prot = ""
    for i in range(0, len(arn), 3):
        codon = arn[i:i+3]
        if len(codon) < 3:
            break
        aa = codones.get(codon, '?')
        if aa == 'STOP':
            break
        prot += aa
    return prot

# Acciones posibles
acciones = ["transcribir", "traducir", "mutar", "reparar", "reforzar-promotor", "bloquear-ribosoma"]

def mostrar_estado():
    print("\nESTADO ACTUAL")
    for j in jugadores:
        print(f"Jugador {j} | ARN: {jugadores[j]['arn']} | Prot: {jugadores[j]['prot']} | Energía: {jugadores[j]['energia']} | Errores: {jugadores[j]['errores']} | Bloqueado: {jugadores[j]['turnos_bloqueado']}")

# Motor principal
turno = 0
while True:
    mostrar_estado()
    jugador = "A" if turno % 2 == 0 else "B"
    rival = "B" if jugador == "A" else "A"

    if jugadores[jugador]['turnos_bloqueado'] > 0:
        print(f"\nJugador {jugador} está bloqueado este turno!\n")
        jugadores[jugador]['turnos_bloqueado'] -= 1
        turno += 1
        continue

    print(f"\n🎮 Turno de Jugador {jugador}")
    print("Acciones disponibles:", ", ".join(acciones))
    accion = input("> ").strip().lower()

    if accion == "transcribir":
        jugadores[jugador]['arn'] = transcribir_adn(jugadores[jugador]['gen'])
        print("Se transcribió el gen a ARN.")

    elif accion == "traducir":
        if jugadores[jugador]['arn']:
            jugadores[jugador]['prot'] = traducir_arn(jugadores[jugador]['arn'])
            print("Se tradujo el ARN a proteína.")
        else:
            print("Primero necesitás ARN para traducir.")

    elif accion == "mutar":
        if jugadores[jugador]['energia'] >= 2:
            pos = random.randint(0, len(jugadores[rival]['gen']) - 1)
            jugadores[rival]['errores'].append(pos)
            jugadores[jugador]['energia'] -= 2
            print(f"Mutación insertada en el gen del jugador {rival} en la posición {pos}.")
        else:
            print("No tenés suficiente energía.")

    elif accion == "reparar":
        if jugadores[jugador]['energia'] >= 2 and jugadores[jugador]['errores']:
            pos = jugadores[jugador]['errores'].pop()
            jugadores[jugador]['energia'] -= 2
            print(f"Reparaste una mutación en la posición {pos}.")
        else:
            print("No hay mutaciones para reparar o no tenés energía.")

    elif accion == "reforzar-promotor":
        jugadores[jugador]['energia'] += 1
        print("Ganaste 1 punto de energía adicional.")

    elif accion == "bloquear-ribosoma":
        if jugadores[jugador]['energia'] >= 3:
            jugadores[rival]['turnos_bloqueado'] = 1
            jugadores[jugador]['energia'] -= 3
            print(f"Bloqueaste la traducción del jugador {rival} por 1 turno.")
        else:
            print("No tenés suficiente energía.")

    else:
        print("Acción no válida.")
        continue

    # Condición de victoria simple
    if jugadores[jugador]['prot'] and len(jugadores[jugador]['prot']) >= 4:
        print(f"\n🎉 El Jugador {jugador} completó una proteína funcional y gana el juego! 🎉")
        break

    turno += 1
