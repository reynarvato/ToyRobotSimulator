# Toy Robot Simulator

An application that simulates a toy robot moving on a 5x5 tabletop. The robot can be placed, moved, and rotated via text commands, with boundary checking to prevent it from falling off the table.

## Requirements

- Python 3.7+
- No external dependencies

## Usage

Edit `robot/commands.txt` with your commands (one per line), then run:

```
cd robot
python main.py
```

## Commands

| Command | Description |
|---|---|
| `PLACE X,Y,F` | Place the robot at position (X,Y) facing F (NORTH, SOUTH, EAST, or WEST). The origin (0,0) is the south-west corner. |
| `MOVE` | Move the robot one unit forward in the direction it is facing. Ignored if it would fall off the table. |
| `LEFT` | Rotate the robot 90 degrees left. |
| `RIGHT` | Rotate the robot 90 degrees right. |
| `REPORT` | Print the robot's current position and direction. |

All commands before a valid `PLACE` are ignored. Invalid or unrecognised commands are silently discarded.

## Example

Input:
```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

Output:
```
3,3,NORTH
```

## Project Structure

```
robot/
├── robot.py            # Robot and Table classes
├── main.py             # Simulator logic and entry point
├── test_simulator.py   # Unit tests
└── commands.txt        # Input commands
```

## Running Tests

```
cd robot
python -m unittest test_simulator -v
```

### Test cases from the brief

| Test | Input | Expected Output |
|---|---|---|
| a | PLACE 0,0,NORTH → MOVE → REPORT | 0,1,NORTH |
| b | PLACE 0,0,NORTH → LEFT → REPORT | 0,0,WEST |
| c | PLACE 1,2,EAST → MOVE → MOVE → LEFT → MOVE → REPORT | 3,3,NORTH |

### Additional edge case tests

| Test | Input | Expected Output | What it checks |
|---|---|---|---|
| d | MOVE → PLACE 0,0,NORTH → REPORT | 0,0,NORTH | MOVE before PLACE is ignored |
| e | PLACE -1,-1,NORTH → REPORT | *(no output)* | Out-of-bounds PLACE is ignored |
| f | PLACE 0,0,SOUTH → MOVE → REPORT | 0,0,SOUTH | MOVE off the table edge is blocked |
| g | PLACE 1,1,NORTH → LEFT → REPORT | 1,1,WEST | LEFT rotates NORTH to WEST |
| h | PLACE 0,0,NORTH → PLACE 3,3,NORTH → REPORT | 3,3,NORTH | Second PLACE replaces the first |
| i | testing123 1,2,WEST → PLACE 0,0,NORTH → REPORT | 0,0,NORTH | Unrecognised commands are ignored |