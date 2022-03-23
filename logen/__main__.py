"""
    LOGEN
    Simple Changelog Generator for Github Log
    Copyright (C) 2022

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Description:
        Logen use github log to generate cheangelog

    Author:
        Bengart Zakhar
"""

#!/opt/ziem/venv/bin/python
import os
import sys
import argparse
import pkg_resources

from logen.logen import main

def showlicense():
    license = ('Simple Changelog Generator for Github Log\n'
               'Copyright (C) 2021 Bengart Zakhar\n\n'
               'This program is free software: you can redistribute it and/or modify\n'
               'it under the terms of the GNU General Public License as published by\n'
               'the Free Software Foundation, either version 3 of the License, or\n'
               '(at your option) any later version.\n\n'
               'This program is distributed in the hope that it will be useful,\n'
               'but WITHOUT ANY WARRANTY; without even the implied warranty of\n'
               'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n'
               'GNU General Public License for more details.\n\n'
               'You should have received a copy of the GNU General Public License\n'
               'along with this program.  If not, see <https://www.gnu.org/licenses/>.')
    print(license)

if __name__ == "__main__":
    version = pkg_resources.get_distribution('logen').version
    print('ZLOG {} Simple Changelog Generator for Github Log\n'
          'Copyright (C) 2021 Bengart Zakhar\n'
          'This program comes with ABSOLUTELY NO WARRANTY\n'
          'This is free software, and you are welcome to redistribute it\n'
          'under certain conditions; type `--license` for details.\n'.format(version))
    print(' _____   __    ____  ______\n'\
          '/__  /  / /   / __ \/ ____/\n'\
          '  / /  / /   / / / / / __  \n'\
          ' / /__/ /___/ /_/ / /_/ /  \n'\
          '/____/_____/\____/\____/   \n')
    parser = argparse.ArgumentParser(
        prog='logen', 
        usage='%(prog)s [options]')
    parser.add_argument(
        "-g", 
        "--generate", 
        help="Generate Changelog file from git logs", 
        action="store_true")
    parser.add_argument(
        "-o", 
        "--output", 
        help="Save to file", 
        action="store_true")
    parser.add_argument(
        "-f", 
        "--format", 
        help="Choose format md, txt", 
        action="store_true")
    args = parser.parse_args()
    if args.generate:
        print('\n[*] Generate Changelog file\n----------------')
        main()
    elif args.output:
        print(2)
    elif args.format:
        print(3)
    else:
        parser.print_help()
        sys.exit(1)
