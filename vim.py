from os import makedirs, path, system
from platform import system as get_OS
from shutil import copyfile

FILEPATH = path.split(path.abspath(__file__))[0]
ISWINDOWS = get_OS() == "Windows"
HOME_DIR = path.expanduser("~")
DIRS = ["backup", "swp", "undo"]
VIMRC_NAME = f"{'_' if ISWINDOWS else '.'}vimrc"


def create_dot_vim_dir():
    try:
        for dir in DIRS:
            makedirs(fr"{HOME_DIR}/.vim/{dir}")
    except OSError:
        print("Error while creating .vim dir")
    else:
        print("~/.vim created")


def install_vimplug():
    if ISWINDOWS:
        cmd = "iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |` ni $HOME/vimfiles/autoload/plug.vim -Force"
    else:
        cmd = "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
    system(cmd)


def copy_vimrc():
    try:
        copyfile(fr"{FILEPATH}/vimrc", fr"{HOME_DIR}/{VIMRC_NAME}")
    except IOError:
        print("Error while copying vimrc file")
    else:
        print("vimrc copied to", HOME_DIR)


create_dot_vim_dir()
install_vimplug()
copy_vimrc()