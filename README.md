# DSC 180A [FA 22] Project 1:<br> Community Detection using Spectral Embedding 
***Featuring generated test data, political data, and NIPS data***

<!--This site was built using [GitHub Pages](https://pages.github.com/).-->

## Commands

The build script can be run directly from bash `python run.py`

| Command | Description |
| --- | --- |
| `clean`  | Clears remnents of previous networks or communitiy detection  |
| `test-data`  | Generates and loads data network from test data  |
| `nips`  | Downloads, extracts, and prepares data network from NIPS dataset  |
| `data` (or `political`)  | Downloads, extracts, and prepares data network from Political dataset  |
| `spectral`  | Runs spectral embedding community detection  |
| `test`  | equivilent of running `test-data` `spectral`
| `all`  | equivilent of running `data` `spectral`  |

## Data Background

- **Political Dataset**
- ~~**NIPS Papers**~~
- **Generated Test Data**
## Run

Clone the project

```bash
  git clone https://github.com/anmokhta/DSC180A-Project1
```
## Deployment

After running Docker and logging into your account, launch the docker image:

```bash
  launch.sh -i anmokhta/dsc180a-proj1:kaggle
```

From there, copy in the directory, change directories into the project and run commands from bash using run.py:

```bash
  cp DSC180A-Project1 .
  cd DSC180A-Project1
  python run.py test
```


## Authors

- [@anmokhta](https://www.github.com/anmokhta)
- [@darehunt](https://www.github.com/darehunt)
- [@Btran206](https://www.github.com/Btran206)
- [@jul016](https://www.github.com/jul016)

