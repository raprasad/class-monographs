import sys
import os
from os.path import join, isdir, isfile
import shutil

#from docx import Document

def msg(s): print s
def dashes(char='-'): msg(40*char)
def msgt(s): dashes(); msg(s); dashes()
def msgx(s): dashes('\/'); msg(s); dashes('\/'); sys.exit(0)


input_folder = '../round3-consolidate'

def make_toc(folder_name):

    if not isdir(folder_name):
        msgx("Not a folder: %s" % folder_name)
    else:
        msg('folder found: %s' % folder_name)

    fnames = os.listdir(folder_name)
    fnames = [x for x in fnames if x.endswith('.docx')]
    cnt = 0
    toc_line = []
    csv_lines = []
    for f in fnames:
        fullname = join(folder_name, f)
        #doc  = Document(fullname)
        #import ipdb; ipdb.set_trace()
        cnt+=1
        # split by '.', discard extension
        items = f.replace('_', ' ').split('.')[:-1]
        if len(items) != 2:
            msgx("Not a two part name: %s" % items)

        herb, person = items
        csv_lines.append('%s,%s' % (herb, person))
        print '%d) %s%s(%s)' % (cnt, herb, '\t\t', person)
    open('toc.csv', 'w').write('\n'.join(csv_lines))


if __name__ == '__main__':
    make_toc(input_folder)


"""
mf - 41
rp - 38
    79 total
"""
