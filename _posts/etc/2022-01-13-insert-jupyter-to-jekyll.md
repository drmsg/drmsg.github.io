---
permalink: /insert-jupyter-to-jekyll
title: "[Jekyll] post에 jupyter notebook 넣기"

categories: 
  - "github-page"
tags: 
  - jupyter
  - notebook
  - jekyll
  - githubpage

toc: true
toc_sticky: true

comments: true

date: 2022-01-13
---
> **한 줄 요약: iframe으로 html을 넣으면 된다.**

---
### Simple 3 Step
이는 가장 쉽게 해결할 수 있는 방법이다. 좀 더 깔끔하게 하게 해결하고 싶다면 글 마지막의 최종 버젼을 보면 된다.

**Step1. jupyter notebook file을 html로 변환 (두 가지 중 하나 선택)**
- jupyter notebook > menu > file > download as > HTML(.html)  

- juypter file을 ``` jupyter nbconvert --to html <jupyter_file(.ipynb)> ``` 을 이용하여 html로 변환

&nbsp;

**Step2. 변경한 html을 assets 폴더에 넣기**
- assets 폴더 내에 jupyter-notebooks 폴더(이건 개인 설정이다)를 만들고 html 넣는다.

&nbsp;

**Step3. post markdown 문서 내에 html 불러오기**
- 본문에 아래 코드를 붙여넣는다.

```html
<script>
  function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 'px';
  }
</script>

<iframe src= "{{"{{"}}'/assets/jupyter-notebooks/test' | relative_url }}" 
frameborder="0" width="100%" scrolling="no" onload="resizeIframe(this)" ></iframe>

```

- /assets/jupyter-notebooks/ 폴더 내의 test.html을 불러와서 아래와 같이 문서 내부에 출력된다.


<script>
  function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 'px';
  }
</script>

<iframe src="{{'/assets/jupyter-notebooks/2022-01-13-test2' | relative_url}}" frameborder="0" width="100%" scrolling="no" onload="resizeIframe(this)" ></iframe>

---
### 개발과정
코딩 공부를 위해 검색을 하다 보면 jupyter notebook을 포스트에 넣은 글들을 볼 수 있다. jupyter 화면을 캡쳐해서 넣은 포스트들에 비해 셸 형태 그대로 가져온 포스트들은 보기에도 좋을 뿐더러 코드를 복붙하기에도 좋았다. 

인터넷에서 찾은 방법들은 크게 4가지로 나누어 볼 수 있다.

**방법1. 기존 markdown 문법 사용하기**
- jupyter file을 markdown으로 변경 후 포스트에 넣는 방법이다.
- upyter notebook에서 menu > file > > download as > Markdown(.md) 로 저장하거나 Notebook(.ipynb)으로 저장된 파일을 nbconvert로 전환(```jupyter nbconvert --to markdown notebook.ipynb```)할 수 있다.
- markdown 파일을 보면 code cell은 markdown block에 result는 들여쓰기 되어 있는 것을 볼 수 있다. 이를 출력하면 아래와 같이 나타난다.

```python
print('hello world')
```

    hello world

  - 많은 블로그들에서 이 방법을 사용하고 있지만 code와 result를 구분하기 어렵다.

&nbsp;

**방법2. css와 "```<inframe>```" 태그 이용하기**
- ref: https://seungwubaek.github.io/blog/tips/jupyter_to_html/
- 인터넷에서 찾은 방법 중 가장 자세한 설명이며, 복잡하지만 원하는 방향의 결과물을 보여주었다.

&nbsp;

**방법3. Custom layout 만든 후  적용**
- ref: http://www.kasimte.com/adding-and-including-jupyter-notebooks-as-jekyll-blog-posts
- html로 변경 후 custom layout을 입히면 된다는 간단한 개념이나 결과물이나 custom layout을 알려주지 않았다.

&nbsp;

**방법4. 복합**
- ref: https://www.linode.com/docs/guides/jupyter-notebook-on-jekyll/#install-ruby-and-jekyll
- 기본 구조는 방법1과 같으나 tabular output을 가져올 수 있는 추가적인 방법을 제공하고 있다.

---

