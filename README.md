# Docker_Maker



목차

## 프로젝트 소개

<p align="justify">
프로젝트 개요/동기
Git GUI인 Sourcetree와 같이 Docker에 대한 이해만 있다면 어려운 명령어를 외우거나 찾아보지 않아도 누구나 쉽게 GUI 환경에서 도커 컨테이너 서비스를 사용할 수 있게 하는 서비스 구현
</p>

![image](https://user-images.githubusercontent.com/77333310/208288671-10152252-df79-49c9-bef5-30210bedd200.png)

<br>

## 프로젝트 구조
![image](https://user-images.githubusercontent.com/77333310/208288945-9d945ec6-dc0e-45e1-ae0f-de17b51fb1b4.png)


## 기술 스택

| Django | Frontend |  container orchestration tool   |
| :--------: | :--------: | :------: |
|   ![image](https://user-images.githubusercontent.com/77333310/208288786-f702681a-a3b5-49e1-afb1-5c99a3955629.png)   |   ![image](https://user-images.githubusercontent.com/77333310/208288829-1d873556-abb3-4d36-b535-a6ee3d6ee2d8.png)   | ![image](https://user-images.githubusercontent.com/77333310/208288842-a78591e8-06da-47a2-b442-eb6ac6849ee1.png) |

<br>

## 구현 기능

### 도커 로그인, 로그아웃

### 도커 스택 배포, 삭제, 조회

### 도커 서비스 조회, Scale-out, Update, Roll-Back

### 도커 네트워크 생성, 조회, 삭제

### 도커 볼륨 생성, 조회, 삭제

### 도커 이미지 생성, 조회, 삭제, pull-push (to private registry or Docker Hub)

<br>

## 개선사항

<p align="justify">
 1. 프로비저닝 기능 지원  
  프로젝트 서비스를 이용하기 위해서는 사전 환경을 구축해야함. 이는 사용성을 해치므로 프로비저닝 기능을 제공해 사용자가 원하는 환경에 프로젝트의 서비스를 적용할 수 있게 할 것이다  
 2. 프로젝트 이미지화  
  Django 프로젝트를 이미지화를 통해 컨테이너로 쉽게 서비스를 배포할 것이다. 이를 통해 다양한 사용자가 손쉽게 서비스를 이용할 수 있다  
</p>

<br>

## 라이센스

MIT &copy; [NoHack](mailto:lbjp114@gmail.com)

<!-- Stack Icon Refernces -->

[js]: /images/stack/javascript.svg
[ts]: /images/stack/typescript.svg
[react]: /images/stack/react.svg
[node]: /images/stack/node.svg
