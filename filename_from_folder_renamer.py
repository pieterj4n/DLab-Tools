from pathlib import Path

src = Path(r"D:\Pieterjan\nnUNet_raw_data_base\nnUNet_raw_data\Task103_LiverLITS\Unformatted")
dst = Path(r"D:\Pieterjan\nnUNet_raw_data_base\nnUNet_raw_data\Task103_LiverLITS\Unformatted")

for file in src.rglob("*.nii.gz"):
    file.rename(dst / (file.parent / f"{file.parent.name}_{file.name}"))


#dst doesnt really seem to work ;(