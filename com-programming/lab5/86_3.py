"""
TEST CASE

Hello-ณัฐนนท์-64090500431

"""


result = filter(lambda x: 65 <= ord(x) <= 90 or 97 <=
                ord(x) <= 122, list(input()))
print("".join(result))
