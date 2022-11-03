import os
import filecmp
# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

input_small = "data/input.bed"
output_small = "data/testsortoutput.bed"
expected_small = "data/input-sorted.bed"


def test_sort_file_small():

    os.system("python src/sort_bed.py " + input_small + " " + output_small)
    assert filecmp.cmp(output_small, expected_small)


input_big = "data/large.bed"
output_big = "data/testsortoutputlarge.bed"
expected_big = "data/large-sorted.bed"


def test_sort_file_big():

    os.system("python src/sort_bed.py " + input_big + " " + output_big)
    assert filecmp.cmp(output_big, expected_big)
