from os import remove

from automated_file_downloader import afld
from game_link_parser import game_link_parser
from settings2 import file_of_links

if __name__ == "__main__":
    afld()
    game_link_parser()
    remove(file_of_links)
    remove('geckodriver.log')
