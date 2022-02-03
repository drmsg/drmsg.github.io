---
permalink: /use-googledrive-on-line-command
title: "[개발환경] linux, ubuntu line command에서 google drive 사용하기"

categories: 
  - "개발환경"
tags: 
  - linux
  - ubuntu
  - line command
  - google drive

toc: true
toc_sticky: true

date: 2022-02-03
---

> AWS EC2 ubuntu 환경에서 google drive를 사용해보자. 

command line에서 google drive를 사용하기 위해서는 third party command line utility 또는 google drive mount를 사용해야한다.

command line utility가 설치가 좀 더 쉬우며, mount는 사용 시 폴더와 동일한 방식으로 동작한다는 편리함이 있다.

## Command line utility (gdrive)

> 공식 문서는 github repository에서 확인 
> ([github.com/prasmussen/gdrive](https://github.com/prasmussen/gdrive))

### 설치하기

설치에는 두가지 방법이 있다.

**1. using homebrew**

```bash
brew install gdrive
```

&nbsp;

**2. download**

ubuntu에 homebrew를 설치하기 귀찮을 때 좋은 방법이다.

1) https://github.com/prasmussen/gdrive/releases 에서 최신 버젼을 확인 후 wget 명령어를 사용해 다운로드 한다.

```bash
wget https://github.com/prasmussen/gdrive/releases/download/2.1.1/gdrive_2.1.1_linux_386.tar.gz
```

&nbsp;

2) 다운로드 한 파일을 압축해제한다.

```bash
tar -xvf gdrive_2.1.1_linux_386.tar.gz
```

현재 위치를 확인해보면 'gdrive' unix 실행파일이 들어있는 것을 확인할 수 있다. 이를 이용해 google drive를 사용하게 된다.

> 즉, homebrew로 설치 시 gdrive가 command로 인식되지만, unix 실행파일을 사용 시 gdrive 파일 위치로 시작하는 command를 작성해야 한다.(```gdrive help```  vs  ```./gdrive help```)

&nbsp;

### Authentication

사용하기 전 gdrive가 google drive에 접속할 수 있도록 권한 허가가 필요하다.

```bash
./gdrive about
```

```
Authentication needed
Go to the following url in your browser:
https://accounts.google.com/o/oauth2/auth?access_type=....

Enter verification code:
```
출력된 url로 들어가 본인의 아이디로 접속하고 Vertification code를 받아 터미널에 붙여넣으면 권한 허가가 끝난다.

&nbsp;

### 사용하기

#### 간단 upload
- 파일 업로드

  ```bash
  ./gdrive upload directory/file_name
  ```

&nbsp;

- 폴더 업로드

  폴더를 압축하지 않고 통채로 올리려면 ```--recursive``` option을 이용해야된다.
  ```
  ./gdrive upload directory/folder_name -r
  ```

  &nbsp;

  >이렇게 업로드 된 파일은 '내 드라이브'에 저장된다. 특정위치로 업로드 하거나 파일을 다운로드 하기 위해서는 파일 또는 폴더의 id가 필요하다.

&nbsp;


#### File or directory id 확인

파일 리스트를 보여주는 기본 명령어는 ```gdrive list```이다. 이는 최근 생성된 파일 30개만 보여준다. ```--max``` option을 이용하여 전체를 출력하는 방법도 있지만 찾는 시간을 생각하면 비효율적이다. 

하지만 파일 이름을 알고 있다면 ```--query``` option을 이용하여 쉽게 찾을 수 있다.

```bash
./gdrive list --query "name contains 'file_name'"
```

&nbsp;

폴더 내에 있는 파일 리스트도 확인가능하다.
```bash
./gdrive list --query " 'folder_id' in parents"
```

&nbsp;

#### download & upload

위에서 찾은 id로 특정 파일을 download하거나 원하는 위치로 upload할 수 있다.

- download

  ```bash
  ./gdrive download file_id
  ```

  > [참고] ```--recursive``` option을 사용해도 빈폴더는 다운로드 하지 않는다.

&nbsp;

- upload

  ```bash
  ./gdrive upload --parent [구글드라이브 내 폴더 id] [업로드 할 파일]
  ```

---
---

&nbsp;

## Google-drive mount

google-drive-ocamlfuse를 사용하는 방법이다.([github.com/astrada/google-drive-ocamlfuse](https://github.com/astrada/google-drive-ocamlfuse))

&nbsp;

### Install

```bash
sudo add-apt-repository ppa:alessandro-strada/ppa
sudo apt-get update
sudo apt-get install google-drive-ocamlfuse
```

&nbsp;

### Authorization

**1. Enable Google drive API**

먼저 google drive API를 사용 가능하도록 설정해야된다.

1) google api library([https://console.cloud.google.com/apis/library](https://console.cloud.google.com/apis/library))에서 google drive API 검색 후 클릭

2) '사용(enable api)' 클릭

3) 사용자 인증 정보 > 사용자 인증 정보 만들기 > OAuth 클라이언트 ID

4) 어플리케이션 유형을 '데스트톱 앱'으로 설정 후 '만들기'

5) 클라이언트 ID와 클라이언트 보안 비밀 확인 해두기 (사이트에 다시 접속하면 확인할 수 있으므로 따로 저장해 둘 필요는 없다.)

&nbsp;

**2. Authorization**

google drive를 mount할 폴더로 이동 후, 앞에서 확인한 클라이언트 정보로 google-drive-ocamlfuse를 실행하자.

```bash
google-drive-ocamlfuse -headless -label me -id ##yourClientID##.apps.googleusercontent.com -secret ###yoursecret##### 
```
```
Please, open the following URL in a web browser: https://accounts.google.com/o/oauth2/auth?client_id=...
Please enter the verification code:
```
출력된 url로 접속 후 로그인하여 verification code를 받고 터미널에 입력한다.

&nbsp;

**3. mount folder**

mount할 빈 폴더를 만든다.
```bash
mkdir mygdrive
```

만든 폴더에 mount한다.

```bash
google-drive-ocamlfuse -label me mygdrive
```

해당 폴더로 들어가면 구글 드라이브 내 폴더 및 파일을 확인할 수 있으며 local system과 같은 방식으로 파일을 이동, 복사, 생성 할 수 있다.


