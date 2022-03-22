# Updated Headline Generation: Creating Updated Summaries for Evolving News Stories

**Dataset for our ACL-2022 paper "Updated Headline Generation: Creating Updated Summaries for Evolving News Stories"**

We release ids and metadata for selected examples from the [NewsEdits](https://arxiv.org/abs/2104.09647) corpus. The train/valid/test splits of the curated **HREN** dataset that we consider are available in `hren_metadata.gz`. Each example is represented as a JSON object resembling the following structure:

```
{
  m_id (id of the example formatted like XXX),
  meta_info: {
    'has_headline_change': bool,
    'has_nontrivial_headline_change': bool,
    'has_body_change': bool,
    'has_nontrivial_body_change': bool
  }


}
```


If you find this work useful, please consider citing our paper:

```
@inproceedings{PanthaplackelETAL20UpdatedHeadlineGeneration,
  author = {Panthaplackel, Sheena and Benton, Adrian and Dredze, Mark},
  title = {Updated Headline Generation: Creating Updated Summaries for Evolving News Stories},
  booktitle = {Association for Computational Linguistics},
  pages = {To Appear},
  year = {2022},
}
```
