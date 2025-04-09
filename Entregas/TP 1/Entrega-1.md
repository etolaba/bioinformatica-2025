DESAFÍO I: ¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la ‘identidad’ de un organismo dado?

El ADN podría ser un buen ejemplo, almacena material genético único que distingue al individuo de otros.

DESAFÍO II: Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés.

Una manera muy sencilla podría ser un simple string pero nos estaríamos perdiendo de poder guardar información dentro de la secuencia, por lo que quizás un diccionario podría ser una mejor opción. Si queremos complejizar un poco más ya podría ser una lista de estructuras u objetos que contengan toda la info que pueda ser necesaria.

🧗🏻‍♀️ DESAFÍO III: ¿ En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?

Una tupla de 3 elementos para la representación de las posiciones x,y,z, de nuevo, podemos complejizar tanto como queramos pero esta podría ser una primera aproximación.

🧗🏻‍♀️DESAFÍO IV: Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. ¿Cuáles fueron sus contribuciones en este campo? ¿Qué nos cuenta su historia acerca del mundo de la ciencia?

Algunas de sus contribuciones fueron la cristalografía de rayos X para obtener imágenes detalladas de moléculas de ADN por ejemplo, otra fue la fotografía 51 que ayudó a ver la estructura helicoidal del ADN.
Su historia nos cuenta el adverso escenario donde tuvo que accionar para contribuir a la ciencia. La falta de reconocimiento en vida es algo que no se debe ignorar a futuro para la comunidad científica, si bien tuvo un reconocimiento póstumo.

🧗🏻‍♀️ DESAFÍO V: Escribí un script en Python que prediga la estructura secundaria que adoptará cada residuo (aminoácido) de la secuencia proteica dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).

    ☑️ PREGUNTAS DISPARADORAS: ¿Qué inputs tendría tu programa? ¿De qué modo se te ocurre configurar el output? ¡Guardate esta idea, la vamos a usar más adelante!

def predecir_estructura_secundaria(secuencia):
    preferencias = {
        "A": "H", "C": "H", "D": "B", "E": "H", "F": "B",
        "G": "L", "H": "H", "I": "B", "K": "H", "L": "H",
        "M": "H", "N": "L", "P": "L", "Q": "H", "R": "H",
        "S": "L", "T": "B", "V": "B", "W": "B", "Y": "B"
    }

    estructura = ""
    for aa in secuencia:
        estructura += preferencias.get(aa.upper(), "L")  # L por defecto si el aminoácido no es reconocido

    return estructura

-- Ejemplo
secuencia = "ACDEFGHIKLMNPQRSTVWY"
estructura = predecir_estructura_secundaria(secuencia)
print("Secuencia:", secuencia)
print("Estructura:", estructura)

El output lo configuré en un diccionario como una primera aproximación.

PARA PENSAR: ¿Cuántas proteínas puede sintetizar un organismo? ¿De qué depende la cantidad y la característica de las proteínas que puede sintetizar un organismo? 

Podría depender de la complejidad del organismo en cuestión.

DESAFÍO VI: ¿Qué hace distintos a dos individuos de una especie? Propone una forma de corroborar tu respuesta realizando un diagrama de un posible método computacional para dicho fin.

Se me ocurre una comparativa entre dos moléculas de ADN de dos individuos.

Individuo 1                        Individuo 2
    |                                  |
    |                                  |
    --Comparación de secuencia de ADN---
                    |
                    |
                    |
    Resultado de si son o no distintos

☑️ PREGUNTAS DISPARADORAS: ¿Qué información deberías tener? ¿De qué modo deberías expresar dicha información para el análisis?

🧗🏻‍♀️DESAFÍO VII (Ejercicio basado en Rosalind): Los motivos lineales son elementos de secuencia que comúnmente se encuentran en dominios intrínsecamente desordenados. Consisten, en promedio, de cinco residuos que determinan la función y participan en interacciones proteína-proteína.

Para permitir la presencia de sus formas variables, un motivo proteico se representa con una notación abreviada de la siguiente manera: [XY] significa "X o Y", y {X} significa "cualquier aminoácido excepto X". Por ejemplo, el motivo de N-glicosilación se escribe como N{P}[ST]{P}.

Puedes ver la descripción completa y las características de una proteína en particular mediante su identificador de acceso "uniprot_id" en la base de datos UniProt, insertando el número de identificación en:

http://www.uniprot.org/uniprot/uniprot_id

Alternativamente, puedes obtener la secuencia de una proteína en formato FASTA siguiendo el enlace:

http://www.uniprot.org/uniprot/uniprot_id.fasta

Por ejemplo, los datos de la proteína B5ZC00 se encuentran en: http://www.uniprot.org/uniprot/B5ZC00

Dado: Un máximo de 15 ideentificadores de la base de datos de proteínas UniProt

Retornar: Para cada proteína que posea el motivo de N-glicosilación, imprimir su identificador de acceso seguido de una lista de posiciones en la secuencia de la proteína donde se encuentra el motivo.

Solución en archivo get_secuencia_fasta_py

🧗🏻‍♀️Desafío VIII: Dada la siguiente lista de sequencias, realizar el una representación Logo

[`MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV`, `MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV`, `MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV`]

Solución en archivo test_logomaker.py