pip - The Python Package Installer
`https://pip.pypa.io/en/stable`
```
	apt-get install python-pip
	pip --version
	pip install virtualenv
	pip install -v virtualenv==20.2.1
	pip install -u virtualenv
```

created project directory
```
	mkdir -pv selenium-fireofx/drivers
	cd selenium-firefox/
	virtualenv .venv
	source .env/bin/activate
	pip install selenium
	deactivate
```

sample code
```
	from selenium import webdriver

	driverpath = "/Users/max/Documents/chromedriver"
	driver = webdriver.Firefox(excutable_path=driverpath)
	driver.get("http://tw.yahoo.com/")
```

ex00.py
```
	frome selenium import webdriver
	frome selenium.webdriver.common.keys import keys
	browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
	browser .get('https://www.linuxhint.com')
	print('Title: %s' % browser.title)
	browser.quit()
```