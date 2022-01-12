---
title: "[Git] 기본 명령어"

categories: 
  - git
tags: 
  - git

toc: true
toc_sticky: true

date: 2021-01-12
last_modified_at: 2021-01-12
---


### 사용자 정보 설정
- commit 시 함께 저장되는 정보
- 한 번 커밋한 이후에는 정보를 변경할 수 없다.

```
git config --global user.name "<user_name>"
git config --global user.email "<user_email>"
```

---
### git 시작
1) 빈 git 저장소 생성
```
git init <repository_name>
# <repository name> 폴더를 만들고 git 저장소로 사용한다. 폴더내에 .git 폴더가 만들어져있다.

or

mkdir <repository_name>
cd <repository_name>
git init
# 위와 같은 결과
```

2) 기존에 사용중이던 폴더를 git 저장소로 사용
```
cd <project_folder>
git init
```

---
###  git 상태 확인
1) ```git status```
- 현재 branch, 커밋하도록 정하지 않은 변경 사항, 추적하지 않는 파일, 커밋할 변경 사항이 표시된다.
- ```git status -s``` or ```git status --short```로 짤막하게 확인할 수 있다.

2) ```git diff```
- 기존 파일의 변경 사항이 표시된다.

3) ```git log```
- commit 된 사항들이 시간 역순으로 표시된다.

- commit 내용이 많으면 가장 아랫줄이 ```:```으로 표시되고 ```enter```를 칠 때 마다 다음 줄이 출력된다.
중간에 종료를 하고 싶다면 ```q```를 누르면 된다.

- ```git log --oneline```
  - 한 줄에 ```<commit_code> <commit_name>```이 하나 씩 출력되어 간단하게 확인 할 수 있다.
- ```git log --graph --all --decorate```
  - log가 branch graph와 함께 표시된다.

---
### git add
1)  전체 변경사항 add
```
git add -A
or
git add .
```

2) 특정 내용 add
```
git add <dir_or_file>
```
- 지정한 ```<dir_or_file>``` 만 add 된다.
- 여러 개를 한꺼번에 하고 싶다면 ```git add <dir_or_file 1> <dir_or_file 2> ...```

3) add 된 내용 제거
```
git reset HEAD <dir_or_file>
```

---
### commit, reset, revert
1) 변경된 내용 저장
```
git commit -m '<commit_name>'
```

2) 특정 시점으로 되돌리기
```
git reset <log_code>
```
- code 전체가 표시되지 않아도 6자리 이상?의 충분한 code만 포함된다면 상관없다.
- 시점만 되돌아 갈 뿐 이후의 내용은 staged되지 않은 상태로 남아있다.
- ```git reset --hard <log code>``` --hard 옵션 사용 시 해당 시점 이후에 발생했던 변경 사항은 삭제된다.

3) 특정 commit 내용 되돌리기
```
git revert <log_code>
```
- 해당 커밋의 변경사항만 되돌린다. 히스토리 중간의 commit을 revert 하면 해당 commit 이후의 내용은 그대로 남아있다.
- reset과는 달리 새로운 stage로 저장되기 때문에 ```git log```로 확인해 보면 commit이 하나 더 추가 되어있다.
- 실행 직후 커밋 메세지를 입력하라는 창이 뜨는데 commit 이름을 바꿀게 아니라면 그대로 저장하면 된다.

---
### branch 관리
1) branch 만들기
```
git branch <branch_name>
```

2) branch 목록확인
```
git branch
```
- branch 전체 목록이 출력된다.
- 현재 사용 중인 branch가 강조되어 있다.

3) branch 변경
```
git checkout <branch_name>
```
  
4) sub branch에 있는 내용을 가져와서 main branch merge하기
```
git checkout <main_branch>
git merge <sub_branch>
```
- main branch와 sub branch에서 같은 파일이 각각 수정되었다면 충돌이 일어나서 merge되지 않는다.