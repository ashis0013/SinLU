# SinLU Activation function

We propose a new non-linear trainable activation function, called Sinu-sigmoidal Linear Unit (SinLU). Here, we aim to explore the sinusoidal properties in an activation function with maintaining a ReLU-like structure. SinLU is a continuous function with a buffer zone on the negative side of the X-axis similar to GELU and SiLU. Furthermore, SinLU is trainable which means it includes some parameters that get trained during the model training which alters its shape.

<img src="https://user-images.githubusercontent.com/31564734/121135309-00ba1280-c852-11eb-819f-35bc2c2aac03.jpg" width="600px"/>

### Formulation of SinLU
The proposed activation function is inspired by the properties of trainable parameters, sinusoid and ReLU like activation functions. In the ReLU activation function, the output of a neuron is multiplied by 1 or 0. This hard gating property often leads to some minor information loss. Introducing Cumulative Distribution Function (CDF) of the standard normal distribution to the ReLU helps in smoothing the output near *x = 0*. The Logistic Distribution CDF &sigma;(x) can also be used which is known as SiLU *x*⋅ *σ*(*x*). We propose to introduce sinusoidal periodicity in this stage. Multiplying *σ*(*x*) with *x*+sin *x* instead of *x* adds a wiggle in SiLU resulting in a modified loss landscape. We define this function as SinLU<sub>basic</sub> which is formulated in the equation below. 

<img src="https://user-images.githubusercontent.com/31564734/121138086-fb11fc00-c854-11eb-9c8e-5986171b44f6.png" width="300px"/>

A more useful shape of the activation function can be devised by the introduction of some trainable parameters. We propose two such parameters *a* and *b* as shown in equation below.

<img src="https://user-images.githubusercontent.com/31564734/121140274-4927ff00-c857-11eb-906e-f118da50eb8c.png" width="300px"/>

The parameter *a* denotes the amplitude of the sine function which basically determines the participation of the sinusoid in the activation function. A very high value of *a* may lead to a shape that is nowhere close to ReLU like function. The parameter *b* determines the frequency of the sine wave. The figure below gives an idea about how the parameters shape the SinLU curve. This can be very easily avoided by proper initialization and hyperparameter controlled training. We start with the value 1 for both *a* and *b* and train these parameters with the same learning rate as used for the rest of the network.

<img src="https://user-images.githubusercontent.com/31564734/121140616-ade35980-c857-11eb-8f7d-9dc2a9356567.jpg" width="700px" />
