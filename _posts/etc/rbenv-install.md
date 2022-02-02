
ruby를 바로 설치할 수도 있으나 버전 관리를 위해서는 rbenv를 활용하는 것이 좋다. homebrew를 통해 설치하자.

**homebrew설치**
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

```
brew update
```

**rbenv 설치**
```
brew install rbenv
```
```
brew init
```
brew init을 시행하고 나면 아래와 같이 rbenv를 셸에 자동으로 적용시키는 방법이 나온다. (zsh 기준 출력이며 다른 셸을 사용하고 있다면 그에 맞게 수정하면 된다.)
```
# Load rbenv automatically by appending
# the following to ~/.zshrc:

eval "$(rbenv init - zsh)"
```

.zshrc를 vim으로 열어서 수정할 수도 있지만 echo 명령어로 파일에 바로 추가하자.

```
echo eval "$(rbenv init - zsh)" >> ~/.zshrc
```

설치가능한 버젼을 확인하자.
```
ruby install -l
```

확인된 버젼 중 선택하여 설치한다.
```
rbenv install 3.1.0
```

설치한 버젼을 적용한다.
```
rbenv global 3.1.0
```

적용된 ruby 버젼을 확인한다. (참고로 ```rbenv -v```는 rbenv의 version을 확인하는 것이다.)
```
rbenv version
```

