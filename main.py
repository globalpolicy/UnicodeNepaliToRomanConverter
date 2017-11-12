import sys
import os
import argparse

nepaliToEnglishDict = \
    {
        "अ": "a",
        "आ": "aa",
        "ा": "a",
        "इ": "i",
        "ई": "i",
        "र्": "r",
        "उ": "u",
        "ए": "e",
        "े": "e",
        "ै": "ai",
        "ो": "o",
        "ौ": "au",
        "ओ": "o",
        "औ": "au",
        "ं": "n",
        "ँ": "n",
        "ि": "i",
        "ी": "ee",
        "ु": "u",
        "ू": "oo",
        "क": "ka",
        "क्": "k",
        "ख": "kha",
        "ख्": "kh",
        "ग": "ga",
        "ग्": "g",
        "घ": "gha",
        "ङ": "nga",
        "च": "chha",
        "च्": "chh",
        "छ": "cha",
        "ज": "ja",
        "ज्": "j",
        "झ": "jha",
        "ञ": "na",
        "ट": "ta",
        "ट्": "t",
        "ठ": "thha",
        "ठ्": "thh",
        "ड": "da",
        "ढ": "dhha",
        "ण": "na",
        "त": "ta",
        "त्": "t",
        "थ": "tha",
        "थ्": "th",
        "द": "da",
        "ध": "dha",
        "ध्": "dh",
        "न": "na",
        "न्": "n",
        "प": "pa",
        "प्": "p",
        "फ": "pha",
        "ब": "ba",
        "ब्": "b",
        "भ": "va",
        "भ्": "v",
        "म": "ma",
        "म्": "m",
        "य": "ya",
        "र": "ra",
        "रू": "ru",
        "ृ": "ri",
        "ल": "la",
        "ल्": "l",
        "व": "wa",
        "व्": "w",
        "स": "sa",
        "स्": "s",
        "श": "sha",
        "श्": "sh",
        "ष": "sa",
        "ज्ञ": "gya",
        "ह": "ha",
        "१": "1",
        "२": "2",
        "३": "3",
        "४": "4",
        "५": "5",
        "६": "6",
        "७": "7",
        "८": "8",
        "९": "9",
        "०": "0",
        "।": "."
    }


def Convert(inputFilePath, outputFilePath):
    try:
        with open(inputFilePath, encoding='utf-8') as fp:
            nepalicontent = fp.read()
        converted = ''
        for index, char in enumerate(nepalicontent):
            if len(converted) > 0:
                if converted[len(converted) - 1] == 'a':
                    if char == '्':
                        converted = converted[:-1]
                        continue
                    if char == 'ि' or char == 'ी' or char == 'ु' or char == 'ू' or char == 'ृ' or char == 'ो' or char == 'ौ':
                        converted = converted[:-1]
                    if char == 'े':
                        if nepalicontent[index - 1] == 'ा':
                            converted = converted[:-1]
                            converted += 'o'
                            continue
                        converted = converted[:-1]
                    if char == 'ै':
                        if nepalicontent[index - 1] == 'ा':
                            converted = converted[:-1]
                            converted += 'au'
                            continue
                        converted = converted[:-1]
            try:
                converted += nepaliToEnglishDict[char]
            except KeyError:
                converted += char
        if not os.path.exists(outputFilePath):
            with open(outputFilePath, "w", encoding='utf-8') as fp:
                fp.write(converted)
                print("Output file saved to {}".format(outputFilePath))
        else:
            print("Output file already exists!\nAborting to avoid overwriting.")
    except:
        print("Exception : ", sys.exc_info()[0])


argParser = argparse.ArgumentParser(
    description='Convert unicode Nepali script to English based on pronunciation')
argParser.add_argument(
    'inputFilePath', help='Path to the file containing Nepali input')
argParser.add_argument('outputFilePath', help='Path to the output file')
args = argParser.parse_args()
Convert(args.inputFilePath, args.outputFilePath)
