from Bio.Blast import NCBIWWW
from Bio import SeqIO

# Carregando sequências do arquivo e convertendo para uma lista
record = list(SeqIO.parse(open("./src/sequences.fasta"), "fasta"))

# Invocando o algoritmo através da base de dados de nucleotídeos
result_handle = NCBIWWW.qblast("blastn", "nt", record[0].seq)

# Salvando o XML dos resultados
with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()