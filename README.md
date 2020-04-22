# ABL statistics test case

## Instructions

1.  Download or clone the repo  
    Using Sandia's gitlab:  
```bash
$ git clone git@gitlab.sandia.gov:lcheung/ablaveraging.git
```
    Or the public github server:
```bash
$ git clone git@github.com:lawrenceccheung/ablaveraging.git
```

2.  Generate the mesh
```bash
$ abl_mesh -i nalu_abl_mesh.yaml
$ nalu_preprocess -i nalu_preprocess.yaml
```

3.  Run the sample problem
```bash
$ mpirun -np 8 naluX -i ablAveraging.yaml
```

4.  Check the differences
```bash
$ python plotdiff.py
```

As part of the output, you should see the differences between manually
averaging the ABL statistics (using `plotABLstats.py`) and the
automatically averaged statistics from Nalu-Wind directly:

```
Difference between manual and Nalu-wind time-average
------------
<Umag> diff L2: 4.339009e-02
<T>  diff L2:   2.007920e-05
<uu> diff L2:   1.549508e-02
<vv> diff L2:   1.040201e-02
<ww> diff L2:   2.247193e-03
<Tu> diff L2:   1.173367e+02
<Tv> diff L2:   8.263943e-04
<Tw> diff L2:   1.597271e-05
```

