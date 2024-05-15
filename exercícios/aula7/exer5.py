data = str(input("Digite uma data no formato (dd/mm/aaaa): "))

dia = data[:2]
mes = data[3:5]
ano = data[6:10]

if mes == '01':
    mes = "Janeiro"
if mes == '02':
    mes = "Fevereiro"
if mes == '03':
    mes = "Março"
if mes == '04':
    mes = "Abril"
if mes == '05':
    mes = "Maio"
if mes == '06':
    mes = "Junho"
if mes == '07':
    mes = "Julho"
if mes == '08':
    mes = "Agosto"
if mes == '09':
    mes = "Setembro"
if mes == '10':
    mes = "Outubro"
if mes == '11':
    mes = "Novembro"
if mes == '12':
    mes = "Dezembro"

print(dia, "de", mes, "de", ano)