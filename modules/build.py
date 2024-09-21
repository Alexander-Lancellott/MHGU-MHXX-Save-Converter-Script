# import subprocess
# import sys
# import os
# from shutil import copy, copytree, rmtree, ignore_patterns
# from modules.utils import absolute_path


# def main():
#     paths = [
#         'FIX_SAVE - (Switch To Switch)',
#         'MHGU-XX_TO_MHXX - (Switch To 3DS)',
#         'MHXX_TO_MHGU-XX - (3DS To Switch)'
#     ]

#     if os.path.exists(absolute_path('dist')):
#         rmtree(absolute_path('dist'))

#     copytree(
#         absolute_path('Blank_3DS_Save'),
#         absolute_path('dist/Blank_3DS_Save'),
#         symlinks=False, dirs_exist_ok=True
#     )

#     copytree(
#         absolute_path('Blank_Switch_Save'),
#         absolute_path('dist/Blank_Switch_Save'),
#         symlinks=False, dirs_exist_ok=True
#     )

#     copy(
#         absolute_path('README.md'),
#         absolute_path('dist/README.md')
#     )

#     copy(
#         absolute_path('LICENSE'),
#         absolute_path('dist/LICENSE')
#     )

#     for path in paths:
#         src_path = absolute_path(path)
#         dist_path = absolute_path(f'dist/{path}')

#         copytree(
#             src_path,
#             dist_path,
#             ignore=ignore_patterns('*.py'),
#             symlinks=False, dirs_exist_ok=True
#         )

#     command_options = [
#         'pyinstaller', '--onefile', '--name', 'MHXX-MHGU-Save-Converter',
#         '--distpath', absolute_path('dist'),
#         absolute_path('mhgu_mhxx_save_converter.py')
#     ]

#     if sys.platform == 'darwin':
#         command_options.insert(2, '--target-architecture')
#         command_options.insert(3, 'universal2')

#     subprocess.run(command_options, check=False)



# if __name__ == "__main__":
#     main()

import os
import subprocess
from modules.utils import absolute_path


def main():
    path = absolute_path("setup_cx.py")
    py_path_unix = absolute_path(".venv/bin/python")
    py_path_win = absolute_path(".venv\\Scripts\\python")

    if os.name == 'posix':
        command_options = [py_path_unix, path, "build"]
    else:
        command_options = [py_path_win, path, "build"]

    subprocess.run(command_options, check=False)


if __name__ == "__main__":
    main()
