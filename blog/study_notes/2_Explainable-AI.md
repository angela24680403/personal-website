## Cambridge XAI Lecture Notes

### Lecture 1: Introduction & Global Perturbation Methods
Types of XAI questions:
- What does the prediction mean?
- How did the model make a prediction?
- Which features contributed to a certain prediction and how?
- How can a model learn or select features that are the model interpretable or informative?
- How much does each sample contribute to model training?

What does Explainability do?
- Debug and debias predictions.
- Verify systems.
- Improve models.
- Knowledge discovery.

Explainability gives a foundation for responsible AI
- **Competence:** improving/debugging models.
- **Fairness:** removing unwanted bias.
- **Safety:** making safer decisions.
- **Usability:** actionable decision making.
- **Human-AI collaboration:** better control and user interaction.
- **Accountability** enabling documentation and governance.
- **Privacy:** preserve privacy.

Example Models:
1. Decision trees: Interpretable because prediction can be explained with a rule.
2. Deep neural networks: black-box models. Predictions can be made mathematically but the evaluation is highly non-linear. 

Key Definitions:
- **Interpretability**: the ability to explain or provide the meaning in understandable terms to humans.
- **Explainability**: a notion of explanation as an interface between humans and a decision make that is both an accurate proxy of the decision maker and comprehensibly to humans.
- **Transparency**: a model is transparent if by itself it is understandable.

