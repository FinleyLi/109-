# 109-資料處理科一年級【程式語言與設計】
### 參考書籍【Python程式語言與設計(上)】 - 旗立出版
### 軟體版本【Anaconda】 - 1.9.12，【Python】 - 3.8.3

##### 評分方式
=====================
第一次段考: 筆試

第二次段考: 上機實作

第三次段考: 學習歷程報告

作業: 程式實作
=====================

# 109-TSH_Python_3.8.3
紀錄109學年度資處科一年級程式語言與設計的上課範例

###git setup

install git
```
	apt-get install git
	git --version
```

setup account
```
	git config --global user.name "<>"
	git config --global user.email "<>"
```

add repository
```
	mkdir helloGit
	cd helloGit
	git init
	ls -la
```

watch status
	`git status`

clone SSH
	`git clone git@github.com:FinleyLi/109-TSH_Python_3.8.3.git`

clone HTTPS
	`git clone https://github.com/FinleyLi/109-TSH_Python_3.8.3.git`

select file
```
	cd /github/109.../
	git add README.md
	git commit-m 'add git clone use and push'
	git push
	username/mail
	password
```

error use `git pull`