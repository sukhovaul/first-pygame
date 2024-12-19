from pygame import*
from time import*
from random import*

init() #инициализируем pygame

screen = display.set_mode((750,750)) #устанавливаем размер окна
display.set_caption('game') #устанавливаем заголовок

#сохраняем цвета в переменные
brown = (101,67,33)
light_brown = (191,157,123)
red = (255,0,0)
blue = (163, 206, 255)
white = (200,200,200)

#работа с шрифтами
font_path = 'fonts/Dudka Bold.ttf'
font_main = font.Font(font_path, 36)
font_question = font.Font(font_path, 26)
task_font = font.Font(font_path, 20)
element_font = font.Font(font_path, 13)

#загрузка музыки
right_answer = mixer.Sound('music/win_sound.mp3')
wrong_answer = mixer.Sound('music/wrong_answer.mp3')

#функция для создания кнопок
def draw_button(screen, text, rect,font,color,rect_color, btn_width, image_path = None): # шаг 1 - создали функцию создания кнопки
    draw.rect(screen, rect_color, rect, btn_width) #рисуем прямоугольник

    if image_path:
        button_image = image.load(image_path)
        image_rect = button_image.get_rect(center = (rect[0]+rect.width // 2, rect[1]+rect.height//2))
        screen.blit(button_image, image_rect)

    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line != "" else word
        test_surface = font.render(test_line, True, color)

        if test_surface.get_width() <= rect.width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    total_height = len(lines) * 10  # общая высота текста
    y = rect.y + (rect.height - total_height) // 2  # центрирование текста по вертикали

    for line in lines:
        txt_surface = font.render(line, True, color)
        text_rect = txt_surface.get_rect(center=(rect[0] + rect.width // 2, y))
        screen.blit(txt_surface, text_rect)
        y += font.size(line)[1]

button_new_game = Rect(400,200,360,110) #шаг 2 - создали объект с координатами и размерами кнопок
button_continue = Rect(400,350,360,110)
button_exit = Rect(400, 500, 360, 110)
button_back = Rect(620, 30, 105, 51)
button_up2 = Rect(350, 290, 48, 40)
button_up3 = Rect(350, 680, 48, 40)
button_down1 = Rect(350, 70, 48, 40)
button_down2 = Rect(350, 481, 48, 40)
button_wood_close = Rect(602, 75, 21, 20)
button_enter = Rect(640, 300, 100, 40)
button_next_frame = Rect(125, 145, 200, 30)
button_begin = Rect(125, 145, 100,100)
button_start_dialoge = Rect(145, 385, 170, 60)
button_back2 = Rect(620, 30, 105, 51)

answer_rect1 = Rect(80, 320, 500, 30)
answer_rect2 = Rect(75, 370, 485, 50)
answer_rect3 = Rect(75, 350, 450, 50)
answer_rect4 = Rect(83, 330, 50, 50)
answer_rect5 = Rect(83, 360, 130, 50)
answer_rect6 = Rect(83, 340, 260, 50)
answer_rect7 = Rect(83, 340, 260, 50)
answer_rect8 = Rect(73, 360, 500, 50)
answer_rect9 = Rect(90, 420, 300, 50)
answer_rect10 = Rect(75, 320, 285, 50)

image_main = image.load('pictures/castle.png') #загрузили изображение в переменную
image_play_menu = image.load('pictures/castle_holl.png')

bat_images = [
    image.load('pictures/bat_1.png'),
    image.load('pictures/bat_2.png'),
    image.load('pictures/bat_3.png'),
    image.load('pictures/bat_4.png')] #создали список с картинками

ghost_images = [
    image.load('pictures/ghost-1.png'),
    image.load('pictures/ghost-2.png'),
    image.load('pictures/ghost-3.png'),
    image.load('pictures/ghost-right.png'),
    image.load('pictures/ghost-left.png')
]

wizard_images = [
    image.load('pictures/wizard_1.png'),
    image.load('pictures/wizard_2.png')
]

bat_index = 0
last_bat_change = time() #засекли время установки картинки

wizard_index = 0
last_wizard_change = time()

ghost_index = 0
ghost_x = 40 #координата приведения
ghost_y = 375
ghost_speed = 0.6 #настроили скорость
moving_left = False #добавляем переменные отвечающие за перемещение
moving_right = False

input_active = False #создаем переменную, в которой будет сохраняться ведется ввод или нет
user_name = '' #переменная, хранящая имя пользователя
input_rect = Rect(100, 300, 140, 32)

task_answer = ''
right_task_answer = '123'
task_rect = Rect(545, 455, 140, 32)
task_input_active = False
task_done = False
error_message_active = False
message_active = False
task_done_right = False

name_entered = False
dialoge_active = False
question_active = False

hovered_answer1 = False
hovered_answer2 = False
hovered_answer3 = False
hovered_answer4 = False
hovered_answer5 = False
hovered_answer6 = False
hovered_answer7 = False
hovered_answer8 = False
hovered_answer9 = False
hovered_answer10 = False

answer1_selected = False
answer2_selected = False
answer3_selected = False
answer4_selected = False
answer5_selected = False
answer6_selected = False

question_index = 0
question_index2 = 0

alchemy_image = image.load('pictures/alchemy_menu.png')
field_image = image.load('pictures/field.png')

fire_image = image.load('pictures/fire.png')
water_image = image.load('pictures/water.png')
earth_image = image.load('pictures/earth.png')
air_image = image.load('pictures/air.png')
steam_image = image.load('pictures/steam.png')
lava_image = image.load('pictures/lava.png')
plant_image = image.load('pictures/plant.png')
wind_image = image.load('pictures/wind.png')
grass_image = image.load('pictures/grass.png')
frost_image = image.load('pictures/frost.png')
ice_image = image.load('pictures/ice.png')
coal_image = image.load('pictures/coal.png')

last_holl = image.load('pictures/last_holl.png')
last_dialoge_active = False
circles_drawn = True

fire_text = element_font.render('огонь', True, (0,0,0))
water_text = element_font.render('вода', True, (0,0,0))
earth_text = element_font.render('земля', True, (0,0,0))
air_text = element_font.render('воздух', True, (0,0,0))
steam_text = element_font.render('пар', True,(0,0,0))
lava_text = element_font.render('лава', True, (0,0,0))
plant_text = element_font.render('растение', True, (0,0,0))
wind_text = element_font.render('ветер', True, (0,0,0))
grass_text = element_font.render('трава', True, (0,0,0))
frost_text = element_font.render('мороз', True, (0,0,0))
ice_text = element_font.render('лед', True, (0,0,0))
coal_text = element_font.render('уголь', True, (0,0,0))

n = 0

elements = {
    'fire': {'image':fire_image, 'pos':(160, 185), 'text': fire_text, 'text_pos':(162, 220)},
    'water': {'image':water_image, 'pos':(230,185), 'text': water_text, 'text_pos':(236, 220)},
    'earth': {'image':earth_image, 'pos':(300,185), 'text': earth_text, 'text_pos':(302, 220)},
    'air': {'image':air_image, 'pos':(160, 235), 'text': air_text, 'text_pos':(160, 272)},
}

selected_elements = []
positions = [(230,235),(300,235),(160,285),(230,285),(300,285),(160,335),(230,335),(300,335)]

def draw_elements():
    for element in elements.values():
        screen.blit(element['image'], element['pos'])
        screen.blit(element['text'], element['text_pos'])

def new_element():
    global selected_elements
    global positions
    global right_answer

    if (selected_elements[0]=='fire' and selected_elements[1]=='water') or (selected_elements[0]=='water' and selected_elements[1]=='fire'):
        if 'steam' not in elements:
            elements['steam']= {'image': steam_image, 'pos': positions[0], 'text': steam_text, 'text_pos': (positions[0][0]+10, positions[0][1]+37)}
            positions = positions[1:]
            right_answer.play()
    elif (selected_elements[0]=='earth' and selected_elements[1]=='fire') or (selected_elements[0]=='fire' and selected_elements[1]=='earth'):
        if 'lava' not in elements:
            elements['lava']= {'image': lava_image, 'pos': positions[0], 'text': lava_text, 'text_pos': (positions[0][0]+6, positions[0][1]+37)}
            positions = positions[1:]
            right_answer.play()
    elif (selected_elements[0]=='earth' and selected_elements[1]=='water') or (selected_elements[0]=='water' and selected_elements[1]=='earth'):
        if 'plant' not in elements:
            elements['plant']= {'image': plant_image, 'pos': positions[0], 'text': plant_text, 'text_pos': (positions[0][0]-6, positions[0][1]+37)}
            positions = positions[1:]
            right_answer.play()
    elif selected_elements[0]=='air' and selected_elements[1]=='air':
        if 'wind' not in elements:
            elements['wind']= {'image': wind_image, 'pos': positions[0], 'text': wind_text, 'text_pos': (positions[0][0]+3, positions[0][1]+37)}
            positions = positions[1:]
            right_answer.play()
    elif (selected_elements[0]=='plant' and selected_elements[1]=='earth') or (selected_elements[1]=='plant' and selected_elements[0]=='earth'):
        if 'grass' not in elements:
            elements['grass']={'image':grass_image, 'pos': positions[0], 'text': grass_text, 'text_pos': (positions[0][0]+2, positions[0][1]+37)}
            positions = positions[1:]
            right_answer.play()
    elif (selected_elements[0]=='wind' and selected_elements[1]=='air') or (selected_elements[0]=='air'and selected_elements[1]=='wind'):
        if 'frost' not in elements:
            elements['frost']={'image': frost_image, 'pos': positions[0], 'text': frost_text, 'text_pos': (positions[0][0]+2,positions[0][1]+37)}
            positions = positions[1:]
            right_answer.play()
    elif (selected_elements[0]=='frost'and selected_elements[1]=='water') or (selected_elements[1]=='frost'and selected_elements[0]=='water'):
        if 'ice' not in elements:
            elements['ice']={'image': ice_image, 'pos': positions[0], 'text': ice_text, 'text_pos': (positions[0][0]+10, positions[0][1]+37)}
            positions = positions[1:]
            right_answer.play()
    elif (selected_elements[0]=='plant' and selected_elements[1]=='fire') or (selected_elements[1]=='plant' and selected_elements[0]=='fire'):
        if 'coal' not in elements:
            elements['coal']={'image': coal_image, 'pos': positions[0], 'text': coal_text, 'text_pos': (positions[0][0]+2, positions[0][1]+37)}
            positions=positions[1:]
            right_answer.play()
    else:
        print('no element')
        wrong_answer.play()
    selected_elements = []

running = True #переменная running будет использоваться для контроля основного цикла программы
current_screen = 'main_menu' #создали переменную, которая будет хранить текущий экран
last_screen = 'play_menu'

while running == True: #начало основного цикла программа

    for e in event.get(): #строчка перебирает все события, произошедшие с последнего обновления экрана
        if e.type == QUIT: #проверяем тип события, если событие равно QUIT, то значит пользователь закрыл приложение
            running = False #это приведет к окончанию цикла while, программа завершит свою работу
        elif e.type == MOUSEBUTTONDOWN and e.button == 1: #проверка является ли событие нажатием мыши (1-левой)
            if current_screen == 'main_menu':
                if button_new_game.collidepoint(e.pos): #проверка находится ли мышь в области кнопки "новая игра"
                    current_screen = 'game_menu'
                elif button_continue.collidepoint(e.pos):
                    current_screen = last_screen
                elif button_exit.collidepoint(e.pos):
                    running = False


            if current_screen == 'game_menu':
                if button_back.collidepoint(e.pos):
                    current_screen = 'main_menu'
                elif button_up2.collidepoint(e.pos) and not task_done_right:
                    ghost_y = 175
                elif button_up2.collidepoint(e.pos) and task_done_right:
                    question_active = True
                elif button_down2.collidepoint(e.pos):
                    ghost_y = 580
                elif button_up3.collidepoint(e.pos):
                    ghost_y = 375
                elif button_down1.collidepoint(e.pos):
                    ghost_y = 375
                elif answer_rect2.collidepoint(e.pos) and not answer1_selected and not answer2_selected and not answer3_selected and not answer4_selected and not answer5_selected and not answer6_selected:
                    dialoge_active = False
                    ghost_x = 515
                    answer1_selected = True
                elif answer_rect1.collidepoint(e.pos) and not answer1_selected and not answer2_selected and not answer3_selected and not answer4_selected and not answer5_selected and not answer6_selected:
                    question_index = 2
                    answer1_selected = True
                elif answer_rect3.collidepoint(e.pos) and not answer2_selected and answer1_selected and not answer3_selected and not answer4_selected and not answer5_selected and not answer6_selected:
                    question_index = 3
                    print(0)
                    answer2_selected = True
                elif answer_rect4.collidepoint(e.pos) and not answer3_selected:
                    answer3_selected = True
                    question_index = 4
                elif answer_rect5.collidepoint(e.pos) and not answer3_selected:
                    ghost_x = 515
                    dialoge_active = False
                elif answer_rect6.collidepoint(e.pos) and not answer4_selected:
                    answer4_selected = True
                    ghost_x= 515
                    dialoge_active = False
                    task_done_right = True
                elif button_wood_close.collidepoint(e.pos):
                    message_active = False
                elif answer_rect7.collidepoint(e.pos) and not answer5_selected:
                    answer5_selected = True
                    question_index = 6
                elif answer_rect8.collidepoint(e.pos) and not answer6_selected:
                    ghost_x = 515
                    dialoge_active = False
                elif answer_rect9.collidepoint(e.pos) and not answer6_selected:
                    ghost_x = 515
                    dialoge_active = False
                    answer6_selected = True
                elif button_enter.collidepoint(e.pos):
                    current_screen = 'alchemy_menu'
                    last_screen = 'alchemy_menu'
                elif input_rect.collidepoint(e.pos): #если нажато поле вводы, изменяем значение переменной
                    input_active = True
                else:
                    input_active = False
                if task_rect.collidepoint(e.pos):
                    task_input_active = True
                else:
                    task_input_active = False

            if current_screen == 'alchemy_menu':
                for element_name, element in elements.items():  #в переменной element_name сохраняется ключ, а в element значения
                    if e.pos[0] >= element['pos'][0] and e.pos[0] <= element['pos'][0] + 40 and e.pos[1] >= element['pos'][1] and e.pos[1] <= element['pos'][1] + 40:
                        print(f"Элемент: {element_name}")
                        selected_elements.append(element_name)
                    if button_next_frame.collidepoint(e.pos):
                        current_screen = 'last_menu'
                        last_screen = 'last_menu'
                    elif button_back2.collidepoint(e.pos):
                        current_screen = 'main_menu'

            if current_screen == 'last_menu':
                if button_begin.collidepoint(e.pos):
                    current_screen = 'main_menu'
                elif button_start_dialoge.collidepoint(e.pos):
                    last_dialoge_active = True
                elif answer_rect10.collidepoint(e.pos):
                    circles_drawn = False


        elif e.type == KEYDOWN: #если нажата кнопка на клавиатуре
            if input_active:
                if e.key == K_RETURN: #если нажата клавиша enter
                    name_entered = True
                    input_active = False
                    question_index += 1
                elif e.key == K_BACKSPACE:
                    user_name = user_name[:-1] #удаляем последний символ
                else:
                    user_name += e.unicode #добавляем к имени символ
            elif task_input_active:
                if e.key == K_RETURN:
                    task_input_active = False
                    task_done = True
                    message_active = True
                elif e.key == K_BACKSPACE:
                    task_answer = task_answer[:-1]
                else:
                    task_answer += e.unicode
            if e.key == K_RIGHT: #есл нажата правая кнопка
                moving_right = True #начинается пермещение вправо
                ghost_index = 3 #смена картинки
            elif e.key == K_LEFT: #если нажата левая клавиша
                moving_left = True #начинается перемещение влево
                ghost_index = 4 #смена картинки
        elif e.type == KEYUP: #если клавиша больше не нажата
            if e.key == K_RIGHT: #если больше не нажата правая клавиша
                moving_right = False #перемещение заканчивается
                ghost_index = 0 #возвращается картинка
            elif e.key == K_LEFT:
                moving_left = False
                ghost_index = 0
        elif e.type == MOUSEMOTION:
            if current_screen == 'game_menu':
                if answer_rect1.collidepoint(e.pos):
                    hovered_answer1 = True
                else:
                    hovered_answer1 = False
                if answer_rect2.collidepoint(e.pos):
                    hovered_answer2 = True
                else:
                    hovered_answer2 = False
                if answer_rect3.collidepoint(e.pos):
                    hovered_answer3 = True
                else:
                    hovered_answer3 = False
                if answer_rect4.collidepoint(e.pos):
                    hovered_answer4 = True
                else:
                    hovered_answer4 = False
                if answer_rect5.collidepoint(e.pos):
                    hovered_answer5 = True
                else:
                    hovered_answer5 = False
                if answer_rect6.collidepoint(e.pos):
                    hovered_answer6 = True
                else:
                    hovered_answer6 = False
                if answer_rect7.collidepoint(e.pos):
                    hovered_answer7 = True
                else:
                    hovered_answer7 = False
                if answer_rect8.collidepoint(e.pos):
                    hovered_answer8 = True
                else:
                    hovered_answer8 = False
                if answer_rect9.collidepoint(e.pos):
                    hovered_answer9 = True
                else:
                    hovered_answer9 = False
            elif current_screen == 'last_menu':
                if answer_rect10.collidepoint(e.pos):
                    hovered_answer10 = True
                else:
                    hovered_answer10 = False

    screen.fill((255,255,180)) #заполняем экран светло-желтым цветом

    if time()-last_bat_change>=0.3: #проверяем сколько прошло с последнего обновления картинки
        bat_index = (bat_index + 1) % len(bat_images) #обновляем индекс
        last_bat_change = time() #снова засекаем время

    if time()-last_wizard_change>=0.7:
        wizard_index = (wizard_index + 1) % len(wizard_images)
        last_wizard_change = time()

    if current_screen == 'main_menu':

        screen.blit(image_main, (0,0)) #разместили изображение

        screen.blit(bat_images[bat_index],(550,100))

        draw_button(screen, 'начать новую игру', button_new_game, font_main, brown,brown,5,'pictures/main_buttons.png') #шаг 3 - вызвали функцию для отрисовки кнопки
        draw_button(screen, 'продолжить игру', button_continue, font_main, brown,brown,5,'pictures/main_buttons.png')
        draw_button(screen, 'выйти из игры', button_exit, font_main, brown,brown,5,'pictures/main_buttons.png')

    elif current_screen == 'game_menu':

        screen.blit(image_play_menu,(0,0))

        if moving_right: #если пермещение вправо
            ghost_x += ghost_speed #прибавляем к координате скорость
            ghost_x = min(screen.get_width()-ghost_images[ghost_index].get_width(),ghost_x) #настраиваем максимальное значение х
        elif moving_left:
            ghost_x -= ghost_speed
            ghost_x = max(0,ghost_x) #настраиваем минимальное значение х

        screen.blit(ghost_images[ghost_index],(ghost_x,ghost_y))

        if  300 <= ghost_x <= 400 and ghost_y == 375:
            draw_button(screen, '', button_up2, font_main,brown,brown,5, 'pictures/up_btn.png')
            draw_button(screen, '', button_down2, font_main,brown,brown,5, 'pictures/down_btn.png')
        elif 300 <= ghost_x <= 400 and ghost_y == 580:
            draw_button(screen, '', button_up3,font_main, brown, brown,5, 'pictures/up_btn.png')
        elif 300 <= ghost_x <= 400 and ghost_y == 175:
            draw_button(screen, '', button_down1,font_main, brown, brown,5, 'pictures/down_btn.png')

        screen.blit(wizard_images[wizard_index], (570,565))

        questions = [
            "Привет! Меня зовут Волшебник. А как зовут тебя?",
            f'Приятно познакомиться, {user_name}, что тебе нужно?',
            'Тебе же нужно разузнать об этом замке не просто так. Так зачем тебе это?',
            'О, я могу тебе в этом помочь. Только ты должен взамен оказать мне услугу. Ты готов?',
            'Тогда ты должен принести мне книгу с третьего этажа',
            'Снова здравствуй, ты принес книгу?',
            'Хорошо. Тогда, чтобы выбраться из замка тебе нужно сделать зелье в одной из комнат. Дам тебе небольшую подсказку - она находится на втором этаже.',
            'Ну что ты принес зелье?'
        ]

        if 516 <= ghost_x <= 620 and ghost_y == 580:
            dialoge_active = True
            answer1_selected = False
            answer3_selected = False

        if dialoge_active:
            draw.rect(screen, light_brown, (75, 200, 600, 300))
            question_surface = font_question.render(questions[question_index], True, blue)
            max_text_width = 550 #настраиваем максимальную ширину текста
            if question_surface.get_width()>max_text_width: #если текст выходит за пределеы максимальной ширины
                words = questions[question_index].split(' ') #разбиваем вопрос на слова
                lines = [] #создаем список с строками
                current_line = '' #создаем переменную, где будет храниться текущаю строка

                for word in words:
                    test_line = current_line + ' ' + word if current_line != word else word
                    test_surface = font_question.render(test_line, True, blue) #создаем переменную, где будет сохраняться предварительная строка

                    if test_surface.get_width() <= max_text_width: #если ширина не больше максимальной
                        current_line = test_line
                    else:
                        lines.append(current_line) #сохраняем строку без последнего слова
                        current_line = word #в новую строку добавляем последнее слово
                lines.append(current_line)

                y = 220
                for line in lines:
                    question_surface = font_question.render(line, True, blue) #настраиваем каждую строку
                    screen.blit(question_surface, (90, y))
                    y += question_surface.get_height() + 5 #увеличиваем у с учетом отступов
            else:
                screen.blit(question_surface,(100,210))
            input_max_width = 550

            if question_index == 0:
                text_surface = font_question.render(user_name, True, brown)
                text_width = text_surface.get_width()

                if text_width > input_max_width:
                    lines = []
                    current_line = ''

                    for letter in user_name:
                        test_line = current_line + letter
                        test_surface = font_question.render(test_line, True, brown)

                        if test_surface.get_width() <= input_max_width:
                            current_line = test_line
                        else:
                            lines.append(current_line)
                            current_line = letter
                    lines.append(current_line)

                    y = input_rect.y
                    for line in lines:
                        text_surface = font_question.render(line, True, brown)
                        screen.blit(text_surface, (input_rect.x+3, y))
                        y += text_surface.get_height()+5
                    input_rect.height = len(lines)*(text_surface.get_height()+5) + 2
                else:
                    screen.blit(text_surface,(input_rect.x+3, input_rect.y))
                    input_rect.height = text_surface.get_height() + 2
                    input_rect.w = max(20, text_surface.get_width()+5) #настраиваем изменение прямоугольника в зависимости от ширины текста

                draw.rect(screen, brown, input_rect, 2)

        if name_entered and dialoge_active:
            question_surface = font_question.render(questions[question_index], True, blue)
            if question_index == 1 and not answer1_selected:
                answer_color1 = red if hovered_answer1 else blue
                answer_color2 = red if hovered_answer2 else blue
                draw_button(screen, '1.Я хочу узнать больше об этом замке', answer_rect1,font_question, answer_color1, light_brown,0)
                draw_button(screen, '2.Я просто прогуливаюсь(закончить диалог)', answer_rect2, font_question, answer_color2, light_brown,0)

            elif question_index == 2 and not answer2_selected:
                answer1_selected = True
                answer_color3 = red if hovered_answer3 else blue
                draw_button(screen, '1.Ты прав. Мне нужно узнать как выбраться из этого замка.',answer_rect3, font_question, answer_color3, light_brown, 0)

            elif question_index == 3 and not answer3_selected:
                answer_color4 = red if hovered_answer4 else blue
                answer_color5 = red if hovered_answer5 else blue
                draw_button(screen, '1.Да', answer_rect4, font_question, answer_color4, light_brown,0)
                draw_button(screen, '2.Нет(уйти)', answer_rect5, font_question, answer_color5, light_brown, 0)

            elif question_index == 4 and not answer4_selected:
                answer_color6 = red if hovered_answer6 else blue
                draw_button(screen, '1.Хорошо, принесу', answer_rect6, font_question, answer_color6, light_brown, 1)

            elif question_index == 5 and not answer5_selected:
                answer_color7 = red if hovered_answer7 else blue
                draw_button(screen, '1.Да(отдать книгу)',answer_rect7, font_question,answer_color7, light_brown, 1)

            elif question_index == 6 and not answer6_selected:
                answer_color8 = red if hovered_answer8 else blue
                answer_color9 = red if hovered_answer9 else blue
                draw_button(screen,'1. Я не уверен, что с этим справлюсь.', answer_rect8, font_question, answer_color8, light_brown, 1)
                draw_button(screen, '2. Хорошо, я попытаюсь', answer_rect9, font_question, answer_color9, light_brown, 1)

        if task_done_right:
            screen.blit(image.load('pictures/lock.png'),(320, 175))

        if question_active:
            draw.rect(screen, white, (125, 190, 500, 350))
            screen.blit(image.load('pictures/task.png'), (152, 225))
            text_surface = font_question.render(task_answer, True, (0,0,0))
            screen.blit(text_surface, (task_rect.x + 3, task_rect.y + 3))
            task_rect.w = max(20, text_surface.get_width() + 3)
            draw.rect(screen, (0,0,0), task_rect, 2)
            question_surface = task_font.render('Чтобы попасть на третий этаж - выполни задание', True, (0,0,0))
            screen.blit(question_surface,(130, 195))

        #тест на третьем этаже 1й локации
        if task_done:

            if task_answer == right_task_answer and message_active:
                question_active = False
                draw.rect(screen, light_brown, (125, 75, 500, 100))
                text_surface = font_question.render('Верно! Получен новый объект - книга', True, brown)
                screen.blit(text_surface, (130, 80))
                task_input_active = False
                error_message_active = False
                task_done_right = False
                answer4_selected = True
                question_index = 5
                draw_button(screen, '', button_wood_close, font_question, brown, brown, 5, 'pictures/wood_button.png')

            elif task_answer != right_task_answer:
                task_input_active = True
                error_message_active = True
                task_answer = ''
                task_done = False  #сбрасываем переменную до начального состояния для закрытия окна и возможности ввода

        if error_message_active:
            draw.rect(screen, light_brown, (125,75,500,100))
            text_surface = font_question.render('Неверный ответ. Попробуй снова!', True, brown)
            screen.blit(text_surface,(130,80))

        if  620 <= ghost_x <= 730 and answer6_selected:
            draw_button(screen, 'войти', button_enter, font_question, brown, light_brown, 0)

        draw_button(screen, 'назад',button_back, font_main,white,brown,0,'pictures/back_btn.png')


    elif current_screen == 'alchemy_menu':
        screen.blit(alchemy_image,(0,0))
        screen.blit(field_image, (245, 600))
        draw_elements()
        if len(selected_elements)==1 or len(selected_elements)==2:
            element_image = elements[selected_elements[0]]['image']
            screen.blit(element_image, (265, 650))
        if len(selected_elements)==2:
            element_image = elements[selected_elements[1]]['image']
            screen.blit(element_image, (435, 650))
            current_time = time()
            new_element()
        if 'coal' in elements and 'ice' in elements and 'grass' in elements and 'lava' in elements:
            draw.rect(screen, light_brown,(125,75,500,100))
            text_surface = font_question.render('Молодец! Ты собрал все нужные элементы!', True, brown)
            screen.blit(text_surface, (130, 80))
            draw_button(screen,'Дальше',button_next_frame, font_question,brown, light_brown, 2)
        draw_button(screen,'назад',button_back2,font_main,brown,light_brown,0,'pictures/back_btn.png')

    elif current_screen == 'last_menu':
        screen.blit(last_holl,(0,0))
        screen.blit(wizard_images[wizard_index], (140, 435))
        screen.blit(ghost_images[ghost_index],(180, 465))
        if not last_dialoge_active:
            draw_button(screen,'Начать диалог',button_start_dialoge,font_question,brown,light_brown, 0)
        elif last_dialoge_active:
            draw.rect(screen, light_brown, (75, 200, 600, 300))
            question_surface = font_question.render('И снова здравствуй. Ну что ты принес зелье?', True, blue)
            screen.blit(question_surface, (80, 210))
            answer_color10 = red if hovered_answer10 else blue
            draw_button(screen, 'Да (отдать зелье)', answer_rect10, font_question,answer_color10, light_brown, 2)
        if not circles_drawn:
            for temp in range(80):
                random_center1 = randint(10, 680)
                random_center2 = randint(10, 680)
                random_rad = randint(30, 100)
                colors = [(255, 192, 203),(255, 255, 224),(144, 238, 144),(153, 196, 210),(180, 180, 250),(128, 0, 128),(255, 10, 0),(0, 100, 255)]
                random_color = choice(colors)
                draw.circle(screen,random_color,(random_center1,random_center2),random_rad)
                n+=1
                if n >= 1500:
                    current_screen = 'main_menu'
                    circles_drawn = True
                sleep(0.001)

    display.flip() #обновляем экран, метод flip отображает произведенные изменения на экране


quit() #завершает работу всех модулей pygame, которые были инициализированы