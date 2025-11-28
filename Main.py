from time import time, sleep

print("Darkness Within")

print()
def ask_yes():
    n = input().lower()
    while n != 'да' and n != "нет":
        print('Напиши да или нет')
        n = input().lower()
    return n == "да"

print()
print('Если хотите пропустить вступление? Напишите "да" или "нет"')
if ask_yes():
    flag = False
else:
    flag = True

fail = open("Text.txt", encoding='utf-8')

for i in range(18):
    print(fail.readline(), end = "")
    if flag:
        sleep(2)

point = [0,2]
health, mind, power = 5, 5, 5
game = True
strange_key = False
rat = True
lever = True
bat = True
skeleton = True
thicket1 = True
monster = False
thicket2 = True
matches = False
camp = True
right_text = [[fail.readline()[4:-1] for x in range(5)] for x in range(5)]
left_text = [[fail.readline()[4:-1] for x in range(5)] for x in range(5)]
front_text = [[fail.readline()[4:-1] for x in range(5)] for x in range(5)]
back_text = [[fail.readline()[4:-1] for x in range(5)] for x in range(5)]
wall_right = [[0,4],[1,4],[2,4],[3,4],[4,4],[1, 1], [0, 1], [0, 3], [1, 0], [1, 2], [2, 1], [2, 2], [2, 3], [3, 1], [3,0]]
wall_left = [[0,0],[1,0],[2,0],[3,0],[4,0],[0, 2], [0, 4], [1, 1], [1, 3], [2, 2], [2, 3], [2, 4], [3, 2]]
wall_front = [[4,1],[4,0],[4,2],[4,3],[4,4],[3, 2],[3,1], [3, 3], [2, 0], [2, 3], [1, 0], [1, 2]]
wall_back = [[0,0],[0,1],[0,2],[0,3],[0,4],[2, 0], [3, 0], [4, 2], [4, 3], [4, 1], [3, 3], [2, 2]]

def character():
    global health, mind, power
    print()
    print("Характеристики персонажа:")
    print(f'Здоровье - {health}')
    print(f'Рассудок - {mind}')
    print(f'Энергия - {power}')
    print()

character()

def PossibleDirection():
    global wall_left, wall_front, wall_back, wall_right
    Text = "Возможные направления: "
    if not point in wall_front:
        Text += "север "
    if not point in wall_back:
        Text += "юг "
    if not point in wall_right:
        Text += "восток "
    if not point in wall_left:
        Text += "запад "
    print(Text)

def kinds():
    print("Куда хочешь пойти? ", end = '')
    PossibleDirection()
    n=input().lower()
    while n !="юг" and n!='север' and n!='запад' and n!= "восток" or n=='':
        print("Неправильное направление.")
        PossibleDirection()
        n=input()
    return n

def ShiftPoint(change, Direction):
    global point, wall_right, wall_left
    if change == "юг" and not point in wall_back:
        print(Direction[point[0]][point[1]])
        point[0] -= 1
    elif change == "север" and not point in wall_front:
        print(Direction[point[0]][point[1]])
        point[0] += 1
    elif change == "восток" and not point in wall_right:
        print(Direction[point[0]][point[1]])
        point[1] += 1
    elif change == "запад" and not point in wall_left:
        print(Direction[point[0]][point[1]])
        point[1] -=1
    else:
        print("Выберите другое направление. Там стена")
        return False
    return True

def ChangeAttribute(n, word):
    global health, mind, power
    print(f"{word} {n}")
    if word == "Здоровье":
        health += n
    if word == "Рассудок":
        mind += n
    if word == "Энергия":
        power += n
    character()
    if health <=0 or mind <=0 or power <= 0:
        EndGame(0)

