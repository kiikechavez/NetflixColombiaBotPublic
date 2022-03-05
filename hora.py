from datetime import datetime, date, time, timedelta
import calendar

c = calendar.LocaleTextCalendar(locale='es_CO')
#h = datetime._local_timezone(self=)
año = int(input("Escriba el año (4 dígitos): "))
mes = int(input("Escriba el mes (del 1 al 12): "))
ahora = datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora:", ahora)  # Muestra fecha y hora
print(datetime.today().strftime('%A'))
print(calendar.month(año,mes))

# print("Día:",ahora.day)  # Muestra día
# print("Mes:",ahora.month)  # Muestra mes
# print("Año:",ahora.year)  # Muestra año
# print("Hora:", ahora.hour)  # Muestra hora
# print("Minutos:",ahora.minute)  # Muestra minuto
# print("Segundos:", ahora.second)  # Muestra segundo
#print("Microsegundos:",ahora.microsecond)  # Muestra microsegundo