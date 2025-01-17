# Importing Libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import re

# Adding Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Creating WebDriver instance
wd = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)

# Get the main page
wd.get("https://www.wikipedia.org/")

# Assertion statement
assert "Wikipedia" in wd.title

# Print the entire HTML
# print(wd.page_source)

# Fetching the element by ID
input_element = wd.find_element(by=By.ID, value="searchInput")

# Sending keys
input_element.send_keys('ASD')

# Fetch search button through CSS class name
search = wd.find_element(by=By.CLASS_NAME, value="pure-button")

# Click the search button
wd.execute_script("arguments[0].click();", search)

# Switching windows
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# Assertion statement
assert "ASD - Wikipedia" in wd.title

# Fetch search button through line text
link_text = wd.find_element(By.LINK_TEXT, "Adaptive software development")

# Clicking the link
wd.execute_script("arguments[0].click();", link_text)

# Switching window
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# Assertion statement
assert "Adaptive software development - Wikipedia" in wd.title

# Fetch all elements with <p> tags
p_tags = wd.find_elements(by=By.TAG_NAME, value="p")
print("Number of tags found:", len(p_tags))

# Extract text from all elements
text_lines = ''
for p_tag in p_tags: 
    text_lines = p_tag.text

#print(text_lines)

# Match all digits within square brackets in the string and replace the m with an empty string 
pattern = r'\[[0-9]\]'
new_string = re.sub(pattern, '', text_lines)

# print(new_string)

# Extract nested elements using CSS selector 
elems = wd.find_elements(by=By.CSS_SELECTOR, value='p > a')

# Creating dictionary
link_dict = {}
for elem in elems: 
    link_dict[elem.text] = elem.get_attribute('href')
print(link_dict)

# Save Dictionary to File 
f = open("links.txt", "w")
print("Writing to file...")
for key in link_dict: 
    f.write(f'{key}\n')
    f.write(f'{link_dict[key]}\n\n')
f.close()
print('Written to file')
print("Successfully loaded the page ",wd.title)