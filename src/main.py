# coding:utf8
import subprocess
from numpy.core.numeric import NaN
import pandas
import sys
# import genetic_algorithm as ga # implemenation 1
import imple_1.genetic_algorithm as ga1
import imple_2.genetic_algorithm as ga2
import imple_3.genetic_algorithm as ga3

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
    # print(check(STUDENT_ID, ["PASSWORD", "ALGOGEN"]))
    g_a = NaN
    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            p = loadParameters(0)
            g_a= ga1.Genetic_algorithm(int(p["n"]), int(p["nbgen"]),p["pc"], p["mu"],p["c"],int(p["call"]),
                            check,STUDENT_ID, 18)
        if sys.argv[1] == "2":
            p = loadParameters(1)
            g_a= ga2.Genetic_algorithm(int(p["n"]), int(p["nbgen"]),p["pc"], p["mu"],p["c"],int(p["call"]),
                            check,STUDENT_ID, 18)
        if sys.argv[1] == "3":
            p = loadParameters(2)
            g_a= ga3.Genetic_algorithm(int(p["n"]), int(p["nbgen"]),p["pc"], p["mu"],p["c"],int(p["call"]),
                            check,STUDENT_ID, 18)
    else:
        p = loadParameters(2)
        g_a= ga3.Genetic_algorithm(int(p["n"]), int(p["nbgen"]),p["pc"], p["mu"],p["c"],int(p["call"]),
                            check,STUDENT_ID, 18)
        
    g_a.resolution()