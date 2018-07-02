# git 다운로드 받기
mac : git-scm.com/downloads
windows : gitforwindows.org

#git 설정
1. 깃허브에 가입하기
2. git config --global user.name "깃헙아이디"
   git config --global user.email example@domain.com
3. 비밀번호 저장하기 : git config credential.helper store 


#git 연결하기
1. git init
2. git remote add origin https://github.com/happysmileboy/"해당저장소이름"
3. git pull origin master


사용방법
#브렌치 만들기
1. git branch "브랜치 이름"

#브랜치 변경하기
1. git checkout "브랜치 이름"

#로컬과 깃헙 연결하기 : 첫푸시를 해봅시당
1. touch Readme.txt
2. git status
3. git add Readme.txt
4. git commit -m "Add Readme.txt"
5. git push (브랜치를 바꾸었기 때문에 에러가 뜰겁니다 에러를 고쳐봅시다)
6. git push -u origin test

#항상 풀부터 먼저 받는 습관을 가집시다.
1. git pull

#과제 올리기
1. 해당 깃로컬저장소가 있는 폴더로 들어가기
1.5 git branch로 현재 저장소 확인하기
2. git status로 변경사항 확인하기
3. "git add ."(모든 파일 올리기) 혹은 git add "파일"(해당파일만 올리기)
4. git commit -m "변경사항에 대한 설명"
5. git push
