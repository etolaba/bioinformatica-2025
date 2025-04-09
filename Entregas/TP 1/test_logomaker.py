import logomaker
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

secuencias = [
    "MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV"
]

# Verificar que tienen el mismo largo
assert all(len(seq) == len(secuencias[0]) for seq in secuencias), "Las secuencias deben estar alineadas y tener el mismo largo"

# Construir una lista con la frecuencia de aminoácidos en cada posición
frecuencias = []
for i in range(len(secuencias[0])):
    columna = [seq[i] for seq in secuencias]
    conteo = Counter(columna)
    total = sum(conteo.values())
    frecuencias.append({aa: conteo[aa] / total for aa in conteo})

# Convertir a DataFrame
df = pd.DataFrame(frecuencias).fillna(0)

# Crear el logo
logo = logomaker.Logo(df)

# Guardar como imagen
plt.savefig("secuencia_logo.png")
print("Logo generado como 'secuencia_logo.png'")
