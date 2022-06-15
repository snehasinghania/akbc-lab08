# Lab 08: Knowledge Base Construction from Language Models

This repository contains the dataset and scripts for Lab 08 of [AKBC course](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/teaching/ss2022/akbc) 

## Download the dataset and scripts

```bash
$ git clone https://github.com/snehasinghania/akbc-lab08.git
cd akbc-lab08
```

## Usage

1. Install the required dependencies to run the baseline and evaluate scripts.

```
pip install -r requirements.txt
```

2. To run the baseline script:

```
python baseline.py [-h] [--model_type MODEL_TYPE] [--input_dir INPUT_DIR] 
                  [--prompt_output_dir PROMPT_OUTPUT_DIR] 
                  [--baseline_output_dir BASELINE_OUTPUT_DIR]

Probe a Language Model and Run the Baseline Method on Prompt Outputs

optional arguments:
  -h, --help            show this help message and exit
  --model_type MODEL_TYPE
                        HuggingFace model name
  --input_dir INPUT_DIR
                        input directory containing the subject-entities for each relation to probe the language model
  --prompt_output_dir PROMPT_OUTPUT_DIR
                        output directory to store the prompt output
  --baseline_output_dir BASELINE_OUTPUT_DIR
                        output directory to store the baseline output                        
```

3. To run the evaluation script:

```
python evaluate.py [-h] [--input_dir INPUT_DIR] [--ground_truth_dir GROUND_TRUTH_DIR] 
                    [--results_dir RESULTS_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        input directory containing the baseline or your method output
  --ground_truth_dir GROUND_TRUTH_DIR
                        ground truth directory containing true object-entities for the subject-entities for which the LM was probed and then baseline or your
                        method was applied
  --results_dir RESULTS_DIR
                        results directory for storing the F1 scores for baseline or your method
```

The baseline method achieves the following scores after running the evaluate.py script:
| Relation                        | Precision   | Recall     | F1-score  |
|---------------------------------|------------:|-----------:|----------:|
| CountryBordersWithCountry       | 0.02        | 0.007      | 0.01      |
| RiverBasinsCountry              | 0.28        | 0.192      | 0.215     |
| PersonLanguage                  | 0.12        | 0.0817     | 0.0913    |
| PersonProfession                | 0.0         | 0.0        | 0.0       |
| PersonInstrument                | 0.0         | 0.0        | 0.0       |
| macro average                   | **8.4**     | **5.61**   | **6.32**  |

4. Implement your idea in the ``your_solution`` function in the [``solution.py``](solution.py) file.