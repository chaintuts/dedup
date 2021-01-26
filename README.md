## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
*  Dedup finds duplicate files by content using cryptographic hashes

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Searches a given directory for duplicate files by content
* Uses the SHA-256 hash

### Requirements
* Requires Python

### Platforms
* Windows
* Linux
* MacOSX

## Usage
____________

### Command line usage
* Run `dedup.py <directory>` to list duplicate files by content (hash)
