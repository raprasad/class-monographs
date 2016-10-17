import sys
import os
from os.path import join, isdir, isfile
import shutil

def msg(s): print s
def dashes(char='-'): msg(40*char)
def msgt(s): dashes(); msg(s); dashes()
def msgx(s): dashes('\/'); msg(s); dashes('\/'); sys.exit(0)


input_folder = '../round2'

def rename_files(folder, person_name, really_rename=False):
    """Add person's name to the file"""

    d = join(input_folder, folder)
    if not isdir(d):
        msgx("Not a folder: %s" % d)
    else:
        msg('folder found: %s' % d)
    fnames = os.listdir(d)
    fnames = [x for x in fnames if x.endswith('.docx')]
    cnt = 0
    for f in fnames:
        cnt+=1
        msgt("(%s) Rename: %s" % (cnt, f))

        # old name
        full_old_name = join(d, f)

        # new name
        new_name = '%s.%s.%s' % (''.join(f.split('.')[:-1]), person_name, 'docx')
        new_name = new_name.replace(' ', '_')
        full_new_name = join(d, new_name)

        msg('old name: %s' % full_old_name)
        msg('new name: %s' % full_new_name)

        # rename it
        if really_rename:
            shutil.move(full_old_name, full_new_name)
            msg('File moved!!')

if __name__ == '__main__':

    #rename_files('rp/Michelle Jones', 'Michelle_Jones')#, True)
    #rename_files('rp/Dana Demetrio', 'Dana Demetrio')#, True)
    #rename_files('rp/Michelle Wong', 'Michelle Wong')#, True)
    #rename_files('rp/Monica Donhert', 'Monica Donhert')#, True)
    #rename_files('rp/Sandi Coyne', 'Sandi Coyne')#, True)
    #rename_files('rp/Stephanie Swanson', 'Stephanie Swanson')#, True)
    pass
