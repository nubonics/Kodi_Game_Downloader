from lxml import etree

# LOCAL IMPORTS
from settings2 import xml_filename


root = etree.Element("datafile")
header = etree.SubElement(root, "header")


def header_initialization():
    header_pairs = {"emu_name": "Nintendo Entertainment System",
                    "emu_description": "Nintendo Entertainment System",
                    "emu_baseurl": "https://drive.google.com/",
                    "emu_downloadpath": "default",
                    "emu_postdlaction": "unzip_rom",
                    }

    for key, value in header_pairs.items():
        add = etree.SubElement(header, key)
        add.text = value


def create_xml_file():
    data = etree.tostring(root, xml_declaration=True, pretty_print=True, encoding='UTF-8')
    with open(xml_filename, 'wb') as writer:
        writer.write(data)


def add_game_element(game_name, rom_text):
    game_name = game_name.rsplit('.')[0]
    game = etree.SubElement(root, 'game')
    game.set('name', game_name)
    description = etree.SubElement(game, 'description')
    description.text = game_name
    rom = etree.SubElement(game, 'rom')
    rom.set('name', rom_text)
    rom.set('size', '0')


if __name__ == "__main__":
    # Add the header elements to the xml file
    header_initialization()
