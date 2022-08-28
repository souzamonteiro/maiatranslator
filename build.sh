#!/bin/sh

rm -rf build/*
rm -rf docs/*

cp src/maiatranslator.maia build/
cp build/maiatranslator.maia bin/
cp src/translator.py build/
cp build/translator.py bin/

chmod 755 bin/*

jsdoc -c ./jsdoc.json -d ./docs ./package.json ./src

#cp manual/* docs/