# Lexical Analyzer Generator
This software was built as the first project for the Formal Languages and Compilers course (INE5421) at Universidade Federal de Santa Catarina.
Its objective is to implement a lexical analyzer generator that takes regular expressions as input and produces a deterministic finite automaton (DFA) capable of tokenizing source text.

The project guides students through fundamental stages of lexical analysis, including:
1. Converting regular expressions (REs) to nondeterministic finite automata (NFAs),
2. Converting NFAs to deterministic finite automata (DFAs),
3. Constructing a lexical analysis table,
4. Identifying and classifying tokens from input text.

This educational tool reinforces theoretical concepts in automata theory while providing hands-on experience with core components of compiler construction.

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
python src/main.py <prefix>
```

- `<prefix>` is the prefix of the matching regular expressions and source text defined in the `inputs` folder.
    - For example, if you want to use the regular expressions and source text defined in `inputs/main_regex.txt` and `inputs/main_source.txt`, you should run:
    ```bash
    python src/main.py main
    ```

The default input file is `inputs/main.txt`. You can change it with `-in {file}` flag.