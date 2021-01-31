# решение задания 5 из урока 2
# почему new_digit не итеративный объект?
# цикл не запускается

my_list = [7, 5, 3, 3, 2]

while True:
    new_digit = input('Введите новый элемент рейтинга: ')
    new_digit = int(new_digit)

    for my_list in range(1, len(my_list)):
          if new_digit >= max(my_list):
            my_list.insert(0, new_digit)
            break
          elif new_digit <= min:
            my_list.append(new_digit)
            break
          elif my_list[i-1] >= new_digit >= my_list[i]:
              my_list.insert(1, new_digit)
              break

    print(my_list)

