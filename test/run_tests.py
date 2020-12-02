# run all matplotlib based tests
import glob
import matplotlib
matplotlib.use('Agg')
# Find all test files.
test_files = glob.glob('test_*.py')
for f in test_files:
    print('running %s...' % f)
    exec(open(f).read())
