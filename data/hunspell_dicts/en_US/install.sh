#!/bin/sh
import os
if [ ! `which wget` ]; then
  sudo dnf -y install wget
fi
if [ ! `which unzip` ]; then
  sudo dnf -y install unzip
fi
if [ ! -d dictionaries ]; then
  exit 1
fi

cd /tmp
hunspell_en_US_dic=en_US.dic
hunspell_en_US_aff=en_US.aff
hunspell_en_US_zip=hunspell-en_US-2018.04.16.zip
if [ ! -f "$hunspell_en_US_dest" ]; then
   if [ ! -f $hunspell_en_US_zip ]; then
     wget -O $hunspell_en_US_zip http://downloads.sourceforge.net/wordlist/$hunspell_en_US_zip
   fi
   unzip $hunspell_en_US_zip
   rm $hunspell_en_US_zip
fi
