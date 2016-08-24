from multiprocessing import Pool
import os
import sys
import time
from robot.conf.settings import RobotSettings
from robot.result import ExecutionResult
from robot.running.model import TestSuite


def run(run_name):
    os.chdir(sys.argv[1])
    # os.system("start cmd /k robot -t "+run_name+" -o xml_"+run_name+".xml -l log_"+run_name+".html -r report_"+run_name+" eServiceWebPostPaidLogin.txt")
    os.system("start cmd /k robot -t " + run_name + " -d D:\\ArcadiaAtlas\\" + run_name + " " + sys.argv[2])


def parallel_execution():
    run_name = []
    for i in range(3, sys.argv.__len__()):
        run_name.append(sys.argv[i])

    if __name__ == "__main__":
        pool = Pool(processes=sys.argv.__len__() - 3)
        pool.map(run, run_name)


# if __name__ == "__main__":
#     parallel_execution()


def get_available_tests(source):
    suite = TestSuite([os.path.abspath(source)])
    return list(get_tests(suite))


def get_tests(suite):
    for s in suite.suites:
        for t in get_tests(s):
            yield t
    for t in suite.tests:
        yield t

def get_test_suites(suite):
    for s in suite.suites:
        for test_suite in get_test_suites(s):
            yield test_suite
    if suite.tests:
        yield suite

def get_available_test_suites(source):
    settings = RobotSettings()
    suite = TestSuite([os.path.abspath(source)], settings)
    return list(get_test_suites(suite))


test_suites =  get_available_tests(os.path.dirname('D:/ArcadiaAtlas/Robot/eServiceWebPostPaid_BuffeStyle/eServiceWebPostPaidLogin.txt'))
print len(test_suites)
