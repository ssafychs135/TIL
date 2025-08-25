# CSS 상속(Inheritance) 완벽 가이드

CSS 상속은 부모 요소(parent element)에 적용된 특정 CSS 속성들이 그 자식 요소(child element)에게 그대로 전달되어 적용되는 현상을 말합니다. 이 개념을 잘 이해하면 코드의 양을 획기적으로 줄이고, 스타일이 적용되는 방식을 쉽게 예측할 수 있습니다.

---

## 1. CSS 상속이란 무엇인가? (개념)

CSS 상속은 **부모 요소에 적용된 특정 CSS 속성들이 그 자식 요소에게 그대로 전달되어 적용되는 현상**입니다.

마치 현실에서 자식이 부모의 특정 형질(눈 색깔, 머리카락 색 등)을 물려받는 것과 같습니다. HTML 문서 구조에서 `<body>` 태그 안에 `<p>` 태그가 있다면, `<body>`는 부모, `<p>`는 자식이 됩니다.

**왜 필요할까요?**
만약 상속이 없다면, 우리는 웹 페이지의 모든 요소 하나하나에 글자 크기, 색상, 글꼴 등을 전부 따로 지정해야 할 겁니다. 상속이 있기 때문에 `<body>` 태그에 한 번만 글꼴과 색상을 지정하면, 대부분의 자식 요소들이 그 스타일을 물려받아 통일성 있는 디자인을 쉽게 구현할 수 있습니다.

---

## 2. 모든 속성이 상속될까? (상속되는 속성 vs. 안 되는 속성)

**아니요, 모든 CSS 속성이 상속되지는 않습니다.** 상속 여부는 속성의 성격에 따라 결정됩니다.

#### ✅ **상속되는 속성들 (주로 텍스트 관련)**
자식에게 물려주었을 때 전체적인 통일성을 부여하는 속성들입니다.

*   **글자/글꼴 관련:** `color`, `font-family`, `font-size`, `font-weight`, `font-style`, `line-height`
*   **텍스트 정렬 관련:** `text-align`, `text-indent`, `text-transform`
*   **목록 관련:** `list-style`, `list-style-type` 등
*   **가시성:** `visibility`
*   **커서:** `cursor`

#### ❌ **상속되지 않는 속성들 (주로 박스 모델 관련)**
자식에게 물려주면 레이아웃이 망가질 수 있는 속성들입니다.

*   **박스 모델:** `width`, `height`, `margin`, `padding`, `border`
*   **배경:** `background`, `background-color`, `background-image` 등
*   **위치/레이아웃:** `position`, `top`, `left`, `display`, `float`, `clear`
*   **Flexbox, Grid 관련 속성들**

---

## 3. 상속을 제어하는 방법 (Inheritance Keywords)

CSS는 상속을 개발자가 직접 제어할 수 있도록 특별한 키워드 값을 제공합니다.

#### 1) `inherit` (강제 상속)
*   **기능:** 원래 상속되지 않는 속성을 **강제로 부모로부터 상속받게** 만듭니다.
*   **사용 예시:**
    ```css
    .parent {
      border: 2px solid blue;
    }
    .child {
      /* 원래 border는 상속되지 않지만, inherit 키워드로 강제 상속 */
      border: inherit; 
    }
    ```

#### 2) `initial` (초기값으로 리셋)
*   **기능:** 부모로부터 상속받은 값이 무엇이든 무시하고, 해당 속성의 **브라우저가 정의한 기본값(초기값)으로 되돌립니다.** 상속의 연결을 끊는 역할을 합니다.
*   **사용 예시:**
    ```css
    body {
      color: blue; /* 모든 자식에게 파란색을 물려줌 */
    }
    .special-text {
      /* 부모로부터 물려받은 blue를 무시하고, color의 초기값(보통 black)으로 설정 */
      color: initial; 
    }
    ```

