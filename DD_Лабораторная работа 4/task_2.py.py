def get_count_char(str_):
    count_char_dict_ = {}
    for symbol in str_.lower():
        if symbol.isalpha():
            if symbol in count_char_dict_:
                count_char_dict_[symbol] += 1
            else:
                count_char_dict_[symbol] = 1
    return count_char_dict_

def percent_char (count_char_dict_):
    i = 0
    percent_dict = {}
    for char in count_char_dict_:
        i += count_char_dict_.get(char)
    for char in count_char_dict_:
        percent_dict[char] = round((count_char_dict_.get(char)/i)*100, 2)
    check = 0
    for char in percent_dict:
        check += percent_dict.get(char)
    return percent_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(percent_char(get_count_char(main_str)))