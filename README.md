## 📚 literaturesearch
A Python package that searches the PubMed for scientific articles, summarize abstracts, and ranks the abstracts with respect to topic of interest using LLM. 

## 🚀 Features

🔍 Search PubMed using simple keyword queries via metapub

✨ Summarize abstracts using an LLM (e.g. Gemma or OpenAI models).

📊 Rank articles from 1–5 based on relevance to a target topic.

🧾 Export results to CSV for further analysis.

## Installation

The package requires an ollama, and gemma3:1b to work. Follow the instructions from [ollama](https://github.com/ollama/ollama) to install ollama models locally. I decide to go with this, I got issues into using OpenAI or Anthropic models, they need me to pay. 

Installing locally.
```
git clone git@github.com:rlesiyon/LiteratureSearch.git
cd literaturesearch
pip install -e .
```

## ⚙️ Usage

```{r}
from literaturesearch import summarize

# Run a full search, summarization, and ranking pipeline
results_df = summarize("diabetes insipidus")

# Save results are also written to output.csv
print(results_df.head())
```


