Stack capture
=============

This project implements a cross-platform tool for capturing images
with a DLSR that can be used for focus stacking.

Installation
------------

1. Clone the code from GitHub


```bash
git clone git@github.com:stibe88/stack_capture.git
```

2. Setup a Python virtual environment

```bash
cd stack_capture
python3 -m venv venv
./venv/bin/activate
```

3. Install all requirements

```bash
pip install -r requirements.in
```

Basic usage
-----------

Launch the application with:

```bash
cd stack_capture
./venv/bin/activate
python app/stack_capture_app.py
```

First, it captures a very short video.
This is a workaround that enables using the view finder.

Second, the GUI (in German) appears.

The group box "Kameraeinstellungen" shows the camera name
and inherits some useful camera settings as:
- shutter speed
- aperture
- ISO speed

The group box "Fokus" incorporates
- a button "Fokus-Initialisierung"
  - starts the focus initialization progress
  - the initialization progress takes 1-2 minutes
- a slider element, which shows the current focus setting
- three line elements showing
  - the minimum focus value
  - the current focus value
  - the maximum focus value

The group box "Fokusserie" contains all the settings
necessary to take a series of images
with differently focused lenses:
- elements for specifying the folder path
- two spin boxes
  - to specify the focus change between two images
  - to specify the number of images to capture

Limitations
-----------

- Only one camera model is supported:
  - Nikon DSC D300s (PTP mode)
- Bundles or deployments not yet available
- Versioning not yet implemented
- ...
