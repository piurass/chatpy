import sys

if len(sys.argv)>=2:
        s=''
        for i in sys.argv[1:]:
                s=s + " " + i
        print("Chatbot Humanizazdo:" + s)
else:
        print("Erro: sem parametros de entrada\n")


