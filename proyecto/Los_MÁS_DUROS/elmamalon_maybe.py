#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Converts MIPS instructions into binary and hex
#import os
import sys
from project_conv_func import apertura_en_lect, conv_bin
#from project64 import apertura_en_lect, conv_bin

#Arreglo para etiquetado
arr_etiq_temp = [] 
#Arreglo de linea de etiqueta
arr_etiqueta = []
arr_etiq_val = []
etiqueta_x = {}

def main():

    print("\n")
    print("                         PROYECTO FINAL \n")
    arch_textus = input(" Por favor, ingrese el nombre de su archivo de instrucciones (ej: codigo1.txt): ")
    print(" Archivo generado en /Los_MÁS_DUROS/binarios.txt \n")
    textus_assign = apertura_en_lect(arch_textus)

    # Ciclo de busqueda de etiquetado, separando caracteres encontrados en las líneas
    # y almacenando los valores correspondientes 
    for j in range(len(textus_assign)):
        if(":" in textus_assign[j]):
            arr_etiq_val.append(j+1)
            arr_etiq_temp.extend(textus_assign[j].split(":"))
            arr_etiqueta.append(arr_etiq_temp[j])
            del arr_etiq_temp[j]
        else:
            arr_etiq_temp.extend(textus_assign[j].split(":"))

    for j in range (len(arr_etiqueta)):
        etiqueta_x[arr_etiqueta[j]] = arr_etiq_val[j]
    
    # Crea el archivo de instrucciones en binario, lo escribe y lo cierra
    cons_origen = sys.stdout 
    name_bin = 'binarios.txt'
    sys.stdout = open(name_bin, "w")
    for x in range(len(arr_etiq_temp)-1):
        textus_assign[x] = conv_bin(arr_etiq_temp[x])
    sys.stdout.close()
    sys.stdout = cons_origen

if __name__=="__main__":
    main()
