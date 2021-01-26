# This file contains code for finding file duplicates by content in a directory
#
# Author: Josh McIntyre
#
import os
import hashlib
import argparse

# Build the duplicates listing
# This function enumerates the files in the directory and hashes each
# If 2 hashes match, add them to the duplicates listing
def find_duplicates(directory):

    # Get a file listing
    os.chdir(directory)
    names = [ name for name in os.listdir(directory) if os.path.isfile(name) ]

    # Create a dict of file hashes, names
    hashes = {}
    duplicates = {}
    for name in names:
        with open(name, "rb") as f:
            content = f.read()
            digest = hashlib.sha256(content).hexdigest()

            # If the digest is already in the hash map, add an entry to duplicates
            # Otherwise, just add the first file to the listing
            if digest in hashes:
                hashes[digest].append(name)
                duplicates[digest] = hashes[digest]
            else:
                hashes[digest] = [ name ]

    return duplicates

# Output the found duplicates
def output_duplicates(duplicates):

    for digest, names in duplicates.items():
        print("Found duplicates -  " + digest[:8] + ": " + ", ".join(names))

# The main entry point for the program
def main():

    # Fetch the directory from the command line args
    parser = argparse.ArgumentParser(description="Find duplicate files by content")
    parser.add_argument("directory", type=str, help="The directory to search")
    args = parser.parse_args()

    # Generate the listing
    duplicates = find_duplicates(args.directory)
    
    # Output the duplicates list
    output_duplicates(duplicates)

if __name__ == "__main__":
    main()
