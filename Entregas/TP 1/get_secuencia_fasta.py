import requests
import re

def obtener_secuencia_fasta(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        fasta = response.text

        secuencia = ''.join(fasta.split('\n')[1:])
        return secuencia
    else:
        print(f"Error al obtener {uniprot_id}")
        return None

def buscar_motivo(secuencia):
    patron = re.compile(r'N[^P][ST][^P]')
    return [m.start() + 1 for m in patron.finditer(secuencia)] 

def main():
    uniprot_ids = [
        "B5ZC00",
    "P07204",
    "P20840",
    "P01112",
    "Q9Y263",
    "P69905",
    "P68871",
    "P01308",
    "Q96IY4",
    "Q9H0H5",
    "P02768",
    "Q9NQ94",
    "Q9H9B1",
    "Q8N1N4",
    "P05067"
    ]
    
    for uid in uniprot_ids:
        secuencia = obtener_secuencia_fasta(uid)
        if secuencia:
            posiciones = buscar_motivo(secuencia)
            if posiciones:
                print(uid)
                print(' '.join(map(str, posiciones)))

if __name__ == "__main__":
    main()
