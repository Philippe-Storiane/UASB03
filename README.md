# code2seq
This is an unofficial implementation of the model described in:

[Uri Alon](http://urialon.cswp.cs.technion.ac.il), [Shaked Brody](http://www.cs.technion.ac.il/people/shakedbr/), [Omer Levy](https://levyomer.wordpress.com) and [Eran Yahav](http://www.cs.technion.ac.il/~yahave/), "code2seq: Generating Sequences from Structured Representations of Code" [[PDF]](https://openreview.net/pdf?id=H1gKYo09tX)

Appeared in **ICLR'2019** (**poster** available [here](https://urialon.cswp.cs.technion.ac.il/wp-content/uploads/sites/83/2019/05/ICLR19_poster_code2seq.pdf))

An **online demo** is available at [https://code2seq.org](https://code2seq.org).

This is a TensorFlow implementation of the network, with Java and C# extractors for preprocessing the input code. 
It can be easily extended to other languages, 
since the TensorFlow network is agnostic to the input programming language (see [Extending to other languages](#extending-to-other-languages).
Contributions are welcome.



## Citation 

[code2seq: Generating Sequences from Structured Representations of Code](https://arxiv.org/pdf/1808.01400)

```
@inproceedings{
    alon2018codeseq,
    title={code2seq: Generating Sequences from Structured Representations of Code},
    author={Uri Alon and Shaked Brody and Omer Levy and Eran Yahav},
    booktitle={International Conference on Learning Representations},
    year={2019},
    url={https://openreview.net/forum?id=H1gKYo09tX},
}
```
