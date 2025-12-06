from sniffer.api import *
import os
import termstyle
from subprocess import call

pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

watch_paths = ['.']


def find_go_test_dirs():
    test_dirs = set()
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('_test.go'):
                test_dirs.add(root)
                break
    return test_dirs


@file_validator
def go_files(filename):
    return filename.endswith('.go') and not os.path.basename(filename).startswith('.')


@runnable
def run_go_tests(*args):
    test_dirs = find_go_test_dirs()
    if not test_dirs:
        print("No test directories found")
        return True

    all_passed = True
    for test_dir in sorted(test_dirs):
        print(f"\n{'='*50}")
        print(f"Running tests in: {test_dir}")
        print('='*50)
        result = call(['go', 'test', '-v', './...'], cwd=test_dir)
        if result != 0:
            all_passed = False

    return all_passed