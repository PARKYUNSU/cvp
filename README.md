# 개인형 이동장치 교통법규 위반 탐지 : Segmentation 객체탐지와 알고리즘을 활용한 위반 탐지
(Detection of Personal Mobility Traffic Violations: Violation Detection Utilizing Segmentation Object Detection and Algorithms)

---

## 프로젝트 개요

---

도시 교통환경 변화로 개인형 이동장치의 교통사고와 법규 위반 문제가 증가하고 있습니다. 이에 대응하기 위해 CCTV 이미지를 활용하여 개인형 이동장치의 교통 법규 위반을 탐지하고 사용자에게 알리는 프로젝트입니다.

---

## 역할

| Name | Role | 
| ---- | ---- |
|박윤수| Detectron2 조사, 데이터 전처리, 모델링, 알고리즘, PPT, 웹페이지|
|박재현| YOLOv8 조사, 데이터 전처리, 모델링, 알고리즘, 웹페이지|
|주형진| YOLOv7 조사, 데이터 전처리, SAM, 모델링, 알고리즘, 웹페이지|

---
## 프로젝트 목표

---

1. 객체 간 거리와 상관 관계를 분석하여 교통 법규 위반을 탐지합니다.
2. 모델(YOLOv8)을 사용하여 위반을 탐지합니다.

## 아키텍처

---

<img width="500" alt="스크린샷 2024-05-04 오후 3 53 05" src="https://github.com/PARKYUNSU/cvp/assets/125172299/3008bce2-e02a-4854-b95c-45b572bec84e">


## 프로젝트 수행 절차

---

1. AI HUB에서 데이터를 받아 전처리를 진행합니다.
2. SAM과 JSON 데이터를 사용하여 도로 지형지물을 YOLOv8 세그멘테이션으로 학습합니다.
3. 학습을 위한 각 객체의 세그멘테이션 좌표 및 Bbox 좌표에 대해서 손수 라벨링 작업을합니다.
4. YOLOv8로  객체를 학습시킵니다.
5. 학습된 모델을 플라스크로 구현하여 도로와 개인형 이동장치 사이의 알고리즘을 통해 교통 법규 위반을 탐지합니다.

---

## 모델 설명

<img width="400" alt="스크린샷 2024-05-04 오후 4 31 02" src="https://github.com/PARKYUNSU/cvp/assets/125172299/b74cb4eb-0ddc-4977-9981-ce081f740f16"><img width="445" alt="스크린샷 2024-05-04 오후 5 09 38" src="https://github.com/PARKYUNSU/cvp/assets/125172299/e41cb506-d995-40ba-9806-fa2dcc71b460">


객체 탐지에는 두가지 방법이 있습니다.

- 하나는 2-stage detector 다른 하는 1-stage detector가 있습니다.
2-stage detector는 물체의 위치를 찾는 로컬라이제이션과 클레스픽케이션을 순차적으로 실행하며
1-stage detector는 로컬라이제이션과 클레스픽케이션을 한번에 실행합니다.

- R-CNN은 정밀도가 높은 2-stage Detector를 사용하고 있습니다.
Yolo는 1 stage Detector를 사용하고 있습니다.


기존에는 객체탐지 성능은 R-CNN이 정확도는 높았으나 

Yolo가 점점 발전해오면서 오른쪽 표처럼 yolo3의 모델이 걸린 시간도 빠르고 성능도 좋아져서 R-CNN모델인 detectron을 사용하는 것 보단 yolo 모델이 더 낫다고 생각해서  yolo로 학습을 진행했습니다.



## 알고리즘 설명

<img width="400" alt="그림 설명" src="https://github.com/PARKYUNSU/cvp/assets/125172299/4192c4c9-ed0b-43f2-a31d-3f360f7cd6a0"> <img width="430" alt="그림 설명" src="https://github.com/PARKYUNSU/cvp/assets/125172299/a60ba126-09a4-4b6f-abc7-5f48352d591c">

