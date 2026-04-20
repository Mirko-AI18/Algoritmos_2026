# print ("Primer Guia Practica" ) 


# print ("Ejercicio 1" ) 

# #  5 + 4 + 3 + 2 + 1 + 0 = 15
# # sum(n) = n + sum(n-1)          ->   sum(0) = 0

# def suma(num: int) -> int:
#     if num == 0:
#         return num
#     else:
#         return num + suma(num-1)
    
# # print(suma(5))



# # 2 * 3 = 2 + 2 + 2 = 6
# # prod(n, m) = n + prod(n, m-1)    -> n, m = 0 -> 0


# def serie_h(num: int) -> float:
#     if num == 1:
#         return num
#     else:
#         return 1/num + serie_h(num-1)

# print(serie_h(4))



# print ("Ejercicio 8 " ) 

# Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
# ma binario.

# def dec_bi(num: int) -> str:
#     if num == 0:
#         return num
#     elif num == 1:
#         return "1"
#     else:
#         return dec_bi(num // 2) + str(num % 2)
    
# print(dec_bi(10))



# print ("Ejercicio 10 " ) 

# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

# def cant_dig(num: int) -> int:
#     if num < 10:
#         return 1
#     else:
#         return 1 + cant_dig(num // 10)      
    
# print(cant_dig(6300))

# print ("Ejercicio 11 " )    

# Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

# def inv_num(num: int)  -> int:
#     if num < 10:
#         return num
#     else:
#         return (num % 10) * (10 ** (cant_dig(num) - 1)) + inv_num(num // 10)    
    
# print(inv_num(1234))