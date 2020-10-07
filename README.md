# Instagram Liking Bot

Automating likes on Instagram using [Selenium](https://www.selenium.dev/) and [ChromeDriver](https://chromedriver.chromium.org/).

## Prerequisites

 - First of all, you'll need to install the Python requirements using [pip](https://pip.pypa.io/en/stable/):
 
 ```bash
pip install -r requirements.txt
````

 - [Download the ChromeDriver](https://chromedriver.chromium.org/downloads) for your OS and the version of your computer's Google Chrome (you can use other drivers such as Mozilla Firefox WebDriver)
 
 - Create a **.txt** file with the hashtags that you want to like the related posts on Instagram (one hashtag per line). You can use the example file **hashtags.txt**
 
## Usage

To run the script, you'll need to give 2 arguments when running the Python code at the prompt:

 - **-t** or **--tags**: Here you'll give the path to the hashtag file;
 - **-d** or **--driver**: Here you'll give the path to the WebDriver file;
 
   ```bash
python auto_insta.py -t foo/foo/hashtags.txt -d foo/foo/chromedriver.exe
````
```bash
python auto_insta.py --tags foo/foo/hashtags.txt --driver foo/foo/chromedriver.exe
````

 - **-h** or **--help**: Will show you the options mentioned above.
 
```bash
 python auto_insta.py -h
````
```bash
 python auto_insta.py --help
````
