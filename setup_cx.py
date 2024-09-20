from cx_Freeze import setup, Executable
from modules.utils import absolute_path

build_exe_options = {
    "build_exe": absolute_path("dist"),
    "include_files": [
        absolute_path("FIX_SAVE - (Switch To Switch)"),
        absolute_path("MHGU-XX_TO_MHXX - (Switch To 3DS)"),
        absolute_path("MHXX_TO_MHGU-XX - (3DS To Switch)"),
        absolute_path("Blank_3DS_Save"),
        absolute_path("Blank_Switch_Save"),
        absolute_path("LICENSE"),
        absolute_path("README.md"),
    ],
    "zip_exclude_packages": [],
    "zip_include_packages": "*",
    "optimize": 2,
}

setup(
    name="MHXX-MHGU-Save-Converter",
    version="1.1.0",
    author="Alexander-Lancellott",
    description="MHXX-MHGU-Save-Converter",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            absolute_path("mhgu_mhxx_save_converter.py"),
            target_name="MHXX-MHGU-Save-Converter",
            base="console",
            icon=absolute_path("overlay.ico"),
        )
    ],
)