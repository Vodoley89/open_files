
with open ('recipes.txt' , 'r' , encoding= 'utf-8') as file:
    for l in file:
        dish = l.strip()
        list_products =[]
        ingrid_count = file.readline()
        for i in range(int(ingrid_count)):
            ingridient = file.readline()
            ingredient_name , quantity , measure = ingridient.strip().split(' | ')
            list_products.append({'ingredient_name': ingredient_name , 'quantity': quantity, 'measure': measure})
        blank = file.readline()
        cook_book = {dish: list_products}
        print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    cook_dict = {}
    dishes = cook_book.keys()
    for dish in dishes:


        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] in cook_dict:
                cook_dict['ingredient_name']['quantity'] += ingridient['quantity']

            else:
                cook_dict = {ingridient['ingredient_name']: {ingridient['quantity'], ingridient['measure']}}
                print(cook_dict)
    for ingredient_name in cook_dict.keys():
        person = ingridient['quantity'] * person_count

get_shop_list_by_dishes(['Омлет'], 2)




