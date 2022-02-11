#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#import sys
#sys.path.append("/tuple_reg_etiq")
import tuple_reg_etiq as t

def reg_decode(tipo, instruc, reggie):
    
    #INSTRUCCIONES TIPO R
    if tipo == "r":   
        
        # SLL INSTRUCTION
        if (instruc == "sll"): 
            #REGRESA REGISTROS RT, RD Y FILL
            #PUEDE SER TANTO SHIFT LEFT LOGIC COMO SHIFT RIGHT LOGIC
            if (reggie[0] < reggie[1]):
                return [t.reg_princ[reggie[1]], t.reg_princ[reggie[1]], t.reg_princ[reggie[1]], 0]
            else:
                return [t.reg_princ[reggie[0]], t.reg_princ[reggie[1]], t.reg_princ[reggie[0]], 0] 
        
        # INSTRUCCION SRL
        if (instruc == "srl"): 
            #REGRESA REGISTROS RT, RD Y FILL
            #PUEDE SER TANTO SHIFT LEFT LOGIC COMO SHIFT RIGHT LOGIC
            if (reggie[0] < reggie[1]):
                return [t.reg_princ[reggie[1]], t.reg_princ[reggie[1]], t.reg_princ[reggie[1]], 0] 
            else:
                return [t.reg_princ[reggie[0]], t.reg_princ[reggie[1]], t.reg_princ[reggie[0]], 0] 

        # INSTRUCCION JR
        if (instruc == "jr"): 
                #REGRESA REGISTROS RS, RT, RD Y FILL
                return [t.reg_princ[reggie[0]], 0, 0, 0]
            
        #FUNC -> R          
        try:   
            #REGRESA REGISTROS RS, RT, RD Y FILL   
            return[t.reg_princ[reggie[1]], t.reg_princ[reggie[2]], t.reg_princ[reggie[0]], 0]
        except:
            return None
    else:
        return None
