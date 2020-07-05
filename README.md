This is, for now, just a personal project to try things with a python project.

If you want to try it yourself:

- download Python (I work with 3.83.3, but I don't think I use many new features)
- install pygame (I work with 1.9.6)
- run with the command "python -m src"

Here is a list of the different things you can do now:

Title screen:
On launch, a title screen appears on a blue background.
The title rises, and buttons appear. You can rotate between them with the arrows, and select some of them with the spacebar.
You have:
- the reset button that resets the title page.
- the quit button that closes the game.
- the battle button that launch a sample battle.

Battle mode:
For now, a map appear with a cursor on it. You can't do anything yet.
The camera is linked to the position of the cursor. To try it, modify the cursor position in Data/Maps/sample.py, in init_cursor, and re-launch the game. Try a valid position (on the grid), else the camera won't follow it.