# this sol'n is from u/Specter_Terrasbane
wires = 'white\nred\ngreen\nwhite'
import re

_PATTERN = re.compile(r'\A(w[prgo]|rg|b[bpr]|o[rb]|g[ow]|p[rb])\Z')

def disarm(wires):
    colors = ''.join(line[0] for line in wires.splitlines())
    result = all(_PATTERN.match(a + b) for a, b in zip(colors, colors[1:]))
    return 'Bomb defused' if result else 'Boom'

print disarm(wires)
