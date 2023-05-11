# Barcode Experiment w/ Python

## Usage

**Env Setup**

```console
git clone https://github.com/SrejonKhan/py-barcode-experiment.git

cd py-barcode-poc

python -m venv .venv

// windows
"./.venv/Scripts/activate.bat"

// linux
source .venv/Scripts/activate

pip install -r requirements.txt
```

**Commands**

```console
python barcode_generator.py <content> <output>
```

- `<content>`- Required: Content in string format that will be hashed
- `<output>` - Required: Output path of generated barcode img

```console
python barcode_img_reader.py <input>
```

- `<input>`- Required: Path of any barcode image file
