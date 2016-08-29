from multiprocessing import Pool
import os
import sys
import time
from robot.conf.settings import RobotSettings
from robot.result import ExecutionResult
from robot.running.model import TestSuite
from robot.api import TestSuiteBuilder


def run(run_name):
    os.chdir(sys.argv[1])
    #os.system("start cmd /k robot -t "+run_name+" -o xml_"+run_name+".xml -l log_"+run_name+".html -r report_"+run_name+" eServiceWebPostPaidLogin.txt")
    os.system("start cmd /k robot -t " + run_name + " -d D:\\ArcadiaAtlas\\" + run_name + " " + sys.argv[2])


def parallel_execution():
    run_name = []
    path = sys.argv[1]+'\\'+sys.argv[2]
    suite = TestSuiteBuilder().build(path)
    tests = suite.tests
    #for i in range(3, sys.argv.__len__()):
    for test in tests:
        run_name.append(test)

    if __name__ == "__main__":
        pool = Pool(processes=sys.argv.__len__() - 3)
        pool.map(run, run_name)

if __name__ == "__main__":
     parallel_execution()




