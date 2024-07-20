#!/bin/zsh



raw_csv=$(mdb-export /Users/julianickodemus/Coding/R/ipedsData/IPEDS201011.accdb C2010_A)

echo $raw_csv > C2010_A.csv


