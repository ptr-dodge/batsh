# Batch Compiler API
This python script utilizes the API endpoint provided by `https://batsh.org/compile` to make a POST request with the batsh code, and compile it to bash or batch.

I made this script for use in my other project, [Batshuino](https://github.com/ptr-dodge/batshuino). I didn't want to install OCaml or make that a part of my project, so I found another way to integrate this programming language in to my project.

## Usage
This script is pretty simple to use:
```bash
python batsh.py --winbat -i test.batsh -o test.bat
```
Or to compile to bash:
```bash
python batsh.py --bash -i test.batsh -o test.sh
```
---
There is an optional argument `--silent` to control verbosity.