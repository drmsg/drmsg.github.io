---
title: [Python] "ModuleNotFoundError: No module named", 상위 디렉토리 import, sys.path에서 insert와 append 차이

excerpt: excerpt

caterogies: - python
tags: - [python], [module]

toc: true

date: 2021-01-12
last_modified_at: 2021-01-12
---

### ModuleNotFoundError: No module named
import 시행 시 ```sys.path``` 리스트에 있는 디렉토리에서만 import 가능하며,
기본적으로 상위 또는 같은 계층에 있는 다른 폴더에서는 import 불가능하다.

```
parent_dir/
  child_dir/
    run.py
  module.py
```
파일이 위와 같은 시스템으로 되어있을 때 run.py에서 ```import module```을 시행한다면
"ModuleNotFoundError: No module named 'module'" 에러를 맞이하게 된다.

이를 해결하기 위해서는 sys.path에 상위 폴더의 절대 경로를 추가해주어야한다.

---
### 1. 상위 폴더 절대 경로 구하기
디렉터리명은 ```os.path```로 구할 수 있다.
```python
from os import path

# 현재 위치
path.abspath('.')	

# 상위 폴더 위치
path.abspath('..')

# 두 단계 상위 폴더 위치
path.abspath('../..')
# or
path.dirname(path.abspath('..')

```
---
### 2. sys.path에 추가
```sys.path.insert```, ```sys.path.append``` 모두 추가한다는 개념은 같으나 ```sys.path```에서 나오는 결과가 다르다.

추가하지 않은 상태에서 ```sys.path```를 출력해보면 현재 디렉토리가 가장 처음에 들어있는 리스트가 나온다.
```python
import sys

sys.path
# >> ['~/parent_dir/child_dir',...,'~/lib/python3.9',...,'~/lib/python3.9/site-packages',...]
```

append 사용 시 추가한 디렉터리는 리스트 가장 끝에 들어가며 insert 사용 시 지정한 위치에 끼워 넣어진다.


```python
sys.path.append(path.abspath('..'))
# >> ['~/parent_dir/child_dir',...,'~/parent_dir]

sys.path.insert(1,path.abspath('..'))
# >> ['~/parent_dir/child_dir','~/parent_dir,...]

sys.path.insert(0,path.abspath('..'))
# >> ['~/parent_dir,'~/parent_dir/child_dir',...]
```

import할 module을 찾을 때 sys.path 리스트 내의 순서대로 찾기 때문에 같은 이름의 module이 있다면 결과가 달라 질 수 있다. 만약 아래와 같이 module.py가 child_dir 안에도 들어있다고 한다면 insert 방법에 따라 결과가 달라질 수 있다.

```
parent_dir/
  child_dir/
    run.py
    module.py
  module.py
```

```
sys.path.insert(0,path.abspath('..'))
import module
# >> parent_dir의 module이 import
```

```
sys.path.append(path.abspath('..')) # or sys.path.insert(1,path.abspath('..'))
import module
# >> child_dir의 module이 import

```
