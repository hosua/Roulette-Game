import cx_Freeze, os
executable = [cx_Freeze.Executable("Roulette_GUI_V2.py")]

cx_Freeze.setup(
    name = "Roulette V2",
    options={"build_exe": {"packages":["tkinter", "random", "string", "PIL", "functools"],
                           "include_files": ["Roulette_table.png", "Roulette_wheel.png", "roulette_ball.png",
                                             "win_ball.png", "lose_ball.png", "ka-ching.mp3", "lose.mp3"]}},
    executables = executable

)