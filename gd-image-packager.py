import tarfile
import os
import shutil

def fatal_error(prompt: str, reason: str) -> None:
    print(f'[ FATAL ERROR | {prompt} ]: {reason}')
    print('KILLING PROCESS WITH STATUS OF 1')
    shutil.rmtree('gdimage')
    exit(1)


def compile_gdimage(pd: str, ad: str) -> None:
    print('\nCOMPILING!\n')

    print('Copying GD Files')
    print('  Copying GD Program Files')
    shutil.copytree(pd, 'gdimage/progfiles')
    print('  Copying GD AppData Files')
    shutil.copytree(ad, 'gdimage/appdata')

    print('Writing installation metadata')
    print('  Target install files')
    with open('gdimage/data/procfiles.target', 'w') as file:
        file.write(pd)
    with open('gdimage/data/appdata.target', 'w') as file:
        file.write(ad)
    
    print('Compressing image files')
    tar = tarfile.TarFile('geometrydash.gdimg', 'w')
    tar.add('gdimage/data')
    tar.add('gdimage/progfiles')
    tar.add('gdimage/appdata')
    tar.close()

    print('Cleaning up')
    shutil.rmtree('gdimage')

    print('\nOUTPUT: ./geometrydash.gdimg')
    print('  Exiting with status of 0')
    exit(0)

if __name__ == '__main__':
    os.mkdir('gdimage')
    os.mkdir('gdimage/data')

    program_dir = input('GD Program Files directory: ')
    if not os.path.exists(program_dir):
        fatal_error('DIRNOTFOUND', 'No such directory')
    data_dir = input('GD AppData directory: ')
    if not os.path.exists(data_dir):
        fatal_error('DIRNOTFOUND', 'No such directory')
    
    print('\nCURRENT SETUP:')
    print(f'  GD Program directory: {program_dir}')
    print(f'  GD AppData directory: {data_dir}\n')
    yorn = input('Would you like to compile GDIMAGE (Y or n): ')
    if yorn.lower() == 'y':
        compile_gdimage(program_dir, data_dir)
    elif yorn.lower() == 'n':
        print('\nCANCELLING INSTALLATION')
        shutil.rmtree('gdimage')
        exit(0)
    else:
        print('\nINVALID OPTION, Assuming cancellation')
        shutil.rmtree('gdimage')
        exit(0)
