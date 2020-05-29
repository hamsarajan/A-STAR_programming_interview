## Question 2

For equivalent networks, the rotation (multiplication of matrices $W^{(i)}$) and shifting (addition of bias $b^{i}$) must be the same.

The simplest of such solutions has the following conditions.

$W^{(1)} = \tilde{W}$

$b^{(1)} = \tilde{b}$

$W^{(2)} = W^{(3)} = I$ (identity matrix)

$b^{(2)} = b^{(3)} = 0$ (no biases)

Alternatively, a more general formula can be:

$\tilde{W} + \tilde{b} = W^{(3)}(W^{(2)}(W^{(1)} + b^{(1)}) + b^{(2)}) +b^{(3)}$

$\tilde{W} + \tilde{b} = W^{(3)}(W^{(2)}W^{(1)} + W^{(2)}b^{(1)} + b^{(2)}) +b^{(3)}$

$\tilde{W} + \tilde{b} = W^{(3)}W^{(2)}W^{(1)} + W^{(3)}W^{(2)}b^{(1)} + W^{(3)}b^{(2)} +b^{(3)}$
