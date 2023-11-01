from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import shutil
import os

# Define the relative paths for image and SVG files
image_folder = 'png'
svg_folder = 'svg'

# Get the absolute path of the current working directory
current_directory = os.getcwd()

# Create the absolute path for the image file to upload
file_to_upload = os.path.abspath(os.path.join(current_directory, image_folder, os.listdir(image_folder)[0]))

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://online.rapidresizer.com/tracer.php')

try:
    # Click "Upload a file to trace" button
    upload_button = driver.find_element(By.NAME, 'traceFile')
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
