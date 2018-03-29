from VALID import binn, ns
import subprocess
def AB(preg):
    while preg!=("A") and preg!=("B"):
        preg=input("Escribe solo A o B segun su opción: ")
    return preg

def ent(n):
    ln=len(str(n))
    summ=0
    for k in n:
        if k==("1"):
            summ+=2**(ln-1)
        ln-=1
    return summ

def sol_bina(n):
    for i in n:
        if i!="0" and i!="1" and i!=" ":
            n=sol_bina(str(input("Introduzca solo código binario: ")))
            break
    return n
        
while True:
    print("TRADUCTOR BINARIO-TEXTO/TEXTO-BINARIO")
    print("Qué desea hacer?")
    print("A)Descifrar codigo binario")
    print("B)Traducir a binario")
    op=AB(input("Esciba aquí su opción: "))
    code=[]
    if op==("A"):
        inn=sol_bina(str(input("Introduzca código binario: ")))
        lista_inn=inn.split(" ")
        for i in lista_inn:
            res=ent(i)
            code.append(chr(res))
        final=("").join(code)
        print("")
        print("TRADUCCIÓN: ",final)
        print("")
        
    else:
        text=input("Tu texto aquí: ")
        preg=AB(input("¿A partir del primer 1 (A) o incluir 0(B): "))
        preg2=AB(input("¿En lista (A) o en columna (B)?: "))
        tex_lis=list(text)
        texx=[]
        for i in tex_lis:
            if preg==("A"):
                bi=binn(ord(i))
                if preg2==("A"):
                    texx.append(bi) 
                else:
                    print(bi)
            elif preg==("B"):
                bi=(bin(ord(i)))
                lista=list(bi)
                del(lista[1])
                num_final=("").join(lista)
                if preg2==("B"):
                    print(num_final)
                else:
                    texx.append(num_final)
        if preg2==("A"):
            resul=(" ").join(texx)
            print(resul)
    c=ns(input("¿Desea continuar?: "))
    if c==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
            
