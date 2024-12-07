#!/usr/bin/env bash

# Generate a python file with permissions to execute it

echo '#!/usr/bin/env python3' > "$1.py"
echo >> "$1.py"
echo "print('Hello World')" >> "$1.py"

chmod u+x "$1.py"
