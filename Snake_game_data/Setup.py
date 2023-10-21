from cx_Freeze import setup, Executable

setup(       
        name = 'Snake Game',
        version = "1.0",
        description = "Control Snake and eat food. ENJOT!",
        executables = [Executable(r"Snake_Game.py")]
)