# DeepPoseKit

There are some little fixes for the [Original Repo](https://github.com/jgraving/DeepPoseKit), reference the [Original Document](README_orig.md) for more details. 

Here are my install steps which have been tested on the following platforms:

- `Ubuntu 20.04.5 LTS ARM` on `VMWare Fusion` hosted on Apple Macbook with M Series CPU

- `Ubuntu 20.04.6 LTS` on `Microsoft WSL2` hosted on Generic x86_64 PC

You can start from any stage, but start from any small steps are not recommended, unless you are aware what you are doing.

---

### Install Guide

- Configure your system

    1. Update system and packages

        ```
        sudo apt update && sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt update && sudo apt upgrade
        ```

    2. Install tools

        ```
        sudo apt install nano git zsh tree htop curl wget screen tmux openssh-server net-tools gcc make cmake 
        ```

- Install conda Environment

    1. Download Miniconda

        ```
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-`uname -m`.sh
        ```

    2. Install Miniconda

        ```
        chmod +x Miniconda3-latest-Linux-`uname -m`.sh && ./Miniconda3-latest-Linux-`uname -m`.sh
        ```

- Create Work Environment

    1. Create Virtual Environment

        ```
        conda create -n tf tensorflow
        ```

    2. Enter Virtual Environment

        ```
        conda activate tf
        ```

    3. Install dependencies by installing and removing pre-built version of ```deepposekit``` and ```scikit-learn``` with pip

        ```
        pip install deepposekit scikit-learn keras-core
        
        pip uninstall deepposekit scikit-learn
        ```

- Build ```deepposekit``` and ```scikit-learn``` from source to avoid some errors mostly caused by Architecture diffirences of your CPU

    1. Fetch source of ```scikit-learn``` from GitHub

        ```
        git clone https://github.com/scikit-learn/scikit-learn
        ```

    2. Install dependencies needed by compile progress

        ```
        pip install cython wheel numpy scipy
        ```

    3. Compile and Install ```scikit-learn```

        ```
        cd scikit-learn

        pip install -v --no-use-pep517 --no-build-isolation -e .
        ```

    4. Test Install and following command should execute without error

        ```
        python -c "import sklearn; sklearn.show_versions()"
        ```

- Install ```DeepPoseKit```

    1. Fetch source of ```DeepPoseKit``` from GitHub

        ```
        cd ~ 
        
        git clone https://github.com/hmxf/DeepPoseKit
        ```

    2. Install ```DeepPoseKit```

        ```
        cd DeepPoseKit

        python setup.py develop
        ```

    3. Setup architecture-related Environment Variable

        ```
        ./scripts/setup.sh
        ```

- Test your Installation with pre-downloaded data within 5 miniutes ;)

    Pre-downloaded data is located in ```data/``` directory and has been used by ```scripts/train.py``` and ```scripts/predict.py``` for fast test purpose only.

    ```
    python scripts/train.py
    ```

    After a model train process, you can verify if model data has been generated successfully under `data/` directory. If your model data has been stored as a single file `data/saved_model.h5`, then you can view its structure and weight parameters by using ```scripts/hdf5_file_reader.py``` script.

    ```
    python scripts/hdf5_file_reader.py
    ```

    One more step, you can use the trained model to do some predictions.

    ```
    python scripts/predict.py
    ```
