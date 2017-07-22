#!/usr/bin/env python3

import argparse
import base64
import marshal
import textwrap
from pathlib import Path
from types import CodeType

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Simple Python obfuscator')
    parser.add_argument('script', type=str, help='Script file name')
    parser.add_argument('output', type=str, help='Output file name')
    args = parser.parse_args()
    script = ''
    if Path(args.script).is_file():
        with open(args.script) as s:
            script = s.read()
        script = compile(script, '', 'exec')
        # Trimming sensitive information about source code
        script = CodeType(0, 0, script.co_nlocals, script.co_stacksize,
                          script.co_flags, script.co_code, script.co_consts,
                          script.co_names, script.co_varnames, script.co_name, '', 1, b'',
                          script.co_freevars, script.co_cellvars)
        script = base64.b64encode(marshal.dumps(script))
        with open(args.output, 'w') as o:
            o.write('import marshal, base64\n')
            o.write('from types import FunctionType\n')
            o.write('\n'.join(textwrap.wrap('script = \"\"\"' + script.decode() + '\"\"\"')) + '\n')
            o.write('script = marshal.loads(base64.b64decode(script))\n')
            o.write('script = FunctionType(script, globals={\'__builtins__\': __builtins__})\n')
            o.write('script()\n')
