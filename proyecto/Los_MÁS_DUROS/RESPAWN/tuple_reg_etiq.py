#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#REGISTROS POR INSTRUCCIÓN, REFERENTES AL PRIMER REGISTRO FUENTE, SEGUNDO REGISTRO FUENTE Y REGISTRO DESTINO.
reg_princ = {
    "x0" : 0,
    "x1" : 1,
    "x2" : 2,
    "x3" : 3,
    "x4" : 4,
    "x5" : 5,
    "x6" : 6,
    "x7" : 7
}

#ETIQUETAS EN RELACIÓN Y ORDEN A LOS CÓDIGOS DADOS
etiquetas = {
    "MAIN" : 1,
    "INC" : 4,
    "DEC" : 9,
    "FUNC" : 8,
    "EXIT" : 15
}