# SlepianCoeffsToSH

Convert a function expressed in Slepian coefficients to spherical harmonic coefficients.

# Usage

call SlepianCoeffsToSH(`flm`, `salpha`, `galpha`, `lmax`, `nalpha`, `exitstatus`)

# Parameters

`flm` : output, real\*8, dimension (2, `lmax`+1, `lmax`+1)
:   The spherical harmonic coefficients of the global function.

`salpha` : input, real\*8, dimension (`nalpha`)
:   A vector containing the Slepian coefficients of the function.

`galpha` : input, real\*8, dimension ((`lmax`+1)**2, `nalpha`)
:   An array containing the spherical harmonic coefficients of the Slepian functions. Each column corresponds to a single function of which the spherical harmonic coefficients can be unpacked with `SHVectorToCilm`.

`lmax` : input, integer
:   The spherical harmonic bandwidth of the Slepian functions.

`nalpha` : input, integer
:   The number of expansion coefficients to compute.

`exitstatus` : output, optional, integer
:   If present, instead of executing a STOP when an error is encountered, the variable exitstatus will be returned describing the error. 0 = No errors; 1 = Improper dimensions of input array; 2 = Improper bounds for input variable; 3 = Error allocating memory; 4 = File IO error.

# Description

`SlepianCoeffsToSH` will compute the spherical harmonic coefficients of a global function `flm` given the Slepian functions `galpha` and the corresponding Slepian coefficients `salpha`. The Slepian functions are determined by a call to either (1) `SHReturnTapers` and then `SHRotateTapers`, or (2) `SHReturnTapersMap`. Each row of `galpha` contains the (`lmax`+1)**2 spherical harmonic coefficients of a Slepian function that can be unpacked using `SHVectorToCilm`. The Slepian functions must be normalized to have unit power (that is the sum of the coefficients squared is 1), and the spherical harmonic coefficients are calculated as

`f_lm = sum_{i}^{nalpha} s(alpha) g_lm(alpha)`  

# See also

[shreturntapers](shreturntapers.html), [shreturntapersmap](shreturntapersmap.html), [shrotatetapers](shrotatetapers.html), [shvectortocilm](shvectortocilm.html)