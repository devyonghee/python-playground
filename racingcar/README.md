# 자동차 경주 게임

- 주어진 횟수 동안 n대의 자동차는 전진 또는 멈출 수 있음
- 사용자는 몇 대의 자동차로 몇 번의 이동을 할 것인지를 입력할 수 있어야 함
- 전진하는 조건은 0에서 9 사이에서 random 값을 구한 후 random 값이 4이상인 경우
- 자동차의 상태를 화면에 출력

- 자동차 이름 부여 자동차 이름은 최대 5자
- 전진하는 자동차를 출력할 때 자동차 이름을 같이 출력
- 자동차 이름은 쉼표(,)를 기준으로 구분
- 자동차 경주 게임을 완료한 후 우승자 출력
- 우승자는 한명 이상

## Model

### RacingCar

- 자동차 이름을 관리
- 움직임의 이동거리 판단

### Track

- 자동차 위치 관리
- 자동차 움직임에 따라 위치 변경

### MoveStrategy

- 랜덤한 숫자를 생성하여 전진 여부 판단

### RacingStadium

- 트랙들을 준비하고 관리
- 지정된 횟수대로 트랙 진행
