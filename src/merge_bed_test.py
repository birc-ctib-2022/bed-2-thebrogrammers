# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
import os
import filecmp
file = "data/input-sorted.bed"
out = "data/testoutmerge.bed"
expected = "data/input-merged.bed"


def test_merge():
    os.system("python src/merge_bed.py " + file +
              " " + file + " -o" + out)
    assert filecmp.cmp(out, expected)
