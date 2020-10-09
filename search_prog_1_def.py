import re
import sys
import group_info_1 as f

# all the groups and words are imported from group_info_1.py
# make content groups from back cover text (takzir)
# write txt file

# run the program in idle or pycharm etc
# part 1 - user input
'''
input from user ->
the fastest way to run the program is ->
enter -> * enter -> copy clean takzir -> cmd d or ctrl d -> watch the results
'''


def user_input():
    book_name=input("book name (optional, enter its ok) ->")
    category = []
    print("-------")
    x=True
    while x:
     app=input("choose category - new category in each line, to end list press / or press * to choose all categories ->")
     # remove white space form start, end of input
     app_inp=app.strip()
     category.append(app_inp)
     if app_inp == "/":
       x=False
     if app_inp=="*":
       category=f.all_groups_str
       x=False
     print(category)
     print("-------")
     print("copy clean takzir here - press cmd d or enter and ctrl d (or ctrl z) after ->")

     # multi line stuff
     text = sys.stdin.readlines()

     print("-------")
     print(book_name)
     print(text)
     print("-------")
     return text, book_name, category


print()

# part 2 - find words
# choose on what category to run from all_groups list  ->
# then run over the category group (holder) and find words in keys values with re.search()


def search_words(text, category):
    # for info.txt
    text_result = []
    sign = "\n"
    len_all_groups_str=len(f.all_groups_str)
    for groupi in f.all_groups_str:
     for cat in category:
        #print(cat, groupi)
         if cat==groupi:
            print (groupi, f.all_groups_str.index(cat))
            group_to_print=groupi
            tempr=f.all_groups_str.index(cat)
            holder = f.all_groups[tempr]
            # the actual code - finds the words
            len_holder = len(holder)
            for group in range(len_holder):
                for item in holder[group]:
                # print(item)
                    for key, val in item.items():
                       for line in text:

                            k_search = re.search(rf"{key}", line)
                            if k_search:
                                print(group_to_print, ": ", k_search.group(), " - ", key)

                                text_result.append(group_to_print)
                                text_result.append(k_search.group())
                                text_result.append(key)
                                text_result.append(sign)

                            for valey in val:
                                val_search = re.search(rf"{valey}", line)
                                if val_search:
                                    print(group_to_print, ": ", val_search.group(), " - ", key)

                                    text_result.append(group_to_print)
                                    text_result.append(val_search.group())
                                    text_result.append(key)
                                    text_result.append(sign)
    return text_result

# part 3 - write results to txt file


def write_file(text, category, book_name, text_result):
    f = open("info2.txt", "a")

    f.write("\n שם הספר: \n")
    f.write(book_name)
    f.write("\n")

    f.write("\n התקציר: \n")
    for lines in text:
      f.write(lines)
    f.write("\n")

    f.write("\n קטגוריות החיפוש: \n")
    for groupa in category:
        f.write(groupa)
        f.write(" ")
    f.write("\n")

    f.write("\n הקבוצות והמילים: \n")
    for found in text_result:
        f.write(found)
        f.write(" ")
    f.write("\n")
    f.write(" ------------------------------------------------------------------------------- ")

    f.close()


n_text, n_book_name, n_category = user_input()
text_results = search_words(n_text, n_category)
write_file(n_text, n_category, n_book_name, text_results)
#print(text_results)




