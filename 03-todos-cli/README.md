
# Todos CLI

Simple Command-line tool to track and manage todos.

## Features

- Track, update & manage todos
- File based local data persistence

## Installation

```bash
pip install git+https://github.com/shubham-kv/mini-python-projects.git#egg=todos_cli\&subdirectory=03-todos-cli
```

## Usage

```bash
$ todos add "Try todos CLI"
Todo Added!

$ todos list
✗ 1 Try todos CLI

$ todos add "Do Development"
Todo Added!

$ todos list
✗ 1 Try todos CLI
✗ 2 Do Development

$ todos update --name "Do Python Dev" 2
Todo Updated!

$ todos list
✗ 1 Try todos CLI
✗ 2 Do Python Dev

$ todos done 1
Todo marked as done!

$ todos list
✔ 1 Try todos CLI
✗ 2 Do Python Dev

$ todos done 2
Todo marked as done!

$ todos list
✔ 1 Try todos CLI
✔ 2 Do Python Dev

$ todos delete 1
Todo Deleted!

$ todos list
✔ 2 Do Python Dev
```

## LICENSE

MIT
