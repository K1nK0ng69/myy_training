calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(info):
    count_calls()
    return len(info), info.upper(), info.lower()

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

res1 = string_info('Capybara')
res2 = string_info('Armageddon')
res3 = is_contains('Urban',['ban','BaNaN','urBAN'])
res4 = is_contains('cycle', ['recycling', 'cyclic'])

print(res1)
print(res2)
print(res3)
print(res4)

print(calls)