#### 1) 도로 지형지물과 PMD 탐지 알고리즘:
1) 학습된 세그멘테이션 모델을 활용하여 이미지 상에 있는 도로 지형지물을 예측하고, 각 항목의 세그멘테이션 좌표를 추출하여 저장합니다.
2) Bbox 모델은 이동식 개인장치(PMD) 객체를 탐지하고 해당 객체의 좌표를 추출하여 저장합니다.
3) 각 도로 지형지물과 객체의 알고리즘을 활용하여 위반사항을 탐지합니다.
4) PMD의 Bbox 아래 두 지점을 활용하여 인도 위에서 오토바이나 자전거 탑승자 객체가 감지된다면 인도 주행 위반으로 간주됩니다.
또한, 신호등 적색 신호 객체를 탐지하여 정지선, 횡단보도, 교차로에서의 위반을 탐지합니다.

<img width="500" alt="스크린샷 2024-05-04 오후 4 30 36" src="https://github.com/PARKYUNSU/cvp/assets/125172299/e8e798d9-3d17-4967-95e1-dfcb983703ef">

#### 2) 헬멧 탐지 알고리즘:
1) PMD 탑승자 객체와 헬멧 객체를 따로 학습한 후, 헬멧을 쓴 객체는 두 개의 bounding box가 쳐지며, 헬멧을 쓰지 않은 객체는 하나의 bounding box로 식별됩니다.
2) 헬멧 객체와 PMD 탑승자 객체 간의 거리를 계산하여, 헬멧을 쓰지 않은 탑승자를 헬멧 미착용 위반으로 판단합니다.

**1) 도로지형지물 Segmentation 탐지**

<img src="https://github.com/PARKYUNSU/cvp/assets/125172299/033a63bf-e989-4f3e-abf6-eeb2552b23a0)![C000063_024_0012_C_D_F_0_jpg rf 397c33da0befa57813096f14aa4c2a71" width=420><img src="https://github.com/PARKYUNSU/cvp/assets/125172299/4850ec32-411c-4b8d-a633-e457469634f6)![C000057_049_0168_C_D_R_0_jpg rf 96822a287a2269b96b6ddf8b55397525" width=250><img src="https://github.com/PARKYUNSU/cvp/assets/125172299/75c5f8e5-3941-44e0-9413-1493b9467a7e" width=250>

---

**2) 도로지형지물과 객체 탐지**



<img src="https://github.com/PARKYUNSU/cvp/assets/125172299/07c100d6-3fcd-4d3b-8b97-6f5c4760a9f7" width=370>

<img src="https://github.com/PARKYUNSU/cvp/assets/125172299/672aefd4-e73d-4f95-b3c5-c05184eb75bb" width=250>

<img src="https://github.com/PARKYUNSU/cvp/assets/125172299/5c4b633e-5d26-4662-acc8-6573246cba12" width=250>


## 프로젝트 결과

---

1. 세그멘테이션을 통해 도로 지형지물을 정확하게 탐지하고, YOLOv8를 사용하여 개인형 이동장치를 탐지합니다.
2. 위반 탐지 결과 및 표시를 이미지에 표시해줍니다.


## Result
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <img src="https://github.com/PARKYUNSU/cvp/assets/125172299/2950cd9c-a0df-4176-b411-1f75bf84c52f" width="250"><br>자전거 도로 주행 및 헬멧 미착용 | <img src="https://github.com/PARKYUNSU/cvp/assets/125172299/5126d514-6644-4e11-8621-749b0b34aefb" width="250"><br>오토바이 횡단보도 주행 및 정지선 위반 |
| <img src="https://github.com/PARKYUNSU/cvp/assets/125172299/a3ab4254-9861-4060-bb80-de413fb0fd72" width="250"><br>오토바이 정지선 위반 | <img src="https://github.com/PARKYUNSU/cvp/assets/125172299/dfe4116c-3ca6-4460-a287-5dbd1fb60d4c" width="250"><br>오토바이 도로 주행 |
| <img src="https://github.com/PARKYUNSU/cvp/assets/125172299/4d8b3876-372a-4a63-8dde-96ae94b5302a" width="250"><br>자전거 도로 주행 및 헬멧 미착용 | <img src="https://github.com/PARKYUNSU/cvp/assets/125172299/b5b23f41-132a-4fc7-8c57-827e3cdb72f5" width="250"><br>오토바이 도로 주행 |

