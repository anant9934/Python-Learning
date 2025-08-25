marks = {
    "anant": 99,
    "bikash": 20,
    "chandra": 30,
    "deepak": 40,
    100:"santosh",
    "table" :[1, 2, 3, 4, 5],
}

print(marks, type(marks))  # <class 'dict'>
print(marks["anant"])  # 99

marks.update({"anant": 100, "bikash": 50})
print(marks)  # {'anant': 100, 'bikash': 50, 'chandra': 30, 'deepak': 40, 100: 'santosh', 'table': [1, 2, 3, 4, 5]}
print(marks.get("anant"))  # 100
print(marks.get("santosh", "not found"))  # not found
print(marks.get(100))  # santosh
print(marks.get("santosh"))  # None
print(marks.keys())  # dict_keys(['anant', 'bikash', 'chandra', 'deepak', 100, 'table'])
print(marks.values())  # dict_values([100, 50, 30, 40, 'santosh', [1, 2, 3, 4, 5]])
print(marks.items())  # dict_items([('anant', 100), ('bikash', 50), ('chandra', 30), ('deepak', 40), (100, 'santosh'), ('table', [1, 2, 3, 4, 5])])
print(marks.pop("anant"))  # 100