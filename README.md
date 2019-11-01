# SIGN

Script for Initial Generation of Names

This script generates possible acronyms using your key words. Could be useful for naming clinical trials, or astronomy and software projects.

# Prerequisites

- [Python 3](https://www.python.org/)
- this repository
- a file containing key words that you want to abbreviate
- (optional) a list of possible acronyms for those key words
- (optional) UNIX-like environment (for example, Apple Mac, Linux, Windows Cygwin) to follow the steps below

# Usage

1. Put all the keywords you want in a file (such as `keywords.txt`), one word per line like this:

  ```
python
snake
automatic
electronic
routine
method
program
abbreviation
acronym
acrostic
  ```

  Note: *the words must be all lowercase!*

2. Run the script from your console and redirect output to file. By default we search the English dictionary for acronyms. May take a few minutes.
  ```
  ./sign.py keywords.txt > possible_acronyms.txt
  ```

  You may optionally include a 2nd file containing preapproved words that you want to use as possible acronyms. This file must be all lowercase as well.
  ```
  ./sign.py keywords.txt your_list_of_approved_words.txt > possible_acronyms.txt
  ```

  If you can't run the Python script, try
  ```
  chmod +x sign.py
  ```
  to make the script executable or try
  ```
  python sign.py
  ```
  to start the script using the Python interpreter

3. The resulting file shows parts of your keywords that can be made into abbreviations. You can either browse through the file (can be very large) or search for words that you like. Here I choose "sign" and show 5 lines around that word. If you get no results here then try searching either other words or parts of words.
  ```
  grep -C 5 -P '^sign' possible_acronyms.txt
  ```

  ```
women
[['WOrdplay'], ['MEthod'], ['Name', 'Namer']]
[['WOrdplay'], ['Method', 'Mark', 'Moniker', 'Maker'], ['Electronic', 'Epithet', 'Execution'], ['Name', 'Namer']]

sign
[['Snake', 'Stamp', 'Style', 'Synthesis', 'Script', 'Synonym'], ['Initial'], ['Generator'], ['Name', 'Namer']]

case
[['CAll'], ['Snake', 'Stamp', 'Style', 'Synthesis', 'Script', 'Synonym'], ['Electronic', 'Epithet', 'Execution']]
[['Composition', 'Call', 'Crafting', 'Choosing'], ['Automatic', 'Abbreviation', 'Acronym', 'Acrostic', 'Alias'], ['Snake', 'Stamp', 'Style', 'Synthesis', 'Script', 'Synonym'], ['Electronic', 'Epithet', 'Execution']]
  ```

4. Put those words together. This step is up to you.
  ```
  Script for Initial Generation of Names
  ```
   Nice.


# Frequently Asked Questions

Q: How come I get no results?

- make sure both the keywords and the acronym files are formatted properly (one word per line, all lowercase, UNIX line breaks)
- for best results, choose keywords that start with common English letters such as vowels, T, S, N, H, R, L, D so it will be easier to find words that can be spelled using your keywords
- try opening the results file in another program and see if it's still empty
- possible bug in the script -- please include small, public, detailed reproducible data for debugging

Q: What about recursive acronyms?

This script doesn't handle recursive acronyms but they are easy to make.
For example, say I want to make this script sound more EXTREME so I put 'X' in front of the name to get XSIGN: Script for Initial Generation of Names. Maybe for version 2.0.

Q: I put some long names in the abbreviation file but they don't show up in my results. Why?

Possibilities:
- You can't spell such a long name using the keywords. Try putting more words in the keywords file.
- This script can't split long words so it ignores them. This is necessary because there are 2^(n-1) ways to split a string n characters long, and each of those splits could be the start of a keyword. No way around this limitation.

# Author, license, acknowledgements

Copyright (C) 2019 Alan Tseng

License: GPLv3

Notes:
- google-10000-english.txt file is from [https://github.com/first20hours/google-10000-english](https://github.com/first20hours/google-10000-english)

