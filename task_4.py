""" Pеализовать функцию bank, которая приннимает следующие аргументы:
сумма депозита, кол-во лет, и процент.
Результатом выполнения должна быть сумма по истечению депозита """

def bank(depos_sum, years, procent:float):
    result = 0
    while years > 0:
        result = depos_sum + (depos_sum*procent)
        years -= 1
    return result

what_u_get_after = bank(2000, 3, 0.2)
print(what_u_get_after)