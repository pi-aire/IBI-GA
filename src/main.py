# coding:utf8

import subprocess
import pandas
# import genetic_algorithm as ga # implemenation 1
import imple_3.genetic_algorithm as ga

from pandas.core.frame import DataFrame

STUDENT_ID = 11914433

def loadParameters() -> DataFrame:
    param = pandas.read_csv("properties.csv",sep=",").loc[0]
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
    p = loadParameters()
    print(p)
    print(check(STUDENT_ID, ["PASSWORD", "ALGOGEN"]))
    g_a= ga.Genetic_algorithm(int(p["n"]), int(p["nbgen"]),p["pc"], p["mu"],p["c"],int(p["call"]),
                         check,STUDENT_ID, 18)
    g_a.resolution()