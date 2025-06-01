## How to run
1. Create a python3 virtual environment
```bash
python3 -m venv venv
```

2. Activate the virtual environment
```bash
source venv/bin/activate
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```

4. Run the main script
```bash
python src/main.py <regex_file> <source_file>
```

The default input file is `inputs/main.txt`. You can change it with `-in {file}` flag.

## Input file format
### Regex file
The regex file should contain one regex per line. Following the rule:
```
<name> :== <regex>
```

E.g.
```
id :== [a-zA-Z0-9_]+
name :== [a-zA-Z]+
```

### Source file
The source file should contain the text to be processed. It can be any text file, and the regexes from the regex file will be applied to it.

There are some simple rules for the source file:
- `;` can only be used as line separator (not necessary)
- The blank spaces and new lines are ignored, but are used as command separator

## What if
### A same command is recognized by multiple regexes?
In this case, the first regex that matches the command will be used. The order of the regexes in the regex file matters, so you can control which regex is applied to which command by changing their order.

### A command is not recognized by any regex?
In this case, the command will be matched as `ERRO`, and the command will be printed as is. This allows you to see which commands were not recognized by any regex.

### How to add a new regex
To add a new regex, simply add a new line to the regex file following the format:
```
<name> :== <regex>
```