#### 3) `unset` (상황에 따라 리셋)
*   **기능:** 가장 똑똑한 키워드로, 속성의 성격에 따라 다르게 동작합니다.
    *   **상속되는 속성(예: `color`)에 사용하면 → `inherit`처럼 동작합니다.**
    *   **상속되지 않는 속성(예: `width`)에 사용하면 → `initial`처럼 동작합니다.**
*   **사용 예시:**
    ```css
    /* 예시 1: 상속되는 속성에 사용 */
    body { color: blue; }
    p { color: unset; } /* 부모(body)로부터 blue를 상속받아 inherit처럼 동작 */

    /* 예시 2: 상속되지 않는 속성에 사용 */
    div { width: 300px; }
    div { width: unset; } /* width는 상속되지 않으므로 initial처럼 동작. width의 초기값인 auto로 설정됨 */
    ```

#### 4) `revert` (한 단계 위로 리셋)
*   **기능:** `initial`보다 한 단계 덜 되돌아갑니다. 현재 요소에 적용된 스타일을 무시하고, **브라우저의 기본 스타일 시트(user-agent stylesheet)가 적용된 상태로** 되돌립니다. (초급 단계에서는 `initial`과 `unset`만으로도 충분합니다.)

---

## 4. 종합 예제

아래 예제는 상속의 모든 개념을 담고 있습니다.

**HTML:**
```html
<div class="grand-parent">
  할아버지 요소입니다.
  <div class="parent">
    부모 요소입니다.
    <p class="child-1">첫째 자식입니다. (일반 상속)</p>
    <p class="child-2">둘째 자식입니다. (상속 덮어쓰기)</p>
    <p class="child-3">셋째 자식입니다. (상속 끊고 초기화)</p>
  </div>
  <a href="#" class="special-link">이 링크는 테두리를 강제 상속받습니다.</a>
</div>
```

**CSS:**
```css
/* 최상위 부모: 기본 스타일을 정의하고 자식들에게 물려줌 */
.grand-parent {
  color: darkblue; /* 글자색: 다크블루 (자식들에게 상속됨) */
  font-family: "Malgun Gothic", sans-serif; /* 글꼴 (자식들에게 상속됨) */
  border: 5px dotted green; /* 테두리 (상속 안 됨) */
  padding: 20px; /* 패딩 (상속 안 됨) */
}

/* 중간 부모: 할아버지의 스타일을 일부 상속받고, 일부는 변경 */
.parent {
  /* color와 font-family는 .grand-parent로부터 상속받음 */
  border: 3px solid orange; /* 자신만의 테두리 지정 (상속 안 됨) */
  padding: 15px; /* 자신만의 패딩 지정 (상속 안 됨) */
}

/* 첫째 자식: 부모(.parent)의 스타일을 그대로 물려받음 */
.child-1 {
  /* 특별히 지정한 스타일이 없으므로, 부모로부터 color와 font-family를 상속받음 */
}

/* 둘째 자식: 부모로부터 상속받은 스타일을 자신만의 스타일로 덮어씀 */
.child-2 {
  color: crimson; /* 부모로부터 상속받은 darkblue를 무시하고 crimson으로 덮어쓰기 */
}

/* 셋째 자식: 부모로부터 상속받은 스타일을 브라우저 초기값으로 되돌림 */
.child-3 {
  color: initial; /* 상속받은 darkblue를 무시하고 브라우저 기본 색상(보통 검은색)으로 리셋 */
}

/* 특별한 링크: 원래 상속되지 않는 border 속성을 강제로 상속받음 */
.special-link {
  display: block; /* a 태그는 inline이라 border를 잘 보여주기 위해 block으로 변경 */
  margin-top: 10px;
  
  /* 
    a 태그의 부모는 .grand-parent 이므로, 
    .grand-parent의 '5px dotted green' 테두리를 강제로 상속받음 
  */
  border: inherit; 
}
```
