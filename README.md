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
- **Reading the whole file**

The two input files are read into the memory all at once. This may not be feasible in case of the huge file.


- **Sequential computation**

For simplicity, the code performs computation for each area sequentially. However, the computation for each area is independent. Multithreading or Multiprocessing can be used to accelerate the computation.

## Running on production

The script is self-contained so it can be run anywhere as long as the dependency(pandas) is satisfied. Also, the input files can be configured at runtime

## How to scale 
If the data is much larger, we can use concurrent computing to accelerate the computation. 

For example, we can create multiple processes where each has a set of areas it is responsible and a portion of land_data corresponding to that. Each process will write the result into its own file. If we want the result as a single file, we can write a script to concatenate all files together which should be straightforward as they all are CSV and have the same headers.
