## README.md (10%)

requirements.txt

這個是直接匯出的，應該直接操作以下指令就可以進行安裝。

```shell
pip install -r requirements.txt
```

## Submission folder (10%)

json file 位於 submission 資料夾底下，一共有五個檔案，在後續會說明。

```
submission/
    -llama-3-8b-bnb-4bit.json
    -DPO_llama-3-8b-bnb-4bit.json
    -DPO_mistral-7b-v0.3-bnb-4bit_dropout0.01.json
    -ORPO_llama-3-8b-bnb-4bit.json
    -ORPO_mistral-7b-v0.3-bnb-4bit_lr1e-6.json
    -ORPO_mistral-7b-v0.3-bnb-4bit_drop0.1.json
```

後面附上所有訓練他們的參數

## DPO & ORPO (20%+20%)

這裡跑了五次訓練 1 epoch 的 unsloth/mistral-7b-v0.3-bnb-4bit 模型，不使用 llama-3-8b-bnb-4bit 的原因是因為顯卡是 3060 12GB，記憶體不夠無法訓練，訓練1 epoch的時間約12小時。

另外有特別加一個dropout參數，因為感覺大模型很容易過擬合，所以還是喜歡加，不過看起來效果沒預期的好。

另外訓練到一半感覺學習率太高了，餘弦退火也沒有把學習率降到多低，後面loss根本降低不下去，就調低了一點學習率再跑。

結果分別是以下參數檔

### DPO_mistral-7b-v0.3-bnb-4bit.json
```shell
python main.py \
    --exp_name "DPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --num_epochs 1
```

### DPO_mistral-7b-v0.3-bnb-4bit_dropout0.01.json
```shell
python main.py \
    --exp_name "DPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --dropout 0.01 \
    --num_epochs 1
```

### ORPO_mistral-7b-v0.3-bnb-4bit.json
```shell
python main.py \
    --exp_name "ORPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --num_epochs 1
```

### ORPO_mistral-7b-v0.3-bnb-4bit_lr1e-6.json
```shell
python main.py \
    --exp_name "ORPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --lr 0.000001 \
    --num_epochs 1
```

### ORPO_mistral-7b-v0.3-bnb-4bit_drop0.1.json
```shell
python main.py \
    --exp_name "ORPO" \
    --model_name "unsloth/mistral-7b-v0.3-bnb-4bit" \
    --train \
    --wandb_token "26da30cfdb66ab84c1a739777ea9b6a00b63b8af" \
    --lr 0.000001 \
    --dropout 0.1 \
    --num_epochs 1
```

從json內容看起來DPO雖然loss很小，但可能是學習率太高或者是單純優化方式問題，所以導致很多問題答不太出來，看起來ORPO在這方面好很多，所以後續開始以ORPO來做實驗。

