#!/usr/bin/env python3

import argostranslate.package, argostranslate.translate
import sys

inputFile = ""
outputFile = ""
targetText = ""
sourceText = ""
from_code = "pt"
to_code = "en"

n = len(sys.argv)
if (n > 1):
    i = 1
    while i < n:
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            print("Translator Command Line Interface (CLI)")
            print("Usage: translator [options] [input file] [--] [arguments]")
            print("Options:")
            print("-h     --help               Displays this help message.")
            print("-i     [input file]         Input file name.")
            print("-o     [output file]        Output file name.")
            print("       --source             Source language.")
            print("       --target             Target language.")
            exit(0)
        elif sys.argv[i] == "-i":
            i = i + 1
            inputFile = sys.argv[i]
        elif sys.argv[i] == "-o":
            i = i + 1
            outputFile = sys.argv[i]
        elif sys.argv[i] == "--source":
            i = i + 1
            from_code = sys.argv[i]
        elif sys.argv[i] == "--target":
            i = i + 1
            to_code = sys.argv[i]
        else:
            inputFile = sys.argv[i]
            break
        i = i + 1

if inputFile != "":
    sourceTextFile = open(inputFile, 'r')
    sourceText = sourceTextFile.read()
    sourceTextFile.close()

    # Download and install Argos Translate package.
    available_packages = argostranslate.package.get_available_packages()
    available_package = list(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )[0]
    download_path = available_package.download()
    argostranslate.package.install_from_path(download_path)

    # Translate text.
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = list(filter(
        lambda x: x.code == from_code,
        installed_languages))[0]
    to_lang = list(filter(
        lambda x: x.code == to_code,
        installed_languages))[0]
    translation = from_lang.get_translation(to_lang)
    targetText = translation.translate(sourceText)

    if outputFile != "":
        targetTextFile = open(outputFile, 'w')
        targetTextFile.write(targetText)
        targetTextFile.close()
    else:
        print("Translator Command Line Interface (CLI)")
        print("Usage: translator [options] [input file] [--] [arguments]")
else:
    print("Translator Command Line Interface (CLI)")
    print("Usage: translator [options] [input file] [--] [arguments]")
