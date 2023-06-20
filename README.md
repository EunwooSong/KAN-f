# KAN-f: Korean Automatic Noise function
2023-data-science-B-team-fig

2023 Data Science Project

팀원: 송은우, 이동혁, 조태현

KoBART Translation 기반으로 모델 성능 평가를 진행함.
[KoBART Translation](https://github.com/seujung/KoBART-translation)
모델 학습 이후, NMT-blue-score를 이용해 모델간 성능을 계산함.

AI Hub의 "일상생활 및 한-영 번역 병렬 말뭉치 데이터"를 사용.

## 폴더 설명
- NMT-blue-score: 모델간 BLEU 성능 평가 진행
- KAN-f: KAN-f 노이즈 정의, 데이터 셋 구축
- collecting-nmt-data: Naver Neural Machine Translation(N2MT), Google Neural Machine Translation(GNMT) 데이터를 받아올 때 사용한 코드를 활용할 수 있음.(papago_response_tsv, google_response_tsv 파일을 최종 사용)
- base-project: 암호화해서 학습시켰을 때, 분류를 잘 하는지에 대한 논문 코드
- gpt-api-project: OpenAI API 테스트