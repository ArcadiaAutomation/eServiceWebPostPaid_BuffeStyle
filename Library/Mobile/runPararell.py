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
    #for test in range(3, sys.argv.__len__()):
    for test in tests:
         run_name.append(str(test))
    print run_name
    pool = Pool(processes=11)
    pool.map(run, run_name)
    # pool.map(run, ['test', '[F01-001]eServiceWeb-PO-Login-NumberNotComplete', '[F01-002]eServiceWeb-PO-Login-NumberDtac',
    #                '[F01-003]eServiceWeb-PO-Login-OtpNotcomplete',
    #                '[F01-004]eServiceWeb-PO-Login-InputWrongOtp', '[F01-005]eServiceWeb-PO-Login-NotInputOtp',
    #                '[F01-006]eServiceWeb-PO-Login-InputOtpWithCharacter', '[F01-007]eServiceWeb-PO-Login-CancelOtp',
    #                'TestPararell1', 'TestPararell2', 'TestPararell3'])


if __name__ == "__main__":
    parallel_execution()



