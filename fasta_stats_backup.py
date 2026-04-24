import glob
from Bio import SeqIO


def find_all_orfs(seq):

    stop_codons={"TAA","TAG","TGA"}
    orfs=[]

    # search all 3 forward frames
    for frame in range(3):

        for i in range(frame,len(seq)-2,3):

            if seq[i:i+3] == "ATG":

                for j in range(i+3,len(seq)-2,3):

                    codon=seq[j:j+3]

                    if codon in stop_codons:
                        orfs.append(seq[i:j+3])
                        break

    return sorted(orfs,key=len,reverse=True)


all_gc=[]


for file in glob.glob("data/*.fasta"):

    print(f"\nProcessing {file}")

    for record in SeqIO.parse(file,"fasta"):

        seq=str(record.seq).upper()

        A=seq.count("A")
        T=seq.count("T")
        G=seq.count("G")
        C=seq.count("C")

        valid_bases=A+T+G+C

        at=(A+T)/valid_bases*100
        gc=(G+C)/valid_bases*100

        all_gc.append(gc)

        print(record.id)
        print(f"Length: {len(seq)}")
        print(f"GC: {gc:.2f}%")
        print(f"A:{A} T:{T} G:{G} C:{C}")
        print(f"AT: {at:.2f}%")
        print(f"GC+AT: {gc+at:.2f}%")
        print()

        # ORF analysis
        orfs=find_all_orfs(seq)

        if orfs:
            print("Top ORFs:")
            for x in orfs[:5]:
                print(
                    f"{len(x)} bp | Protein {(len(x)//3)-1} aa"
                )
        else:
            print("No ORFs found")

        print()

        N=seq.count("N")
        if N>0:
            print(f"Warning: {N} ambiguous bases")
            print()

print(f"Average GC: {sum(all_gc)/len(all_gc):.2f}%")
