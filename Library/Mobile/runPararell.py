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


def call_script(args):
    subp.call(args, shell=True)


def testHello(str1, str2):
    print "Str1 = " + str1 + " Str2 = " + str2


def parallel_execution(robotPath, RobotTestSuite, tag="*", LANG="EN", BROWSER="gc"):
    print "begin"
    run_name = []
    path = robotPath + '\\' + RobotTestSuite
    suite = TestSuiteBuilder().build(path)
    suite.filter(included_tags=tag)
    tests = suite.tests
    for test in tests:
        run_name.append(str(test))
    threads = []
    for i in range(len(run_name)):
        os.chdir(robotPath)
        command = "robot -t " + run_name[i] + " -d D:\\ArcadiaAtlas\\" + RobotTestSuite + " -o output" + run_name[
            i] + " -r report" + run_name[i] + " -l log" + run_name[
                      i] + " -v ar_LANG:" + LANG + " -v ar_BROWSER:" + BROWSER + " -i " + tag + " " + RobotTestSuite
        thread = Thread(target=call_script, args=(command,))
        threads.append(thread)
    [t.start() for t in threads]
    [t.join() for t in threads]
