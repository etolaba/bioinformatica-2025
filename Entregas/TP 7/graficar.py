import json
import matplotlib.pyplot as plt

# Hay que instalar matplotlib antes de ejecutar este script:
# Windows: pip install matplotlib
# Linux: sudo pip3 install matplotlib
# (en algunos sistemas puede ser necesario: sudo apt install python3-matplotlib)
# MacOS: pip3 install matplotlib

# Cargar archivo JSON
with open("test_3b510_0_scores_rank_001_alphafold2_ptm_model_4_seed_000.json") as f:
    data = json.load(f)

plddt = data["plddt"]

# Graficar
plt.figure(figsize=(10, 4))
plt.plot(plddt, label="pLDDT por posición")
plt.xlabel("Residuo")
plt.ylabel("pLDDT")
plt.title("Confianza por posición")
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
