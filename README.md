# Updated Headline Generation: Creating Updated Summaries for Evolving News Stories

**Dataset for our ACL-2022 paper "Updated Headline Generation: Creating Updated Summaries for Evolving News Stories"**

We release ids and metadata for selected examples from the [NewsEdits](https://arxiv.org/abs/2104.09647) corpus. The train/valid/test splits of the curated **HREN** dataset that we consider are available in `hren`. Each example is represented as a JSON object resembling the following structure:

```
{
  id: str,
  meta_info: {
    'has_headline_change': bool,
    'has_nontrivial_headline_change': bool,
    'has_body_change': bool,
    'has_nontrivial_body_change': bool
  },
  'old_headline_version_url': str,
  'new_headline_version_url': str,
  'old_body_version_url': str,
  'new_body_version_url': str
}
```

Note that the `id` field is formatted using the following structure:

```
[DB SOURCE]_[ARTICLE ID]:[OLD HEADLINE VERSION INDEX]-[NEW HEADLINE VERSION INDEX]-[OLD BODY VERSION INDEX]-[NEW BODY VERSION INDEX]:[PAIR INDEX]
```

To obtain the full headline and body texts, you will need to map the ids back to the NewsEdits corpus using the following components: `DB SOURCE`, `ARTICLE ID`, `OLD HEADLINE VERSION INDEX`, `NEW HEADLINE VERSION INDEX`, `OLD BODY VERSION INDEX`, and `NEW BODY VERSION INDEX`.

We have also provided ids and metadata for a larger corpus of examples in `XXX`.

Additionally, we include annotations from human evaluation in `XXX`. These are represented using the following structure:

```

```


If you find this work useful, please consider citing our paper:

```
@inproceedings{PanthaplackelETAL22UpdatedHeadlineGeneration,
  author = {Panthaplackel, Sheena and Benton, Adrian and Dredze, Mark},
  title = {Updated Headline Generation: Creating Updated Summaries for Evolving News Stories},
  booktitle = {Association for Computational Linguistics},
  pages = {To Appear},
  year = {2022},
}
```
