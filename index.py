from dotenv import load_dotenv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Initialize the WebDriver
driver = webdriver.Chrome()

# Load environment variables from .env file
load_dotenv()

# Read email and password from environment variables
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
app_url = os.getenv("APP_URL")

try:
    print("Navigating to login page...")
    driver.get(app_url)
    time.sleep(1)

    print("Maximizing window...")
    driver.maximize_window()
    time.sleep(1)

    # User Login
    print("Entering username...")
    uname = driver.find_element(By.ID, 'ion-input-0')
    uname.send_keys(email)

    print("Entering password...")
    pwd = driver.find_element(By.ID, 'ion-input-1')
    pwd.send_keys(password)

    login_btn = driver.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-welcome/ion-content/ion-row/ion-col/div/form/ion-button')
    login_btn.click()

    print("Clicking Share Talent button...")

    # Wait for navigation and the Share Talent button to be clickable
    syt = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ShareTalentBtn"))
    )

    # Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView();", syt)

    print("Clicking Share Talent button...")
    syt.click()

    # Select Online Class Option
    print("Selecting Online Class Option...")
    onlineclass = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/ion-radio-group/ion-item[1]/ion-radio'))
    )

    # Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView();", onlineclass)

    onlineclass.click()

    print("Confirming Selection of Online Class Option...")

    # Wait for the button that becomes enabled after selecting Online Class
    select_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div/ion-button'))
    )

    # Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView();", select_button)

    print("Clicking Select button...")
    select_button.click()

    # Confirm Selection
    ok_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ion-overlay-4"]/div[2]/div[3]/button[2]'))
    )

    # Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView();", ok_btn)

    ok_btn.click()

    # Set start time (optimized)
    start_time_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div[1]/div/ion-row[1]/ion-col[1]/ion-item/ion-input/input'))
    )
    start_time_input.clear()  # Optional: clear input if needed
    start_time_input.send_keys("14:00")

    # Set end time (optimized)
    end_time_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div[1]/div/ion-row[1]/ion-col[2]/ion-item/ion-input/input'))
    )
    end_time_input.clear()  # Optional: clear input if needed
    end_time_input.send_keys("16:00")

    print("Selecting timezone...")
    # Select Timezone from Dropdown (Ion Select)
    # timezone_select = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//ion-select[@placeholder='Timezone']"))
    # )

    timezone_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div[1]/div/ion-row[1]/ion-col[3]/ion-item/ion-select'))
    )

    timezone_select.click()

    # Wait for the desired radio button (e.g., EST) to be clickable
    timezone_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(@class, "alert-radio-button") and .//div[contains(text(), "PST")]]'))
    )

    # Click the desired timezone option
    timezone_option.click()

    print("Clicking OK button...")

    # Wait for the OK button to be clickable
    ok_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "alert-button") and .//span[text()="OK"]]'))
    )

    # Click the OK button
    ok_button.click()

    # Click the toggle button
    # toggle_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div[1]/div/ion-row[2]/ion-col[1]/ion-item/ion-toggle'))
    # )

    # toggle_button.click()

    print("Setting start date...")

    # Set start date (optimized)
    start_date = WebDriverWait(driver, 35).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div[1]/div/ion-row[2]/ion-col[2]/ion-item/ion-input/input'))
    )
    start_date.clear()  # Optional: clear input if needed
    start_date.send_keys("10/15/2024")

    print("Setting end date...")

    # Set end date (optimized)
    end_date = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div[1]/div/ion-row[2]/ion-col[3]/ion-item/ion-input/input'))
    )
    end_date.clear()  # Optional: clear input if needed
    end_date.send_keys("10/11/2024")

    # Click the Save button (optimized)
    save_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH,
    '/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div[2]/ion-button[2]'))
    )
    save_button.click()


    print("Setting program title...")

    # Wait for the input field using the placeholder 'Enter Program title'
    program_title_label = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/ion-row[1]/ion-col[2]/ion-item'))
    )

    # Click the input field to trigger the label floating effect
    program_title_label.click()
    time.sleep(2)

    program_title = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Enter Program title "]'))
    )
    # Send keys to set the program title
    driver.execute_script("arguments[0].scrollIntoView();", program_title)
    program_title.send_keys("Classical dance")
    time.sleep(1)

    print("Setting program details...")

    # Step 1: Wait for the content editable div inside the ngx-editor to be visible
    editor_field = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ProseMirror.NgxEditor__Content'))
    )


    # Step 2: Use JavaScript to set the value of the content editable div
    program_details = "Here, we are ready to serve you by providing a Classical dance program in Orange County. Sign up today to secure your seat!"

    driver.execute_script("""
    arguments[0].innerHTML = arguments[1];
    """, editor_field, program_details)

    print("Program details set successfully!")

    # Set 3: Delay to see the result before continuing
    time.sleep(2)

    print("Setting capacity...")
    # Step 1: Wait for the input number field (e.g., identified by placeholder or name)
    capacity_field = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter Capacity "]'))
    )

    # Step 2: Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView(true);", capacity_field)

    # Step 3: Click on the field to bring it into focus
    capacity_field.click()  # This will activate the field and move the label
    time.sleep(2)

    # Step: 4 Send keys to set the program title
    capacity_field.send_keys("10")
    print("Capacity set successfully!")

    print("Selecting currency...")
    # Step 1: Wait until the ion-select element (the dropdown button) is clickable
    currency_dropdown = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'ion-select[aria-label*="Currency"]'))
    )

    # Step 2: Click the dropdown to display the options
    currency_dropdown.click()

    time.sleep(2)
    # Step 3: Select option
    desired_currency = WebDriverWait(driver, 30).until(
    # EC.element_to_be_clickable((By.XPATH, "//button[@aria-checked='false']//div[text()='INR']"))
    EC.element_to_be_clickable((By.XPATH, "//button[@role='radio']//div[text()='INR']"))

    )

    # Step 4: Click the desired currency option (e.g., INR)
    desired_currency.click()
    print("Currency set to INR successfully!")

    # Optional: Wait a bit before continuing
    time.sleep(2)

    # Step 5: Confirm the selection (if there's a confirmation button)
    # Scroll the OK button into view before clicking
    confirm_button = WebDriverWait(driver, 30).until(
    # EC.element_to_be_clickable((By.XPATH, "//button[@class='alert-button ion-focusable ion-activatable sc-ion-alert-ios']//span[text()='OK']"))
    EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/ion-app[1]/ion-alert[1]/div[2]/div[4]/button[2]"))

    )

    driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
    confirm_button.click()
    print("Setting cost")

    # Entering cost for the program by clicking in the input filed.

    cost = WebDriverWait(driver,30).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/ion-row[1]/ion-col[6]/ion-item/ion-input/input'))
    )
    # Entering desirable amount by using send keys.
    cost.send_keys("450")
    time.sleep(2)

    # selecting program level by selecting from the dropdown button.
    program_levelBox= WebDriverWait(driver,30).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/ion-row[1]/ion-col[7]'))
    )
    # click the input area to activate it
    program_levelBox.click()
    time.sleep(3)
    #
    # # selecting surface of program levels
    # leve_surface=WebDriverWait(driver,30).until(
    #     EC.element_to_be_clickable((By.XPATH,'//*[@id="ion-overlay-4"]/div[2]/div[3]'))
    # )

    # Selecting the program level by clicking in it.
    bigginer_level = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='radio']//div[text()='Intermediate']"))
    )

    #  click the label to see the check mar for final selection.
    bigginer_level.click()
    time.sleep(2)

    # # clicking in the ok button to confirm the program.
    ok_btn = WebDriverWait(driver,30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'button[class="alert-button ion-focusable ion-activatable sc-ion-alert-ios"]'))

    )
    ok_btn.click()
    time.sleep(5)
    print("Uploading cover photo...")

    print("Selecting categories")
    # Selecting  categories that are already present by default.
    add_category_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//ion-icon[@name="add"]'))
    )
    add_category_button.click()
    time.sleep(2)

    # Wait for the categories list to be visible
    categories_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'categories-list-wrapper'))
    )

    # Define the categories you want to select
    categories_to_select = ["Accounting", "Fashion", "Legal", "Technology"]

    for category_name in categories_to_select:
        # Scroll through the list and find each category by visible text
        category_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[text()='{category_name}']"))
        )

        # Scroll to each category
        driver.execute_script("arguments[0].scrollIntoView(true);", category_element)
        time.sleep(1)

        # Click the element using JavaScript to bypass any overlapping elements
        driver.execute_script("arguments[0].click();", category_element)

        # Click the category
        # category_element.click()

        print(f"Successfully selected the category: {category_name}")
        time.sleep(1)  # Pause briefly to observe the selection

    print("Save categories")
    # After selecting categories, wait for the save button to be clickable
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'save-btn'))
    )

    # Scroll to the save button if necessary
    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)

    # Click the save button using JavaScript
    driver.execute_script("arguments[0].click();", save_button)
    print("Save button clicked successfully!")
    print("Categories set successfully.")

    #Upload cover photo
    # Locate the file input element (you can use any method to locate it, here using class)
    file_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.choose-docs'))
    )

    # Scroll into view to avoid click interception
    driver.execute_script("arguments[0].scrollIntoView(true);", file_input)

    # Define the path to the file you want to upload
    file_path = os.path.abspath("files/img.png")  # Replace with your actual file path

    # Step 2: Upload the file using send_keys
    file_input.send_keys(file_path)
    print("File uploaded successfully!")
    time.sleep(3)


    # Selecting program host platform that are already present by default.
    program_host= WebDriverWait(driver,20).until(
     EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/ion-row[2]/ion-col/ion-item/ion-select'))
    )
    program_host.click()
    time.sleep(3)

    print("click in the program host options")

    google_meet=WebDriverWait(driver,40).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@id='alert-input-9-1']"))
    )
    google_meet.click()
    time.sleep(3)
    final_okbtn = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='ion-overlay-9']/div[2]/div[4]/button[2]"))
    )
    final_okbtn.click()
    time.sleep(3)


    save_and_continue = WebDriverWait(driver,30).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div/ion-button[2]'))
    )
    save_and_continue.click()
    time.sleep(6)

    # Upload final document
    # Locate the file input element (you can use any method to locate it, here using class)
    file_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.choose-docs'))
    )

    # Scroll into view to avoid click interception
    driver.execute_script("arguments[0].scrollIntoView(true);", file_input)

    # Define the path to the file you want to upload
    file_path = os.path.abspath("files/hanuman.jpg")  # Replace with your actual file path

    # Step 2: Upload the file using send_keys
    file_input.send_keys(file_path)
    print("File uploaded successfully!")
    time.sleep(3)



    # review
    # Wait for the "Review" button to be clickable using its visible text
    review_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,".save-button.ios.button.button-round.button-solid.ion-activatable.ion-focusable.hydrated"))
    )
    review_button.click()
    time.sleep(3)

    # semi_final_review

    semi_review_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='action-sheet-group sc-ion-action-sheet-ios'] button:nth-child(1)"))
    )
    semi_review_button.click()
    time.sleep(3)
    print("click review button successfully")


    #publish button
    # Wait for the "Review" button to be clickable using its visible text
    # publish_buttons = WebDriverWait(driver, 50).until(
    #     EC.visibility_of_all_elements_located((By.XPATH,"/html[1]/body[1]/app-root[1]/ion-app[1]/ion-router-outlet[1]/app-create-program[1]/ion-content[1]/ion-row[1]/ion-col[1]/div[1]/div[2]/div[1]/div[1]/ion-button[2]"))
    # )
    print("click publish button")

    publish_buttons = WebDriverWait(driver, 50).until(
        EC.visibility_of_all_elements_located((By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-create-program/ion-content/ion-row/ion-col/div/div[2]/div/div/ion-button[2]'))
    )
    # Select the first element from the list of elements
    publish_button = publish_buttons[0]
    # Scroll into view to avoid click interception
    driver.execute_script("arguments[0].scrollIntoView(true);", publish_button)
    publish_button.click()
    time.sleep(3)

    final_ok= WebDriverWait(driver,30).until(
        EC.element_to_be_clickable((By.XPATH,"//button[@class='alert-button ion-focusable ion-activatable alert-button-role-cancel sc-ion-alert-ios']"))
    )
    final_ok.click()
    time.sleep(3)

finally:
       #lose the browser after completion
    time.sleep(5)  # Pause to see the result before closing (optional)
    driver.quit()