![Types of Explainable Models](https://github.com/angela24680403/personal-website/blob/main/blog/study_notes/imgs/explainable_ai/types_explainability.png?raw=true)

A Taxonomy for XAI Methods for Black-box Models
- When is explanation extracted? In-model (inherently interpretable) or post-hoc (black box)?
- Does it explain a particular sample or the whole model? Local, global, or both?
- Does it depend on a particular model? Model-specific or model-agnostic?
- Does it explain the model or an approximation of the model? Visualisation or surrogate?

Explainable modes:
1. **Analytic statement**: natural language descriptions of elements and context that support the decision.
2. **Visualisations**: highlight parts of data that support the decisions and allow user to make their own understanding.
3. **Cases**: give typical/illustrative examples that support the decision.
4. **Rejections or alternate choice**: counterfactual or common misconceptions that argue against the alternative decisions.


#### Knowledge Distillation
Intuition: an interpretable model is trained to approximate the predictions of a black model and then used to explain its predictions.  
![Steps in knowledge distillation.](https://github.com/angela24680403/personal-website/blob/main/blog/study_notes/imgs/explainable_ai/knowledge-distillation.png?raw=true)

#### Surrogate Alignment
Using surrogate models to achieve alignment. This means creating interpretable models that mimic behaviour of complex systems to ensure the output aligns with human values. 

$  R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{\sum^n_{i=1}(y^*_i - \hat{y}_i)^2}{\sum^n_{i=1} (\hat{y}_i - \bar{\hat{y}})^2} $
- SSE: Sum of squares error
- SST: Sum of squares total
- $y^*_i$: surrogate model predict instance i.
- $\hat{y}_i$: black box model predict instance i.
- $\bar{\hat{y}}_i$: mean of black box model predictions.


### Global Perturbation Methods
This is an XAI technique that helps us understand how a model behaves across the entire input space. In other words, it tries to answer the following: "If I change this feature across many inputs, how does it affect the model's output overall?"

Partial Dependence Plot (PDP):
Measures the marginal effect of a feature on the prediction of the model while holding the other features constant.

PDP-based feature importance:
- Intuition: the more the PDP varies the more important the feature is.
- Formulation: How to measure flatness/variability. 

PDP Shortcomings:
- Interactable for high dimensional data.
- Does not factor in feature interactions.
- It is defined over unique values of features, regardless of their frequency. 

### Lecture 2: Local Perturbation Methods

What does it mean to be local?
- Key assumption in local explainability: Even though globally the model may be complex, it may be less complex locally.
- Locality refers to the vacinity of a particular sample for which we seek an explanation.
- Local explanations vary for each sample despite being based on the same complex model.

Explaining a sample one feature at a time:
- Common for humans to explain things based on features.
- Feature attribution/importance: we want a sense of which features were most relevant for the prediction of the model.

Shapley Scores
- A score that fairly assigns credit across all players/features by averaging marginal contribution of a feature across all possible coalitions.
- All this equation says is that we compute a feature's importance by marginalising over its contributions across all possible subsets of features.
- However it is too expensive to look at every subset of features.

SHAP
- Shapley Additive exPlanation (SHAP) efficiently estimates Shapley scores by looking at how a model's output deviates from its mean one feature at a time.
- It is used to explain how much each feature contributes to a particular prediction.
- For each feature, SHAP asks: If I add this feature to the model (in every possible order), how much does it change the prediction on average?
- E.g.: Model prediction = 0.5 (base) + 0.2 (age helped) - 0.1 (income lowered) + 0.3 (education helped)
- Drawback: SHAP can be computationally expensive due to local model creation.

$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|! \, (|F| - |S| - 1)!}{|F|!} \Big[ f_{S \cup \{i\}}(x_{S \cup \{i\}}) - f_S(x_S) \Big] $

Saliency Maps: Vanilla Gradient
- partial derivatives represent sensitivity of otput to input change.
- Vanilla gradient: For an input x and label y, we calculate the gradient for the prediction wrt input features.
- Problem with this: ReLU saturation problem. Inputs that contributed to the output negatively may be disregarded and their attribution may be concealed. 

Saliency Maps: SmoothGrad
- Remove noise by adding noise!
- For an image of interest, we create multiple versions by adding nosie.
- For each version, we get the saliency map.
- We average over all of them.

### Lecture 3: Saliency and Post-hoc Concept-based Methods

Global Average Pooling (GAP)
- Takes each feature map from the last convolutional layer.
- Computes the average value of all spatial elements in the feature map.
- Produces a vector of size equal to the number of the channels.
- Used instead of fully connected layers at the end of CNN.
- Interperitable Properties: Allows the weight of the linear layer directly translate to importance of spatial features for a class.

Why do we compute the gradient for grad-CAM?
- If the gradient is positive and large, the spatial feature increases $y^c$. The network wants that feature there to recognise class c.
- If the gradient is negative, that feature hurts the score for class c.
- If the gradient is near zero, the feature doesnt matter much for $y^c$.
- So, gradients measure how important each spatial feature activation is for the target class.

Class Activation Mapping (CAM)
1. CNN looks at an image and creates many feature maps.
2. At the end, there is the GAP layer which summarizes each feature map into one number.
3. The model uses these numbers with weights to decide the class.
4. CAM takes those weights and feature maps, combines them and makes a coloured map. Red areas = most important for the prediction. Blue areas = not important.
5. Grad-CAM is a generalisation of CAM that works with any architecture.

$\text{Activation Maps} + \text{Gradient-based feature importance}$

- Activation maps: spatial feature maps produced by convolution layers in a CNN. They shohw where in the input image the network is focusing when making predictions.
- Gradient-based feature importance: Gradients of the target class score with respect to these activation maps tell us how important each feature map is for the class. By computing the global average of these gradients over spatial dimensions, we can get weights of each channel.

Grad-CAM Formulation
1. Compute gradient of class score w.r.t feature maps.
2. Grad-CAM heatmap for class c.

What's wrong with feature attribution?
1. Low-level features like individual pixels are not always semantically meaningful.
2. Feature maps lack actionability.
3. They are susceptible to adversarial attacks.

Concept-based Explainability
- What are concepts? They are high-level and semantically meaningfull units of information.
- Do NN naturally learn concepts? Evidents show lower levels are detecting texture or surface whilst higher levels learn more semantically meaningful concepts.

Post-Hoc Concept-based Explainability
- T-CAV (Concept activation vector) provides global explanations for a class of interest.
- Learns concepts from examples.
- Quantifies the degree to which a user-defined concept is important to a classification result.
- T-CAV asks: If we increase the presence of concept C (e.g. “stripes”) in the network's representation at layer l, does the class score for k (e.g. “zebra”) increase?

T-CAV Formulation
1. Choose an intermediate layer with m neurons.
2. Learn the concept activation vectors (CAVs). Train a linear classifier to distinguish between the activations of concept's examples and randome ones. CAV is the vector orthogonal to the classification boundary.
3. Getting importance scores from CAVs. TCAV gauges the sensitivity of class k to concept C. Given a sample's latent representation and the CAV, how do you think you should gauge this sensitivity? TCAv uses the directional derivative to gauge how much a classification changes with a change in concept.


Automatic Concept Extraction (ACE)
- patches of pixels found across images can be thoguht of as a concept.
1. Segment the sample across multi-resolutions.
2. Cluster extracted segments using a hidden layer of a CNN as feature extractor. Then get rid of outliers as these are not useful concepts.
3. Use TCAV with the newly discovered concepts to explain the prediction of the sample of interest.

Grounding ACE (limitations)
1. We can never be certain that we properly cover all useful concepts.
2. We won't detect concepts that interact non-linearly with the output labels.

Completeness-aware concept extraction (CCE)
- Explains a DNN $\psi(x)$ by discovering a complete set of concepts.
- We assume that $\psi(x)$ can be decomposed into: (1) A mapping $\phi$ from the inputs x to an intermediate hidden layer $\phi(x)$. (2) A mapping f from that intermediate hidden layer $\phi(x)$ to the output layer's prediction.
- Learn a matrix of concept vectors and use a "concept completeness score" to measure their completeness.

Overall equation:
$$
n_f(c_1, \ldots, c_m) = 
\frac{
\sup_g \mathbb{P}_{x,y \sim \nu} \left[ y = \arg\max_{y'} f_{y'}(g(C\phi(x))) \right] - a_r
}{
\mathbb{P}_{x,y \sim \nu} \left[ y = \arg\max_{y'} f_{y'}(x) \right] - a_r
}
$$

Let's break this down, starting with the numerator:
$$
\sup_g \mathbb{P}_{x,y \sim \nu} \left[ y = \arg\max_{y'} f_{y'}(g(C\phi(x))) \right]- a_r
$$
This expression finds the best possible decoder g that can use the concept. The g is picked by looking at the probability that the predicted label based on concept representation $C\phi(x)$ equals the true label y.
Note that $a_r$ is a random baseline. 

Now looking at the denominator:
$$
\mathbb{P}_{x,y \sim \nu} \left[ y = \arg\max_{y'} f_{y'}(x) \right]- a_r
$$
This noramlizes the numerator by the maximum achievable performance of the original model. 

We then update C by optimising this score.
The concept completeness score basically says: "If I project the hidden state into the concept space defined by C, can I faithfully reconstruct it afterwards?"

We want to learn k concept vecots such that:
- Each vector represents a distinct concept direction.
- When a hidden layer of the input DMM is projected into the concept space, their resulting score preserves all the information needed to reconstruct the hidden layer.


Reading List:

- [Cambridge Explainable Artificial Intelligence Module Material](https://www.cl.cam.ac.uk/teaching/2425/L193/materials.html)
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)
