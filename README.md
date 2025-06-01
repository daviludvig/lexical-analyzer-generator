# Lexical Analyzer Generator
This software was built as the first project for the Formal Languages and Compilers course (INE5421) at Universidade Federal de Santa Catarina.
Its objective is to implement a lexical analyzer generator that takes regular expressions as input and produces a deterministic finite automaton (DFA) capable of tokenizing source text.

The project guides students through fundamental stages of lexical analysis, including:
1. Converting regular expressions (REs) to nondeterministic finite automata (NFAs),
2. Converting NFAs to deterministic finite automata (DFAs),
3. Constructing a lexical analysis table,
4. Identifying and classifying tokens from input text.

This educational tool reinforces theoretical concepts in automata theory while providing hands-on experience with core components of compiler construction.

## Development info
Benchmark time
```bash
python -m cProfile -s time script.py
```