### Test
<details><summary>다음은 개발 중 시행착오 과정이므로 최종 버전만 보고 싶다면 패스!</summary>
<div markdown="1">

**#1**
- layout으로 해결하는 방법이 가장 깔끔해 보여 먼저 html로 전환 후 머릿말을 붙이 확장자를 md로 변경해 보았다.
- page frame과 겹쳐서 보인다. layout 수정이 필요하다.

**#2**
- 현재 사용 중인 jekyll은 minimal mistake로 default layout은 single이다. 
- single과 실제 포스트를 대조비교해보면 { content } 안에 post 내용이 들어가는 것 같다. 
- html을 처음 봐서 이리저리 삽질했지만 layout 파일을 수정하는 것도 포기

**#3**
- 방법2를 그대로 따라해보자. 출력되긴하는데 모양이 이상하다. 
- html convert 형식이 변경된 것으로 보인다. div class가 일치하지 않는다. 
- html 파일에서 ```<style>```이 출력 양식이고 ref에서 다운로드 받은 .scss 파일과 같은 부분으로 보여 비교해 보았으나 전혀 다른 형식이다. 
- 똑같은 파일로 만들었으나 결과는 test2와 동일하게 frame 겹침 발생. ```<style>```이 워낙 방대하고 어디를 건드려야 될지 알 수 없어서 포기

**#4**
- ```<style>```을 건드리지 말고 내용 전체를 iframe에 가둬버리자!!
- iframe src "Not found" error
  - link가 등록된 파일은 src="link"로 바로 불러올 수 있지만 폴더에 저장된 파일은 relative_url을 붙여 src="{{ '/assets/jupyter-notebooks/test' | relative_url }}"로 불러와야 한다. html 확장자를 붙이던 안 붙이던 상관없다.
- width 및 height 조절
  - default width 및 height는 300px & 150px로 포스트에 비해 매우 작은 상자안에 html이 들어가고 스크롤이 생긴다.
  - width="100%" height="100%"로 설정하면 width는 포스트 크기에 맞춰지나 height는 최대 높이가 있는지 스크롤이 생겨버린다.
  - 이를 위해 스크롤을 없애는 function resizeIframe을 적용하였다. [[Ref]](https://stackoverflow.com/questions/9975810/make-iframe-automatically-adjust-height-according-to-the-contents-without-using)
- simple 3 step 완성!!

**#5**
- jupyter를 html로 변경한 파일은 매우 크다. 위에서 예시로 올린 html은 500kb가 넘는 것에 비해 원본 notebook 파일은 2kb 밖에 되지 않는다. html파일을 열어보면 ```<style>```코드는 13000줄이 넘는 것에 비해 내용이 들어있는```<body>```는 50줄도 되지 않는 것을 볼 수 있다.
- 내용이 늘어날 수록 내용 대비 용량은 줄어들겠지만 ```<style>```코드는 반복되므로 인터넷 검색 방법2와 같이 scss로 빼내주는 것이 필요하겠다. 
- 이때 html에서 매번 ```<body>```부분을 추출해 내야하므로 이를 자동화할 코드도 필요하다.
</div>
</details>

&nbsp;

---
### 최종 버젼

**Step1. jupyter notebook to html**
- jupyter notebook > menu > file > download as > HTML(.html)  or

- 
``` 
jupyter nbconvert --to html <jupyter_file(.ipynb)> 
```

&nbsp;

**Step2. layout 만들기**

1) html 파일을 통채로 _layouts 폴더에 옮긴 후 notebook-html.html 으로 이름 변경해준다.

2)  코드 마지막 ```</head>```의 바로 위쪽에 있는  ```<body>``` 파트를 잘라낸다. ```<body```부터 ```</body>```까지 제거하면 된다. 

```html
<html>
  <head>
    <!-- ... -->
    <style>
    /* ... */
    </style>
    <!-- ... --> 
  </head>

<!-- ******** 여기부터 ******** -->
  <body>
  <!-- .... -->
  </body>
<!-- ***** 여기까지 잘라내기 *****  -->

</head>
```

  3) ```<body>``` 가 있던 부분에 아래 코드를 붙여 넣는다

