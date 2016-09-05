from multiprocessing import Pool
from multiprocessing import Process
from threading import Thread
import subprocess as subp
import os
import sys
import time
from robot.conf.settings import RobotSettings
from robot.result import ExecutionResult
from robot.running.model import TestSuite
from robot.api import TestSuiteBuilder
import threading

from functools import partial

def f(x):
    return x*x


def copy_run():
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))


def call_script(run_dir, run_name):
    print "in call script"
    # command = "robot -t " + run_name + " -d " + dir_path + " -o output" + run_name + " -r report" + run_name \
    #           + " -l log" + run_name + " -v ar_LANG:" + LANG + " -v ar_BROWSER:" + BROWSER + " -i " + tag + " " \
    #           + robot_test_suite
    command = "robot -t " + run_name + " -d " + run_dir + " -o output" + run_name + " -r report" + run_name \
              + " -l log" + run_name + " -v ar_LANG:" + "EN" + " -v ar_BROWSER:" + "gc" + " -i " + "ptest" + " " \
                + "eServiceWebPostPaidLogin.txt"
    print "command is a " + command
    os.system(command)
    # subp.call(args, shell=True)
    # thread = Thread(group=None, target=lambda: os.system(command))
    # thread.start()
    # thread.join()
#
#
# def run(run_name):
#     print "run_name : " + run_name
#     # os.chdir(sys.argv[1])
#     # os.system("start cmd /k robot -t "+run_name+" -o xml_"+run_name+".xml -l log_"+run_name+".html -r report_"+run_name+" eServiceWebPostPaidLogin.txt")
#     # os.system("start cmd /k robot -t " + run_name + " -d D:\\ArcadiaAtlas\\" + run_name + " " + "-v ar_LANG:EN -v ar_BROWSER:gc " + sys.argv[2])
#     # command = "robot -t " + run_name + " -d " + dir_path + " -o output" + run_name + " -r report" + run_name \
#     #           + " -l log" + run_name + " -v ar_LANG:" + "EN" + " -v ar_BROWSER:" + "gc" + " -i " + "ptest" + " " \
#     #           + "eServiceWebPostPaidLogin.txt"
#     # os.system(command)
#     # subp.check_call(command, shell=True)
#     # thread = Thread(group=None, target=lambda: os.system(command))
#     # thread.run()
#     # # Later
#     # if thread.is_alive():
#     #     # Still running
#     #     print('running...')
#     # else:
#     #     # Has finished
#     #     print('running done...')
#
#     print('finish run...')
#
#
# def test_copy(str1):
#     print "Test Copy : Test1=> " + str1
#
#
# def test_hello(str1, str2):
#     print "Str1 = " + str1 + " Str2 = " + str2
#
#
# def f(x):
#     return x*x
#
#


def parallel_execution(robot_path, robot_test_suite, tag="*", LANG="EN", BROWSER="gc"):
    print "begin"
    run_name = []
    path = robot_path + '\\' + robot_test_suite
    suite = TestSuiteBuilder().build(path)
    suite.filter(included_tags=tag)
    tests = suite.tests
    print tests
    for test in tests:
        run_name.append(str(test))
    threads = []
    print "path : " + path
    dir_path = path.replace(".txt", "")
    print "dir_path : " + dir_path
    print "len : " + str(len(run_name))
    # run_name = ['[F01-001]eServiceWeb-PO-Login-NumberNotComplete', '[F01-002]eServiceWeb-PO-Login-NumberDtac']
    # run_dir = "D:\ArcadiaAtlas\Robot\eServiceWebPostPaid_BuffeStyle"
    # run_name = tests
    run_dir = dir_path
    os.chdir(robot_path)
    pool = Pool(len(run_name))
    func = partial(call_script, run_dir)
    pool.map_async(func, run_name)
    pool.close()
    pool.join()
    # for i in range(len(run_name)):
    #     # os.chdir(robot_path)
    #
    #     # command = "robot -t " + run_name[i] + " -d " + dir_path + " -o output" + run_name[
    #     #     i] + " -r report" + run_name[i] + " -l log" + run_name[
    #     #               i] + " -v ar_LANG:" + LANG + " -v ar_BROWSER:" + BROWSER + " -i " + tag + " " + robot_test_suite
    #     print "run_name => " + run_name[i]
    #     pool.apply_async(test_copy, args=(run_name[i],))
    #
    # pool.close()
    # pool.join()
        # thread = Thread(target=call_script, args=(command,))
        # threads.append(thread)
    # [t.start() for t in threads]
    # [t.join() for t in threads]

    print "finished..."

if __name__ == "__main__":
    # (robot_path, robot_test_suite, tag = "*", LANG = "EN", BROWSER = "gc")
    parallel_execution("D:\ArcadiaAtlas\Robot\eServiceWebPostPaid_BuffeStyle", "eServiceWebPostPaidLogin.txt", "ptest")

# def call_script(args):
#     subp.call(args, shell=True)
#
#
# def testHello(str1, str2):
#     print "Str1 = " + str1 + " Str2 = " + str2
#
#
# def parallel_execution(robot_path, robot_test_suite, tag="*", LANG="EN", BROWSER="gc"):
#     print "begin"
#     run_name = []
#     path = robot_path + '\\' + robot_test_suite
#     suite = TestSuiteBuilder().build(path)
#     suite.filter(included_tags=tag)
#     tests = suite.tests
#     print tests
#     for test in tests:
#         run_name.append(str(test))
#     threads = []
#     print "path : " + path
#     dir_path = path.replace(".txt", "")
#     print "dir_path : " + dir_path
#
#     for i in range(len(run_name)):
#         os.chdir(robot_path)
#         command = "robot -t " + run_name[i] + " -d " + dir_path + " -o output" + run_name[
#             i] + " -r report" + run_name[i] + " -l log" + run_name[
#                       i] + " -v ar_LANG:" + LANG + " -v ar_BROWSER:" + BROWSER + " -i " + tag + " " + robot_test_suite
#         thread = Thread(target=call_script, args=(command,))
#         threads.append(thread)
#     [t.start() for t in threads]
#     [t.join() for t in threads]