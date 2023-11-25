import os
import sys
import time
import subprocess
import psutil
from Bio.Align.Applications import ClustalOmegaCommandline, MuscleCommandline, TCoffeeCommandline

#run python3 benchmark.py

def run_msa(algorithm, input_file, output_file):
    start_time = time.time()
    # initial_memory = psutil.Process(os.getpid()).memory_info().rss

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
            subprocess.run(command, check=True)
            print("Muscle alignment completed successfully.")

        except subprocess.CalledProcessError as e:
            return f"Error running Muscle: {e}"

    if algorithm == "tcoffee":
        muscle_path = "insert tcoffee path"


    # final_memory = psutil.Process(os.getpid()).memory_info().rss
    execution_time = time.time() - start_time
    # memory_usage = final_memory - initial_memory


    return execution_time

def run_fastsp(test_alignment, reference_alignment):
    #this is for accuracy score 
    fastsp_command = f"java -jar fastsp.jar -r {reference_alignment} -e {test_alignment}"
    process = subprocess.Popen(fastsp_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode()
    sp_score = extract_metric(output, "SP Score") 
    tc_score = extract_metric(output, "TC Score")

    return sp_score, tc_score

def calculate_accuracy(output_alignment, reference_alignment):
    sp_score, tc_score = run_fastsp(output_alignment, reference_alignment)
    accuracy_score = sp_score + tc_score  # Adjust as needed
    return accuracy_score

def main():
    working_directory = os.getcwd()

    input_sequences = working_directory + ("/input_files/BOX001.fasta")
    output_alignment = working_directory + ("/output_files/BOX001.fasta")

    #reference_alignment = "path_to_reference_alignment.aln"  

    # Assessing Clustal Omega
    # time_clustal, memory_clustal = run_msa("clustalomega", input_sequences, output_alignment)
    # print("CLUSTAL: ")
    # print(time_clustal)
    # print(memory_clustal)
    #accuracy_clustal = calculate_accuracy(output_alignment, reference_alignment)

    # Assessing MUSCLE
    time_muscle = run_msa("muscle", input_sequences, output_alignment)
    print("MUSCLE: ")
    print(time_muscle)

    #accuracy_muscle = calculate_accuracy(output_alignment, reference_alignment)

    # Assessing T-Coffee
    # time_tcoffee, memory_tcoffee = run_msa("tcoffee", input_sequences, output_alignment)
    # print("T-COFFEE: ")
    # print(time_tcoffee)
    # print(memory_tcoffee)
    #accuracy_muscle = calculate_accuracy(output_alignment, reference_alignment)




if __name__ == '__main__':
    main()


