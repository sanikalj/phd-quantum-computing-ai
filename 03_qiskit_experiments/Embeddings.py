import numpy as np
from openai import embeddings

vocab=['h','e','l','l','o']

embeddings_dim=4
embeddings={ch:np.random.randn(embeddings_dim) for ch in vocab}
print("Embeddings for h:", embeddings['h'])