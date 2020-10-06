from setuptools import setup, find_packages

setup(
  name = 'unet_stylegan2',
  packages = find_packages(),
  scripts=['bin/unet_stylegan2'],
  version = '0.4.3',
  license='GPLv3+',
  description = 'StyleGan2 with UNet Discriminator, in Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/unet-stylegan2',
  keywords = ['generative adversarial networks', 'artificial intelligence'],
  install_requires=[
      'fire',
      'numpy',
      'retry',
      'tqdm',
      'torch',
      'torchvision',
      'pillow',
      'linear_attention_transformer>=0.12.1'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)