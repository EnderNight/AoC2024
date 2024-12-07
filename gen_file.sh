#!/usr/bin/env bash

# Generate a python file with permissions to execute it

echo '#!/usr/bin/env python3' > "$1.py"
echo >> "$1.py"
echo "with open('input.txt', 'r') as file" >> "$1.py"
echo "    for line in file:" >> "$1.py"
echo "        print(line)" >> "$1.py"

chmod u+x "$1.py"
