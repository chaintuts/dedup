# This file contains code for finding file diffs by content in 2 different directory
# Useful for syncing files manually
#
# Author: Josh McIntyre
#
import os
import hashlib
import argparse

# Build the directory hash listing
def find_hashes(directory):

    # Get a file listing
    os.chdir(directory)
    names = [ name for name in os.listdir(directory) if os.path.isfile(name) ]

    # Create a dict of file hashes, names
    hashes = {}
    for name in names:
        with open(name, "rb") as f:
            content = f.read()
            digest = hashlib.sha256(content).hexdigest()
            hashes[digest] = name

    return hashes

# Calculate the diff list
def find_diff(hashes, hashes2):

    keyset = set(hashes2) - set(hashes)
    diff = { k : hashes2[k] for k in keyset }
    return diff

# Output the found duplicates
def output_diff(diff):

    for digest, name in diff.items():
        print("Found diff -  " + digest[:8] + ": " + name)

# The main entry point for the program
def main():

    # Fetch the directory from the command line args
    parser = argparse.ArgumentParser(description="Find duplicate files by content")
    parser.add_argument("directory", type=str, help="The first directory to compare")
    parser.add_argument("directory2", type=str, help="The second directory to compare")
    args = parser.parse_args()

    # Generate the listing
    hashes = find_hashes(args.directory)
    hashes2 = find_hashes(args.directory2)
    
    # Calculate the diff
    diff = find_diff(hashes, hashes2)
    
    # Output the duplicates list
    output_diff(diff)

if __name__ == "__main__":
    main()
