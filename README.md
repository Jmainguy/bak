# bak
```
usage: bak [-h] [-a APPEND] [-d] [-f] [-u] Source

Backup a file, defaults to same path and .bak

positional arguments:
  Source                file to backup

optional arguments:
  -h, --help            show this help message and exit
  -a APPEND, --append APPEND
                        characters to append to source file instead of .bak
  -d, --date            add the date .YYYYMMDD to the end of the file
  -f, --force           overwrite backup if exists
  -u, --unbak           Unbak a file to its original location, force overwrite
                        (if your filesystem supports extended file attributes)
```
# unbak
```
usage: unbak [-h] Source

Restore a file created by bak, this is the same as bak -u

positional arguments:
  Source      bak file to restore

optional arguments:
  -h, --help  show this help message and exit
```
## RPM
to create a RPM, run

```
make rpm
```

then yum install the result in the dist/ directory it creates
note this requires rpm-build installed on the host building the rpm and pyxattr installed on the target.

### unbak, bak -u
bak -u allows you to restore a file backed up using bak. 

By default bak creates metadata on the .bak file (https://en.wikipedia.org/wiki/Extended_file_attributes)

bak would then try to restore to the path stored in the metadata, if the metadata is removed, this wont work.

It is really easy to lose the metadata, and you need to take active measures to preserve metadata if moving/copying the backup file.

http://www.lesbonscomptes.com/pages/extattrs.html

mv preserves xattrs
cp will only preserve xattrs if given the option --preserve=xattr
rsync 3.0.9 with option -X or --xattrs will preserve attributes

If copying to a filesystem that does not support metadata (tmpfs for example) metadata will be lost
