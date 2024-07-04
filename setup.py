from cx_Freeze import setup, Executable

setup(
    name="Daffodil",
    version="1.0",
    description="MP3 downloader",
    executables=[Executable("main.py", base=None)]
)
