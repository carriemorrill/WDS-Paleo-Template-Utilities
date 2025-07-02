#!/usr/bin/env python
# coding: utf-8

#----------- set input values -------------------------------------------------

file_path = r"C:\Users\carrie.morrill\Desktop\New-Study-QC\GBR-0703"
infile_name = r"\lewis2018-gfb33b.txt"
outfile_name = r"\hold.txt"
col_start = 15 # first column to save (not zero-indexed)
col_end = 16  # last column to save (not zero-indexed)

#------------ opens file, extracts columns, writes to new file ----------------

vals = []
with open(file_path+infile_name,"r",encoding='utf-8') as fin:
    for line in fin:
        if not line.startswith("#"):
            vals.append(split_at_tabs(line, col_start-1, col_end)+"\n")

with open(file_path+outfile_name, 'w') as f:
    f.writelines(vals)

# ------------- functions -----------------------------------------------------

def split_at_tabs(s, i, j):
    """
    Splits a tab-separated string `s` and returns the substring consisting of the
    tab-separated fields from index `i` (inclusive) to `j` (exclusive).

    Parameters:
        s (str): The input string containing tab ('\\t') separators.
        i (int): The starting index (inclusive) of the tab-separated fields to include.
        j (int): The ending index (exclusive) of the tab-separated fields to include.

    Returns:
        str: A substring containing the selected tab-separated fields, joined by tabs.

    Raises:
        IndexError: If `j` is greater than or equal to the number of fields in the string.

    Example:
        split_at_tabs("a\tb\tc\td", 1, 3)  # Returns 'b\tc'
    """
    parts = s.split('\t')
    if j >= len(parts):
        raise IndexError("Index j is out of range")
    return '\t'.join(parts[i:j])


def files_are_textually_equal(file1, file2):
    """
    Compares the contents of two text files line by line to determine if they are 
    textually identical.

    Parameters:
        file1 (str): Path to the first text file.
        file2 (str): Path to the second text file.

    Returns:
        bool: True if both files have the same content (line by line, including 
              line endings), False otherwise.

    Notes:
        - The comparison is done using UTF-8 encoding.
        - Stops at the first differing line.
        - Files must match in both content and length (i.e., one file being a prefix 
           of the other returns False).

    Example:
        files_are_textually_equal("data1.txt", "data2.txt")  # Returns True if files are identical
    """
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return False
        return f1.readline() == '' and f2.readline() == ''