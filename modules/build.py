import subprocess
import sys
import os
from shutil import copy, copytree, rmtree, ignore_patterns


def absolute_path(path: str = ''):
    return os.path.abspath(path).replace('\\modules', '')


def main():
    files_path = [
        'FIX_SAVE - (Switch To Switch)/fix_save.py',
        'MHGU_TO_MHXX - (Switch To 3DS)/mhgu_to_mhxx.py',
        'MHXX_TO_MHGU - (3DS To Switch)/mhxx_to_mhgu.py'
    ]

    if os.path.exists(absolute_path('dist')):
        rmtree(absolute_path('dist'))

    copytree(
        absolute_path('Blank_3DS_Save'),
        absolute_path('dist/Blank_3DS_Save'),
        symlinks=False, dirs_exist_ok=True
    )

    copytree(
        absolute_path('Blank_Switch_Save'),
        absolute_path('dist/Blank_Switch_Save'),
        symlinks=False, dirs_exist_ok=True
    )

    copy(
        absolute_path('README.md'), 
        absolute_path('dist/README.md')
    )

    copy(
        absolute_path('LICENSE'), 
        absolute_path('dist/LICENSE')
    )

    for file_path in files_path:
        path = absolute_path(file_path)
        src_path = os.path.dirname(path)
        dist_path = absolute_path(f'dist/{file_path.split("/")[0]}')

        copytree(
            src_path,
            dist_path,
            ignore=ignore_patterns('*.py'),
            symlinks=False, dirs_exist_ok=True
        )

        command_options = [
            'pyinstaller', '--onefile',
            '--distpath', dist_path,
            path
        ]

        if sys.platform == 'darwin':
            command_options.insert(2, '--target-architecture')
            command_options.insert(3, 'universal2')

        subprocess.run(command_options)


if __name__ == "__main__":
    main()
