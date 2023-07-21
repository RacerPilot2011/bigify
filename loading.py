import sys
import time
import shutil

# Get the width of the terminal
terminal_width = shutil.get_terminal_size().columns

def load(say: str, until: int):
    t_end = time.time() + until
    sys.stdout.write(say + "...")
    sys.stdout.flush()
    while time.time() < t_end:
        for c in ['/', '-', '\\', '|']:
            sys.stdout.write('\b' + c)
            sys.stdout.flush()
            time.sleep(0.4)
    sys.stdout.write('\r' + ' ' * (terminal_width - len(say) - 3) + '\r')
    sys.stdout.write(say[:-3] + "ed\n")
    sys.stdout.flush()