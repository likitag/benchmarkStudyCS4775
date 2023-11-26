import os
import sys
import time
import subprocess
import psutil
from Bio.Align.Applications import ClustalOmegaCommandline, MuscleCommandline, TCoffeeCommandline
from Bio import AlignIO
import psutil
import os

"""run python3 benchmark.py"""

def run_msa(algorithm, input_file, output_file):
    """Runs the specified algorithm on the input file and returns the execution time"""
    start_time = time.time()


    if algorithm == "clustalomega":
        clustal_path = "/Users/likitag/Downloads/clustal-omega-1.2.4/clustalo"

    if algorithm == "muscle":
        muscle_path = "/Users/likitag/Downloads/muscle-5.1.0/src/Darwin/muscle"

        command = [
            muscle_path,
            "-align", input_file,
            "-output", output_file
        ]

        try:
            process = psutil.Process(os.getpid())
            mem_before = process.memory_info().rss / 1024 / 1024
            subprocess.run(command, check=True)
            mem_after = process.memory_info().rss / 1024 / 1024
            print(f"Memory used: {mem_after - mem_before} MB")
            print("Muscle alignment completed successfully.")

        except subprocess.CalledProcessError as e:
            return f"Error running Muscle: {e}"

    if algorithm == "mafft":
        command = "/Users/likitag/Downloads/mafft/core/mafft " + input_file + " > " + output_file
        os.system(command)




    execution_time = time.time() - start_time
    


    return execution_time

def accuracy_comparison(output_alignment, reference_alignment): 
    """Given the output alignment and the benchamrk reference alignment, will calculate an accuracy score."""
    total_accuracy = 0

    #convert each fasta file to a dictionary mapping 
    ref_dic = fasta_to_dict(reference_alignment)
    out_dic = fasta_to_dict(output_alignment)

    #calculate accuracy for each sequence, and add to total 
    for seq in out_dic: 
        seq1 = out_dic[seq]
        seq2 = ref_dic[seq]
        
        matches = sum(c1 == c2 for c1, c2 in zip(seq1, seq2))
        total = max(len(seq1), len(seq2))

        if total > 0: 
            total_accuracy+=(matches/total)

    #compute average accuracy across all sequences (should be between 0 and 1)
    return total_accuracy / len(out_dic)



def fasta_to_dict(file_path):
    """Convert a FASTA file to a dictionary where keys are sequence IDs and values are sequences."""
    sequences = {}
    current_id = None

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                current_id = line[1:].split()[0] 
                sequences[current_id] = ""
            elif current_id is not None:
                sequences[current_id] += line.strip()

    return sequences

def msf_to_fasta(input_file, output_file):
    """Convert a MSF file to a FASTA file, since the Balibase database has reference files in msf format, but we want to convert it to fasta format """
    
    alignment = AlignIO.read(input_file, "msf")
    AlignIO.write(alignment, output_file, "fasta")

    return

def main():
    working_directory = os.getcwd()
    msf_ref = working_directory + ("/reference_files/test1_ref.msf")

    input_sequences = working_directory + ("/input_files/test1_input.fasta")



    output_alignment = working_directory + ("/output_files/muscle/test1_output.fasta")
    reference_alignment = working_directory + ("/reference_files/test1_ref.fasta")

    msf_to_fasta(msf_ref, reference_alignment)

    #Assessing MUSCLE
    time_muscle = run_msa("muscle", input_sequences, output_alignment)

    print("MUSCLE execution time: " + str(time_muscle))

    accuracy_score = accuracy_comparison(output_alignment, reference_alignment)
    print("MUSCLE Accuracy: " + str(accuracy_score))

    #Assesing MAFFT
    output_alignment = working_directory + ("/output_files/mafft/test1_output.fasta")

    time_mafft = run_msa("mafft", input_sequences, output_alignment)

    print("MAFFT execution time: " + str(time_mafft))
    accuracy_score = accuracy_comparison(output_alignment, reference_alignment)
    print("MAFFT Accuracy: " + str(accuracy_score))







if __name__ == '__main__':
    main()


