import pandas as pd
from gensim import corpora
from gensim.models import LdaModel
from sklearn.feature_extraction.text import CountVectorizer

def perform_topic_modeling_gensim(data, num_topics=5, num_words=10, sample_size=None):
    # Subsample the data if a sample size is provided
    if sample_size:
        data = data.sample(n=sample_size, random_state=42)

    # Ensure the 'headline' column exists
    if 'headline' not in data.columns:
        raise ValueError("The dataset must contain a 'headline' column.")

    # Initialize CountVectorizer for basic keyword extraction
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(data['headline'].dropna())
    vocab = vectorizer.get_feature_names_out()

    # Convert to gensim corpus and dictionary
    id2word = corpora.Dictionary([vocab])
    corpus = [[(id2word.token2id[word], freq) for word, freq in zip(vocab, doc.data)] for doc in dtm]

    # Fit LDA model using gensim
    lda_model = LdaModel(corpus=corpus, num_topics=num_topics, id2word=id2word, passes=15, random_state=42)

    # Print topics
    topics = lda_model.print_topics(num_topics=num_topics, num_words=num_words)
    for topic in topics:
        print(f"Topic {topic[0]}: {topic[1]}")

    return lda_model, corpus, id2word
