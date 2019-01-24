# torsiondrive_examples
Examples for torsiondrive

code repository:  https://github.com/lpwgroup/torsiondrive

## steps for a clean setup to run the examples

1. install anaconda

2. create new conda env
```
conda create -n test_td python=3.6
```

3. activate conda env
```
conda activate test_td
```

4. install torsiondrive
```
pip install torsiondrive
```

5. (optional) install cctools/work_queue for distributed computing.
A quick way is to use script (it works with python 3.6 but not 3.7)
```
https://github.com/leeping/forcebalance/blob/master/tools/install-cctools-6.2.10.sh
```

6. go to the examples/ folder, find the interested one
```
cd examples/hooh-1d/psi4/run_local/geomeTRIC/
```

7. (optional) You can also decompress the `opt_tmp` folder to repeat a previous run. If so,
the torsiondrive run will reuse the existing data and finish instantly.
```
tar xf opt_tmp.tar.gz
```

8. install the quantum chemistry software, for psi4:
```
conda install -c psi4 psi4
```

9. run the example:
```
bash run_command
```