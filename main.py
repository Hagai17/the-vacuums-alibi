"""Write one robot-vacuum excuse line to /output/entry.txt.

The line is a single line of at most 200 characters: the funniest excuse a
robot vacuum can give for missing a spot, in the machine's own deadpan voice.
"""

import os

LINE = (
    "I mapped that corner as 'stairs' in 2022. I would rather miss it forever "
    "than admit a mapping error in front of the thermostat."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
