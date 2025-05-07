"""
Usando calendar para calendários e datas
calendar é usado para coisas genéricas de
calendários e datas.
-Qual o ultímo dia do mês (ex.: monthrange)
-Qual o nome e números do dia de determinada data
(ex.: weekday)
-Criar um calendário em si (ex.: monthcalendar)
-Trabalhar com coisas específicas de calendário
(ex.: calendar, month)
Por padrão dia da semana começa em 0 até 6
0 = segunda-feira | 6 = domingo
"""

import calendar

# print(calendar.calendar(2022)) #->calendário do ano
# print(calendar.month(2025, 5)) #-> dias do mes do ano
# print(calendar.monthrange(2025, 5))  # -> ultimo dia do mes de um ano
# print(list(calendar.day_name))  # -> dias da semana
# print(list(enumerate(calendar.day_name)))

# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2025, 5)
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2025, 5)
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.weekday(2025, 5, ultimo_dia))
# print(calendar.day_name[calendar.weekday(2025, 5, ultimo_dia)])

# print(calendar.monthcalendar(2025, 5))

for week in calendar.monthcalendar(2025, 5):
    # print(list(enumerate(week)))
    for day in week:
        if day == 0:
            continue
        print(day)
