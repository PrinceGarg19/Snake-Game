from cx_Freeze import setup, Executable


setup(
    name="Snake Game",
    version = "2.0",
    author = "Prince (Raaj)",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["main.jpg","music.wav","instruct.jpg","Home.wav","Game_over.wav","front.jpg","food.wav","food.jpg","font_1.ttf","font_2.ttf","font_3.ttf","cross.png","Button.wav"]},
            'bdist_msi': {"install_icon": "1.ico"}},
    executables = [Executable(r"C:\Users\princ\Documents\Project\Snake_game\Snake_Game.py",
                base = "Win32GUI",
                icon = r"1.ico",
                shortcutName = "Snake Game",
                shortcutDir = "DesktopFolder")]
    )
