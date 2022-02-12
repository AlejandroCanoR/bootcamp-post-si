from instrucciones import i_decodificado 
from etiquetas_regist import reg_decode

def apertura_en_lect(fileName): #Funcion que abre u archivo en modo lectura, divide una linea y despues cierra el archivo.
    archivo_op = open(fileName, "r")
    linea = archivo_op.read().split("\n")
    archivo_op.close()
    return linea

def conv_bin(ins_base): # Funcion principal de conversion de instrucciones a codigo maquina.
    # En este apartado se reemplazan ciertos espacios y caracteres por lo necesario segun la instruccion.
    ins_base = ins_base.replace(" ", "")
    ins_base = ins_base.replace(",", " ")
    ins_base = ins_base.replace("  ", " ")
    ins_base = ins_base.replace("	", "")
    ins_base = ins_base.replace(":", " ")

    # Division de argumentos cada espacio
    arr = ins_base.split(" ")

    # La instruccion se guarda en el espacio 0 del arreglo
    ins_ward = arr[0]
   
    # Se incluyen las instrucciones desde i_decodificado y se asignan a inst_arregladas, se asigna el opcode, el tipo de funcion
    # y los valores de cada registro
    inst_arregladas = i_decodificado(ins_ward)
    tipo = inst_arregladas[0]
    REGIST_v = reg_decode(tipo, ins_ward, arr[1:])
    
    # Si no se reconocen valores en los registros envía un error.
    if REGIST_v == None:
        print("ERROR DE LECTURA")
        return
    
    # FUNCIONES TIPO R
    if tipo == "r":            
        op = '{0:04b}'.format(inst_arregladas[1])
        rsource_RS = '{0:03b}'.format(REGIST_v[0])
        rsource2_RT = '{0:03b}'.format(REGIST_v[1])
        rdestiny_RD = '{0:03b}'.format(REGIST_v[2])
        Rell = '{0:05b}'.format(REGIST_v[3])

        # IMPRIME BINARIO DE INS R
        b_101 = op+rsource_RS+rsource2_RT+rdestiny_RD+Rell
        print(b_101)
    
    # FUNCIONES TIPO I (BRANCH)
    elif tipo == "b":
        op = '{0:04b}'.format(inst_arregladas[1])
        rsource_RS = '{0:03b}'.format(REGIST_v[0])
        rsource2_RT = '{0:03b}'.format(REGIST_v[1])
        label = '{0:08b}'.format(REGIST_v[2])

        # IMPRIME BINARIO DE INS BRANCH
        b_101 = op+rsource_RS+rsource2_RT+label
        print(b_101)

    # FUNCIONES TIPO I
    elif tipo == "i":
        op = '{0:04b}'.format(inst_arregladas[1])
        rsource_RS = '{0:03b}'.format(REGIST_v[0])
        rsource2_RT = '{0:03b}'.format(REGIST_v[1])
        if REGIST_v[2] < 0:
            immediate = (bin(((1 << 8) -1) & REGIST_v[2])[2:]).zfill(8)
        else:
            immediate = '{0:08b}'.format(REGIST_v[2])
        
        # IMPRIME BINARIO DE INS I
        b_101 = op+rsource_RS+rsource2_RT+immediate
        print(b_101)
    
    # FUNCIONES TIPO J  
    elif tipo == "j":
        op = '{0:04b}'.format(inst_arregladas[1])
        immediate = '{0:014b}'.format(REGIST_v[0])

        # IMPRIME BINARIO DE INS J
        b_101 = op+immediate
        print(b_101) 
    else:
        return 
    return
