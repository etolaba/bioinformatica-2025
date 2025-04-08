DESAFÍO I: ¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la ‘identidad’ de un organismo dado?

DESAFÍO II: Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés.

🧗🏻‍♀️ DESAFÍO III: ¿ En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?

🧗🏻‍♀️DESAFÍO IV: Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. ¿Cuáles fueron sus contribuciones en este campo? ¿Qué nos cuenta su historia acerca del mundo de la ciencia?



🧗🏻‍♀️ DESAFÍO V: Escribí un scrip en Python que prediga la estructura secundaria que adoptará cada residuo (aminoácido) de la secuencia proteica dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).

    ☑️ PREGUNTAS DISPARADORAS: ¿Qué inputs tendría tu programa? ¿De qué modo se te ocurre configurar el output? ¡Guardate esta idea, la vamos a usar más adelante!

PARA PENSAR: ¿Cuántas proteínas puede sintetizar un organismo? ¿De qué depende la cantidad y la característica de las proteínas que puede sintetizar un organismo? 



DESAFÍO VI: ¿Qué hace distintos a dos individuos de una especie? Propone una forma de corroborar tu respuesta realizando un diagrama de un posible método computacional para dicho fin.

☑️ PREGUNTAS DISPARADORAS: ¿Qué información deberías tener? ¿De qué modo deberías expresar dicha información para el análisis?

🧗🏻‍♀️DESAFÍO VII (Ejercicio basado en Rosalind): Los motivos lineales son elementos de secuencia que comúnmente se encuentran en dominios intrínsecamente desordenados. Consisten, en promedio, de cinco residuos que determinan la función y participan en interacciones proteína-proteína (Podes leer más aquí).

Para permitir la presencia de sus formas variables, un motivo proteico se representa con una notación abreviada de la siguiente manera: [XY] significa "X o Y", y {X} significa "cualquier aminoácido excepto X". Por ejemplo, el motivo de N-glicosilación se escribe como N{P}[ST]{P}.

Puedes ver la descripción completa y las características de una proteína en particular mediante su identificador de acceso "uniprot_id" en la base de datos UniProt, insertando el número de identificación en:

http://www.uniprot.org/uniprot/uniprot_id

Alternativamente, puedes obtener la secuencia de una proteína en formato FASTA siguiendo el enlace:

http://www.uniprot.org/uniprot/uniprot_id.fasta

    Por ejemplo, los datos de la proteína B5ZC00 se encuentran en: http://www.uniprot.org/uniprot/B5ZC00

    Dado: Un máximo de 15 identificadores de la base de datos de proteínas UniProt

    Retornar: Para cada proteína que posea el motivo de N-glicosilación, imprimir su identificador de acceso seguido de una lista de posiciones en la secuencia de la proteína donde se encuentra el motivo.

    🧗🏻‍♀️Desafío VIII: Dada la siguiente lista de sequencias, realizar el una representación Logo

[`MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV`, `MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV`, `MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV`]