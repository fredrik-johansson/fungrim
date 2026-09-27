import os
import sys

# Make the Fungrim snapshot (and the grim2mathjson package) importable when
# pytest is invoked from anywhere.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
