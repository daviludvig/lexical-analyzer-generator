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

After running the script, it will output the results to the console and also save them to `outputs/` folder.

## Output
- Every DFA built from the regexes will be saved in a separate file in the `outputs/automatos` folder. 
- The symbol table will be saved in `outputs/symbol_table.txt`.
- The tokens built from the source file will be saved in `outputs/tokens.txt`.

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

## Processing flow
1. **Argument Parsing**

   * The program expects two command-line arguments: a regex definition file and a source code file.
   * If not provided, it exits with usage instructions.

2. **File Validation**

   * It checks if both files exist (`regex_file` and `source_file`).
   * If either is missing, it exits with an error message.

3. **Token Type Generation**

   * Parses the regex definition file to extract token types (`TokenType` objects).
   * Each token type includes a regular expression associated with a name (e.g., `ID`, `NUM`, `PR`, etc.).

4. **DFA Construction**

   * Each regular expression is converted into a DFA using:

     * **Regex to postfix** (Shunting Yard algorithm),
     * **Postfix to NFA**,
     * **NFA to DFA**.
   * A list of DFAs is created, where the first position (`dfas[0]`) is initially set to `None` to hold the full language DFA later.

5. **Full Language DFA Generation**

   * All DFAs are merged into a single **"full language DFA"** using epsilon-union and determinization.
   * This unified DFA (`dfas[0]`) accepts the language of all valid lexemes (full language).

6. **Symbol Table Initialization**

   * A `SymbolTable` instance is created to track lexemes and their token types.

7. **Source Code Tokenization**

   * The source code is read and parsed using the DFAs.
   * Lexemes are identified, validated, and categorized into tokens or errors.
   * Tokens are printed to the console.

8. **Output Generation**

   * The output directory is cleaned and recreated.
   * For each DFA, its tabular representation is saved to a file.
   * The list of tokens is saved in `tokens.txt`.
   * The symbol table is saved in `symbol_table.txt`.

9. **Program Exit**

   * The program exits with `sys.exit(0)` after successful execution.