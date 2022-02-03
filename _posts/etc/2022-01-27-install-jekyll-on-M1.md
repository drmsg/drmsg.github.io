---
permalink: /install-jekyll-on-M1
title: "[개발환경세팅] M1에서 jekyll 설치하기"

categories: 
  - "개발환경세팅"
tags: 
  - macbook
  - M1
  - jekyll

toc: true
toc_sticky: true

date: 2022-01-27
---

> githubpage를 위해 jekyll을 설치해 보자. (M1 Mac)

jekyll은 ruby 프로그래밍 언어로 작성된 정적 사이트 생성기이다. 
사실 githubpage를 만들고 공개되어 있는 jekyll theme를 적용하는데는 jekyll를 설치할 필요가 없다. 
본인의 경우 로컬 서버를 생성하여 github에 올리지 않고도 변경사항을 바로 확인할 목적으로 설치하였다. 

## bundler 와 jekyll 설치
먼저 ruby가 설치되어 있어야 한다. 최신 맥에는 설치에 필요한 2.4.0 version 이상의 ruby가 이미 들어있다.
(설치가 필요하다면 [여기](https://drmsg.github.io/install-rbenv) 참고)

write permission이 없다는 코드들에 대해 sudo로 실행하였다.

```zsh
sudo gem install bundler jekyll
```

실행 도중 아래와 같은 error가 발생하였다.

>RDoc is not a full Ruby parser and will fail when fed invalid ruby programs.
>
>The internal error was:
>
>(NoMethodError) undefined method `[]' for nil:NilClass
>
>ERROR:  While executing gem ... (NoMethodError)

RDoc을 설치해주자.
```zsh
sudo gem install rdoc
```
설치해주고 다시 ```sudo gem install bundler jekyll```을 실행하면 성공적으로 설치된다.

githubpage 디렉토리로 이동 후 로컬 서버를 생성해보자.
```zsh
bundle exec jekyll serve
```

M1 환경에서 다른 설정을 하지 않았다면 다음과 같은 에러가 발생할 것이다.

>/Library/Ruby/Gems/2.6.0/gems/ffi-1.15.5/lib/ffi.rb:5:in `require': dlopen(/Library/Ruby/Gems/2.6.0/gems/ffi-1.15.5/lib/ffi_c.bundle, 0x0009): tried: '/Library/Ruby/Gems/2.6.0/gems/ffi-1.15.5/lib/ffi_c.bundle' (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e')), '/usr/lib/ffi_c.bundle' (no such file) - /Library/Ruby/Gems/2.6.0/gems/ffi-1.15.5/lib/ffi_c.bundle (LoadError)


이는 jekyll이 x86 기반으로 만들어졌으나 M1은 arm64 기반이기 때문에 발생한다. 이를 해결하기 위해서는 x86 언어를 해석할 수 있는 Rosetta를 사용하여 터미널을 열거나 arch 명령어를 통해 실행하여야 한다.

터미널에서 ```arch```를 실행하면 현재 시스템 아키텍쳐를 확인할 수 있다.
```zsh
arch
```
> arm64

**Rosetta를 사용하여 터미널 열기**

Finder > 찾기 > 터미널 검색(ex. 터미널 or iterm) > 정보 가져오기(cmd+i) > Rosetta를 사용하여 열기 체크

터미널을 다시 열고  ```bundle exec jekyll serve```를 사용하여 로컬 서버를 실행하자.

```
Generating... 
       Jekyll Feed: Generating feed for posts
                    done in 0.605 seconds.
 Auto-regeneration: enabled for '/Users/seungjinmoon/Desktop/myproject/blog/githubpage'
    Server address: http://127.0.0.1:4000
  Server running... press ctrl-c to stop.
```

위와 같이 출력되고 나면 ```http://127.0.0.1:4000```를 통해 로컬 서버를 확인할 수 있다.

Rosetta로 연 터미널에서 ```arch```를 실행하면 i386이 나온다. Rosetta는 에뮬레이터이기 때문에 가벼운 프로그램에서는 상관없을 수 있지만 무거운 프로그램을 돌릴 때는 느려질 수 있어 가급적 arch 명령어를 사용하는 것이 좋다.

**arch 사용**

```arch -arch x86_64```를 붙여 실행한다.

```
arch -arch x86_64 bundle exec jekyll serve 
```

