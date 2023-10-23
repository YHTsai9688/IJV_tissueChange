Internal-Jugular-Vein Project
===
-   Author: Chin-Hsuan Sun
-   License: MIT License
-   Update date: 2023/10/23

>:bulb: This is the description of the IJV project, which aims to ensure code behavior consistency. Please ensure that your environment aligns with the following specifications.

![Static Badge](https://img.shields.io/badge/python-v3.8.0-blue)
![Static Badge](https://img.shields.io/badge/pip-v20.2.0_(python3.8)-orange)
![Static Badge](https://img.shields.io/badge/cuda-v11.7.0-green)


## Table of Contents
- [Introduction](#Introduction)
- [Installation](#Installation)
- [Project Flows](#Project-Flows)
    - [Simulation](#Simulation)
    - [*In-vivo*](#In-vivo)
- [Desciprtion of Each Folder](#Desciprtion-of-Each-Folder)
- [Reference](#Reference)

## Introduction
- TODO

## Installation
Create a virtual environment and activate it.
> **How to creaete a virtual environment?**
> For **Anaconda** user, Read [**this document**](https://hackmd.io/@aMXX54b3ToSm3kTNB_LuWQ/BJ_No2Rkp)

Install the dependencies.
```
pip install -r requirements.txt
```


## Project Flows
### Simulation
1. Building Numerical Model of IJV by Ultrasound Image
2. MCX (Monte Carlo) simulation
3. Surrogate Model (To accerlerate the MC simulation)
    > To understand the concept, read this paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5905904/
5. Prediction Model 
### *In-vivo*
1. In-vivo experiment to validate simulation (ex: hyperventilation, valsalva maneuver, etc.)
2. Preprocess raw data
3. Calibration (remove system response)
4. Feed processed data into prediction data

## Desciprtion of Each Folder
* MCX_src_modified_by_MD703
    * We modified the source code of MCX (https://github.com/fangq/mcx). Please see **this file** to check what we modified if you're intereseted in.  
* absoprtion_spectrum_by_substance
    * The diffuse reflectance spectra is generated by the chromophore in the tissue.
* find_OPs_boundary
    * Based on multiple literature, finding the possible boundary of each optical parameters.
* mcx_sim
    * Run Monte Carlo simulation based on the open source **MCX** we modified
* ultrasound_image_processing_parallel
    * Constuct the numerical model of IJV by ultrasound image.


## Reference
* To understand more detail, basically this repository is followed by my master thesis. Please check NAS:Data/BOSI Lab/Thesis/R10 to access the full text version.

