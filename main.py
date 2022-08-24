from random import *
word_list = ['мазда', 'пушка', 'гонка', 'сорняки',
             'полынь', 'стихотворение', 'микроволновка',
             'забулдыжничество', 'узкоспециальный',
             'поздравление', 'одиннадцатиклассница']
d = 'абвгдежзийклмнопрстуфхцчшщъьыэюя'
def get_word():
    return(choice(word_list))
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def alphaa(l):
    count = 0
    for i in l:
        if i not in d:
            count += 1
    return count == 0
print('Добро пожаловать в угадайку слов. У тебя будет 6 попыток'
      ', чтобы отгадать слово, которое я загадал')
def play(word):
    word_completion = list('_' * len(word)) # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 7  # количество попыток
    print('твоё слово - ',  *word_completion)
    while True:
        alpha = input('Введи букву или слово целиком ').lower()
        while alpha in guessed_words or alpha in guessed_letters:
            print('Эту букву/слово ты уже вводил')
            alpha = input('Введи букву или слово целиком ').lower()
        while alphaa(alpha) == False:
            print('Ты ввел неверно. Надо ввести маленькую букву без пробелов или слово целиком')
            alpha = input('Введи букву или слово целиком ')

        if alpha == word:
            print('Ты угадал, поздравляю. Но ты расстроил толпу:(')
            break
        if alpha in word:
            for i in range(len(word)):
                if word[i] == alpha:
                    word_completion[i]=alpha
            print(*word_completion)
        if word_completion == list(word):
            print('Вы угадали! И расстроили толпу')
            break
        if alpha not in word:
            print('Неверно, толпа уже собирается на площади')
            tries -= 1
            print(display_hangman(tries))
            print('У тебя осталось', tries, 'попыток')
            guessed_letters.append(alpha)
        if tries == 0:
            print('Ты проиграл, толпа ликует')
            print('Твоё слово было - ', word)
            break
        if len(alpha) > 1 and alpha != word:
            guessed_words.append(alpha)
            print('Неверное слово, попробуй снова')
            tries -= 1
            print(display_hangman(tries))


start = input('Начнем игру? Введи на клавиатуре д - если хочешь играть '
              'или н - чтобы выйти из игры ')
while start == 'д':
    play(get_word())
    start = input('Повторим игру? Введи на клавиатуре д - если хочешь играть '
              'или н - чтобы выйти из игры ')

q = input('Для выхода нажмите enter')