def FightRat():
    global rat
    if rat:
        print("Ты можешь дать бой или убежать")
        print("Дать бой?")
        if ask_yes():
            print("После долгого сражения и двух укусов твоей ноги злой Рататуй повержен, хотя под конец тебе даже стало его немного жалко.")
            print("Стена на Востоке")
            ChangeAttribute(-1, "Здоровье")
            back_text[3][1] = "Раньше здесь жила крыса, пока не пришел ты."
            right_text[2][0] = "Раньше здесь жила крыса, пока не пришел ты."
            right_text[2][1] = "Wall"
            front_text[1][1] = "Раньше здесь жила крыса, пока не пришел ты."
            rat = False
        else:
            print("Стена на Востоке")

def Camp():
    global matches, front_text, left_text, camp
    print("В инвентарь добавлен предмет: Спички")
    matches = True
    camp = False
    print("Выпить содержимое фляги?")
    if ask_yes():
        print("Желание пить взяло над вами верх. К вашему счастью вода не отравлена, даже лучше - это энергетик!")
        ChangeAttribute(2, "Энергия")
    else:
        print("В детстве тебя учили не пить из неизвестных мест. Ты кладешь флягу туда, где она и лежала.")
    left_text[2][1] = "Ты пришёл к лагерю. Все ценное ты отсюда уже забрал."
    print("Вы в тупике.")

def Skeleton():
    global skeleton, wall_left
    print("Рядом со скелетом лежит сумка. Решив, что она ему не нужна ты забираешь её себе.")
    print("В сумке лежат: красный флакон, зеленый флакон, фиолетовый флакон и ржавый ключ")
    print("Выпить содержимое красного флакона?")
    if ask_yes():
        print("У жидкости оказался противный вкус и не менее противный эффект. У вас кружится голова и болит живот.")
        ChangeAttribute(-2, "Здоровье")
        ChangeAttribute(-2, "Рассудок")
    else:
        print("Ты решил не пить странную жидкость.")
    print("Выпить содержимое зеленого флакона?")

    if ask_yes():
        print("Выпив содержимое флакона, тебе кажется, что сил стало больше.")
        ChangeAttribute(1, "Здоровье")
        ChangeAttribute(2, "Энергия")
    else:
        print("Ты решил не пить странную жидкость.")
    print("Выпить содержимое фиолетового флакона?")

    if ask_yes():
        print("Выпив странную жидкость вы без сознания падаете на пол. Все-таки не стоит пить все что попало.")
        EndGame(0)
        return 0
    else:
        print("Ты решил не пить странную жидкость.")
    front_text[1][3] = "Ты пришел к скелету. Ему повезло меньше, чем тебе. Ты в тупике. Единственный путь - на Юг."
    print("В инвентарь добавлен предмет: Ржавый ключ")
    wall_left.remove([1,0])
    print("Ты в тупике. Единственный путь - назад.")
    skeleton = False

def Lever():
    global lever, wall_front

    if ask_yes():
        print("После нажатия рычага, ты услышал отчётливый металлический скрежет. Нехило испугавшись, ты понимаешь, что запустил какой-то механизм.")
        ChangeAttribute(-1, "Рассудок")
        wall_front.remove([4,1])
        front_text[4][1]="Ты подходишь к открытой решетке. Поздравляю, выход найден, жизнь спасена, хотя ты до сих пор не вернулся туда, откуда пришёл. Это точно... Выход? "
        back_text[1][4] = "Ты уже исследовал это помещение. Повторное нажатие на рычаг не даёт никаких результатов."
        lever = False

    else:
        print("Ты не стал нажимать на рычаг. А вдруг это ловушка?")

