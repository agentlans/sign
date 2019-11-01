#!/usr/bin/python

# SIGN: Script for Initial Generation of Names
# Copyright (C) 2019  Alan Tseng
#
# This file is part of SIGN.
#
# SIGN is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SIGN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SIGN.  If not, see <https://www.gnu.org/licenses/>.

import sys
import acronym_algo

def print_usage():
  print('Usage: python sign.py keyword_file [abbreviation_file]')

def load_word_file(filename):
  ''' Loads file containing words on separate lines.
Returns result as list.'''
  try:
    f = open(filename, 'r')
  except:
    print('Error opening file ' + filename)   
  words = []
  for line in f:
    words.append(line.strip())
  f.close()
  return words


def main():
  # Print help
  if len(sys.argv) <= 1 or len(sys.argv) > 3:
    print_usage()
    exit()
  # See which files we need to open
  keyword_file = sys.argv[1]
  if len(sys.argv) == 3:
    abbreviation_file = sys.argv[2]
  else:
    abbreviation_file = 'google-10000-english.txt'
  # Open the files
  keywords = load_word_file(keyword_file)
  abbreviations = load_word_file(abbreviation_file)
  # Try to spell acronyms
  for w in abbreviations:
    try:
      expansions = acronym_algo.spell_acronym(w, keywords)
      if expansions != []:
        print(w)
        for expansion in expansions:
          print(expansion)
        print("")
    except RuntimeError:
      # sometimes maximum recursion depth exceeded
      pass

if __name__ == '__main__':
  main()

