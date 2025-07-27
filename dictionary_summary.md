# Python 딕셔너리(Dictionary) 총정리

이 문서는 Python의 `dict` 자료형에 대한 기본 개념부터 주요 메소드, 그리고 뷰(View) 객체까지의 내용을 종합적으로 정리합니다.

## 1. 딕셔너리란?

Python의 딕셔너리(`dict`)는 **Key-Value(키-값) 쌍**으로 이루어진 데이터를 저장하는 변경 가능한(mutable) 컬렉션입니다. 중괄호 `{}`를 사용하여 생성하며, 각 항목은 `Key:Value` 형태로 구성되고 쉼표로 구분됩니다.

### 주요 특징

*   **Key-Value 쌍**: 각 항목은 고유한 `Key`와 그에 해당하는 `Value`로 구성됩니다.
*   **변경 가능 (Mutable)**: 생성 후에도 항목을 추가, 삭제, 수정할 수 있습니다.
*   **순서 유지 (Python 3.7+ 부터)**: Python 3.7 버전 이상부터는 입력된 순서가 유지됩니다. 이전 버전에서는 순서가 보장되지 않았습니다.
*   **고유한 Key**: 딕셔너리 내의 `Key`는 중복될 수 없습니다. `Key`는 문자열, 숫자, 튜플과 같이 **변경 불가능한(immutable)** 타입만 사용할 수 있습니다.

## 2. 기본 사용법

### 2.1. 딕셔너리 생성

```python
# 딕셔너리 생성
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)
# 출력: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

### 2.2. 항목 접근, 수정, 추가

```python
# 값 접근 (Key 사용)
print(person["name"])
# 출력: Alice

# 값 변경
person["age"] = 26
print(person)
# 출력: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# 새 항목 추가
person["email"] = "alice@example.com"
print(person)
# 출력: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
```

### 2.3. 항목 삭제

```python
# del 키워드를 사용하여 항목 삭제
del person["city"]
print(person)
# 출력: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
```

## 3. 주요 메소드와 사용 예시

```python
# 예시 딕셔너리
person = {
    "name": "John",
    "age": 30,
    "city": "Seoul"
}
```

### `get(key, default)`

`key`를 사용하여 값을 안전하게 가져옵니다. `key`가 존재하지 않을 경우 오류를 발생시키는 대신 `default` 값을 반환합니다. (`default`가 지정되지 않으면 `None`을 반환)

```python
print(person.get("age"))       # 출력: 30
print(person.get("country"))   # 출력: None
print(person.get("country", "Unknown")) # 출력: Unknown
```

### `pop(key, default)`

`key`에 해당하는 항목을 딕셔너리에서 **제거하고** 그 `value`를 반환합니다. `key`가 없을 경우 `default` 값을 반환하며, `default`가 없으면 오류가 발생합니다.

```python
removed_city = person.pop("city")
print(f"제거된 값: {removed_city}") # 출력: 제거된 값: Seoul
print(f"pop 후 딕셔너리: {person}") # 출력: pop 후 딕셔너리: {'name': 'John', 'age': 30}
```

### `clear()`

딕셔너리의 모든 항목을 제거하여 빈 딕셔너리로 만듭니다.

```python
person.clear()
print(person) # 출력: {}
```

## 4. 딕셔너리 뷰(View) 객체: `keys()`, `values()`, `items()`

`.keys()`, `.values()`, `.items()` 메소드는 단순한 리스트가 아닌 **뷰(View) 객체**를 반환합니다.

### 4.1. 뷰 객체란?

뷰 객체는 원본 딕셔너리의 데이터를 실시간으로 보여주는 **동적인 창**입니다.

*   **동적(Dynamic)**: 원본 딕셔너리가 변경되면 뷰 객체도 즉시 변경 사항을 반영합니다.
*   **반복 가능(Iterable)**: `for` 루프에서 사용할 수 있습니다.
*   **메모리 효율적**: 데이터의 복사본을 만들지 않아 메모리를 절약합니다.

### 4.2. 뷰 객체의 종류와 사용법

```python
person = {'name': 'Chris', 'age': 35, 'city': 'London'}

# 1. keys() -> dict_keys
# 모든 키를 보여주는 뷰를 반환합니다.
keys_view = person.keys()
print(keys_view) # 출력: dict_keys(['name', 'age', 'city'])

# 2. values() -> dict_values
# 모든 값을 보여주는 뷰를 반환합니다.
values_view = person.values()
print(values_view) # 출력: dict_values(['Chris', 35, 'London'])

# 3. items() -> dict_items
# 모든 (키, 값) 쌍을 튜플로 묶어 보여주는 뷰를 반환합니다.
items_view = person.items()
print(items_view) # 출력: dict_items([('name', 'Chris'), ('age', 35), ('city', 'London')])
```

### 4.3. 뷰 객체 활용 (for 루프)

뷰 객체는 `for` 루프와 함께 사용할 때 매우 유용합니다.

```python
# 키 순회
for key in person.keys():
    print(f"Key: {key}")

# 값 순회
for value in person.values():
    print(f"Value: {value}")

# 키와 값 동시 순회 (가장 일반적인 사용법)
for key, value in person.items():
    print(f"{key}: {value}")
```

### 4.4. 뷰를 리스트로 변환하기

뷰 객체는 동적이기 때문에 특정 시점의 데이터를 고정된 리스트로 만들고 싶을 때 `list()` 생성자를 사용합니다.

```python
keys_list = list(person.keys())
print(keys_list) # 출력: ['name', 'age', 'city']

# 리스트로 변환하면 원본 딕셔너리가 변경되어도 리스트는 영향을 받지 않습니다.
person['job'] = 'Developer'
print(keys_list) # 출력: ['name', 'age', 'city'] (변경 없음)
```
