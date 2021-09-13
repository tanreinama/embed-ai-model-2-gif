# Embed and expand the AI model in a PNG file.

When we save an AI model file as a PNG file for content distribution reasons, you can expand it.

## Usage

If you have obtained a model file to be used in the [Japanese GPT2](https://github.com/tanreinama/gpt2-japanese) Text Generator AI, you can run the model in your computer as follows.

```sh
### Download your AI model file to XXXX.png
$ git clone https://github.com/tanreinama/embed-ai-model-2-png.git
$ cd embed-ai-model-2-png
$ pip3 install -r requirements.txt
$ python3 extract-png.py --file ../XXXX.png
gpt2ja-XXXX/
gpt2ja-XXXX/checkpoint
gpt2ja-XXXX/hparams.json
gpt2ja-XXXX/model-1000000.data-00000-of-00001
gpt2ja-XXXX/model-1000000.index
gpt2ja-XXXX/model-1000000.meta
### Get gpt2-japanese program
$ git clone https://github.com/tanreinama/gpt2-japanese.git
$ cd gpt2-japanese
$ pip3 install -r requirements.txt
### Run Japanese Text Generator
$ python3 gpt2-generate.py --model ../gpt2ja-XXXX
### Generated text will be displayed
```
