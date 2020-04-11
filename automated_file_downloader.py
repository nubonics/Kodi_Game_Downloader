from pyperclip import paste
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options


# LOCAL IMPORTS
from game_link_parser import strip_top_of_links_file
from xml_file_creation import add_game_element, create_xml_file
from settings2 import email, \
    password, student_id_number, \
    gecko_driver_path, \
    file_of_links


def remove_blank_lines():

    with open(file_of_links, 'r') as reader:
        fol = reader.readlines()

    with open(file_of_links, 'w') as writer:
        for line in fol:
            if not line.isspace():
                writer.write(line)


def build():
    options = Options()

    # init profile
    profile = webdriver.FirefoxProfile()

    # Block flash
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
    profile.set_preference("media.peerconnection.enabled", False)

    # save to FF profile
    profile.update_preferences()
    driver = webdriver.Firefox(profile, executable_path=gecko_driver_path, options=options)

    return driver


def download_file(driver, download_link):
    gdrive_url = "https://drive.google.com/drive/my-drive"
    colbycc_url = "https://colbycc.onelogin.com/"
    colbycc_portal_url = "https://colbycc.onelogin.com/portal/"

    driver.get(gdrive_url)

    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "identifier")))
    email_field.send_keys(email)
    email_field.send_keys(Keys.ENTER)

    while colbycc_url not in driver.current_url:
        sleep(0.5)

    student_id_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    student_id_field.send_keys(student_id_number)
    student_id_field.send_keys(Keys.ENTER)

    student_password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    student_password_field.send_keys(password)
    student_password_field.send_keys(Keys.ENTER)

    portal_counter = 0

    while colbycc_portal_url not in driver.current_url and portal_counter < 5:
        sleep(1)
        portal_counter += 1

    try:
        skip_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'skip')]")))
        skip_button.click()
    except TimeoutException:
        pass

    driver.get(download_link)

    while True:
        source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html")))
        source.send_keys(Keys.CONTROL, 'a')
        source.send_keys(Keys.CONTROL, 'c')

        data = paste()

        if "finished" in data:
            break
        else:
            sleep(1)

    data = data.replace('\n\n', '\n')
    data = data.replace('\n\n\n', '\n')

    with open(file_of_links, 'w') as writer:
        writer.write(data)

    # input('Does links.txt exist?')
    strip_top_of_links_file()
    remove_blank_lines()

    driver.close()
    driver.quit()

    with open(file_of_links, 'r') as reader:
        results = reader.readlines()

    for item in results:
        filename, link = item.split('https:')
        link = "https:" + link

        name = filename.rsplit('.')[0]

        link = str(link.split('&export')[0] + '&amp;name=/' + filename)
        # Hide link source
        link = link.replace('a/apps.losrios.edu/uc?id=', 'uc?export=download&id=')
        # Hide link source
        link = link.replace('a/colbycc.edu/uc?id=', 'uc?export=download&id=')

        add_game_element(game_name=name, rom_text=link)

    # This might need to be done better...
    # This will create an xml file at the very end of parsing the data...
    # Instead, it should be updated
    create_xml_file()


def afld(download_link):
    print('Automated game link downloader has started...')
    driver = build()
    download_file(driver, download_link)
    print('Automated game link downloader has completed...')


if __name__ == "__main__":
    afld(download_link)
