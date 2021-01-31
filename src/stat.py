# coding:utf8
import subprocess
from numpy.core.fromnumeric import mean
from numpy.core.numeric import NaN
from numpy.lib.function_base import median
import pandas
import sys
import imple_3.genetic_algorithm as ga
import matplotlib.pyplot as plt

from pandas.core.frame import DataFrame

STUDENT_ID = 11914433

def loadParameters(row) -> DataFrame:
    param = pandas.read_csv("properties.csv",sep=",").iloc[row,:]
    return param

def check(student_id:int, passwords:list) -> list: 
    proc = subprocess.Popen(["./unlock64.exe", str(student_id)] \
        + passwords, stdout=subprocess.PIPE)
    results = []
    while True: 
        line = proc.stdout.readline()
        if not line: 
            break
        results.append(float(str(line).split("\\t")[1] \
            .split("\\r")[0] \
            .split("\\n")[0]))
    return results

if __name__ == "__main__":
    p = loadParameters(2)
    nb_gen = []
    find_res = 0
    nb_reso = 50
    for _ in range(nb_reso):
        g_a = ga.Genetic_algorithm(int(p["n"]), int(p["nbgen"]),p["pc"], p["mu"],p["c"],int(p["call"]),
                                check,STUDENT_ID, 18)
        find,gen = g_a.resolution(True)
        nb_gen.append(gen)
        if find:
            find_res += 1
    
    plt.plot([i+1 for i in range(nb_reso)],nb_gen)
    plt.xlabel("Résolution")
    plt.ylabel("Génération")
    plt.title(f"Nombre de génration par résolution;\nMoyenne:{mean(nb_gen)}, Medianne:{median(nb_gen)}, Pourcentage de réussite: {(find_res/nb_reso)*100}%", fontsize=10)
    plt.savefig(f"../img/impl3_stat.png")
    print(f"Moyenne:{mean(nb_gen)}, Medianne:{median(nb_gen)},\n Pourcentage de réussite: {(find_res/nb_reso)*100}%")