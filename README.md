# Django
## 前置作業
#### 先在虛擬環境安裝套件：
* django
* pylint
* pylint_django
* autopep8
* psycopg2 (連線到postgresSQL)

#### VScode延伸模組安裝：
* Python
* code runner
* Django
* Django Template

#### 開新專案
* 終端機中輸入指令
`django-admin.py startproject mysite`
* 切到 mysite 資料夾後啟動django內建伺服器
`python manage.py runserver`

## 觀念
##### 三振法則
* 確認每個範本(template)裡重複的部分
* 將重複出現的資料放到base template,然後定義一些區域標籤(block tag),讓其他範本可以置換區塊內容
* 其他的範本繼承基礎範本,並各自設定區塊的內容

##### 後端安全系統
* 在function前加上 `@login_required` ,表示必須為登入狀態才能執行該function
