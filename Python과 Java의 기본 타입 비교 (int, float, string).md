# Python과 Java의 기본 타입 비교: 숫자와 문자열

## 1. 숫자 타입 (int, float)

### 정수 (Integers)

가장 극적인 차이를 보이는 부분입니다.

#### **Python: `int`**
*   **임의 정밀도 (Arbitrary-precision):** 파이썬의 `int`는 메모리가 허용하는 한 **무한한 크기**를 가질 수 있습니다. 오버플로우(Overflow)가 발생하지 않습니다.
*   **단일 타입:** 작은 정수든, 아주 큰 정수든 모두 `int` 타입 하나로 통일됩니다.

```python
# 파이썬에서는 숫자가 아무리 커져도 int 타입 하나로 처리됩니다.
a = 10
b = 123456789012345678901234567890
print(type(a))  # <class 'int'>
print(type(b))  # <class 'int'>
```

#### **Java: `int`, `long`, `BigInteger`**
*   **고정 크기 (Fixed-size):** Java의 정수 타입은 크기가 정해져 있어 표현할 수 있는 값의 범위가 명확합니다.
    *   `int`: 32비트, 약 -21억 ~ 21억
    *   `long`: 64비트, `int`보다 훨씬 큰 범위를 다룰 때 사용 (숫자 뒤에 `L`을 붙여 표시).
*   **오버플로우 발생:** 정해진 범위를 넘어서는 값을 할당하면 오버플로우가 발생하거나 컴파일 에러가 납니다.
*   **`BigInteger` 클래스:** 파이썬의 `int`처럼 무한한 크기의 정수를 다루려면 `BigInteger`라는 별도의 클래스를 사용해야 합니다.

```java
// Java에서는 값의 크기에 따라 다른 타입을 사용해야 합니다.
int a = 10;
long c = 1234567890123L; // long 타입을 사용하고 L 접미사 필요

// 아주 큰 숫자는 BigInteger 클래스를 사용해야 합니다.
BigInteger d = new BigInteger("123456789012345678901234567890");
```

### 실수 (Floating-point numbers)

#### **Python: `float`**
*   **64비트 정밀도:** 파이썬의 `float`은 **64비트 부동소수점 숫자(double-precision)**를 사용합니다. Java의 `double`과 동일합니다.
*   **단일 타입:** 소수점을 가지는 숫자는 모두 `float` 타입 하나로 처리됩니다.

#### **Java: `float`, `double`**
*   **두 가지 타입:** Java는 정밀도에 따라 두 가지 실수 타입을 제공합니다.
    *   `float`: 32비트 단일 정밀도(single-precision).
    *   `double`: 64비트 배 정밀도(double-precision). **기본(default)** 실수 타입입니다.

### **숫자 타입 핵심 요약**

| 구분 | Python | Java |
| :--- | :--- | :--- |
| **기본 정수** | `int` (크기 무제한) | `int` (32비트), `long` (64비트) |
| **아주 큰 정수** | `int`가 자동으로 처리 | `BigInteger` 클래스 사용 |
| **기본 실수** | `float` (64비트, Java의 `double`과 동일) | `double` (64비트) |
| **타입 시스템** | 동적 타이핑 | 정적 타이핑 |
| **편의성** | 높음 (하나의 타입으로 대부분 처리) | 낮음 (값의 크기와 정밀도에 따라 선택) |

---

## 2. 문자열 타입 (str vs String)

### 핵심 공통점: 불변성 (Immutability)

파이썬의 `str`과 Java의 `String` 객체 모두 **불변(immutable)**입니다. 즉, 한번 생성되면 그 내용을 변경할 수 없으며, 변경 시 새로운 객체가 생성됩니다.

### Python: `str` (편의성과 유연성)

*   **따옴표의 유연성:** `'`와 `"`를 구분 없이 사용할 수 있습니다.
*   **여러 줄 문자열:** `'''` 또는 `"""`를 사용해 여러 줄 문자열을 쉽게 만듭니다.
*   **문자열 포매팅 (f-string):** `f"Hello, {name}"` 형태는 매우 간결하고 가독성이 높습니다.
*   **슬라이싱 (Slicing):** `[start:end:step]` 문법으로 문자열의 일부를 매우 쉽게 잘라낼 수 있습니다.

```python
name = "Alice"
# f-string
greeting = f"Hello, my name is {name}."
# 슬라이싱
text = "Python is fun"
print(text[7:9])     # 'is'
```

### Java: `String` (정적인 구조와 명시성)

*   **선언:** `String` 클래스 타입으로 변수를 선언하고, `"`만을 사용합니다.
*   **가변 문자열 처리:** 문자열을 반복적으로 수정할 때는 가변(mutable) 클래스인 **`StringBuilder`** 또는 **`StringBuffer`**를 사용하는 것이 표준입니다.
*   **메서드 기반 접근:** `charAt(index)`, `substring(begin, end)` 등 모든 조작을 메서드 호출로 수행합니다.
*   **문자열 포매팅:** `String.format("... %s ...", name)` 방식을 사용합니다.

```java
String name = "Alice";
// 문자열 포매팅
String greeting = String.format("Hello, my name is %s.", name);
// 가변 문자열
StringBuilder sb = new StringBuilder();
sb.append("Hello");
// 자르기
String text = "Java is fun";
System.out.println(text.substring(5, 7));  // "is"
```

### **문자열 타입 핵심 요약**

| 구분 | Python (`str`) | Java (`String`) |
| :--- | :--- | :--- |
| **불변성** | **불변 (Immutable)** | **불변 (Immutable)** |
| **선언 방식** | `'`, `"`, `'''`, `"""` 모두 사용 가능 | `"` 만 사용, `String` 타입 명시 |
| **문자열 포매팅** | **f-string (강력하고 간결)** | `String.format()` (기능적이지만 장황) |
| **슬라이싱** | **인덱싱/슬라이싱 `[ ]` (매우 간결)** | `substring()` 메서드 호출 |
| **가변 문자열** | 별도 타입 없음 (`list` 변환 후 `join`) | **`StringBuilder`, `StringBuffer` 클래스** |
