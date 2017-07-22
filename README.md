Compile script in bytecode and run without `exec` call

Output example for `Hello, world!` program:
```
import marshal, base64
from types import FunctionType
script = """4wAAAAAAAAAAAAAAAAIAAABAAAAAcwwAAABlAGQAgwEBAGQBUwApAnoNSG
VsbG8sIHdvcmxkIU4pAdoFcHJpbnSpAHICAAAAcgIAAADaCDxtb2R1bGU+2gABAAAA8wAA
AAA="""
script = marshal.loads(base64.b64decode(script))
script = FunctionType(script, globals={'__builtins__': __builtins__})
script()
```

**Usage**:
./simple_python_obfuscator.py input.py output.py
