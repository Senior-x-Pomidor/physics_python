# Ball Simulator (Terminal)

A simple terminal-based ball simulator written in Python. The ball (`O`) moves inside a rectangular field bordered by `#`, bouncing off the walls with slight damping. The field dynamically adapts to your terminal size.

---

## Features

- Ball moves and bounces inside the terminal.
- Speed is slightly damped on collisions.
- Field adapts to terminal size.
- Press any key to exit the simulation.

---

## Requirements

- Python 3.x
- `curses` module  
  - Built-in on Unix/Linux/macOS  
  - On Windows, install `windows-curses`:

```bash
pip install windows-curses
