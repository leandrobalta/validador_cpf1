while True:
    print('Olá, sou um validador de cpf.')
    cpf = input('Digite seu cpf: ')
    lista_cpf = []
    tamanho = len(cpf)
    for digitos in cpf:
        if not tamanho == 11:
            print('Cpf inválido.')
            break

        elif not cpf.isnumeric():
            print('Cpf inválido.')
            break

        else:
            lista_cpf.extend(cpf)
            m1 = (int(lista_cpf[0]) * 10)
            m2 = (int(lista_cpf[1]) * 9)
            m3 = (int(lista_cpf[2]) * 8)
            m4 = (int(lista_cpf[3]) * 7)
            m5 = (int(lista_cpf[4]) * 6)
            m6 = (int(lista_cpf[5]) * 5)
            m7 = (int(lista_cpf[6]) * 4)
            m8 = (int(lista_cpf[7]) * 3)
            m9 = (int(lista_cpf[8]) * 2)
            all = (m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9)
            d1 = 11 - (all % 11)
            if 11 >= d1 > 9:
                d1 = 0
                if d1 == lista_cpf[9]:
                    pass
                else:
                    print('Cpf inválido.')
                    print()
                    break

            else:
                d1 = d1
                if str(d1) == lista_cpf[9]:
                    pass
                else:
                    print('Cpf inválido.')
                    print()
                    break

            m_0 = (int(lista_cpf[0]) * 11)
            m_1 = (int(lista_cpf[1]) * 10)
            m_2 = (int(lista_cpf[2]) * 9)
            m_3 = (int(lista_cpf[3]) * 8)
            m_4 = (int(lista_cpf[4]) * 7)
            m_5 = (int(lista_cpf[5]) * 6)
            m_6 = (int(lista_cpf[6]) * 5)
            m_7 = (int(lista_cpf[7]) * 4)
            m_8 = (int(lista_cpf[8]) * 3)
            m_9 = (int(lista_cpf[9]) * 2)
            all_2 = (m_0 + m_1 + m_2 + m_3 + m_4 + m_5 + m_6 + m_7 + m_8 + m_9)
            d2 = 11 - (all_2 % 11)
            if 11 >= d2 > 9:
                d2 = 0
                if d2 == lista_cpf[10]:
                    print('Cpf válido!')
                    break
                else:
                    print('Cpf inválido.')
                    print()
                    break
            else:
                d2 = d2
                if str(d2) == lista_cpf[10]:
                    print('Cpf válido!')
                    print()
                    break

                else:
                    print('Cpf inválido.')
                    print()
                    break
