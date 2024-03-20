# :office: META-JOB

### :bookmark: 구직 활동을 도와주는 인공지능 취업 도우미 서비스 '메타 잡'

<br />

## :thought_balloon: 프로젝트 기획

> 이력서 사진 합성  
> 이력서 평가  
> 가상 모의 면접 평가  
> 합격자 평균 스펙  

## :calendar: 프로젝트 기간

> 2023.11.01 ~ 12.12

## :family: 참여 인원

<table>
  <tr>
    <td align="center"><a href="https://github.com/OHTaEH">
      <img src="https://avatars.githubusercontent.com/OHTaEH" width="150px;" alt="">
    </td>
    <td align="center"><a href="https://github.com/jeanDeluge">
      <img src="https://avatars.githubusercontent.com/jeanDeluge" width="150px;" alt="">
    </td>
    <td align="center"><a href="https://github.com/yechan-9208">
      <img src="https://avatars.githubusercontent.com/yechan-9208" width="150px;" alt="">
    </td>
    <td align="center"><a href="https://github.com/wahoman">
      <img src="https://avatars.githubusercontent.com/wahoman" width="150px;" alt="">
    </td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/OHTaEH"><b>오태훈</b></td>
    <td align="center"><a href="https://github.com/jeanDeluge"><b>홍진영</b></td>
    <td align="center"><a href="https://github.com/yechan-9208"><b>원예찬</b></td>
    <td align="center"><a href="https://github.com/wahoman"><b>여형구</b></td>
  </tr>
 <tr>
    <td align="center">Oh Tae Hoon</td>
    <td align="center">Hong Jean Young</td>
    <td align="center">Won Ye Chan</td>
    <td align="center">Yeo Hyung Goo</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/narae3759">
      <img src="https://avatars.githubusercontent.com/narae3759" width="150px;" alt="">
    </td>
    <td align="center"><a href="https://github.com/haeniKim">
      <img src="https://avatars.githubusercontent.com/haeniKim" width="150px;" alt="">
    </td>
    <td align="center"><a href="https://github.com/cykim1228">
      <img src="https://avatars.githubusercontent.com/cykim1228" width="150px;" alt="">
    </td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/narae3759"><b>김나래</b></td>
    <td align="center"><a href="https://github.com/haeniKim"><b>김해니</b></td>
    <td align="center"><a href="https://github.com/cykim1228"><b>김찬영</b></td>
  </tr>
 <tr>
    <td align="center">Kim Na Rae</td>
    <td align="center">Kim Hae Ni</td>
    <td align="center">Kim Chan Young</td>
  </tr>
</table>

## :white_check_mark: 역할 분담
#### LLM 파트 - 이력서 (포트폴리오) 분석  
> - 오태훈 : 포트폴리오 평가 요소 기획 + 피드백 프롬프트 작성
> - 홍진영 : 포트폴리오 분석 결과 구현 + BackEnd 구성
> - 원예찬 : 면접 후 피드백 프롬프트 작성 + 사용자의 면접 답변 STT
> - 여형구 : 포트폴리오 기반 면접 질문 생성 + 면접관 페르소나 부여

#### CV 파트 - 가상 면접  
> - 김나래 : 면접 중 실시간 행동 감지 (집중도, 표정관리, 행동습관) + UI 기획
> - 김해니 : 면접 질문 TTS 로 면접관 보이스 생성 + UI 기획
> - 김찬영 : 이력서 사진 합성 + 가상 면접관 합성 + FrontEnd 구성

## :moneybag: 프로젝트 예산

#### 공용 서버 
> Intel i9 / GTX 4090 24G VRAM x2 / 64G RAM  

#### BackEnd 서버
> 공용 서버 이용  
#### FrontEnd 서버
> 공용 서버 이용  
#### LLM 이용 금액
> 포트폴리오 1개 기준 3000 토큰 발생  
> GPT 3.5 기준 Input 0.01$ / 1K , Output 0.03 / 1K  
> GPT 4 기준 Input 0.03 / 1K , Output 0.06 / 1K  
> GPT 4 사용 시 포트폴리오 검사 1회 당 약 400원 비용 발생  

## :books: 사용 기술

#### BackEnd

> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
> <img src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white">
> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

#### FrontEnd

> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
> <img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=white">
> <img src="https://img.shields.io/badge/nodejs-339933?style=for-the-badge&logo=nodedotjs&logoColor=white">

#### AI Models

> <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">
> <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">

> FaceSwap - Inswapper  
> UpScaling - GFP GAN  
> AI Assistant - GPT 4  
> Voic Clone - xTTS_v2  
> Lip Synchronization - Video Retalking, Face3D, LNet  
> Face, Hand Landmarks - OpenCV, Mediapipe  
> STT - Whisper  

## :bar_chart: 구조

<details>
<summary>ERD</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/meta-job/.github/assets/40597647/0eb8c7fe-1535-427c-adf7-270efcc1b8a8"/>
</div>
</details>

<details>
<summary>Structure</summary>
<div markdown="1" style="padding-left: 15px;">
</div>
</details>

<details>
<summary>Flow</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/meta-job/.github/assets/40597647/a9cdcdf1-2032-4be1-b815-adf95d517121" />
</div>
</details>

## :key: 핵심 기능

#### :one: 이력서 사진 합성

> 사용자가 합성을 원하는 본인의 사진을 업로드하고  
> 여러 이력서 사진 템플릿 중 1개를 선택하여 버튼을 누르면  
> 해당 템플릿과 사용자의 사진의 합성을 통해 정장 사진이 생성됩니다.  
> [코드 보러가기](https://github.com/meta-job/client/blob/main/app.py#L29)

#### :two: 포트폴리오 분석

> 사용자가 입력한 이력서와 포트폴리오를 기반으로  
> 인공지능을 이용해 분석 및 평가를 진행합니다.  
> [코드 보러가기](https://github.com/meta-job/evaluate-portfolio/blob/main/app/ai_util/portfolioEditor.py#L12)

#### :three: 가상 면접

> 사용자가 입력한 여행장소들을 바탕으로 여행일정을 만듭니다.  

## :dart: 이슈 사항

#### :one: 클라이언트 측 카메라 접근

> 가상 면접 시 공용 서버에서 서버 작동 후  
> 클라이언트 PC 에서 가상 면접 진행 시 웹 페이지 내에 카메라를 받아오지 못해  
> 사용자의 웹캠이 나오지 않는 증상이 발생

## :pushpin: 참고 자료

## :video_camera: 시연 영상
