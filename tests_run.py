import os
import re
import sys
import unittest


import coverage


COVERAGE_FILE = "coverage.txt"
OMIT = ["tests/tests_*.py", "kemono/__init__.py"]

def capture_coverage() -> coverage.Coverage:
    cov = coverage.Coverage()
    cov.start()

    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="tests/", pattern="tests_*.py")
    test_runner = unittest.runner.TextTestRunner()
    results = test_runner.run(tests)
    if 0 < len(results.failures) or 0 < len(results.errors):
        sys.exit(1)
    cov.stop()
    cov.save()
    return cov

def parse_coverage():
    regex = re.compile(r"^([^\s]+)\s+\d+\s+\d+\s+(\d+)%$")
    cov = capture_coverage()
    with open(COVERAGE_FILE, "w+") as report:
        cov.report(omit=OMIT, file=report)
    with open(COVERAGE_FILE, "r") as report:
        report_content = report.read().split("\n")[2:-3]
    for line in report_content:
        print(line)
        yield regex.findall(line)[0]
    os.unlink(COVERAGE_FILE)

def github_action_annotation():
    handle = open("parsed-coverage.txt", "w+")
    for file, cover in parse_coverage():
        cover = float(cover)
        if 80 > cover:
            handle.write(f"::warning::{file} is covered at {cover}%, could be better\n")
        if 20 > cover:
            handle.write(f"::error::{file} is covered at only {cover}%\n")
    handle.close()

github_action_annotation()
