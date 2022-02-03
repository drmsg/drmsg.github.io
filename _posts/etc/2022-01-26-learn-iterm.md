---
permalink: /learn-iterm
title: "[개발환경] iterm 터미널 설치 및 사용"

categories: 
  - "개발환경"
tags: 
  - macbook
  - iterm
  - terminal

toc: true
toc_sticky: true

date: 2022-01-26
---

>iterm은 기본 terminal을 대체하며 추가적인 기능을 제공하는 프로그램이다. [공식문서](https://iterm2.com/documentation.html)에서 알려주는 다양한 기능들 중 가장 자주 사용할 수 있는 몇 가지 기능들을 알아보자.

&nbsp;

---

## install
```
brew install --cask iterm2
```

&nbsp;

---

## window setting
**Tab bar location**

tab bar를 왼쪽에 둘 수 있다. tab이 많을 때 유용하다.

> Preferences(cmd+,) > Apperance > General > Tar bar location > left

&nbsp;

**Status bar**

battery, CPU, memory 등을 확인할 수 있는 status bar를 만들 수 있다.

> Preferences > profile > session >
> 1) status enabled (가장 아래) 체크버튼 클릭
> 2) configure status bar > 원하는 component drag&drop

&nbsp;

---

## 추가 기능들
### A. Text

**1. Text Selection**

mouse 없이 Text selection 가능하며 두 가지 방식이 있다.

-  Mouseless copy (find & select)
    1. 복사하고 싶은 구간의 첫 번째 단어를 ```cmd+f```로 찾는다. (여러 개가 있으면 enter로 이동 가능)
    2. tab을 누르면 단어 단위로 selection이 연장된다. 원하는 만큼 범위 지정한다. (```shift+tab```을 하면 찾았던 단어의 앞으로 연장된다.)
    3. copy한 후 ```esc```를 눌러 원래의 command line으로 돌아온다.

- Copy mode
    1. Edit>Copy Mode (```cmd+shift+c```) 를 실행하면 방향키로 움직일 수 있는 커서가 생긴다.
    2. ```space```를 누르면 selection이 시작되고 방향키로 선택할 수 있다. space를 한 번 더 누르면 selection 종료, 한 번 더 누르면 새로운 위치에서 selection 시작.
    3. ```esc``` or ```q``` or ```cmd+shift+c``` 로 종료하고 command line으로 돌아간다.

&nbsp;

**2. Paste History**

- ```cmd+shift+h```를 누르면 iterm 내에서 복사 또는 붙여넣기 했던 목록이 나온다.

- 리스트가 떠 있는 상태에서 검색할 단어를 입력하면 리스트 내 검색이 되며 backspace를 누르면 검색 취소가 된다. (타이핑 해도 아무 글자가 안 뜬다면 한글입력으로 설정되어있을 것이다.)

&nbsp;

### B. Screen

**1. Full Screen**

- ```cmd+enter```로 전체화면으로 전환 & 복귀를 할 수 있다.

&nbsp;

**2. Split Panes**

- tab 내에서 분할창 기능을 제공한다.

- ```cmd+d``` 또는 ```cmd+shift+d``` 를 사용하면 어플리케이션 내 화면이 수직 또는 수평으로 나뉘면서 새로운 terminal session이 생성된다.

- 생성된 session은 ```cmd+opt+arrow``` 또는 ```cmd+[ or ]```를 통해 이동할 수 있다.

- ```cmd+shift+enter```를 누르면 해당 세션을 최대화고 나고 나머지 session을 숨긴다. 다시 누르면 원상복구된다.

- ```cmd+w```로 해당 세션을 닫는다. (탭 전체가 닫히지는 않는다.)