def Door():
    global point, back_text, front_text, strange_key
    if not strange_key:
        if point == [1, 3]:
            point = [1, 4]
        elif point == [1, 4]:
            point = [1, 3]
        if ask_yes():
            ChangeAttribute(-1, "Здоровье")
            ChangeAttribute(-1, "Энергия")
            print("Дверь крепче вас. Она даже не шелохнулась. Ты ударился и устал.")
            print("Стена на Западе, на Востоке - дверь.")
        else:
            print("Без ключа её не открыть. Возможно когда-нибудь ты его найдёшь.")

    if strange_key:
        back_text[2][3] = "Ты здесь уже был. На Западе стена, на Востоке открытая дверь."
        front_text[0][4] = "Ты вышел из тупика. На Западе - открытая дверь. На Востоке - стена."
        back_text[2][4] = "Ты вышел из тупика. На Западе - открытая дверь. На Востоке - стена."

def Thicket(th):
    global matches
    thicket = th
    if matches and thicket:

        if ask_yes():
            print("Воспользовавшись спичкой, ты поджигаешь заросли. Свет от огня ослепляет тебя, но проход теперь свободен.")
            ChangeAttribute(-1, "Здоровье")
            return False

        else:
            print("Ты решаешь пробираться через заросли своими силами. Колючки режут твоё тело, чем дальше ты идешь тем хуже.")
            print("Но в конце концов заросли кончаются, а ты уставший и израненный садишься на холодный пол.")
            ChangeAttribute(-1, "Энергия")
            ChangeAttribute(-2, "Здоровье")

    elif thicket and not matches:
        print("Ты пробираешься через заросли. Колючки режут твоё тело, чем дальше ты идешь тем хуже.")
        print(" Но в конце концов заросли кончаются, а ты уставший и израненный садишься на холодный пол.")
        ChangeAttribute(-1, "Энергия")
        ChangeAttribute(-2, "Здоровье")
    return True

def Monster():
    global back_text, right_text, monster
    monster = True
    if ask_yes():
        print("Ты решил побежать и не оглядываться. Существо погналось за тобой. Коридор свернул на Юг. Вы перед развилкой: продолжить бежать на Юг или свернуть на Запад?")
    else:
        print("Любопытство взяло верх перед инстинктом самосохранения. Вы обернулись посмотреть - что за существо за вами идет.")
        print("Жаль, но, не успев разглядеть сущность, вы почувствовали, что ваша голова отделена от тела. Кажется вы... погибли.")
        EndGame(0)

def Hatch():
    global power,point

    if ask_yes():
        if power >= 3:
            print("Вам хватает сил, чтобы поднять люк.")
            print("Поздравляю вы выбрались из лабиринта.")
            EndGame(2)
        else:
            print("Вам не хватило сил поднять люк.")
            print("Больше ничего примечательного в этой комнате нет")
    else:
        print("Ты решил не открывать странный люк на потолке. Тебе понравилось в подземелье?")

def EndGame(n):
    global clock, game
    print()
    if n==0:
        print("К сожалению ваш персонаж погиб. :((")
    else:
        print(f"Поздравляю вы прошли на концовку: Концовка {n}")
    print(f"Время прохождения: {round((time()-clock)/60)} минут {(int(time()-clock)%60)} секунд")
    print("Спасибо за игру!")
    game = False

clock=time()

