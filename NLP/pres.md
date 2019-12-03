---
title: NLP Project Presentation
author: Akshay Goindani, Zubair Abid
theme: Metropolis
---

# Unsupervised Multilingual Word Embeddings (Chen and Cardie, 2018)

## Overview

- Proposes a framework to learn Multilingual Word Embeddings (MWEs)
- Exploits relations between all language pairs
- Performs in $O(N)$ time, where N is the number of languages

# Related Work

- Most use cross-lingual supervision, some sort of parallel corpora
- pivot-BWEs: mapping all languages individually into a target language space (training Bilingual Word Embeddings, N times)
    - Does not capture relations between all language pairs
- BWE-Direct: training embeddings for all language pairs. 
    - Computational Complexity: $O(N^2)$

# Solution

- Maps all monolingual embeddings into a shared space via a two-step algorithm:
    - Multilingual Adversary Training (MAT)
    - Multilingual Pseudo-Supervised Refinement (MPSR)
- Outperforms both pivot-BWE and BWE-Direct
- $O(N)$ complexity

# Definitions for the Architecture

For each language $l \in L$ (where $L$ is the set of languages considered), we take the embedding $E_l$ that is in the embedding space $S_l$

- The models learn:
    - Encoder $M_l$ into target space $T$ s.t. $M_l: S_l \to T$
    - Decoder $M_l^{-1}$, so $M_l^{-1}: T \to S_l$

Encoders $M_l$ are all orthogonal linear matrices

# Definitions for the Architecture (cont.)

*Language classifiers* $D_l$: a binary classifier with a sigmoid layer on top, trained to identify how likely it is a vector is from space $S_l$

# Multilingual Adversary Training

## Overview

- Setup an adversarial relation between $D_l$ and $M_l$
- Stimulates $M_l$ to learn a shared multilingual embedding space 
    - So that $D_l$ cannot predict if the vector is genuine or converted from another language

# Multilingual Adversary Training (cont.)

## Language Discriminators

- For random pair $(l_i, l_j)$ convert vector from $S_i$ to $S_j$ (using $M_{l_i}$, $M_{l_j}^{-1}$ and via $T$)
- Objective: confuse $D_j$
- Formal definitions: TODO

# Multilingual Adversary Training (cont.)

## Other improvements and optimizations

- $l_i$ and $l_j$ can be the same language (adversarial autoencoder is formed, shown to be beneficial)
- Instead of random sampling throughout, the external iteration loops through all languages to ensure updation of all language discriminators at least once

# Multilingual Pseudo-Supervised Refinement

## Overview

- MAT gives reasonable quality embeddings, but not SOTA
- May be due to noisy training signals from $D$
- Improvement: Induce a dictionary of *highly confident word pairs* for each language pair, and use this











