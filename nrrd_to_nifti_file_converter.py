from pathlib import Path
import nrrd #pip install pynrrd if not installed
import nibabel as nib #pip install nibabel if not installed
import numpy as np

input_dir = Path(r'C:\Users\piete\Python\nnUNet\Kaggle\Test\Test')
output_dir = input_dir / 'Output'
files = sorted(input_dir.rglob('*.nrrd'))

for file in files:
#load nrrd 
  _nrrd = nrrd.read(str(file))
  data = _nrrd[0]
  header = _nrrd[1]

#save nifti
  img = nib.Nifti1Image(data, np.eye(4))
  nib.save(img, str(output_dir / file.parent.stem) + '.nii.gz')