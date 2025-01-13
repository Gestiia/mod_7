team1_num = 10
team2_num = 4

score_1 = 22
score_2 = 15

team1_time = 31.12
team2_time = 25.54

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print("В команде Мастера кода участников: %s ! " % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

print("Колличесво задач решенных командой: {} !".format(score_1))
print("Команда Волшебники данных решила задач: {} !".format(score_2))

print("Время за которое команда 2 решила задачи: {} с !".format(team1_time))
print("Волшебники данных решили задачи за: {} с !".format(team2_time))

print(f'Команды решили {team1_num} и {team2_num} задач.')

print(f'Результат битвы: {challenge_result}')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total  
print(f'Сегодня было решено {tasks_total} задач,',
      f'в среднем по {time_avg:.1f} секунды на задачу!')