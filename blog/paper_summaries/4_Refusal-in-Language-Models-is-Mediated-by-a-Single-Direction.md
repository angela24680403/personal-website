## 💡Paper Summary

Review Date: 15/10/25
Paper Link: [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/pdf/2406.11717)

What is a Residual Stream?
It is the main data pathway where information flows through and accumulates across layers in transformers. In other words, it is the vector that carries the model's internal representation of the input as it moves through the layers. 

Chat models often refuse to answer some queries that could lead to getting a toxic response. This paper discovered that this refusal behaviour is controlled by a single direction in the internal data flow of the model (the residual stream). This means that adding this direction, the model starts to even refuse to answer some harmless requests, which indivates that the refusal process is easy to manipulate. This shows that current safety models can be easily bypassed. 
