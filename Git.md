# Git

# 분산 버전 관리 시스템

---

# 버전 관리

- 변화를 기록하고 추적하는 것
- 3.1에서 4.0 으로 변화하였을 때 어떤 **변화**가 있었는지 기록하는 것에 관심이 있다
- 각 버전에는 변화된 내용만 기록, 최종본의 누적을 기록한 것이 아니다
- 그렇기에 과거로의 회귀가 쉬움
- **변화 내용**만 기록하기 때문에 저장된 내용의 용량이 줄어듦

---

# 분산

- 분산 구조의 장점
    - 중앙 서버에 의존하지 않고 작업 수행
        - 개발자들 간의 충돌 방지
    - 중앙 서버의 장애나 손실에 대비하여 백업과 복구 용이
    - 인터넷에 연결되지 않은 환경에서도 작업을 계속 할 수 있음
        - 변경이력과 코드를 로컬에 저장하고 나중에 중앙 서버에 동기화
        

---

# git의 역할

- 코드의 **변경 이력**을 기록하고 **협업**을 원활하게 하는 도구

---

# git의 3가지 영역

- Working Directory
    - 실제 작업 중인 파일들이 위치하는 영역
- Staging Area
    - WD에서 변경된 파일 중, 다음 버전에 포함 할 파일들을 선택적으로 추가하거나 제외 할 수 있는 중간 준비 영역
    - 변경된 모든 것을 기록하는 것이 아니라 원하는 변경 내용만 선택할 수 있게 도와줌
- Repository
    - 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전(commit)과 변경 이력이 기록됨

# Commit (버전)

변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 **snapshot**이라고 하기도 함

# 명령어