while game:

    word = kinds()

    if word == "юг":
        if point==[3,4] and monster:
            monster = False
            print("Ты очень устал.")
            ChangeAttribute(-2,"Энергия")
            print("Кажется ты оторвался от преследователя. Находясь в пустом коридоре, вас не покидает ощущение, что эта сущность может напасть в любой момент.")
        if point == [1,0] and thicket1:
            thicket1 = Thicket(thicket1)
        if point == [2,1] and rat:
            print("Тебе удалось сбежать от Крысы. Устал, но не покусан")
            ChangeAttribute(-1, "Энергия")
        pos = ShiftPoint(word, back_text)
        if point == [0, 2]:
            strange_key = True
            left_text[1][4] = "Перед тобой на вид прочная деревянная дверь. Попробовав открыть её, давно найденным ключом, она поддалась. За ней развилка - на Север и Юг? На Западе стена"
            right_text[1][3] = "Перед тобой на вид прочная деревянная дверь. Попробовав открыть её, найденным ранее ключом, она поддалась. За ней развилка - на Север и Юг? На Востоке стена"
            print("Обернувшись и сделав шаг, ты упираешься в... дверь? В попытках отыскать ручку, ты находишь замочную скважину, внутри которой ключ.")
            print("В инвентарь добавлен предмет: Странный ключ")
        if point == [2,1]:
            FightRat()
        if point == [0,4] and lever:
            Lever()
        if point == [3,0] and pos and thicket2:
            thicket2 = Thicket(thicket2)
            print("Ты в тупике. Единственный путь на Север.")
        if point == [2,2] and pos:
            Hatch()

    if word == "север":
        if point == [3,4] and monster:
            print("Любопытство взяло верх перед инстинктом самосохранения. Вы обернулись посмотреть - что за существо за вами идет.")
            print("Жаль, но, не успев разглядеть сущность, вы почувствовали, что ваша голова отделена от тела.")
            EndGame(0)
        if point == [3,4]:
            print('Вы долго идете по темному коридору, ничего интересного по пути не было. ')
            if not lever:
                print("Случайно, ты замечаешь решетку - она зависла в полуоткрытом положении. Возможно это выход?")
            point=[4,1]
        if (point == [3,0] and thicket2) or (point == [0,0] and thicket1):
            if matches:
                print("Перед тобой заросли. Растения сухие, но очень колючие. У тебя есть спички. Поджечь заросли?")
            else:
                print("Перед тобой заросли. Растения сухие, но очень колючие. Были бы у тебя спички...")
            if point == [3,0]:
                thicket2 = Thicket(thicket2)
                if not thicket2:
                    front_text[3][0] = "Ты проходишь по золе, оставленной после сожжения колючек. Единственный звук, в этом месте - твои шаги."
            else:
                thicket1 = Thicket(thicket1)
        if point == [2, 1] and rat:
            print("Тебе удалось сбежать от Крысы. Устал, но не покусан")
            ChangeAttribute(-1, "Энергия")
        pos = ShiftPoint(word,front_text)
        if point == [4,4]:
            point = [3,4]
        if point == [2,3] and skeleton:
            Skeleton()
        if point == [1, 2]:
            ShiftPoint("запад", left_text)
            ChangeAttribute(-1, "Здоровье")
        if point == [2, 1]:
            FightRat()

    if word == "восток":
        pos = ShiftPoint(word,right_text)
        if point == [1,4]:
            Door()
        if point == [0, 3] and pos:
            ChangeAttribute(-1, "Рассудок")
        if point == [2, 1]:
            if rat and not pos:
                print("Крыса вас укусила. Ты не смог сбежать")
                ChangeAttribute(-1, "Здоровье")
                ChangeAttribute(-1, "Энергия")
            FightRat()
        if point == [4,2]:
            point = [3,4]
            Monster()

    if word == "запад":
        if point==[3,4] and monster:
            monster = False
            print("Ты очень устал.")
            ChangeAttribute(-2, "Энергия")
            print("Кажется ты оторвался от преследователя. Находясь в пустом коридоре, вас не покидает ощущение, что эта сущность может напасть в любой момент.")
        if point == [2, 1] and rat:
                print("Тебе удалось сбежать от Крысы. Устал, но не покусан")
                ChangeAttribute(-1, "Энергия")
        pos = ShiftPoint(word, left_text)
        if point == [2, 0] and camp:
           Camp()
        if point == [1,3]:
            Door()
        if point == [0,0] and bat:
            bat = False
            right_text[0][1] = "Вроде летучая мышь уже улетела, но ты готов к худшему."
            ChangeAttribute(-1, "Рассудок")

    if point == [1,-1]:
        EndGame(3)
    if point == [5,1]:
        EndGame(1)
print("Нажмите Enter чтобы закрыть игру")
a=int(input())

