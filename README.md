# streamlit-50-startups

## 프로젝트 소개

이 앱은 미국 50개 스타트업의 경영 데이터를 바탕으로, R&D/마케팅/관리비 지출과 지역(State) 정보를 활용해 회사의 수익(Profit)을 예측하는 Streamlit 기반 웹앱입니다.

- **데이터:** `data/50_Startups.csv`
- **주요 기능:**
	- 데이터 탐색(EDA): 변수별 통계, 분포, 상관관계, 시각화, 필터링/다운로드
	- 수익 예측: 입력값 기반 ML 예측(ML 탭)
	- 간단한 데이터 미리보기 및 다운로드(Home 탭)

## 폴더 구조

```
├── app.py              # 메인 Streamlit 앱
├── app_home.py         # Home 탭 화면
├── app_eda.py          # EDA(탐색적 데이터 분석) 탭 화면
├── app_ml.py           # ML(머신러닝 예측) 탭 화면
├── data/
│   └── 50_Startups.csv # 분석 데이터
├── requirements.txt    # 필요한 파이썬 라이브러리 목록
└── README.md           # 프로젝트 설명 파일
```

## 실행 방법

1. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
```

2. 앱 실행

```bash
streamlit run app.py
```

3. 웹 브라우저에서 [http://localhost:8501](http://localhost:8501) 접속

## 주요 라이브러리
- streamlit
- pandas
- matplotlib
- seaborn
- scikit-learn

## 참고
- 데이터 출처: Kaggle 등 공개 데이터셋
- ML/EDA 코드는 각 탭별로 분리되어 관리됩니다.

---
문의/기여: [Issues](https://github.com/Kooooo9/streamlit-50-startups/issues) 활용