- git init
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice
    $ git init
    Initialized empty Git repository in C:/Users/SSAFY/Desktop/git-practice/.git/
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ cd ..
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop
    $ cd git-practice/
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ 
    ```
    
    로컬 저장소 설정(초기화)
    
    git의 버전 관리를 시작할 디렉토리에서 진행
    
    init을 실행한 디렉토리에만 (master)가 붙어있는것을 볼 수 있음
    

- git status
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git status
    On branch master
    
    No commits yet
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            first.py
    
    nothing added to commit but untracked files present (use "git add" to track)
    ```
    
    빨간색으로 표시 된 [first.py](http://first.py) 가 생성된것 감지, 그러나 Stage Area에 추가 된적 없다는 안내
    
- git add
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git add first.py
    ```
    

Stage Area에 해당 파일을 추가함

- git commit
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git commit -m "first commit"
    [master (root-commit) ffe8464] first commit
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 first.py
    ```
    
    [first.py](http://first.py) 가 commit 되었다는 메시지
    
    단 commit 전에 서명(사용자)을 등록해야함
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git config --global user.email "ssafychs135@gmail.com"
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git config --global user.name "ssafychs135"
    ```
    

- git log
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git log
    commit ffe84640bb5989df0d9324bd9095fcead02c127d (HEAD -> master)
    Author: ssafychs135 <ssafychs135@gmail.com>
    Date:   Thu Jul 17 12:20:29 2025 +0900
    
        first commit
    
    ```
    
    git status에선 commit 내역을 볼 수 없음, git log 로 조회 가능
    

- [first.py](http://first.py) 의 내용을 변경하고 it status 를 다시 해보자
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git status
    On branch master
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   first.py
    
    no changes added to commit (use "git add" and/or "git commit -a")
    ```
    
    modified에 [first.py](http://first.py) 가 추가 되어있는 것을 볼 수 있다. 변경됨을 감지
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git add first.py 
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git commit -m "second commit"
    [master 23c8be8] second commit
     1 file changed, 1 insertion(+)
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git log
    commit 23c8be8b684e1346c69cdad1d00506a679acd48b (HEAD -> master)
    Author: ssafychs135 <ssafychs135@gmail.com>
    Date:   Thu Jul 17 12:28:23 2025 +0900
    
        second commit
    
    commit ffe84640bb5989df0d9324bd9095fcead02c127d
    Author: ssafychs135 <ssafychs135@gmail.com>
    Date:   Thu Jul 17 12:20:29 2025 +0900
    
        first commit
    ```
    
    git add 로 SA 에 파일 추가 후 second commit을 실행한 모습
    
    log에  fisrt commit 과 second commit 모두 잘 기록되었다
    

---

# 주의사항

## git 로컬 저장소 내에 또 다른 git 로컬 저장소를 만들지 말것

- git init 된 폴더 내부에 다른 폴더에서 git init을 하면 안된다는 뜻
- 로컬 저장소내에 로컬저장소는 git이 감시할 수 없기 때문
- 그렇기때문에 홈 디렉토리나 바탕화면등에서 git init을 하면 피곤해짐
- 혹시 실수했다면 **.git**디렉토리를 삭제하면 됨

---

# 참고

- 로컬
    - 현재 사용자가 직접 접속하고 있는 기기 또는 시스템
- git log - -oneline
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git log --oneline
    26c8846 (HEAD -> master) a,b file add
    23c8be8 second commit
    ffe8464 first commit
    ```
    
    commit 내용을 축약하여 출력
    
- git config - - global -l
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git config --global -l
    user.email=ssafychs135@gmail.com
    user.name=ssafychs135
    ```
    
    git global 설정 조회
    

- git 은 commit 메시지가 동일하여도 해쉬값으로 구분하기 때문에 무관

---

# commit 수정하기

메시지 수정과 전체 수정은 같은 git commit - - amend 옵션으로 수행 가능, 단 시행 시점으로 구분됨

- commit 메시지 수정
    
    ```bash
    git commit --amend
    ```
    

vim editor 에서 commit이 열리고 수정해야함

 [vim Editor](https://www.notion.so/vim-Editor-23316d6ec1438063b754e07432e3e918?pvs=21) 

- commit 에 추가하기
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-amend-practice (master)
    $ git add .
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-amend-practice (master)
    $ git status
    On branch master
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   b.txt
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-amend-practice (master)
    $ git commit --amend
    [master ba5366f] B기능 구현 완료 / b.txt도 추가됨
     Date: Thu Jul 17 13:52:55 2025 +0900
     2 files changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 README.md
     create mode 100644 b.txt
    ```
    
    빠진 파일을 추가하는 상황을 가정해보자
    
    b.txt를 기존 커밋에 추가하려면 git add 를 진행하고 나서 commit - -amend 진행
    
    vim editor 에서 메시지를 추가해도 됨
    

---

# 원격 저장소

repo를 만들때 README.md를 만들고 시작했다면 clone 부터 해야함

- 왜? README.md를 만들면 commit이 하나 등록되기 때문!

- git remote add origin remote_repo_url
    - 원격 저장소의 url을 origin 이란 별칭을 붙여 등록
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git remote add origin https://github.com/ssafychs135/remote-practice
    
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git remote -v
    origin  https://github.com/ssafychs135/remote-practice (fetch)
    origin  https://github.com/ssafychs135/remote-practice (push)
    ```
    

- git push origin master
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git push origin master
    info: please complete authentication in your browser...
    Enumerating objects: 8, done.
    Counting objects: 100% (8/8), done.
    Delta compression using up to 16 threads
    Compressing objects: 100% (4/4), done.
    Writing objects: 100% (8/8), 658 bytes | 164.00 KiB/s, done.
    Total 8 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
    To https://github.com/ssafychs135/remote-practice
     * [new branch]      master -> master
    ```
    
    원격 저장소에 commit 목록을 push 함 (변경 사항 만큼 업로드)
    
    push는 과거의 역사를 비교하고나서 변경사항만큼 쌓아 올림
    
- git clone {remote_repo_url}
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop
    $ git clone https://github.com/ssafychs135/remote-practice
    Cloning into 'remote-practice'...
    remote: Enumerating objects: 8, done.
    remote: Counting objects: 100% (8/8), done.
    remote: Compressing objects: 100% (4/4), done.
    remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0 (from 0)
    Receiving objects: 100% (8/8), done.
    ```
    
    전체 복사 (git init 되어있음)
    
- git pull origin master
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-practice (master)
    $ git pull origin master
    remote: Enumerating objects: 4, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (2/2), done.
    remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0 (from 0)
    Unpacking objects: 100% (3/3), 316 bytes | 26.00 KiB/s, done.
    From https://github.com/ssafychs135/remote-practice
     * branch            master     -> FETCH_HEAD
       26c8846..be19934  master     -> origin/master
    Updating 26c8846..be19934
    Fast-forward
     README.md | 1 +
     1 file changed, 1 insertion(+)
     create mode 100644 README.md
    ```
    
    원격 저장소의 변경사항을 받아옴
    
- gitignore
    
    ```bash
    SSAFY@2□□PC041 MINGW64 ~/Desktop/git-remote-practice (master)
    $ git status
    On branch master
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            .gitignore
    
    nothing added to commit but untracked files present (use "git add" to track)
    ```
    
    git의 감시에서 제외할 파일 목록을 작성
    
    단, 한번이라도 git에 감시를 받게 된 파일은 뺄 수 없음(추가 명령어 git rm  - -cache 필요)