---
permalink: /install-rbenv
title: "[개발환경] rbenv으로 ruby 설치하기"

categories: 
  - "개발환경"
tags: 
  - ruby
  - rbenv

toc: true
toc_sticky: true

date: 2022-01-27
---

> ruby를 바로 설치할 수도 있으나 버전 관리를 위해서는 rbenv를 활용하는 것이 좋다. homebrew를 통해 설치해보자.

### install homebrew
```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew update
```

&nbsp;

---

### install rbenv
```zsh
brew install rbenv
```

&nbsp;

---
### rbenv setting

rbenv init을 시행하고 나면 아래와 같이 rbenv를 셸에 자동으로 적용시키는 방법이 나온다. (zsh 기준 출력이며 다른 셸을 사용하고 있다면 그에 맞게 수정하면 된다.)

```zsh
rbenv init
```

```
# Load rbenv automatically by appending
# the following to ~/.zshrc:

eval "$(rbenv init - zsh)"
```

&nbsp;

.zshrc를 vim으로 열어서 수정할 수도 있지만 echo 명령어로 파일에 바로 추가하자.

```zsh
echo eval "$(rbenv init - zsh)" >> ~/.zshrc
```

&nbsp;

---

### install ruby

설치가능한 버젼을 확인하자.
```zsh
rbenv install -l
```
```
2.6.9
2.7.5
3.0.3
3.1.0
jruby-9.3.3.0
mruby-3.0.0
rbx-5.0
truffleruby-22.0.0.2
truffleruby+graalvm-22.0.0.2

Only latest stable releases for each Ruby implementation are shown.
Use 'rbenv install --list-all / -L' to show all local versions.
```

&nbsp;

확인된 버젼 중 선택하여 설치한다.
```zsh
rbenv install 3.1.0
```

&nbsp;

설치되어 있는 버젼들을 확인하자.
```zsh
rbenv versions
```

```
* system (set by /Users/.../.ruby-version)
  3.1.0
```

system은 기존에 깔려있는 ruby이다.


원하는 버젼을 global로 설정해준다.
```zsh
rbenv global 3.1.0
```

> 현재 터미널에서만 특정 version을 사용하고 싶다면 ```rbenv local [version]```을 실행하면 된다.

&nbsp;

적용된 ruby version을 확인한다. (참고로 ```rbenv -v```는 rbenv의 version을 확인하는 것이다.)
```zsh
ruby -v
```

```
ruby 3.1.0p0 (2021-12-25 revision fb4df44d16) [x86_64-darwin21]
```

> rbenv으로 설치한 version이 제대로 뜨지 않는다면 ```eval "$(rbenv init - zsh)"```이 제대로 적용되어있지 않았을 가능성이 높다. ```which ruby```로 확인 시 ```/users/.../.rbenv/shims/ruby```로 나오는지 확인해보자.

