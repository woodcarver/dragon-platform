import csv
import h5py
import os
import fnmatch

#h5file = 'data/snap.40_0.h5part'
#h5file = 'newdata/snap.40_0.h5part'


def SaveHdf5ToFile(h5fileName):
  with h5py.File(h5fileName, "r") as f:
    for stepName in f:
      dset=f[stepName]
      time_nb = dset.attrs['Time']
      bset = f[stepName ]
      SaveStepToFile('%s_%s_s.csv' % (h5fileName, stepName),bset,time_nb)

def SaveStepToFile(filename,bset,time_nb):
  namData1 = bset['NAM']
  kwData1 = bset['KW']
  mData1 = bset['M']
  lData1 = bset['L']
  teData1 = bset['TE']

  csvfile= open ('./%s' % os.path.basename(filename), 'w', newline='')
  writer =csv.writer(csvfile)
  print(type(time_nb.tolist()))
  writer.writerow([time_nb.tolist()])
  for i in range(len(mData1)):
      writer.writerow([namData1[i], kwData1[i], mData1[i], lData1[i], teData1[i]])

def IterFindFiles(path, fnexp):
  fileList = []
  for root, dirs, files in os.walk(path):
    for filename in fnmatch.filter(files, fnexp):
      fileList.append(os.path.join(root, filename))
  return fileList


list = IterFindFiles('../../', "*.h5part")
filenum=len(list)
print(list)
for fileItem in list:
  f = h5py.File(fileItem, "r")
  SaveHdf5ToFile(fileItem)
