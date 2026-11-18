# When does a probability law barely change under convolution?

Choose two independent even hours on a 12-hour clock, uniformly from 0, 2, 4, 6, 8 and 10. Add them modulo 12. The sum is again uniform on the six even hours. A probability law with this property is called *idempotent* under convolution.

On a locally compact group, an exactly idempotent probability law is uniform on a compact subgroup, in the sense of Haar probability. How close must a law be to one of these exact examples if combining two independent draws changes the distribution only slightly?

## Distance to a subgroup law

Let $\mu$ be a regular probability law on a locally compact Hausdorff group. Write $\eta$ for the total variation distance between $\mu$ and the law of the product of two independent draws from $\mu$. Total variation is the largest difference in the probability assigned to the same event.

For $\eta\le 2^{-39}$ there is a compact subgroup $H$ whose Haar probability $u_H$ satisfies

$$
d_{\rm TV}(\mu,u_H)\ \le\ \frac{1-\sqrt{1-32\eta}}8 .
$$

For very small defects the bound is $2\eta+O(\eta^2)$. The leading coefficient 2 is optimal over this class of groups. The theorem leaves open how far the defect range can be enlarged.

## Finite quantum groups

A related question concerns a state on a finite Kac quantum group. Here convolution combines states through the coproduct of the algebra. For sufficiently small $\eta=\|\phi*\phi-\phi\|$, there is an exactly idempotent state $\psi$ on the same algebra with $\|\phi-\psi\|\le 6\eta$. Both distances use the norm of linear functionals on that algebra. The bound and the small-defect threshold are uniform in its dimension.

Franz and Skalski describe the structure of exact idempotent states on finite quantum groups. The stability bound concerns the distance to such a state when idempotence holds only approximately. [Franz and Skalski, *On idempotent states on quantum groups*](https://arxiv.org/abs/0808.1683)
