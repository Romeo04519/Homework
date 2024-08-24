calls = 0

def count_calls():
    global calls
    calls +=1

def string_info(string = 'BaZinga'):
    count_calls()
    first_func = len(string), string.upper(), string.lower()
    print(first_func)

def is_contains (string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        string = string.lower()
        list_to_search_low = list_to_search[i].lower()
        if string == list_to_search_low:
            return print(True)
        else:
            return print(False)

string_info()
string_info('LunaTic')
is_contains('home',['HoMe','garden','HomeWork'])
is_contains('he', ['she','HEhe','we'])
print(calls)