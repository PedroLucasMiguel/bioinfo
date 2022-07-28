from Bio import pairwise2
from Bio import SeqIO

# Carregando sequências do arquivo e convertendo para uma lista
record = list(SeqIO.parse(open("./src/sequences.fasta"), "fasta"))

# Executando o algoritmo de Needleman-Wunsch
results_global = pairwise2.align.globalms(record[0].seq, record[1].seq, match=5, mismatch=-3, open=-4, extend=-4)

# Executando o algortimo de Smith Waterman
results_local = pairwise2.align.localms(record[0].seq, record[1].seq, match=5, mismatch=-3, open=-4, extend=-4)

# Salvando os resultados em um arquivo
with open("output.txt", "w") as f:
    
    f.write(f'Global:\n\n')
    for r in results_global:
        f.write(pairwise2.format_alignment(*r)+"\n")

    f.write(f'\nLocal:\n\n')
    for r in results_local:
        f.write(pairwise2.format_alignment(*r)+"\n")
