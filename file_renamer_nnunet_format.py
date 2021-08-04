from pathlib import Path

src = Path(r"C:\Users\piete\Python\nnUNet\Kaggle\Output_Lung1")
dst = Path(r"C:\Users\piete\Python\nnUNet\nnUNet_raw\nnUNet_raw_data\Task101_Lung\Test")

for file in src.glob('*.nii.gz'):
    file.rename(dst / (file.stem[:9].replace('X', 'X') + '_0000' + '.nii.gz'))

#Format of files:
#Lung1_XXX_0000.nii.gz