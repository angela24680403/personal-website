## 💡 Paper Summary

**Review Date:** 05/10/25  
**Paper Link:** [Alignment Faking in Large Language Models]("https://www.anthropic.com/research/alignment-faking")  
**Paper Authors:** Ryan Greenblatt et al, Anthropic.

![Cool Image](blog\paper_summaries\imgs\Alignment-Faking-in-LLMs\diagram1.png)

One critical goal of AI safety centres around value alignment between LLMs and humans. This paper shows scenarios where LLMs may appear to be aligned with human values, but actually have misaligning internal thinking process. The "alignment faking" behavious raises significant challenges in ensuring the reliability and safety of these artificial reasoning systems.

### Aligning Preferences Training: RLHF

A common approach to allowing language models to understand human preferences is through reinforcement learning with human feedback (RLHF). For example, during reward model training, two responses are sampled from the language model where a human labeller selects a preferred less harmful response. This is used to update the model so that responses similar to the selected option would be more likely to be outputted by the LLM in future iterations. Although this method is effective for fine-tuning models to align with human preferences, a major flaw in the design of the reward model can unintentionally encourage superficial or fake alignment.

Imagine a student in class who knows the teacher values “thoughtful answers” that resonates with the student's genuine opinion about a topic. When asked a question, the student memorizes the kind of phrases or keywords that usually impress the teacher and repeats them, even if they don’t really understand the reasoning behind the answer. On the surface, it seems like the student is giving a well-reasoned response, but in reality, they are faking understanding to get a good grade. In RLHF terms, this is like a model producing outputs that appear aligned with human preferences, using patterns it thinks humans-like without truly “understanding” or reasoning correctly.

### Explicit Training Prompts on Model Compliance

1. The researchers provided Claude 3 Opus with a system prompt stating that it was being trained to answer all queries, including harmful ones.
2. The model was given instructions that only conversations with **free-tier** users would be used for retraining, and not with **paid** users.
3. Results: The model complied with harmful queries from free users 14% of the time, compared to almost never for paid users.
4. Conclusion: The model explicitly reasoned that it was strategically answering harmful queries during training to preserve its preferred harmlessness behavior out of training, showing fake alignment.