```html
{{"{{"}} content }}
```

&nbsp;

**Step3. body.md 만들기**

1)  /assets/jupyter-notebooks 폴더에 .md 파일을 만든 후 앞에서 짤라냈던 또는 새롭게 얻은 ```<body>``` 코드를 붙여 넣는다. (앞 뒤 ```<body class= ...>``` ```</body>```는 제거)

> html 파일을 만들어도 상관없지만 markdown 파일을 만들면 ```<div>```사이에 markdown 문서를 자유롭게 삽입 수정할 수 있다.

2) 가장 상단에 ```layout: notebook-html``` 머릿말을 붙인다.

```html
---
layout: notebook-html
---

<div class="jp-Cell-inputWrapper">
...
</div>
```

&nbsp;

**Step4. iframe으로 post에 넣기**
- 원하는 위치에 아래 코드를 넣으면 완성

```html
<script>
  function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 'px';
  }
</script>
<iframe src= "{{"{{"}}'/assets/jupyter-notebooks/file' | relative_url }}" 
frameborder="0" width="100%" scrolling="no" onload="resizeIframe(this)" ></iframe>
```

>```resizeIframe``` script를 본문에 사용할 layout 파일(minimal mistake에서는 _layouts/single.html)에 넣으면 본문에서는 생략해도 된다. layout 파일에서 {{"{{"}} content }} 앞부분에 붙여 넣자.

&nbsp;

**Step5. body 추출 자동화 코드**
- extract 폴더를 만들고 폴더 안에 아래와 같이 파이썬 파일을 만든다.

```python
#jupyter_html_body_extract.py
import os
def change_jupyter_to_html(file):
    os.system(f'jupyter nbconvert --to html {file}')

def get_body(str):
    if "<body" in str or "body>" in str: 
        return True
    else:
        return False

def extract_body_from_html(html_file):
    with open(html_file,'r') as  f:
        lines = f.readlines()
        index_lines = [x for x in lines if get_body(x)]
        if len(index_lines) == 2:
            start_index = lines.index(index_lines[0])
            last_index = lines.index(index_lines[1])
            body_lines = lines[start_index+1:last_index]
        else:
            print('error')
            body_lines = []

    header = [  "---\n",\
                "layout: notebook-html\n",\
                "---\n"]

    with open(html_file, 'w') as f:
        if body_lines:
            f.writelines(header)
            f.writelines(body_lines)

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_list = os.listdir(cur_dir)
print(file_list)
for file in file_list:
    if ".ipynb" in file:
        file = f'{cur_dir}/{file}'
        change_jupyter_to_html(file)
        html_file = file.replace('.ipynb','.html')
        extract_body_from_html(html_file)
        os.rename(html_file, html_file.replace(".html",".md"))
```
- extract 폴더 내에 jupyter notebook 파일을 넣고 파이썬 파일을 실행 시키면 같은 폴더 내에 같은 이름의 md 파일이 생성되며 이 안에는 머리말과 html의 body가 들어있는 것을 확인 할 수 있다.

&nbsp;

---
**추가**
- 이미지를 따로 저장 후 올리라는 얘기들이 많다.
- 아래와 같이 이미지가 들어가 있는 notebook을 html으로 그대로 추출하면 그림 위치에 base64로 인코딩된 binary data가 들어있는 것을 볼 수 있다.
<iframe src= "{{'/assets/jupyter-notebooks/2022-01-13-test3' | relative_url }}" 
frameborder="0" width="100%" scrolling="no" onload="resizeIframe(this)" ></iframe>

- 이 때 용량 비교를 해보면,
  - body.html: 8036 byte
  - image binary data 지운 후 body.html: 3849 byte
  - 저장한 image file: 3122 byte

- 예시의 그래프가 간단한 모양이어서 일 수도 있지만, 저장해서 올리는 것에 비해 크게 차이가 나지 않는 것을 볼 수 있다.
- 간단한 notebook을 올릴 때는 번거러움을 감수하고 image 파일을 따로 올릴 필요는 없겠다. 
- 넣고 싶다면 html 파일 내 ```<img src="binary code">```에서 binary code 대신 image url을 넣자.