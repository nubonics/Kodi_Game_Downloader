from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


file_of_links = 'links.txt'

email = "NULL"
password = "NULL"
student_id_number = "NULL"

# PARAMETERS YOU NEED TO CHANGE ARE BELOW
xml_base_directory = r"NULL"
xml_filename = r"C:\Users\USERNAME\KODI\portable_data\userdata\addon_data\plugin.program.iagl\dat_files/games.xml"
download_link = 'https://yasirkula.net/drive/downloadlinkgenerator/?state={"ids":["NULL"],"action":"open","userId":"NULL"}'
gecko_driver_path = r"C:\Users\USERNAME\webdrivers\geckodriver.exe"
firefox_binary_location = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")