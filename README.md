<img src="./unet.png"></img>

## UNet Stylegan2

An implementation of Stylegan2 with UNet Discriminator. This repository works largely the same way as <a href="https://github.com/lucidrains/stylegan2-pytorch">Stylegan2 Pytorch</a>. Simply replace all the `stylegan2_pytorch` command with `unet_stylegan2` instead. Will turn this into a full blown repository if experiments are successful.

## Install

```bash
$ pip install unet-stylegan2
```

## Citations

```bibtex
@misc{karras2019analyzing,
    title={Analyzing and Improving the Image Quality of StyleGAN},
    author={Tero Karras and Samuli Laine and Miika Aittala and Janne Hellsten and Jaakko Lehtinen and Timo Aila},
    year={2019},
    eprint={1912.04958},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

```bibtex
@misc{schnfeld2020unet,
    title={A U-Net Based Discriminator for Generative Adversarial Networks},
    author={Edgar Schönfeld and Bernt Schiele and Anna Khoreva},
    year={2020},
    eprint={2002.12655},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```
