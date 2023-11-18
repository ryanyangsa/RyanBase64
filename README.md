# 프로그램 설명

입력 파일을 Base64로 인코딩 및 디코딩을 하는 자바(파이썬) 프로그램

# 개발사유

망분리(network segmentation)를 도입한 기관의 경우, 자료 반출입은 망연계(network connection) 솔루션 혹은 보안 USB를 사용한다. 하지만 업무편의성을 위해 물리PC와 인터넷VDI의 클립보드 복사 기능을 활용할 수 있도록 하는 경우가 있는데, 이 경우 별도의 통제없이 자료 반출입이 가능해진다.

## Base64 소개

    Base64는 바이너리를 어느 문자셋에나 있는 기본문자로 인코딩을 하는 단순 인코딩 기술이다. 다시 말해서 플랫폼 독립적인 환경에서 문자를 위한 파일포맷에 바이너리 데이터를 포함해야 하는 경우, 해당 바이너리 데이터가 시스템 독립적으로 전송하는 걸 보장하게 만든다. 데이터를 Base64로 변환하는 순서는 아래와 같다

      1. A라는 단어를 인코딩 하보자.
      2. 먼저 해당 단어의 문자를 ASCII 코드표에서 찾는다.
      3. 찾은 ASCII 코드를 2진수로 변환한다.
      4. 변환된 2진수를 늘어놓고 6-bit 단위로 자른다.
      5. 6-bit 단위로 잘라진 숫자들을 Base64 배치표에서 찾아 작성한다.
      6. 만약 마지막 비트열이 6-bit 가 아니면 0을 채워 6-bit로 만든다.

# 프로그램 사용방법

<img width="831" alt="image" src="https://user-images.githubusercontent.com/36325375/211181346-248b5049-fcbb-4906-b73f-f747e5195141.png">

## Base64 인코딩 
    java RyanBase64 e 입력파일 출력파일
    
## Base64 디코딩
    java RyanBase64 d 입력파일 출력파일

# 참고사항

윈도우즈 환경이라면 아래 명령어를 통해 출력결과를 클립보드에 복사할 수 있다.

    java RyanBase64 e 입력파일 | clip

클립보드에 있는 내용을 파일로 출력하려면 명령 프롬프트(cmd)로는 별도 프로그램이 필요하기 때문에 powershell 명령어를 사용하면 된다.

    powershell Get-Clipboard > 출력파일 

# 변경사항

파이썬 기반의 GUI 프로그램을 추가했어요. RyanBase64.py, ryanyang_profile.png 파일을 같은 폴더에 두고 아래 명령을 실행하세요. (2023.11.18)

    python RyanBase64.py

<img width="400" alt="image" src="https://github.com/ryanyangsa/RyanBase64/assets/36325375/9830d458-bc1e-4848-a2df-f27671efb009">

# 개발자 연락처

라이언양(ryan.yang.sa@gmail.com)
