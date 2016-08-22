from multiprocessing import Pool
import os
import sys


def run(run_name):
    os.chdir(sys.argv[1])
    os.system("start cmd /k robot -t "+run_name+" -o xml_"+run_name+".xml -l log_"+run_name+".html -r report_"+run_name+" eServiceWebPostPaidLogin.txt")


def parallel_execution():

    run_name=[]
    for i in range(2, sys.argv.__len__()):
        run_name.append(sys.argv[i])

    if __name__ == "__main__":
        pool = Pool(processes=sys.argv.__len__()-2)
        pool.map(run, run_name)

if __name__ == "__main__":
     parallel_execution()