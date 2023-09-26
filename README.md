# Auto-iClicker
This script automatically opens an iClicker course and responds with the "A" answer. Perfect for courses where iClicker is participation only.  

## Setup Instructions
1. Ensure that you have Python installed. Visit [this link](https://www.python.org/downloads/) if you need to install it.
2. Make sure you have Google Chrome installed. [Download it here](https://support.google.com/chrome/answer/95346) if it is not installed already.
3. Open Google Chrome and visit `chrome://version/` to check the browser version
4. Visit this [link](https://chromedriver.storage.googleapis.com/index.html) and find the folder with the closest version to your Google Chrome version
5. Download the appropriate zip file for your system (Windows, Mac, or Linux) and extract the contents
6. Put `chromedriver.exe` in the same folder as the scripts (inside of [`src`](/src))
7. Make sure Selenium is installed for Python. See [this link](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/) for installation instructions.
8. Open your terminal and make sure you are in the right folder ([`src`](/src)). You can use `ls` to look at the folders in your current folder and use `cd FOLDER-NAME` to enter the folder. For example, the last folder movement should be `cd src`. You can do `cd ..` to exit your current folder and go to the parent one.
9. Run `cp setup-example.py setup.py` which will make a copy of [`setup-example.py`](/src/setup-example.py) and name it `setup.py`
10. Inside of `setup.py` configure the following:
- add your iClicker username and password
- add your class name, caps and space-specific
- copy your course page URL - this is the page you see immediately after clicking on the course, before you click the join button
- set how often the script will click a poll response and how long the script will wait until the join button shows up

## Running Instructions
Once in the src folder,
```python iClicker.py```.
