
import argparse
import sys

from pathlib import Path
from glob import glob
from uuid import uuid4


# def set_range(value):
#     value_ = int(value)
#     if value_ < 50 or value_ > 800:
#         raise argparse.ArgumentTypeError('%s is an invalid value, choose from range [50-800]' % value)
#     return value_


def set_arguments():
    # Available Inputs
    available_options = ['mk', 'ren', 'del']
    available_lists =  ['frt', 'num']
    available_renames = ['num', 'uuid']

    # Required Arguments
    parser = argparse.ArgumentParser(description='File Modificator', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('IN_FOLDER', type=str, help='Input folder')
    
    # Optional Arguments
    parser.add_argument('-o', '--options', choices=available_options,
            type=str, default='mk', help='''Available Options: ['mk': create files, 'ren': rename files, 'del': delete files]''')
    parser.add_argument('-l', '--lists', choices=available_lists, type=str, default='num',      
            help='''Available Lists: ['frs': fruits, 'num': numbers from 1-10]''')
    parser.add_argument('-m', '--modes', choices=available_renames,
        type=str, default='num', help='''Available Rename Modes: ['num': numbers, 'uuid': uuid4]''')


    # Set Argument Parser
    args = parser.parse_args()

    return args


class FolderCreator:
    def __init__(self, in_folder, options, lists, modes):
        self.in_folder = in_folder
        self.options = options
        self.lists = lists
        self.modes = modes

    
    def initialize_lists(self):
        if self.lists == 'frt':
            return ['Apple', 'Mango', 'Durian', 'Papaya', 'Orange', 'Kiwi', 'Melon', 'Watermelon']

        elif self.lists == 'num':
            return list(range(0, 11))
        
        return list()
    

    def initialize_modes(self, index):
        if self.modes == 'uuid':
            return uuid4()
    
        elif self.modes == 'num':
            return index


    def methods_manager(self):
        if self.options == 'mk':
            items = self.initialize_lists()
            self.create_files(items=items)

        elif self.options == 'ren':
            self.rename_files()

        elif self.options == 'del':
            self.delete_files()


    def create_files(self, items):
        try:
            Path(self.in_folder).mkdir(parents=True, exist_ok=False)

            for item in items:
                Path(f'{self.in_folder}/{item}.txt').touch(exist_ok=True)

            sys.stdout.write(f'Saving in {Path(self.in_folder).resolve()}\n')
            sys.stdout.write('Successful')

        except FileExistsError:
            sys.stdout.write('FileExistsError')
            sys.exit(0)


    def rename_files(self):
        if not Path(f'{self.in_folder}/').exists():
            sys.stdout.write('Folder does not exist')
            sys.exit(0)

        else:
            try:
                items = glob(f'{self.in_folder}/*.txt')

                for index, item in enumerate(items):
                    old_item = Path(item)
                    new_item = self.initialize_modes(index)
                    old_item.rename(f'{self.in_folder}/{new_item}.txt')
                
            except FileExistsError:
                sys.stdout.write('FileExistsError')
                sys.exit(0)

            sys.stdout.write('Successful')



    def delete_files(self):
        if not Path(f'{self.in_folder}/').exists():
            sys.stdout.write('Folder does not exist')
            sys.exit(0)

        else:
            # parent = Path.cwd()
            # child = Path(self.in_folder).resolve()

            # if parent not in child.parents:
            #     sys.stdout.write('Incorrect directory, do not use ".."')
            #     sys.exit(0)

            # try:
            #     items = glob(f'{self.in_folder}/*.txt')

            #     for item in items:
            #         Path(item).unlink(missing_ok=False)
            #     Path(self.in_folder).rmdir()

            # except FileNotFoundError:
            #     sys.stdout.write('FileNotFoundError')
            #     sys.exit(0)

            sys.stdout.write('Successful')

        
if __name__ == '__main__':
    args = set_arguments()
    
    name = input('What is your name? ')
    print(f'Your name is {name}\n')

    options_map = {'mk': 'make', 'ren': 'rename', 'del': 'delete'}
    print(f'You have selected the IN_FOLDER "{args.IN_FOLDER}" & OPTION "{options_map.get(args.options)}"')
    print(f'Your selected LIST is "{args.lists}" & rename MODE is "{args.modes}"\n')

    folder_creator = FolderCreator(args.IN_FOLDER, args.options, args.lists, args.modes).methods_manager()
    

    

    