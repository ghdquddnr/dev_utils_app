# 개발자 유틸리티 앱 (Dev Utils App)

개발자를 위한 다양한 유틸리티 기능을 제공하는 파이썬 GUI 애플리케이션입니다. 현대적인 UI와 편리한 기능으로 개발 작업을 더 효율적으로 만들어 줍니다.

*Read this in other languages: [English](README.en.md), [日本語](README.ja.md), [简体中文](README.zh-CN.md), [Español](README.es.md), [Français](README.fr.md), [Deutsch](README.de.md)*

![애플리케이션 스크린샷](screenshot.png)

## 주요 기능

### 텍스트 비교 (Text Diff)
- 두 텍스트 사이의 차이점을 시각적으로 표시
- 라인별 비교를 통한 정확한 차이점 하이라이트
- 직관적인 UI로 손쉬운 사용
- 초기화 버튼으로 빠르게 작업 리셋

### JSON 뷰어 (JSON Viewer)
- JSON 문자열을 트리 구조로 시각화
- 노드 접기/펼치기 기능으로 복잡한 구조도 쉽게 탐색
- 예제 데이터 제공으로 빠른 테스트 가능
- 라이트/다크 모드에 따라 자동으로 테마 변경

## 기술 스택

- **프론트엔드**: CustomTkinter (Python GUI 라이브러리)
- **비교 알고리즘**: diff-match-patch 라이브러리
- **JSON 파싱**: Python 내장 json 모듈
- **테마 시스템**: 라이트/다크 모드 지원

## 시스템 요구사항

- Python 3.8 이상
- 아래 파이썬 패키지:
  - customtkinter
  - pillow
  - diff-match-patch

## 설치 방법

### 1. 저장소 클론
```bash
git clone https://github.com/ghdquddnr/dev_utils_app.git
cd dev_utils_app
```

### 2. 가상환경 설정 및 패키지 설치
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 패키지 설치
pip install customtkinter pillow diff-match-patch
```

### 3. 애플리케이션 실행
```bash
python main.py
```

## 사용 방법

### 텍스트 비교 기능
1. 왼쪽 텍스트 영역에 원본 텍스트를 입력합니다.
2. 오른쪽 텍스트 영역에 비교할 텍스트를 입력합니다.
3. "비교하기" 버튼을 클릭하면 두 텍스트 간의 차이점이 색상으로 표시됩니다.
   - 삭제된 부분: 빨간색 배경
   - 추가된 부분: 녹색 배경
4. "초기화" 버튼을 클릭하면 모든 텍스트가 지워지고 새로운 비교를 시작할 수 있습니다.

### JSON 뷰어 기능
1. 왼쪽 텍스트 영역에 JSON 문자열을 입력합니다.
2. "변환하기" 버튼을 클릭하면 오른쪽에 트리 구조로 JSON이 시각화됩니다.
3. 트리 노드의 + 또는 - 버튼을 클릭하여 해당 노드를 펼치거나 접을 수 있습니다.
4. "모두 펼치기"/"모두 접기" 버튼으로 전체 트리를 한번에 제어할 수 있습니다.
5. "예제 데이터" 버튼을 클릭하면 샘플 JSON 데이터가 자동으로 입력됩니다.
6. "초기화" 버튼을 클릭하면 모든 데이터가 지워집니다.

### 테마 변경
- 사이드바 하단의 "테마 변경" 버튼을 클릭하여 라이트/다크 모드를 전환할 수 있습니다.

## 개발 환경 설정

```bash
# 개발용 패키지 설치
pip install -e ".[dev]"
```

## 향후 계획

- 추가 유틸리티 기능 개발 예정
- 성능 최적화
- 사용자 설정 저장 기능

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 기여하기

기여는 언제나 환영합니다! 버그 리포트, 기능 요청 또는 코드 기여를 통해 이 프로젝트를 개선하는데 도움을 주실 수 있습니다. 