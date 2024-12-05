#!/bin/bash

python main.py \
    --exp_name "DPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --num_epochs 1

python main.py \
    --exp_name "ORPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --lr 0.000001 \
    --num_epochs 1

python main.py \
    --exp_name "ORPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --lr 0.000002 \
    --dropout 0.1 \
    --num_epochs 1