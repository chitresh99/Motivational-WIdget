from cx_Freeze import setup, Executable

setup(
    name="MotivationalPuppet",
    version="1.0",
    description="A motivational puppet application",
    executables=[Executable("main.py")]
)
