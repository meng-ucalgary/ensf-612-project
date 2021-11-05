# RadauBVP

Implementation of Radau IIA method to solve ODE for 3 points (order 5). Points on choosing Radau method:

- It is A-stable: can be used with stiff equations
- It can be used for both initial value problem (IVP) and boundary value problem (BVP)
- For IVP it is slower, compared to CVODE (see Sundials package)
- It is more efficient if the problem involves not just solving ODE but also optimising the solution for control parameters, as it can be integrated directly into optimisation frameworks like JuMP (the implementation is being investigated)
- It can be integrated directly into DAE problems (DASSL provides the alternative for IVP, but there is no alternative for BVP)
- It is harder to control the accuracy. Right now it is not implemented.

## Installation

While it is not in METADATA yet, clone this repository using

```julia
Pkg.clone("https://github.com/mobius-eng/RadauBVP.jl.git")
```

## Short documentation

```julia
using RadauBVP

(converged, t, y, raw) = radau3(c!, f!, dc!, df!, y0, t0, tf)
```

where `c!` is a function for boundary conditions, `f!` is the RHS ODE function, `dc!` is the Jacobian of boundary conditions, `df!` is the Jacobian of RHS ODE function, `y0` is initial guess of the solution, `t0` initial time and `tf` is the final time.

For a full documentation see the documentation of `radau3` function (`?radau3`).

For an estended example, see `RadauIIA.ipynb` notebook.

## Implementation detail: use of Jacobians

Technially it is possible to implement the method that wouldn't require a Jacobian: the Jacobian can be constructed using automatic differentiation (AD). However, it is much more efficient to provide the Jacobian manually. This is largerly due to the fact that the Jacobian of `f!` is usually quite sparse. Also, the use of AD means that the type of variables sometimes is not `Float64` but dual numbers (from `ForwardDiff.jl` package, or it can be a "tape" if reverse differentiation is used). This, in turn, creates a problem with pre-allocating internal arrays. So, it was decided not use AD until more efficient implementation is found.

While the Jacobian can be sparse, however, currently the method does not optimise for sparsity (it is on the priority list to implement). As a result, it is not suitable for very large problems due to large memory allocations (the cap should be around 10,000 total variables).

## Future plans

- Usability: overload `radau3` for IVP (no need for `c!`, `dc!` and different form of `y0`)
- Usability: overload `radau3` for BVP but vector `y0` and specifying the number of elements `N`
- Feature: provide integration with JuMP
- Optimisation: use sparse matrix for overall Jacobian
- Feature: get the Jacobian for `f!` and `c!` using AD and construct the overall (sparse) Jacobian manually.

## Copyright & License

(c) 2016 mobius-eng (Alexey Cherkaev)

MIT license (see LICENSE.md)
