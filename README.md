## Running instructions
1. Install pandas.
```
pip install pandas
```
2. Put the input files into the project folder.
3. Execute the script.
```
python get_area_of_interest_value.py --land_data=path_to_land_data_file --area_of_interest=path_to_area_file
```
Ex.
```
python get_area_of_interest_value.py --land_data=data/pp-2020.csv --area_of_interest=data/areas_of_interest.csv
```

## Tradoffs
- Reading the whole file
The two input files are read into the memory all at once. This may not be feasible in case of the huge file.
- Sequential computation
For simplicity, the code performs computation for each area sequentially. However, the computation for each area is independent. Multithreading or Multiprocessing can be used to accelerate the computation

## Running on production

## How to scale
