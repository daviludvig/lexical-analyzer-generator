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
