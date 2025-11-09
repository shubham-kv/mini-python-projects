# calc-cli

A command-line calculator that takes user input or command-line arguments,
performs arithmetic, and prints results.

## Features

1. Command line arguments
2. REPL with history

## Installation

```bash
pip install git+https://github.com/shubham-kv/mini-projects-python.git#egg=calc_cli\&subdirectory=02_calc_cli
```

## Sample Usage

```bash
% calc 1 + 2 
3.0

% calc 3 - 1
2.0

% calc 4 \* 6
24.0

% calc 4 \/ 6
0.6666666666666666

% calc 17 % 3
2.0

% calc 17 \/\/ 3
5.0
```

Escape `*` & `/` characters with a leading `\` so that it doesn't get
picked by your shell.

Running `calc` without any arguments enters into repl mode:

```bash
$ calc
Calculator REPL mode. Type 'quit' or CTRL+D to quit.
>>> 1 + 2
3.0
>>> 3 - 1
2.0
>>> 4 * 6
24.0
>>> 4 / 6
0.6666666666666666
>>> 17 % 3
2.0
>>> 17 // 3
5.0
```

## Dev Setup

Clone this project & install the package in editable mode:

```bash
pip install -e .
```

and run from anywhere:

```bash
calc 2 + 3
```

or run manually with python:

```bash
python main.py 2 + 3
```
