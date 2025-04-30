"""
Criando datas com módulos datetime
datetime (ano, mês, dia)
datatime (ano, mês, dia, horas, minutos, segundos)
datetime.striptime('DATA', 'FORMATO')
datatime.now()
Instalando o pytz
pip instal pytz types-pytz
"""

from datetime import datetime


data_str_data = "2022/04/20 07:49:23"
data_str_data_brazil = "20/04/2022"
data_str_formato = "%Y/%m/%d %H:%M:%S"
data_str_formato_brazil = "%d/%m/%Y"

data = datetime.strptime(data_str_data, data_str_formato)
data_brazil = datetime.strptime(data_str_data_brazil, data_str_formato_brazil)


print(data)
print(data_brazil)
