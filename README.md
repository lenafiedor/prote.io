# prote.io :snake:

This is a version of snake game for biological freaks. Collect all the aminoacids to get the longest peptide possible!

## Installing the dependencies
This project has been created with `pypoetry` package and all dependencies are written in the `pyproject.toml` file. To install them, you need to have poetry installed first. Then you can get all necessary dependencies by executing one line of code.

```
pip install poetry
poetry install
```

## Running the game
Once you've installed all necessary packages, it's time to play. To start the game, open the main prote.io directory and execute the script.

```
cd path/to/prot.io
./snake_game.sh
```

## Rules
They are as simple as possible. Move the snake with **W, A, S, D** keys and collect as many aminoacids as you can. The game engine is keeping track of them, so do not get distracted!<br>
And, last but not least - remember not to bite your own tail.

## Monitoring CPU usage
This game has a built-in function used for monitoring CPU usage over the time. It is a decorator which tracks CPU usage every 1 second.<br>
Exemplary results:
![Very nice CPU plot](plots/cpu_usage.png)

## Have fun creating your own peptide! :shipit:
