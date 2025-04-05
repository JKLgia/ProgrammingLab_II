#from translate import Translator
#from deep_translator import GoogleTranslator
#from reverso_context_api import Client
#from reverso_api.context import ReversoContextAPI
#import os
from deepl import Translator as DlTranslator
import re
import time

'''
This program translate a text file from one language to another using the Google Translator API.
It takes the input file name, output file name, source language, and target language as command line arguments.
It reads the input file, translates the text, and writes the translated text to the output file.
But need to manipulate the file, beacause not all contenet is translatable.
The program also handles the case where the input file is not found and prints an error message.


Da creare funzione che conta quanti caratteri sono presenti nel file prima di tradurli e nel caso
superi il limite deve salvare il resto del file in un altri file e tradurlo in un secondo momento.

Per limitare le parole tradotte si deve creare una funzione che conta il numero di parole uguali e
questo pattern nella traduzione finale, anziche tradurre 20 volte la stessa parola la traduce 1 volta e 
poi la sostituisce nelle frasi in cui la parola è usata.
'''
authKey = "c398ce81-fd6e-4604-b62d-a9e408fc5ad6:fx" # Chiave DEEPL API

def file_translate(peth_file, source_lang = 'it', target_lang = 'en'):

    with open(peth_file, 'r', encoding='utf-8') as file:
        lines = [line for line in file.readlines()]
        lines = [element.strip() for element in lines]

        numero_allarme = []
        messaggio = []
        for elemnt in lines:

            if elemnt.startswith("<source>"):
                numero_allarme.append(''.join(re.findall(r'\d+', elemnt)))
                

        for elemnt in lines:
            if elemnt.startswith("<translation>"):
                messaggio.append(elemnt.split(">")[1].split("<")[0])
        
        #Conta i caratteri delle frasi
        num_carat = 0
        for i in messaggio:
            num_carat += conta_caratteri(i)
        
        print(f"Numero di caratteri: {num_carat}")

        if num_carat > 500000:
            return "Il file supera il limite di 500000 caratteri" #La funzione ritorna un messaggio di errore e non traduce il file
        
        '''
        traduttore = DlTranslator(authKey)
        translate = []
        dictionary = {}
        for message in messaggio:
            try:
                #api = ReversoContextAPI(str(message), source_lang, target_lang)
                #client = GoogleTranslator(source_lang, target_lang)
                translate.append(traduttore.translate_text(str(message), target_lang=target_lang))
                time.sleep(1) # Sleep for 0.5 seconds to avoid hitting the API rate limit
            except Exception as e:
                print(f"Error translating message '{message}': {e}")

        for i in range(len(numero_allarme)):
            dictionary[numero_allarme[i]] = translate[i]
        '''
    return 1 #dictionary

def conta_caratteri(testo):
    #Open file in read mode
    #Count the number of characters in the file
    num_characters = sum(c.isalpha() for c in testo)
    return num_characters


def insert_new_message(number, message, file):
    #Open file in write mode
    with open(file, 'a', encoding='utf-8') as f:
        #Write the new message to the file
        f.write(f"\t\t<message>\n")
        f.write(f"\t\t\t<source>{number}/PLC/PMC</source>\n")
        f.write(f"\t\t\t<translation>{message}</translation>\n") #\t is used to add a tab space
        f.write(f"\t\t</message>\n")



input_file = 'C:\\Users\\Media\\Desktop\\LG_LabProgramming_II\\ProgrammingLab_II\\Traduzione Testi\\oem_alarms_plc_ita.txt'  # Input file name
output_file = 'output.txt'  # Output file name
source_lang = 'it'  # Source language code (e.g., 'en' for English, 'it' for Italian)
target_lang = 'en'  # Target language code (e.g., 'en' for English, 'it' for Italian)

dictionary = file_translate(input_file)
print(dictionary)

    


    