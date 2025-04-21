import random

# Diccionario de aminoácido (1 letra) a posibles codones de ARN
aminoacido_to_codones = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAU', 'AAC'],
    'D': ['GAU', 'GAC'],
    'C': ['UGU', 'UGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'K': ['AAA', 'AAG'],
    'M': ['AUG'],  # Solo tiene un codón
    'F': ['UUU', 'UUC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG']
}

# Lista de codones STOP posibles (elegimos uno al azar al final)
stop_codones = ['UAA', 'UAG', 'UGA']

def traducir_peptido_a_arn(peptido):
    arn_codificante = ['AUG']  # Codón de inicio
    for aa in peptido:
        codones = aminoacido_to_codones.get(aa.upper())
        if codones:
            arn_codificante.append(random.choice(codones))  # Elijo un codón aleatorio
        else:
            print(f"⚠️ Aminoácido no reconocido: '{aa}' → se insertará '???'")
            arn_codificante.append('???')
    arn_codificante.append(random.choice(stop_codones))  # Codón de STOP
    return ''.join(arn_codificante)

# Uso
secuencia_peptido = 'ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'
arn_resultante = traducir_peptido_a_arn(secuencia_peptido)

print("Cadena de ARN codificante generada:")
print(arn_resultante)
