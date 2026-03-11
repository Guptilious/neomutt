#!/usr/bin/env python3

import os

toggle_file = "/tmp/neomutt_toggle_state"

if os.path.exists(toggle_file):
    os.remove(toggle_file)
    print("filtered")
else:
    open(toggle_file, "w").close()
    print("all")

