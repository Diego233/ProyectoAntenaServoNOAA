#!/usr/bin/python
#
# Add satellites from AMSAT website that were not in the Celestrak database
#
import os
#import string
import urllib.request


webfile = 'https://www.celestrak.com/NORAD/elements/noaa.txt'
localfile = './NOOA.txt'
print('Fetching ' + webfile + ' => ' + localfile)
urllib.request.urlretrieve(webfile, localfile)

tlefile = open(localfile, 'r')
catfile = open('./amateur.cat', 'a')
datfile = open('./satellites.dat', 'a')

while 1:
    # read three lines at a time; strip trailing whitespaces
    line1 = tlefile.readline().strip()
    if not line1: break
    line2 = tlefile.readline().strip()
    line3 = tlefile.readline().strip()

    # catalog number; strip leading zeroes
    catnum = line2[2:7].lstrip('0')

    satfilename = './tmp/' + catnum + '.sat'
    if os.path.isfile(satfilename): continue

    print(" Adding " + catnum + " ...")

    catfile.write(catnum+'\n')

    datfile.write("\n["+catnum+"]\n")
    datfile.write('VERSION=1.1\n')
    datfile.write('NAME='+line1+'\n')
    datfile.write('NICKNAME='+line1+'\n')
    datfile.write('TLE1='+line2+'\n')
    datfile.write('TLE2='+line3+'\n')

tlefile.close()
catfile.close()
datfile.close()
