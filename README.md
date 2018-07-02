파이썬 인강 및 과제부분입니다.
안녕하세요 손준혁입니당. 오늘 부족했던 강의에 죄송하다는 말씀을 드립니다ㅜㅜ
부족한 부분은 codeit이라는 인강을 통해 대체를 할게용.

한 강의당 2~5분짜리의 클립형식이고 내용도 엄청 좋기 때문에 이걸 다시 들으면 좋을것 같아용

들어야 하는 강의는 2강자료형 ~ 8강 for문과 리스트 심화 + 11강 객체 지향 프로그래밍입니다.

시간이 남으시면 다 들으면 좋지만 시간이 없는 분들을 위해 제가 꼭 들어야 하는 부분만 정리해드릴게요.

2강 2 - 11번까지는 모르는 개념만 들으세요. 14-15, 19, 21, 24

3강 2-3, 6-8

4강 1~11

5강 1-10, 25(꼭봐주세요!)

6강 1-5

7강 1-13

8강 1-5, 12-17

11강 1-11

과제는 다음 순서대로 해주세요.

(그리고 모르겠으면 5분정도 고민하고 바로 예시답안을 보고 따라적으면서 이해하세요!)
난이도 : 하

2강 10,12

3강 4, 9

5강 4, 6

7강 3

8강 4, 6, 8


난이도 : 중

2강 16

3강 11

4강 12

5강 11, 17

7강 11

8강 14 18 20

난이도 : 상(어려우면 바로 코드부터 보시고 선코딩 후이해가 좋을것같아요)

11강 8 12 14

파이팅하시구 모르는게 있거나 에러가 뜰경우에 언제든지 멘토나 저에게 톡주세요!!

----------------------------------------------------------------
git 부분입니다

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
