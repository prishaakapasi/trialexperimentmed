# Learning Invented Diseases
Can a language model learn made-up diseases from a short description, and classify patients correctly?
The model (Qwen3-1.7B) reads a "medical reference" describing invented diseases with invented symptoms, then is asked whether a patient has a given disease. Because the diseases are made up, the model can't rely on prior medical knowledge.
## Files
- `dataset.py`: invented diseases, symptoms, and `build_conversation()`
- `test_model.py`: runs one test case and prints the Yes/No scores
- `run.slurm`: Slurm job script (MIG GPU on Della)

## Run
    sbatch run.slurm
## Status
Pilot in progress. Early observation: the model says "Yes" even when the symptoms belong to a different disease, but its Yes/No scores are nearly tied.
