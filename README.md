**BART & GECToR: An Unlikely Alliance for Grammatical Error Correction**

Final Code Base
	- Data: Contains all the Test, Train, Development datasets that we used for the models
	
	- Scripts: 
		- GED_model.ipynb (modified from  https://towardsdatascience.com/checking-grammar-with-bert-and-ulmfit-1f59c718fe75)
		- combined.py (script to combine all datasets)
		- m2_to_parallel.py (used to convert m2 files to .src and .tgt files)
		- ensemble.py (for ensembling the BART and GECTor results)
	
	- Models: BART and GECTor models that we use for our results in the report (https://nusu-my.sharepoint.com/:f:/g/personal/e0445473_u_nus_edu/EhPBuknlwF5AgTpX3n5ytiMBoWujv9MPD5uak_WmUf2c4A)
	
	- BART_RESULTS: Corrected outputs for BEA_2019 and CoNNL_2014 by BART and their results
	
	- GECTor_RESULTS: Corrected outputs for BEA_2019 and CoNNL_2014 by GECtor and their results

	- ENSEMBLE RESULTS: Ensemble results from running ensemble.py for BEA_2019 and CoNNL_2014


Workflow:

STAGE 1
Train (using Data/..) and Run Baseline BART FROM https://github.com/Katsumata420/generic-pretrained-GEC
- Clone the repository
- Change the filepaths as needed
- Train and run the model to get BART_RESULTS/bea2019_output.txt and BART_RESULTS/CoNNL_output.txt

STAGE 2
Grammatical Error Detection model (for further analysis on BART results)
- Run the kernels in the Jupyter Notebook to train the model on the CoLA Dataset which can be downloaded from instructions in the notebook
- Save and Load the model in models/model_save_GED, and
- Use it on BART_RESULTS/bea2019_output.txt and BART_RESULTS/CoNNL_output.txt
- Generate graphs for report on correct corrections done by BART based on a BERT-Classifier
(Paths might have to be readjusted)


STAGE 3
Train (using Data/..) and run GECTOR from https://github.com/grammarly/gector
- Clone the repository
- Change the filepaths as needed
- Train and run the model to get GECtor_RESULTS/bea2019_output.txt and GECTor_RESULTS/conll_gector_output.txt


STAGE 4
ENSEMBLE the outputs generated from BART with GECTor using https://github.com/MaksTarnavskyi/gector-large
- Clone the repository (optional, as we ONLY use ensemble.py and its dependencies)
- We ensemble using majority vote
- Run the command:

FOR BEA-2019
```
python ensemble.py --source_file '../Data/Test_Data/ABCN.test.bea19.orig' \
                         --target_files '../GECtor_RESULTS/bea2019_output.txt' '../BART_RESULTS/bea2019_output.txt' \
                         --output_file '../ENSEMBLED_RESULTS/bea_ensembled'
```

FOR CoNNL-2014
```
python ensemble.py --source_file '../Data/Test_Data/official-2014.combined.src' \
                         --target_files '../GECtor_RESULTS/conll_gector_output.txt' '../BART_RESULTS/CoNNL_output.txt' \
                         --output_file '../ENSEMBLED_RESULTS/connl_ensembled'
```
