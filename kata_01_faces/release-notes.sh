#!/bin/bash

(
./face.py --version
git log --oneline --merges
) > release_notes.md
