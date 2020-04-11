from shutil import move
from os import remove
from os.path import exists

# LOCAL IMPORTS
from settings2 import file_of_links
from xml_file_creation import add_game_element, create_xml_file, header_initialization


def strip_top_of_links_file():
    tag = 'Status: finished'
    tag_found = False

    tmp_file = 'tmp.txt'

    with open(file_of_links, encoding="utf8") as in_file:
        with open(tmp_file, 'w', encoding="utf8") as out_file:
            for line in in_file:
                if not tag_found and line.strip() == tag:
                    tag_found = True
                    continue

                if tag_found:
                    out_file.write(line)

    move(tmp_file, file_of_links)
    if exists(tmp_file):
        remove(tmp_file)


def game_link_parser():
    with open(file_of_links, 'r') as reader:
        results = reader.readlines()

    # Remove blank lines from the links file
    with open(file_of_links, 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()

    header_initialization()

    for l in results:
        name = l.split('https:')[0]
        link = l.split('https:')[1].split('.com/')[1].split('&export=download')[0] + "&name=/" + l.split('https:')[0].rstrip(' ')

        try:
            # This needs to be replaced with a regex
            link = link.split('a/colbycc.edu/')[1]
        except IndexError:
            pass
        try:
            link = link.split('a/losrios.edu/')[1]
        except IndexError:
            pass

        add_game_element(game_name=name, rom_text=link)

    create_xml_file()


if __name__ == "__main__":
    game_link_parser()
