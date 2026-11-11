#!/bin/bash
#SBATCH --job-name=testmedicalexperimentmodel
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:15:00
#SBATCH --output=testmedicalexperimentmodel-%j.out
#SBATCH --gres=gpu:1
#SBATCH --partition=mig

module purge
module load anaconda3/2026.7
conda activate torch-env
export HF_HUB_OFFLINE=1
echo "Running on $(hostname)"
python test_model.py