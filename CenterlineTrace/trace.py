from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil

# Set the path to ChromeDriver
# Get the current working directory
current_directory = os.getcwd()

# Define the relative path to chromedriver.exe
chromedriver_path = os.path.join(current_directory, 'chromedriver.exe')

# Define the relative paths for image and SVG files
image_folder = os.path.join(current_directory, 'png')
svg_folder = os.path.join(current_directory, 'svg')

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://online.rapidresizer.com/tracer.php')

try:
    wait = WebDriverWait(driver, 10)

    # Click "Upload a file to trace" button
    upload_button = driver.find_element(By.NAME, 'traceFile')
    file_to_upload = os.path.join(image_folder, os.listdir(image_folder)[0])
    upload_button.send_keys(file_to_upload)
    time.sleep(4)

    # Change file format to SVG
    trace_format = Select(driver.find_element(By.NAME, 'traceFormat'))
    trace_format.select_by_value('svg')

    # Click on "Centerline" radio button
    radio_button = driver.find_element(By.CSS_SELECTOR, 'input[value="centerline"]')
    driver.execute_script("arguments[0].click();", radio_button)
    time.sleep(1)

    # Click the "Download" button
    download_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Download"].traceImage.btn.btn-default.btn-block')
    download_button.click()

    # Find the most recently downloaded SVG file in the Downloads folder
    downloaded_file = max([os.path.join(os.path.expanduser('~'), 'Downloads', file) for file in os.listdir(os.path.expanduser('~') + '\\Downloads')], key=os.path.getctime)

    # Get the destination file name with a consecutive number
    destination_folder_contents = os.listdir(svg_folder)
    destination_base_name = os.path.basename(downloaded_file)
    base_name, ext = os.path.splitext(destination_base_name)
    destination_number = 1

    while destination_base_name in destination_folder_contents:
        destination_base_name = f"{base_name}_{destination_number}{ext}"
        destination_number += 1

    destination_path = os.path.join(svg_folder, destination_base_name)

    # Move the downloaded SVG to the desired folder
    shutil.move(downloaded_file, destination_path)
    
    time.sleep(3)
    print(f"Downloaded SVG: {destination_path}")

finally:
    # Close the browser
    driver.quit()
