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

def binary_lists(length):
  "Returns a list of binary lists of specified length."
  if length == 1:
    return [[0], [1]]
  else:
    bl = binary_lists(length - 1)
    return [[0] + x for x in bl] + [[1] + x for x in bl]

def indices_of_1(binary_list):
  "Returns indices of binary_list that are equal to 1."
  temp = []
  for i, v in enumerate(binary_list):
    if v == 1:
      temp.append(i)
  return temp

def split_at(string, breakpoints):
  "Splits string just before the given indices."
  bp = [0] + breakpoints + [len(string)]
  temp = []
  for i in range(len(bp) - 1):
    temp.append(string[bp[i]:bp[i+1]])
  return temp

def split_string(string):
  "Lists all the ways a string can be taken apart."
  temp = []
  for blist in binary_lists(len(string) - 1):
    cleavage = indices_of_1(blist)
    temp.append(split_at(string, list(map(lambda x: x + 1, cleavage))))
  return temp
# split_string("abcde")

def highlight(string, start, end):
  "Capitalizes part of a string from [start, end)"
  return string[0:start] + string[start:end].upper() + string[end:]
# highlight('spameggsspam', 3, 5)

def find_part(string, vocabulary):
  '''Searches for words in vocabulary that contain the given string
and highlights those parts in those words'''
  sl = len(string)
  temp = []
  for word in vocabulary:
    found_index = word.find(string)
    # We only want parts that start at beginning of word.
    # You can change this to -1 if you want parts anywhere within word.
    if found_index == 0:
      temp.append(highlight(word, found_index, found_index+sl))
  return temp
# find_part("b", ["balloon", "brick", "saffron", "axe", "extra"])

def spell_acronym(string, vocabulary):
  '''Breaks string into parts and finds parts of words in vocabulary that
contain those parts.'''
  expansions = [] # To hold our acronym expansions
  # Split the string every possible way
  str_parts = split_string(string)
  # For each pattern, find words that match
  for pattern in str_parts:
    expansion = [find_part(x, vocabulary) for x in pattern]
    # If we can spell the whole acronym then we save it
    if not ([] in expansion):
      expansions.append(expansion)
  return expansions
# spell_acronym("base", ["balloon", "brick", "saffron", "axe", "extra"])

