# 109-資料處理科一年級【程式語言與設計】

=====================

下載Chrome Driver
	`https://chromedriver.chromium.org/downloads`

install selenium
```
	pip install selenium
```

Getting started`https://chromedriver.chromium.org/getting-started`
```
	import time
	from selenium import webdriver

	driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
	driver.get('http://www.google.com/');
	time.sleep(5) # Let the user actually see something!
	search_box = driver.find_element_by_name('q')
	search_box.send_keys('ChromeDriver')
	search_box.submit()
	time.sleep(5) # Let the user actually see something!
	driver.quit()
```


select file
```
	cd /.../
	git add README.md
	git commit -m 'add google API use import selenium'
	git push
	username/mail
	password
```

error use `git pull`