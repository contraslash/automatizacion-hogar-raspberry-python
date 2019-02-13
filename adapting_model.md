# Adapting the model

First record the adaptation records.

Create two files:

adapting_model.fileids

```text
ad001
ad002
ad003
ad004
ad005
ad006
ad007
ad008
ad009
ad010
```

adapting_model.transcription

```text
<s> prender luz </s> (ad001)
<s> apagar luz </s> (ad002)
<s> prendido </s> (ad003)
<s> apagado</s> (ad004)
<s> prender uno</s> (ad005)
<s> apagar uno </s> (ad006)
<s> prender la luz uno </s> (ad007)
<s> apagar la luz uno </s> (ad008)
<s> prender todo </s> (ad009)
<s> apagar todo </s> (ad010)
```

Then generate the MFCC files

```bash
sphinx_fe \
    -argfile ../isolated_words/etc/feat.params.concrete \
    -samprate 16000 \
    -c adapting_model.fileids \
    -di . \
    -do . \
    -ei wav \
    -eo mfc \
    -mswav yes
```

Convert the definitions to tex plain


```bash
pocketsphinx_mdef_convert \
    -text ../isolated_words/model_parameters/isolated_words.ci_semi/mdef mdef.txt
```

Now execute Baum Welch Algorithm to fit the hidden states with the new data

```bash
/usr/local/libexec/sphinxtrain/bw \
    -hmmdir ../isolated_words/model_parameters/isolated_words.ci_semi/ \
    -moddeffn mdef.txt \
    -ts2cbfn .semi. \
    -feat s2_4x \
    -cmn current \
    -agc none \
    -dictfn ../isolated_words/etc/isolated_words.dic \
    -ctlfn adapting_model.fileids \
    -lsnfn adapting_model.transcription \
    -accumdir accum_dir
```

Now copy the previous model in to the current folder

```bash
cp -a ../isolated_words/model_parameters/isolated_words.ci_semi isolated_words.ci_semi.adapt
```

The use map adapt to create the adaptations

```bash
/usr/local/libexec/sphinxtrain/map_adapt \
    -moddeffn mdef.txt \
    -ts2cbfn .semi. \
    -meanfn ../isolated_words/model_parameters/isolated_words.ci_semi/means \
    -varfn ../isolated_words/model_parameters/isolated_words.ci_semi/variances \
    -mixwfn ../isolated_words/model_parameters/isolated_words.ci_semi/mixture_weights \
    -tmatfn ../isolated_words/model_parameters/isolated_words.ci_semi/transition_matrices \
    -accumdir accum_dir \
    -mapmeanfn isolated_words.ci_semi.adapt/means \
    -mapvarfn isolated_words.ci_semi.adapt/variances \
    -mapmixwfn isolated_words.ci_semi.adapt/mixture_weights \
    -maptmatfn isolated_words.ci_semi.adapt/transition_matrices
```


Now we need to extend the language model, so let's take the original transcription file and add the new text

```python
# Open the model transcriptions
model_transcriptions = open("../isolated_words/etc/isolated_words.transcription")
model_transcriptions_lines = model_transcriptions.readlines()

# Open the new transcriptions
new_transcriptions = open("adapting_model.transcription")
new_transcriptions_lines = new_transcriptions.readlines()

# Now create a new file with the content of the model_transcriptions and the new ones
new_transcriptions_file = open("isolated_words_adapt.transcription", "w+")
for model_transcriptions_line in model_transcriptions_lines:
    new_transcriptions_file.write("{}".format(model_transcriptions_line))

for new_transcriptions_line in new_transcriptions_lines:
    new_transcriptions_file.write("{}\n".format(new_transcriptions_line.split("(")[0]))
new_transcriptions_file.close()
```

Now with the new transcription file, generate the new language model.

```bash
DB_NAME=isolated_words_adapt
text2wfreq < ${DB_NAME}.transcription | wfreq2vocab > ${DB_NAME}.vocab
text2idngram -vocab ${DB_NAME}.vocab -idngram ${DB_NAME}.idngram < ${DB_NAME}.transcription
idngram2lm -vocab_type 0 -idngram ${DB_NAME}.idngram -vocab ${DB_NAME}.vocab -arpa ${DB_NAME}.lm
sphinx_lm_convert -i ${DB_NAME}.lm -o ${DB_NAME}.lm.DMP
```

Now you can test your model with Pocket Sphinx

```bash
pocketsphinx_continuous -hmm isolated_words.ci_semi.adapt/ -lm isolated_words_adapt.lm.DMP -dict ../isolated_words/etc/isolated_words.dic -inmic yes
```