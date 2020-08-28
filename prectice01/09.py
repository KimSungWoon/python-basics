#9 번 딕셔러니 사용
menu = input('메뉴: ')
menu_dic = {}
if menu == '오뎅':
    price = 300
elif menu == '순대':
    price = 400
elif menu == '만두':
    price = 500
else:
    price = 0

print('가격: {0}'.format(menu_dic[.menu]))

print('가격: {0}'.format(menu_dic.get[.menu]))

print('가격: {0}'.format(menu_dic.setdefault((menu,0)))
